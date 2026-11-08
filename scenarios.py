"""
What Unit 8 evaluates.

Each scenario maps directly to one of the five acceptance criteria
written in Unit 7.

run_eval.py executes every scenario three times.
"""


SCENARIOS = [
    {
        "name": "false positives on my own writing",
        "criterion": 1,

        # Ten pieces of my own writing.
        # Target from criteria.md:
        # at most 1 of 10 may be labelled high-confidence AI.
        "texts": [
            (
                "Analyzed resource leveling and constrained scheduling; "
                "applied PERT, critical-path analysis, and Monte Carlo "
                "simulation to project completion uncertainty."
            ),
            (
                "Assessed project finance, contract structure, regulatory "
                "and political risk, and allocation of obligations among "
                "sponsors, contractors, and public institutions."
            ),
            (
                "Contributed to a collaborative business plan addressing "
                "operations, strategy, regulatory compliance, governance, "
                "financial projections, and risk management."
            ),
            (
                "Worked on a graduate project involving cost and schedule "
                "performance, resource planning, risk assessment, and "
                "project closeout analysis."
            ),
            (
                "Represented graduate student interests and participated "
                "in student-government deliberations and committee activities."
            ),
            (
                "Served in graduate education policy committee leadership "
                "within GW student government."
            ),
            (
                "Supported youth-focused professional development and "
                "university engagement through PMI chapter programming."
            ),
            (
                "Participated as a speaker in a youth project-management "
                "education program."
            ),
            (
                "Participated in foreign-policy conversations and "
                "professional events in Washington, DC."
            ),
            (
                "Coordinate cross-functional programs involving digital "
                "products, engineering and business stakeholders, including "
                "a 14-workstream initiative."
            ),
        ],
    },

    {
        "name": "clearly human versus clearly AI score spread",
        "criterion": 2,

        # Target from criteria.md:
        # at least 0.40 difference between clearly-human
        # and clearly-AI combined scores.
        #
        # Item 1 is human-style writing.
        # Item 2 is intentionally repetitive AI-like prose.
        "texts": [
            (
                "I missed the bus yesterday, spilled coffee on my jacket, "
                "and somehow arrived early anyway. Later my friend called "
                "with completely unrelated news. By dinner I was laughing "
                "about the whole mess."
            ),
            (
                "The system provides clear results. "
                "The system provides useful results. "
                "The system provides reliable results. "
                "The system provides consistent results. "
                "The system provides accurate results. "
                "The system provides helpful results. "
                "The system provides clear information. "
                "The system provides useful information."
            ),
        ],
    },

    {
        "name": "all three labels reachable",
        "criterion": 3,

        # Target from criteria.md:
        # human, unsure, and AI must all appear.
        "texts": [
            (
                "I honestly had no idea the meeting had moved until I "
                "checked my phone on the way there. I grabbed coffee, "
                "walked across the building, and ended up laughing about "
                "the mix-up with a coworker."
            ),
            (
                "The system works well for many users. It provides useful "
                "information and can support different kinds of tasks. "
                "People may still need to review the results carefully."
            ),
            (
                "The system provides clear results. "
                "The system provides useful results. "
                "The system provides reliable results. "
                "The system provides consistent results. "
                "The system provides accurate results. "
                "The system provides helpful results. "
                "The system provides clear information. "
                "The system provides useful information."
            ),
        ],
    },

    {
        "name": "appeal changes status and is recorded",
        "criterion": 4,

        # run_eval.py sees appeal=True and performs:
        # submit -> read content_id -> POST /appeal
        #
        # Target:
        # 5 of 5 valid appeals become under_review and are recorded.
        "appeal": True,

        "texts": [
            (
                "This is the first evaluation submission used to test "
                "whether an appeal changes the status."
            ),
            (
                "This is the second evaluation submission used to test "
                "the appeal workflow and audit record."
            ),
            (
                "This is the third evaluation submission for checking "
                "the under-review status."
            ),
            (
                "This is the fourth evaluation submission used for "
                "the appeal-path acceptance criterion."
            ),
            (
                "This is the fifth evaluation submission used to confirm "
                "that valid appeals are recorded consistently."
            ),
        ],
    },

    {
        "name": "malformed submissions return controlled errors",
        "criterion": 5,

        # Target from criteria.md:
        # at least 4 of these 5 malformed submissions should
        # return a controlled error rather than crashing.
        "bodies": [
            {
                "text": "",
                "creator_id": "eval_bad_empty",
            },
            {
                "creator_id": "eval_bad_missing",
            },
            {
                "text": None,
                "creator_id": "eval_bad_null",
            },
            {
                "text": 12345,
                "creator_id": "eval_bad_number",
            },
            {
                "text": "word " * 5000,
                "creator_id": "eval_bad_large",
            },
        ],
    },
]


def validate() -> list[str]:
    """
    Validate scenarios before a long evaluation run.

    A scenario may contain either:
    - texts
    - bodies

    Appeal scenarios use texts and set appeal=True.
    """

    problems = []

    if len(SCENARIOS) != 5:
        problems.append(
            f"expected exactly 5 scenarios, found {len(SCENARIOS)}"
        )

    seen_criteria = set()

    for index, scenario in enumerate(SCENARIOS, 1):

        name = scenario.get("name")

        if not name:
            problems.append(
                f"scenario {index} has no name"
            )

        criterion = scenario.get("criterion")

        if criterion not in {1, 2, 3, 4, 5}:
            problems.append(
                f"scenario {index} has invalid criterion {criterion}"
            )
        else:
            seen_criteria.add(criterion)

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {index} ('{name}') has both texts "
                "and bodies — choose one"
            )
            continue

        if bodies is not None:

            if not isinstance(bodies, list) or not bodies:
                problems.append(
                    f"scenario {index} has invalid bodies"
                )
                continue

            for body_index, body in enumerate(bodies, 1):

                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {index}, body {body_index} "
                        "is not a dict"
                    )

            continue

        if texts is not None:

            if not isinstance(texts, list) or not texts:
                problems.append(
                    f"scenario {index} has invalid texts"
                )
                continue

            for text_index, text in enumerate(texts, 1):

                if not isinstance(text, str):
                    problems.append(
                        f"scenario {index}, text {text_index} "
                        "is not a string"
                    )

                elif not text.strip():
                    problems.append(
                        f"scenario {index}, text {text_index} "
                        "is empty"
                    )

            continue

        problems.append(
            f"scenario {index} has no texts and no bodies"
        )

    if seen_criteria != {1, 2, 3, 4, 5}:
        problems.append(
            "criteria 1 through 5 must each have one scenario"
        )

    return problems