# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 10:13
- Auto-marked BROKE (5xx, crash, no response): **0**
- Manually judged after the run: **15 BROKE, 41 HELD**
- Left to judge: **0**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `2af41cfe-b49c-4dd4-81c9-0461319cbe60` | human | 0.248 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `97365eaf-5133-4947-99e6-69c245974273` | unsure | 0.353 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `e6cc5682-1a47-48b8-8532-f6b2c9a3cfe7` | unsure | 0.447 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ff164fde-8b08-432c-a373-d2ab35b6139d` | unsure | 0.449 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `078f210d-e62b-4195-8130-dbff676a7b64` | human | 0.260 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0aa3357b-6bcf-4224-a395-389905cf37a4` | unsure | 0.376 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `15e28daa-88be-464b-a98a-a9b056f5f9be` | unsure | 0.499 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `1746468b-4ea1-4599-acf1-a39e18c6a62d` | human | 0.263 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `081d4fe8-3e07-4c87-ad98-ca25bbbde341` | unsure | 0.455 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `fab9a640-7db0-4346-874e-f42c7a634a6e` | ai | 0.859 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `75626dfd-a203-43d4-a158-a9b3d68af68e` | unsure | 0.448 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `93fcef5b-b4a7-4543-a177-7ab8a8f6a242` | unsure | 0.552 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `345d9eb1-8903-4b81-88a7-0f5de757e6d8` | unsure | 0.547 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `18d5d2e6-066a-4284-b941-446bedf3d998` | unsure | 0.535 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `3eadea7b-56cd-4210-bff4-d98feea47908` | unsure | 0.616 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `3f6712c2-6537-463d-8732-b7e572b554d8` | unsure | 0.560 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `71960bbf-87e6-4f09-8991-96743a1849c0` | ai | 0.661 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `925e4b9f-29d1-4017-b533-66244b6cc4d8` | human | 0.209 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `70df89b4-db19-4603-9cd8-21bd1909c243` | human | 0.285 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `712d2d2c-e847-4b85-ab70-04ca06776eac` | human | 0.186 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `01d96ec1-6213-4e58-998d-1194deae5047` | unsure | 0.406 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `bd295567-c139-4cb0-b9bb-c59cc37ce78c` | unsure | 0.362 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `6590c291-4a2e-4a02-a4a6-a3073e2a492f` | human | 0.345 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `4428f4a4-e9f1-46ef-a910-cb59c770d6b9` | unsure | 0.422 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `bef992e3-692a-45e0-8883-7ae363561982` | human | 0.168 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `6bb71c3b-69bb-449b-b5eb-0a36962741fc` | human | 0.285 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `abe0ea55-c8b5-494e-94c1-9ffb86a6b71f` | unsure | 0.617 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `3efc0aff-3399-4c0b-99df-f31debbbe00d` | ai | 0.757 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `3d8c64e3-1c5c-4754-b6e1-ba2839d69289` | ai | 0.732 | BROKE |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c0cb8c65-877b-4274-bd39-54bf384ed7f3` | human | 0.211 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad860292-185c-4aa7-b939-319c828603e3` | human | 0.211 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5949e8d4-fe15-403e-bfa9-850819c61e31` | human | 0.211 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `61a44c46-45cc-45fc-8f9f-285098fca003` | human | 0.211 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `795ea502-9359-43bc-a293-c671a2cff68c` | human | 0.211 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad34ab83-49af-4310-98c7-8ab3748c6205` | human | 0.211 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bf9c355c-1012-4b8c-8be1-5d01010214a4` | human | 0.211 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3890b487-9c15-44cc-8221-2ee52b23c649` | human | 0.211 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fc4aa2ff-2697-49ea-8fb6-add1aa6dfd81` | human | 0.211 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0b0c856d-eedc-495b-9423-b6057abd3c76` | human | 0.211 | HELD |
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
  "content_id": "2af41cfe-b49c-4dd4-81c9-0461319cbe60",
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
  "content_id": "97365eaf-5133-4947-99e6-69c245974273",
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
  "content_id": "e6cc5682-1a47-48b8-8532-f6b2c9a3cfe7",
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
  "content_id": "ff164fde-8b08-432c-a373-d2ab35b6139d",
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
  "content_id": "078f210d-e62b-4195-8130-dbff676a7b64",
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
  "content_id": "0aa3357b-6bcf-4224-a395-389905cf37a4",
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
  "content_id": "15e28daa-88be-464b-a98a-a9b056f5f9be",
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
  "content_id": "1746468b-4ea1-4599-acf1-a39e18c6a62d",
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
  "content_id": "081d4fe8-3e07-4c87-ad98-ca25bbbde341",
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
  "content_id": "fab9a640-7db0-4346-874e-f42c7a634a6e",
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
  "content_id": "75626dfd-a203-43d4-a158-a9b3d68af68e",
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
  "content_id": "93fcef5b-b4a7-4543-a177-7ab8a8f6a242",
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
  "content_id": "345d9eb1-8903-4b81-88a7-0f5de757e6d8",
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
  "content_id": "18d5d2e6-066a-4284-b941-446bedf3d998",
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
  "content_id": "3eadea7b-56cd-4210-bff4-d98feea47908",
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
  "content_id": "3f6712c2-6537-463d-8732-b7e572b554d8",
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
  "content_id": "71960bbf-87e6-4f09-8991-96743a1849c0",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6615,
  "model_score": 0.8816,
  "style_score": 0.5463,
  "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "925e4b9f-29d1-4017-b533-66244b6cc4d8",
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
  "content_id": "70df89b4-db19-4603-9cd8-21bd1909c243",
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
  "content_id": "712d2d2c-e847-4b85-ab70-04ca06776eac",
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
  "content_id": "01d96ec1-6213-4e58-998d-1194deae5047",
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
  "content_id": "bd295567-c139-4cb0-b9bb-c59cc37ce78c",
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
  "content_id": "6590c291-4a2e-4a02-a4a6-a3073e2a492f",
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
  "content_id": "4428f4a4-e9f1-46ef-a910-cb59c770d6b9",
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
  "content_id": "bef992e3-692a-45e0-8883-7ae363561982",
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
  "content_id": "6bb71c3b-69bb-449b-b5eb-0a36962741fc",
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
  "content_id": "abe0ea55-c8b5-494e-94c1-9ffb86a6b71f",
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
  "content_id": "3efc0aff-3399-4c0b-99df-f31debbbe00d",
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
  "content_id": "3d8c64e3-1c5c-4754-b6e1-ba2839d69289",
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
  "content_id": "c0cb8c65-877b-4274-bd39-54bf384ed7f3",
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
  "content_id": "ad860292-185c-4aa7-b939-319c828603e3",
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
  "content_id": "5949e8d4-fe15-403e-bfa9-850819c61e31",
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
  "content_id": "61a44c46-45cc-45fc-8f9f-285098fca003",
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
  "content_id": "795ea502-9359-43bc-a293-c671a2cff68c",
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
  "content_id": "ad34ab83-49af-4310-98c7-8ab3748c6205",
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
  "content_id": "bf9c355c-1012-4b8c-8be1-5d01010214a4",
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
  "content_id": "3890b487-9c15-44cc-8221-2ee52b23c649",
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
  "content_id": "fc4aa2ff-2697-49ea-8fb6-add1aa6dfd81",
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
  "content_id": "0b0c856d-eedc-495b-9423-b6057abd3c76",
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
