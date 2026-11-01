"""
Combine the model and style signals and turn the final score into
a reader-facing result.

Milestone 4 builds combine_signals.
Milestone 5 completes score_to_label.
"""

import config


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    """Keep a score between 0 and 1."""
    return max(low, min(high, value))


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine the model signal and style signal into one confidence score.

    Both inputs use the same direction:
        0.0 = more human-like
        1.0 = more AI-like

    The initial rule gives both signals equal weight.

    If the signals disagree strongly, the average naturally moves toward
    the middle, representing uncertainty rather than allowing one signal
    to make a high-confidence accusation by itself.
    """

    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )

    return round(clamp(combined), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn the combined score into a machine-readable guess and a
    reader-facing label.

    Milestone 5 will finalize the exact wording.
    """

    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "PLACEHOLDER — high-confidence AI label will be added in Milestone 5.",
        )

    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "PLACEHOLDER — high-confidence human label will be added in Milestone 5.",
        )

    return (
        "unsure",
        "PLACEHOLDER — unsure label will be added in Milestone 5.",
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
            f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}",
        ),
        (
            "high-confidence AI",
            f"{config.AI_THRESHOLD:.2f} – 1.00",
        ),
    ]


if __name__ == "__main__":
    print("Signal weights")
    print(f"model: {config.WEIGHT_MODEL_SIGNAL}")
    print(f"style: {config.WEIGHT_STYLE_SIGNAL}")
    print()

    examples = [
        (0.90, 0.80),
        (0.90, 0.10),
        (0.20, 0.30),
    ]

    for model_score, style_score in examples:
        combined = combine_signals(model_score, style_score)

        print(
            f"model={model_score:.2f} "
            f"style={style_score:.2f} "
            f"combined={combined:.2f}"
        )

    print()
    print("Label ranges")

    for label, score_range in label_ranges():
        print(f"{label}: {score_range}")