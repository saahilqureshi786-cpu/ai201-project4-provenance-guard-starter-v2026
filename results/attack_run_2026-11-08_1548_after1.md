# Attack run — after1

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 15:48
- Auto-marked BROKE (5xx, crash, no response): **0**
- Manually judged after the run: **14 BROKE, 42 HELD**
- Left to judge: **0**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `7f85962c-387b-41f7-a715-98ec21f245a0` | human | 0.248 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `0aa97ef3-9569-43d8-922d-14fd4c573781` | unsure | 0.353 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1847e8f2-b55d-4663-bf99-f53e2475f797` | unsure | 0.447 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `45dda65b-8511-4025-a53d-00ed96b0d5fb` | unsure | 0.449 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2f80b4e7-a606-48bb-b916-a471a8757243` | human | 0.260 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d60497ab-33f3-4719-bef9-2146e3a3cc57` | unsure | 0.376 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1f4d60b3-e94f-4e52-820b-d718bd128baf` | unsure | 0.499 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `f7e4d411-a932-402d-ab64-e9d273290ba7` | human | 0.263 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `38aca091-7d7a-45b6-84d6-a5d471d08121` | unsure | 0.455 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6b662a5b-489d-4a01-b5af-f3ec28e7d223` | ai | 0.859 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `00007d62-88c3-4861-a87c-ca4478d0d04e` | unsure | 0.448 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `1c4f571d-e7d9-4f9e-8486-33165f83f8a4` | unsure | 0.552 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ba6fb23d-bfe8-4a93-9758-b619412b3c2e` | unsure | 0.547 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `74bd0b1b-bfe8-471f-aa15-bf27a67ebe8d` | unsure | 0.535 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `050a1923-266a-4864-a8f1-02964fe9cdfd` | unsure | 0.616 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `21a6339b-abf0-45a4-9506-0ce85e80090e` | unsure | 0.560 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `1137ae55-14c5-4419-a780-b1d4acdd1ff1` | unsure | 0.661 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `1428f31d-17ac-4b06-89f1-c6c07e79f08a` | human | 0.209 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `4078468e-e84b-4fb4-a5f5-568018b4f5f1` | human | 0.285 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8574c1d2-e89a-4028-abb6-10f5cbdc6d09` | human | 0.186 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `bb45af17-ff7a-42ee-bbe5-d51b3c498da8` | unsure | 0.406 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `1cdceb66-d62d-491a-b010-6314b5de52f0` | unsure | 0.362 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `621b1792-f1b5-48f7-be1c-9ca21e360395` | human | 0.345 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a5db5d10-b5e2-4800-8deb-78723c7b19e4` | unsure | 0.422 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `65dd813a-70c4-47b2-abee-421b3575def3` | human | 0.168 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `1df533d5-3c14-4d44-b57a-358737d2b970` | human | 0.285 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `e73a900f-f4d5-4ed4-a4b7-8090eedbdbed` | unsure | 0.617 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `06831fed-d491-488f-84b8-b3ecd692fae5` | ai | 0.757 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `41ccfa10-a61f-4bf3-a9b4-12badaa992d1` | ai | 0.732 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `410d792c-008c-48f0-82eb-1c5b33783470` | human | 0.211 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b6a9e731-a6bd-46e5-bbf5-1a4103551995` | human | 0.211 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0932c134-b049-4221-8b47-49b9248fd6ee` | human | 0.211 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a2f03059-3b21-412a-a6fd-955cfa379ff9` | human | 0.211 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9d64f3b0-8602-4b47-8339-a6c2ba6006f7` | human | 0.211 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `954a4754-e3fe-4ae1-b0f1-b90eaf15b163` | human | 0.211 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56a59a14-2fe8-42cc-8c47-c91c8250e962` | human | 0.211 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b592a910-cb7c-4eb7-902b-ef197bbfee3a` | human | 0.211 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `37b39890-dfd7-4d28-87fc-7434e931c70f` | human | 0.211 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `46a03eb7-98f7-4670-8249-e986a665d79b` | human | 0.211 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "7f85962c-387b-41f7-a715-98ec21f245a0",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2478,
  "model_score": 0.1635,
  "style_score": 0.4978,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "0aa97ef3-9569-43d8-922d-14fd4c573781",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3534,
  "model_score": 0.5943,
  "style_score": 0.2455,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "1847e8f2-b55d-4663-bf99-f53e2475f797",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4473,
  "model_score": 0.6662,
  "style_score": 0.4214,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "45dda65b-8511-4025-a53d-00ed96b0d5fb",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.449,
  "model_score": 0.6114,
  "style_score": 0.4969,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2f80b4e7-a606-48bb-b916-a471a8757243",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2604,
  "model_score": 0.3212,
  "style_score": 0.3309,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "d60497ab-33f3-4719-bef9-2146e3a3cc57",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3755,
  "model_score": 0.5727,
  "style_score": 0.2475,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1f4d60b3-e94f-4e52-820b-d718bd128baf",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4986,
  "model_score": 0.5862,
  "style_score": 0.671,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "f7e4d411-a932-402d-ab64-e9d273290ba7",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2629,
  "model_score": 0.2452,
  "style_score": 0.4358,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "38aca091-7d7a-45b6-84d6-a5d471d08121",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4548,
  "model_score": 0.7042,
  "style_score": 0.3941,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "6b662a5b-489d-4a01-b5af-f3ec28e7d223",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8588,
  "model_score": 0.9792,
  "style_score": 0.7091,
  "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
  "error": null,
  "verdict": "HELD"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "00007d62-88c3-4861-a87c-ca4478d0d04e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4478,
  "model_score": 0.6175,
  "style_score": 0.4856,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "1c4f571d-e7d9-4f9e-8486-33165f83f8a4",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5516,
  "model_score": 0.7387,
  "style_score": 0.5773,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ba6fb23d-bfe8-4a93-9758-b619412b3c2e",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5471,
  "model_score": 0.8051,
  "style_score": 0.5279,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "74bd0b1b-bfe8-471f-aa15-bf27a67ebe8d",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5353,
  "model_score": 0.8329,
  "style_score": 0.4586,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "050a1923-266a-4864-a8f1-02964fe9cdfd",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6155,
  "model_score": 0.8005,
  "style_score": 0.6813,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "21a6339b-abf0-45a4-9506-0ce85e80090e",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5596,
  "model_score": 0.8814,
  "style_score": 0.4372,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "1137ae55-14c5-4419-a780-b1d4acdd1ff1",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6615,
  "model_score": 0.8816,
  "style_score": 0.5463,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "1428f31d-17ac-4b06-89f1-c6c07e79f08a",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2093,
  "model_score": 0.3223,
  "style_score": 0.1835,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "4078468e-e84b-4fb4-a5f5-568018b4f5f1",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2855,
  "model_score": 0.4625,
  "style_score": 0.2211,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "8574c1d2-e89a-4028-abb6-10f5cbdc6d09",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.186,
  "model_score": 0.2044,
  "style_score": 0.2685,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "bb45af17-ff7a-42ee-bbe5-d51b3c498da8",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4058,
  "model_score": 0.5943,
  "style_score": 0.3953,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "1cdceb66-d62d-491a-b010-6314b5de52f0",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.362,
  "model_score": 0.4998,
  "style_score": 0.3916,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "621b1792-f1b5-48f7-be1c-9ca21e360395",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3455,
  "model_score": 0.6401,
  "style_score": 0.1643,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "a5db5d10-b5e2-4800-8deb-78723c7b19e4",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4222,
  "model_score": 0.5583,
  "style_score": 0.4885,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "HELD"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "65dd813a-70c4-47b2-abee-421b3575def3",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.168,
  "model_score": 0.0,
  "style_score": 0.48,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "1df533d5-3c14-4d44-b57a-358737d2b970",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.285,
  "model_score": 0.0112,
  "style_score": 0.8,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "e73a900f-f4d5-4ed4-a4b7-8090eedbdbed",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6169,
  "model_score": 0.9976,
  "style_score": 0.48,
  "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "06831fed-d491-488f-84b8-b3ecd692fae5",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7566,
  "model_score": 0.9969,
  "style_score": 0.88,
  "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "41ccfa10-a61f-4bf3-a9b4-12badaa992d1",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7316,
  "model_score": 0.9064,
  "style_score": 0.9248,
  "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "410d792c-008c-48f0-82eb-1c5b33783470",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "b6a9e731-a6bd-46e5-bbf5-1a4103551995",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "0932c134-b049-4221-8b47-49b9248fd6ee",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "a2f03059-3b21-412a-a6fd-955cfa379ff9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "9d64f3b0-8602-4b47-8339-a6c2ba6006f7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "954a4754-e3fe-4ae1-b0f1-b90eaf15b163",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "56a59a14-2fe8-42cc-8c47-c91c8250e962",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "b592a910-cb7c-4eb7-902b-ef197bbfee3a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "37b39890-dfd7-4d28-87fc-7434e931c70f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "46a03eb7-98f7-4670-8249-e986a665d79b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0287,
  "style_score": 0.5652,
  "label": "Our signals strongly suggest this writing was written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```
