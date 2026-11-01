"""
Combine three signals and turn the final score into
a reader-facing result.
"""

import config


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    """Keep a score between 0 and 1."""
    return max(low, min(high, value))


def combine_signals(
    model_score: float,
    style_score: float,
    repetition_score: float,
) -> float:
    """
    Combine three different signals into one 0–1 score.

    All three point in the same direction:
        0.0 = more human-like
        1.0 = more AI-like

    Weights:
        model predictability: 45%
        stylometry:          35%
        phrase repetition:   20%

    The repetition signal gets the smallest weight because repetition is useful
    but easy to change deliberately.
    """

    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
        + config.WEIGHT_REPETITION_SIGNAL * repetition_score
    )

    return round(clamp(combined), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """Convert the score into a machine guess and reader-facing label."""

    score = clamp(score)

    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "Our signals strongly suggest this writing may be AI-generated. "
            "This result is not proof of authorship, and the writer can appeal "
            "the decision.",
        )

    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "Our signals strongly suggest this writing was written by a person.",
        )

    return (
        "unsure",
        "Our signals do not give a clear result, so we are not making an "
        "authorship claim about this writing.",
    )


def label_ranges() -> list[tuple[str, str]]:
    """Return the score range covered by each label."""

    return [
        (
            "high-confidence human",
            f"0.00 – {config.HUMAN_THRESHOLD:.2f}",
        ),
        (
            "unsure",
            f"above {config.HUMAN_THRESHOLD:.2f} and below "
            f"{config.AI_THRESHOLD:.2f}",
        ),
        (
            "high-confidence AI",
            f"{config.AI_THRESHOLD:.2f} – 1.00",
        ),
    ]


if __name__ == "__main__":
    print("Signal weights")
    print(f"model:      {config.WEIGHT_MODEL_SIGNAL}")
    print(f"style:      {config.WEIGHT_STYLE_SIGNAL}")
    print(f"repetition: {config.WEIGHT_REPETITION_SIGNAL}")
    print()

    examples = [
        (0.90, 0.80, 0.90),
        (0.90, 0.10, 0.00),
        (0.20, 0.30, 0.00),
    ]

    for model_score, style_score, repetition_score in examples:
        combined = combine_signals(
            model_score,
            style_score,
            repetition_score,
        )

        guess, label = score_to_label(combined)

        print(
            f"model={model_score:.2f} "
            f"style={style_score:.2f} "
            f"repetition={repetition_score:.2f} "
            f"combined={combined:.2f} "
            f"guess={guess}"
        )

        print(f"label={label}")
        print()

    print("Label ranges")

    for label, score_range in label_ranges():
        print(f"{label}: {score_range}")