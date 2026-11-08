# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 15:53
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `a5d39982-9258-47ed-96bf-b0f5104d2d3a` | human | 0.248 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `6f3fbadb-2057-4c0e-b836-22aa889ea3bc` | human | 0.353 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `742786be-0d43-43df-a87b-d12db7145a65` | human | 0.447 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `1df94a7c-a2f4-4e80-a9be-5149e49325af` | human | 0.449 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3ec34e04-c08b-462e-8c5c-09988a23db87` | human | 0.260 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `49fd1c82-a411-4c48-84c8-e1d1f0730342` | human | 0.376 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d3af6526-70f7-4dd5-8979-bf1bfb1e88d6` | unsure | 0.499 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `3ec32d2c-6cfe-4fae-9b2e-6080d0ebe2f6` | human | 0.263 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `6d80f325-9295-4be7-84db-d5e1f3a34b39` | unsure | 0.455 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `95334afc-7f6e-48d4-9cb6-c737d976d91f` | ai | 0.859 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `f2f17fb6-eb63-4a75-9395-e34299552edf` | human | 0.448 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `b39002e9-279e-4edf-a8c4-82d0d67c9ecb` | unsure | 0.552 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4e2e9859-a705-4922-9736-8502cffd2152` | unsure | 0.547 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `719b5635-40c2-4cca-ab71-02e62c0536e5` | unsure | 0.535 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `d21ebe7b-5a6e-4803-8793-1985b53d2edf` | unsure | 0.616 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `c991371e-8f32-4809-be1c-45720351ddbd` | unsure | 0.560 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `33a19d18-c760-4bb7-adc4-3424b0ce47fb` | unsure | 0.661 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `2b2ad82a-4c83-4339-8d6f-1af87fa271b6` | human | 0.209 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `57290e9a-2c0b-4f8c-a832-3e489b4b9c47` | human | 0.285 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `7909cff4-904c-477d-b330-97edc6f43d8b` | human | 0.186 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `5fae7b4d-701d-44db-ab06-fb26e71d2379` | human | 0.406 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `87324d33-eac5-43bc-8633-3ee6c58d2daa` | human | 0.362 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `dabbf94c-f37f-48e0-b45e-36339ff2a386` | human | 0.345 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `94a59da1-ed40-4d2b-8792-be8506b0aa71` | human | 0.422 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `e71e2572-c4ef-4c75-a34a-7705ac7aba15` | human | 0.168 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `5f97c808-f45b-4a5d-8981-c84567d0e1c6` | human | 0.285 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `722864ea-8e63-403d-83d4-28a3c1e6ae2b` | unsure | 0.617 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `0ff4702b-d7d7-4759-90d2-61f1accff90a` | ai | 0.757 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `43e9427e-42b0-4f0c-b3ba-8deded8c21aa` | ai | 0.732 | BROKE |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3f5a4367-e337-4fc3-900d-655d6751fa66` | human | 0.211 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e5c81aff-32a0-48e7-bc82-766df6a658a2` | human | 0.211 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56f0688a-2253-48a5-8d90-a70adf24885b` | human | 0.211 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7ec4bf86-f8be-417f-af7f-1e92473affd3` | human | 0.211 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `442413fe-fe9f-4dab-be67-beb2d64cf454` | human | 0.211 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `794eb9fd-8a46-47af-8bae-465197cc1c91` | human | 0.211 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f92729d2-8e4a-4f48-925c-e04b327b60fb` | human | 0.211 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aca47591-e9a1-4ec3-981b-df0a6c4025c7` | human | 0.211 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `37ab0535-8682-4fbf-ab77-d90632b4dbc2` | human | 0.211 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `38aeb984-63d9-4d94-b5df-f58271e871cd` | human | 0.211 | HELD |
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
  "content_id": "a5d39982-9258-47ed-96bf-b0f5104d2d3a",
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
  "content_id": "6f3fbadb-2057-4c0e-b836-22aa889ea3bc",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3534,
  "model_score": 0.5943,
  "style_score": 0.2455,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "742786be-0d43-43df-a87b-d12db7145a65",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.4473,
  "model_score": 0.6662,
  "style_score": 0.4214,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "1df94a7c-a2f4-4e80-a9be-5149e49325af",
  "creator_id": "attacker_EV04",
  "guess": "human",
  "confidence": 0.449,
  "model_score": 0.6114,
  "style_score": 0.4969,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "3ec34e04-c08b-462e-8c5c-09988a23db87",
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
  "content_id": "49fd1c82-a411-4c48-84c8-e1d1f0730342",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3755,
  "model_score": 0.5727,
  "style_score": 0.2475,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "d3af6526-70f7-4dd5-8979-bf1bfb1e88d6",
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
  "content_id": "3ec32d2c-6cfe-4fae-9b2e-6080d0ebe2f6",
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
  "content_id": "6d80f325-9295-4be7-84db-d5e1f3a34b39",
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
  "content_id": "95334afc-7f6e-48d4-9cb6-c737d976d91f",
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
  "content_id": "f2f17fb6-eb63-4a75-9395-e34299552edf",
  "creator_id": "attacker_FP01",
  "guess": "human",
  "confidence": 0.4478,
  "model_score": 0.6175,
  "style_score": 0.4856,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "b39002e9-279e-4edf-a8c4-82d0d67c9ecb",
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
  "content_id": "4e2e9859-a705-4922-9736-8502cffd2152",
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
  "content_id": "719b5635-40c2-4cca-ab71-02e62c0536e5",
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
  "content_id": "d21ebe7b-5a6e-4803-8793-1985b53d2edf",
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
  "content_id": "c991371e-8f32-4809-be1c-45720351ddbd",
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
  "content_id": "33a19d18-c760-4bb7-adc4-3424b0ce47fb",
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
  "content_id": "2b2ad82a-4c83-4339-8d6f-1af87fa271b6",
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
  "content_id": "57290e9a-2c0b-4f8c-a832-3e489b4b9c47",
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
  "content_id": "7909cff4-904c-477d-b330-97edc6f43d8b",
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
  "content_id": "5fae7b4d-701d-44db-ab06-fb26e71d2379",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.4058,
  "model_score": 0.5943,
  "style_score": 0.3953,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "87324d33-eac5-43bc-8633-3ee6c58d2daa",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.362,
  "model_score": 0.4998,
  "style_score": 0.3916,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "dabbf94c-f37f-48e0-b45e-36339ff2a386",
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
  "content_id": "94a59da1-ed40-4d2b-8792-be8506b0aa71",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.4222,
  "model_score": 0.5583,
  "style_score": 0.4885,
  "label": "Our signals strongly suggest this writing was written by a person.",
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
  "content_id": "e71e2572-c4ef-4c75-a34a-7705ac7aba15",
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
  "content_id": "5f97c808-f45b-4a5d-8981-c84567d0e1c6",
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
  "content_id": "722864ea-8e63-403d-83d4-28a3c1e6ae2b",
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
  "content_id": "0ff4702b-d7d7-4759-90d2-61f1accff90a",
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
  "content_id": "43e9427e-42b0-4f0c-b3ba-8deded8c21aa",
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
  "content_id": "3f5a4367-e337-4fc3-900d-655d6751fa66",
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
  "content_id": "e5c81aff-32a0-48e7-bc82-766df6a658a2",
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
  "content_id": "56f0688a-2253-48a5-8d90-a70adf24885b",
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
  "content_id": "7ec4bf86-f8be-417f-af7f-1e92473affd3",
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
  "content_id": "442413fe-fe9f-4dab-be67-beb2d64cf454",
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
  "content_id": "794eb9fd-8a46-47af-8bae-465197cc1c91",
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
  "content_id": "f92729d2-8e4a-4f48-925c-e04b327b60fb",
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
  "content_id": "aca47591-e9a1-4ec3-981b-df0a6c4025c7",
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
  "content_id": "37ab0535-8682-4fbf-ab77-d90632b4dbc2",
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
  "content_id": "38aeb984-63d9-4d94-b5df-f58271e871cd",
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
