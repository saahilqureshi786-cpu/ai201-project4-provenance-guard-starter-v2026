"""
Signal two: the style signal.

This signal looks at the shape of the writing rather than its meaning.

It measures:
1. sentence-length variation
2. vocabulary variety
3. punctuation density

The final score runs from 0.0 to 1.0.
Higher means the writing looks more AI-like according to these style features.
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split text into rough sentences."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [part for part in parts if part.strip()]


def words(text: str) -> list[str]:
    """Return lowercase words with punctuation removed."""
    return re.findall(r"[a-z0-9']+", text.lower())


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    """Keep a number inside a fixed range."""
    return max(low, min(high, value))


# ── Measure 1: sentence variation ─────────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    Measure how much sentence lengths vary.

    This uses the coefficient of variation:

        standard deviation / mean sentence length

    A low number means sentence lengths are very similar.
    A higher number means sentence lengths vary more.
    """

    sentence_list = sentences(text)

    if len(sentence_list) < 2:
        return 0.0

    lengths = [len(words(sentence)) for sentence in sentence_list]

    # Ignore empty sentence fragments.
    lengths = [length for length in lengths if length > 0]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    spread = statistics.stdev(lengths) / mean_length

    return round(spread, 4)


# ── Measure 2: vocabulary variety ─────────────────────────────────────────

def type_token_ratio(text: str) -> float:
    """
    Return unique words divided by total words.

    Higher values mean the text uses a more varied vocabulary.
    """

    token_list = words(text)

    if not token_list:
        return 0.0

    unique_words = len(set(token_list))
    total_words = len(token_list)

    ratio = unique_words / total_words

    return round(ratio, 4)


# ── Measure 3: punctuation ────────────────────────────────────────────────

def punctuation_density(text: str) -> float:
    """
    Measure punctuation relative to text length.

    Counts common punctuation marks and divides by the total number
    of non-space characters.
    """

    non_space_characters = re.sub(r"\s+", "", text)

    if not non_space_characters:
        return 0.0

    punctuation_marks = re.findall(r"""[.,!?;:'"()\-—]""", text)

    density = len(punctuation_marks) / len(non_space_characters)

    return round(density, 4)


# ── Combine the measures ──────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    Convert the three style measurements into one 0–1 AI-likelihood score.

    Higher means more AI-like.

    The assumptions are:

    - Less sentence-length variation is more AI-like.
    - Less vocabulary variety is more AI-like.
    - Very regular/moderate punctuation is somewhat more AI-like.

    The three internal components are weighted:

        sentence structure: 40%
        vocabulary variety:  40%
        punctuation:         20%
    """

    spread = sentence_length_spread(text)
    vocabulary_ratio = type_token_ratio(text)
    punctuation = punctuation_density(text)

    # ------------------------------------------------------------
    # Sentence component
    #
    # A spread around 0.80 or higher is treated as strongly varied.
    # Low variation produces a higher AI-like score.
    # ------------------------------------------------------------

    spread_ai = 1.0 - clamp(spread / 0.80)

    # ------------------------------------------------------------
    # Vocabulary component
    #
    # Very repetitive vocabulary is more AI-like in this simple signal.
    #
    # TTR <= 0.35 -> strongly AI-like
    # TTR >= 0.90 -> strongly human-like
    # ------------------------------------------------------------

    vocabulary_ai = 1.0 - clamp(
        (vocabulary_ratio - 0.35) / (0.90 - 0.35)
    )

    # ------------------------------------------------------------
    # Punctuation component
    #
    # A moderate punctuation density around 3% is treated as the most
    # regular/polished. Values much lower or higher move away from that.
    #
    # This is intentionally a weak signal because punctuation is easy
    # for a writer to change.
    # ------------------------------------------------------------

    expected_density = 0.03
    distance = abs(punctuation - expected_density)

    punctuation_ai = 1.0 - clamp(distance / 0.05)

    # ------------------------------------------------------------
    # Final style score
    # ------------------------------------------------------------

    score = (
        0.40 * spread_ai
        + 0.40 * vocabulary_ai
        + 0.20 * punctuation_ai
    )

    return round(clamp(score), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")

    print(
        f"sentence_length_spread   "
        f"{sentence_length_spread(text):.4f}"
    )

    print(
        f"type_token_ratio         "
        f"{type_token_ratio(text):.4f}"
    )

    print(
        f"punctuation_density      "
        f"{punctuation_density(text):.4f}"
    )

    print(
        f"style_signal             "
        f"{style_signal(text):.4f}   "
        f"(higher = more likely AI)"
    )