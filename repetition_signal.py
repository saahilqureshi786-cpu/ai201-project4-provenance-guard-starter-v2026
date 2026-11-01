"""
Third signal for the Unit 7 stretch feature.

This signal measures repeated phrase patterns.

It is different from:
- detector.py, which measures language-model predictability
- stylometry.py, which measures sentence variation, vocabulary variety,
  and punctuation density

Higher output means the text contains more repeated local patterns and is
treated as more AI-like for this simple heuristic.
"""

import re


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    """Keep a value inside a fixed range."""
    return max(low, min(high, value))


def words(text: str) -> list[str]:
    """Return lowercase words with punctuation removed."""
    return re.findall(r"[a-z0-9']+", text.lower())


def sentences(text: str) -> list[str]:
    """Split text into rough sentences."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [part for part in parts if part.strip()]


def repeated_trigram_fraction(text: str) -> float:
    """
    Measure how many three-word phrases repeat.

    0.0 means no repeated trigrams.
    Higher values mean more phrase repetition.
    """

    tokens = words(text)

    if len(tokens) < 6:
        return 0.0

    trigrams = [
        tuple(tokens[i:i + 3])
        for i in range(len(tokens) - 2)
    ]

    total = len(trigrams)
    unique = len(set(trigrams))

    repeated_fraction = 1.0 - (unique / total)

    return round(clamp(repeated_fraction), 4)


def repeated_sentence_start_fraction(text: str) -> float:
    """
    Measure whether multiple sentences begin with the same two words.
    """

    sentence_list = sentences(text)

    if len(sentence_list) < 2:
        return 0.0

    starts = []

    for sentence in sentence_list:
        sentence_words = words(sentence)

        if len(sentence_words) >= 2:
            starts.append(tuple(sentence_words[:2]))

    if len(starts) < 2:
        return 0.0

    total = len(starts)
    unique = len(set(starts))

    repeated_fraction = 1.0 - (unique / total)

    return round(clamp(repeated_fraction), 4)


def repetition_signal(text: str) -> float:
    """
    Return a 0–1 repetition score.

    Higher means more AI-like according to this heuristic.

    Repeated three-word phrases count for 70%.
    Repeated sentence openings count for 30%.

    Phrase repetition is normalized so that a repeated-trigram fraction
    around 0.25 or higher is treated as strongly repetitive.
    """

    trigram_repeat = repeated_trigram_fraction(text)
    sentence_start_repeat = repeated_sentence_start_fraction(text)

    trigram_ai = clamp(trigram_repeat / 0.25)

    score = (
        0.70 * trigram_ai
        + 0.30 * sentence_start_repeat
    )

    return round(clamp(score), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system provides clear results. "
        "The system provides useful results. "
        "The system provides reliable results. "
        "The system provides consistent results."
    )

    print(f"repeated_trigram_fraction       {repeated_trigram_fraction(text):.4f}")
    print(
        f"repeated_sentence_start_fraction "
        f"{repeated_sentence_start_fraction(text):.4f}"
    )
    print(
        f"repetition_signal               "
        f"{repetition_signal(text):.4f} "
        f"(higher = more likely AI)"
    )