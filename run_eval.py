#!/usr/bin/env python3
"""
Unit 8 acceptance-criteria evaluator for Provenance Guard.

Runs all five scenarios from scenarios.py three times each.

Usage:
    python run_eval.py --label before
    python run_eval.py --label after
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

import requests

import scenarios


BASE_URL = "http://127.0.0.1:5000"
TRIALS = 3
TIMEOUT = 60

RESULTS_DIR = Path("results")


# ---------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------

def post_submit(body: dict) -> dict:
    """POST one request body to /submit."""

    try:
        response = requests.post(
            f"{BASE_URL}/submit",
            json=body,
            timeout=TIMEOUT,
        )

        try:
            payload = response.json()
        except ValueError:
            payload = {
                "raw_text": response.text,
            }

        return {
            "status_code": response.status_code,
            "payload": payload,
        }

    except requests.RequestException as exc:
        return {
            "status_code": None,
            "payload": {
                "error": str(exc),
            },
        }


def post_appeal(
    content_id: str,
    reasoning: str,
) -> dict:
    """POST one appeal."""

    try:
        response = requests.post(
            f"{BASE_URL}/appeal",
            json={
                "content_id": content_id,
                "reasoning": reasoning,
            },
            timeout=TIMEOUT,
        )

        try:
            payload = response.json()
        except ValueError:
            payload = {
                "raw_text": response.text,
            }

        return {
            "status_code": response.status_code,
            "payload": payload,
        }

    except requests.RequestException as exc:
        return {
            "status_code": None,
            "payload": {
                "error": str(exc),
            },
        }


def get_log(limit: int = 500) -> list[dict]:
    """Fetch audit entries from /log."""

    response = requests.get(
        f"{BASE_URL}/log",
        params={
            "limit": limit,
        },
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    payload = response.json()

    return payload.get(
        "entries",
        [],
    )


# ---------------------------------------------------------------------
# Criterion 1
# ---------------------------------------------------------------------

def run_criterion_1(
    scenario: dict,
    trial: int,
) -> dict:
    """
    Criterion 1:
    At most 1 of 10 clearly-human pieces may receive the AI label.
    """

    outputs = []

    for index, text in enumerate(
        scenario["texts"],
        1,
    ):
        creator_id = (
            f"eval_c1_t{trial}_item{index}"
        )

        result = post_submit({
            "text": text,
            "creator_id": creator_id,
        })

        outputs.append({
            "item": index,
            "creator_id": creator_id,
            **result,
        })

    ai_count = sum(
        1
        for output in outputs
        if output["payload"].get("guess") == "ai"
    )

    passed = (
        len(outputs) == 10
        and all(
            output["status_code"] == 200
            for output in outputs
        )
        and ai_count <= 1
    )

    return {
        "criterion": 1,
        "trial": trial,
        "metric": f"{ai_count}/10 labeled AI",
        "passed": passed,
        "details": outputs,
    }


# ---------------------------------------------------------------------
# Criterion 2
# ---------------------------------------------------------------------

def run_criterion_2(
    scenario: dict,
    trial: int,
) -> dict:
    """
    Criterion 2:
    Clearly-human and clearly-AI examples must differ
    by at least 0.40 in combined score.
    """

    outputs = []

    for index, text in enumerate(
        scenario["texts"],
        1,
    ):
        creator_id = (
            f"eval_c2_t{trial}_item{index}"
        )

        result = post_submit({
            "text": text,
            "creator_id": creator_id,
        })

        outputs.append({
            "item": index,
            "creator_id": creator_id,
            **result,
        })

    scores = [
        output["payload"].get("confidence")
        for output in outputs
    ]

    valid_scores = (
        len(scores) == 2
        and all(
            isinstance(score, (int, float))
            for score in scores
        )
    )

    if valid_scores:
        spread = abs(
            scores[1] - scores[0]
        )
    else:
        spread = None

    passed = (
        valid_scores
        and spread >= 0.40
        and all(
            output["status_code"] == 200
            for output in outputs
        )
    )

    return {
        "criterion": 2,
        "trial": trial,
        "metric": (
            f"score spread = {spread:.4f}"
            if spread is not None
            else "score spread unavailable"
        ),
        "passed": passed,
        "details": outputs,
    }


# ---------------------------------------------------------------------
# Criterion 3
# ---------------------------------------------------------------------

def run_criterion_3(
    scenario: dict,
    trial: int,
) -> dict:
    """
    Criterion 3:
    human, unsure, and ai must all be reachable.
    """

    outputs = []

    for index, text in enumerate(
        scenario["texts"],
        1,
    ):
        creator_id = (
            f"eval_c3_t{trial}_item{index}"
        )

        result = post_submit({
            "text": text,
            "creator_id": creator_id,
        })

        outputs.append({
            "item": index,
            "creator_id": creator_id,
            **result,
        })

    guesses = {
        output["payload"].get("guess")
        for output in outputs
        if output["status_code"] == 200
    }

    required = {
        "human",
        "unsure",
        "ai",
    }

    passed = (
        guesses == required
    )

    return {
        "criterion": 3,
        "trial": trial,
        "metric": (
            "labels reached = "
            + ", ".join(
                sorted(
                    str(value)
                    for value in guesses
                )
            )
        ),
        "passed": passed,
        "details": outputs,
    }


# ---------------------------------------------------------------------
# Criterion 4
# ---------------------------------------------------------------------

def run_criterion_4(
    scenario: dict,
    trial: int,
) -> dict:
    """
    Criterion 4:
    Five valid appeals must:
    - return under_review
    - appear in the audit log
    """

    outputs = []

    appealed_content_ids = []

    for index, text in enumerate(
        scenario["texts"],
        1,
    ):
        creator_id = (
            f"eval_c4_t{trial}_item{index}"
        )

        submission = post_submit({
            "text": text,
            "creator_id": creator_id,
        })

        content_id = (
            submission["payload"].get(
                "content_id"
            )
        )

        appeal_result = None

        if (
            submission["status_code"] == 200
            and content_id
        ):
            appeal_result = post_appeal(
                content_id=content_id,
                reasoning=(
                    "Evaluation appeal: "
                    "please review this decision."
                ),
            )

            appealed_content_ids.append(
                content_id
            )

        outputs.append({
            "item": index,
            "creator_id": creator_id,
            "submission": submission,
            "appeal": appeal_result,
        })

    audit_entries = get_log()

    successful = 0

    for output in outputs:
        submission = output["submission"]
        appeal_result = output["appeal"]

        content_id = (
            submission["payload"].get(
                "content_id"
            )
        )

        response_under_review = (
            appeal_result is not None
            and appeal_result["status_code"] == 200
            and appeal_result["payload"].get(
                "status"
            )
            == "under_review"
        )

        logged_under_review = any(
            entry.get("content_id")
            == content_id
            and entry.get("event")
            == "appeal"
            and entry.get("status")
            == "under_review"
            for entry in audit_entries
        )

        output["response_under_review"] = (
            response_under_review
        )

        output["logged_under_review"] = (
            logged_under_review
        )

        if (
            response_under_review
            and logged_under_review
        ):
            successful += 1

    passed = successful == 5

    return {
        "criterion": 4,
        "trial": trial,
        "metric": (
            f"{successful}/5 appeals "
            "under_review and logged"
        ),
        "passed": passed,
        "details": outputs,
    }


# ---------------------------------------------------------------------
# Criterion 5
# ---------------------------------------------------------------------

def run_criterion_5(
    scenario: dict,
    trial: int,
) -> dict:
    """
    Criterion 5:
    At least 4 of 5 malformed requests must return
    controlled client errors rather than crashing.
    """

    outputs = []

    for index, original_body in enumerate(
        scenario["bodies"],
        1,
    ):
        body = dict(original_body)

        # Make creator IDs unique across trials so the
        # rate limiter does not contaminate the test.
        if isinstance(
            body.get("creator_id"),
            str,
        ):
            body["creator_id"] = (
                f"{body['creator_id']}_t{trial}"
            )

        result = post_submit(
            body
        )

        status_code = result[
            "status_code"
        ]

        controlled = (
            isinstance(
                status_code,
                int,
            )
            and 400 <= status_code < 500
        )

        outputs.append({
            "item": index,
            "body_summary": {
                key: (
                    value
                    if not (
                        key == "text"
                        and isinstance(
                            value,
                            str,
                        )
                        and len(value) > 200
                    )
                    else (
                        f"<string length "
                        f"{len(value)}>"
                    )
                )
                for key, value
                in body.items()
            },
            "controlled_error": controlled,
            **result,
        })

    controlled_count = sum(
        1
        for output in outputs
        if output["controlled_error"]
    )

    passed = (
        controlled_count >= 4
    )

    return {
        "criterion": 5,
        "trial": trial,
        "metric": (
            f"{controlled_count}/5 "
            "controlled errors"
        ),
        "passed": passed,
        "details": outputs,
    }


# ---------------------------------------------------------------------
# Scenario dispatcher
# ---------------------------------------------------------------------

def run_scenario(
    scenario: dict,
    trial: int,
) -> dict:

    criterion = scenario[
        "criterion"
    ]

    if criterion == 1:
        return run_criterion_1(
            scenario,
            trial,
        )

    if criterion == 2:
        return run_criterion_2(
            scenario,
            trial,
        )

    if criterion == 3:
        return run_criterion_3(
            scenario,
            trial,
        )

    if criterion == 4:
        return run_criterion_4(
            scenario,
            trial,
        )

    if criterion == 5:
        return run_criterion_5(
            scenario,
            trial,
        )

    raise ValueError(
        f"Unknown criterion: {criterion}"
    )


# ---------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------

TARGETS = {
    1: (
        "At most 1 of 10 clearly-human "
        "pieces labeled AI"
    ),
    2: (
        "At least 0.40 combined-score spread"
    ),
    3: (
        "All 3 labels reachable"
    ),
    4: (
        "5 of 5 appeals under_review "
        "and logged"
    ),
    5: (
        "At least 4 of 5 malformed requests "
        "return controlled errors"
    ),
}


def overall_verdict(
    trial_results: list[dict],
) -> str:
    """
    A criterion is MET only if it meets its target
    in all three trials.
    """

    return (
        "MET"
        if all(
            result["passed"]
            for result in trial_results
        )
        else "MISSED"
    )


def make_markdown(
    label: str,
    all_results: dict[int, list[dict]],
) -> str:

    lines = []

    lines.append(
        f"# Evaluation run — {label}"
    )

    lines.append("")

    lines.append(
        "- Produced by: `run_eval.py::main`"
    )

    lines.append(
        "- Service: `app.py::submit`"
    )

    lines.append(
        f"- Trials per criterion: **{TRIALS}**"
    )

    lines.append("")

    lines.append(
        "## Run Log"
    )

    lines.append("")

    lines.append(
        "| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |"
    )

    lines.append(
        "|---|---|---|---|---|---|"
    )

    for criterion in range(1, 6):

        results = all_results[
            criterion
        ]

        cells = []

        for result in results:
            prefix = (
                "PASS"
                if result["passed"]
                else "FAIL"
            )

            cells.append(
                f"{prefix} — {result['metric']}"
            )

        verdict = overall_verdict(
            results
        )

        lines.append(
            f"| {criterion} | "
            f"{TARGETS[criterion]} | "
            f"{cells[0]} | "
            f"{cells[1]} | "
            f"{cells[2]} | "
            f"**{verdict}** |"
        )

    lines.append("")

    lines.append(
        "## Real output from each criterion"
    )

    lines.append("")

    for criterion in range(1, 6):

        result = all_results[
            criterion
        ][0]

        lines.append(
            f"### Criterion {criterion}"
        )

        lines.append("")

        lines.append(
            f"Trial 1 result: "
            f"{'PASS' if result['passed'] else 'FAIL'}"
        )

        lines.append("")

        lines.append(
            f"Metric: `{result['metric']}`"
        )

        lines.append("")

        lines.append(
            "```json"
        )

        lines.append(
            json.dumps(
                result["details"],
                indent=2,
                ensure_ascii=False,
            )
        )

        lines.append(
            "```"
        )

        lines.append("")

    return "\n".join(
        lines
    ) + "\n"


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--label",
        required=True,
        help=(
            "Name for this evaluation run, "
            "for example before or after."
        ),
    )

    args = parser.parse_args()

    problems = scenarios.validate()

    if problems:
        print(
            "Scenario validation failed:"
        )

        for problem in problems:
            print(
                f"  - {problem}"
            )

        raise SystemExit(1)

    print(
        f"Running 5 criteria × "
        f"{TRIALS} trials against {BASE_URL}"
    )

    print(
        f"Label: {args.label}"
    )

    print()

    all_results = {
        criterion: []
        for criterion in range(
            1,
            6,
        )
    }

    scenario_by_criterion = {
        scenario["criterion"]: scenario
        for scenario in scenarios.SCENARIOS
    }

    for trial in range(
        1,
        TRIALS + 1,
    ):

        print(
            f"=== Trial {trial}/{TRIALS} ==="
        )

        for criterion in range(
            1,
            6,
        ):

            scenario = (
                scenario_by_criterion[
                    criterion
                ]
            )

            print(
                f"Criterion {criterion}: "
                f"{scenario['name']}"
            )

            result = run_scenario(
                scenario,
                trial,
            )

            all_results[
                criterion
            ].append(
                result
            )

            status = (
                "PASS"
                if result["passed"]
                else "FAIL"
            )

            print(
                f"  {status}: "
                f"{result['metric']}"
            )

        print()

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H%M"
    )

    output_path = (
        RESULTS_DIR
        / (
            f"eval_run_{timestamp}_"
            f"{args.label}.md"
        )
    )

    markdown = make_markdown(
        args.label,
        all_results,
    )

    output_path.write_text(
        markdown,
        encoding="utf-8",
    )

    print(
        "=" * 60
    )

    print(
        f"Wrote {output_path}"
    )

    print()

    for criterion in range(
        1,
        6,
    ):
        results = all_results[
            criterion
        ]

        print(
            f"Criterion {criterion}: "
            f"{overall_verdict(results)}"
        )

        for result in results:
            print(
                f"  Trial {result['trial']}: "
                f"{result['metric']}"
            )

    print(
        "=" * 60
    )


if __name__ == "__main__":
    main()