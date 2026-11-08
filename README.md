# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard is a backend service that accepts a piece of writing and estimates whether the text appears more likely to be human-written, AI-generated, or too uncertain to make a confident judgment.

A submission takes this path through the service:

1. A writer sends JSON containing `text` and `creator_id` to the `POST /submit` endpoint.
2. The service validates the request and creates a unique `content_id`.
3. The text is sent to the model signal in `detector.py`, which measures how predictable the writing is to a local language model.
4. The text is also sent to the style signal in `stylometry.py`, which measures features of the writing itself such as sentence-length variation, vocabulary variety, and punctuation.
5. The signal scores are combined into one confidence score by `scoring.py::combine_signals`.
6. The confidence score is mapped to one of three reader-facing results: high-confidence human, unsure, or high-confidence AI.
7. The decision and signal scores are written to `logs/audit.jsonl`, and the result is returned to the writer.

If the writer thinks the system made a wrong decision, they can send the `content_id` and their reasoning to `POST /appeal`. A valid appeal changes the item's status to `under_review` and records the appeal in the audit log.

### False-positive path

The failure I am most concerned about is a real writer being labeled high-confidence AI. For example, a person who uses simple vocabulary and short sentences may produce writing that is very predictable to the model even though they wrote every word themselves. If the combined score crosses the AI threshold, the writer sees the AI-facing label. The appeal endpoint gives that writer a way to challenge the decision and moves the content to `under_review` instead of treating the detector as final proof.

### Endpoint contracts

`POST /submit`

Input:

```json
{
  "text": "The writing to evaluate.",
  "creator_id": "creator-123"
}
```

The completed response will contain:

```json
{
  "content_id": "unique-id",
  "guess": "human | unsure | ai",
  "confidence": 0.0,
  "label": "reader-facing label",
  "model_score": 0.0,
  "style_score": 0.0
}
```

`POST /appeal`

Input:

```json
{
  "content_id": "unique-id",
  "reasoning": "Why the writer believes the decision is incorrect."
}
```

A successful appeal will confirm that the content exists, record the reasoning, and change its status to `under_review`.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:**  
The model signal measures how predictable the submitted text is to the local GPT-2 language model. Lower perplexity means the model found the sequence easier to predict, which is converted into a higher AI-likelihood score.

**Why that might differ between human and AI writing:**  
Language models generate text by repeatedly selecting likely next tokens. Because of that, some AI-generated writing may contain more statistically predictable word sequences than naturally varied human writing.

**What it can't see:**  
Predictability is not proof of authorship. A real person who writes with common vocabulary, simple grammar, or short sentences can also produce highly predictable writing. A second-language writer or someone deliberately writing in plain English could therefore receive an artificially high AI score.

### Signal two — the style signal

**What it measures:**  
The style signal measures the structure or shape of the writing rather than its meaning. It will use features such as sentence-length variation, unique-word ratio, and punctuation density.

**Why that might differ between human and AI writing:**  
Human writing often contains irregular sentence lengths, individual vocabulary habits, and inconsistent punctuation choices. Generated text may sometimes appear more structurally regular or polished, so these features can provide information that differs from the language-model signal.

**What it can't see:**  
The style signal cannot understand what the text means or determine who actually wrote it. Small surface-level changes such as inserting punctuation, adding typos, changing sentence breaks, or replacing a few words can change the style measurements without changing the real authorship.

### The combining rule

**The rule:**  
The initial two-signal version will use a weighted average. Both signals point in the same direction, where a larger score means more likely AI-generated. The model signal and style signal will initially receive equal weight. When the signals strongly disagree, their average should move the combined result toward the unsure range instead of allowing one signal alone to make a high-confidence accusation.

**The numbers:**  
Model signal weight = `0.45`
Style signal weight = `0.35`
Repetition signal weight = `0.20`

Initial thresholds:

- `0.00–0.35` → high-confidence human
- above `0.35` and below `0.65` → unsure
- `0.65–1.00` → high-confidence AI

These values are defined in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

**A case where my signals split, and what my rule does with it:**

In one scoring test, model=0.90, style=0.10, and repetition=0.00 produced a combined score of 0.44. That falls in the unsure range. This shows that one strongly AI-like signal does not automatically create a high-confidence accusation when the other signals disagree.

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | Our signals strongly suggest this writing was written by a person. |
| unsure | above 0.35 and below 0.65 | Our signals do not give a clear result, so we are not making an authorship claim about this writing. |
| high-confidence AI | 0.65–1.00 | Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision. |

**Why I worded the "unsure" one this way:**  
I do not want an uncertain score to sound like an accusation. The label clearly says that the system does not have enough evidence to make an authorship claim, which is especially important because a real writer may be reading the result.

---

**A submission**

## Sample Run

### Submission

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"The system provides clear results. The system provides useful results. The system provides reliable results. The system provides consistent results. The system provides accurate results.","creator_id":"third-signal-test"}'
```

```json
{
  "confidence": 0.9424,
  "content_id": "c93ed807-fa03-46ff-9e35-b25d45958ac1",
  "guess": "ai",
  "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
  "model_score": 0.9072,
  "repetition_score": 0.94,
  "style_score": 0.9891
}
```

### Appeal

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"88325713-3ae2-4231-b47e-cb8a9127a3b4","reasoning":"I wrote this myself and believe the system made the wrong decision."}'
```

The appeal changed the status to:

```json
{
  "content_id": "88325713-3ae2-4231-b47e-cb8a9127a3b4",
  "status": "under_review",
  "message": "Your appeal was recorded and the item is now under review."
}
```

The audit log also records:

```json
{
  "content_id": "88325713-3ae2-4231-b47e-cb8a9127a3b4",
  "creator_id": "label-human",
  "event": "appeal",
  "status": "under_review",
  "reasoning": "I wrote this myself and believe the system made the wrong decision."
}
```

### Stretch — GET /content

```bash
curl "http://127.0.0.1:5000/content/2ec48116-d6f9-4273-8058-97342b27014f"
```

```json
{
  "confidence": 0.3648,
  "content_id": "2ec48116-d6f9-4273-8058-97342b27014f",
  "creator_credential": "verified-human",
  "creator_id": "verified-test-user",
  "guess": "unsure",
  "model_score": 0.4338,
  "repetition_score": 0.0,
  "status": "decided",
  "style_score": 0.4845,
  "verified_human": true
}
```

### Stretch — verified-human path

`POST /verify-human` returned:

```json
{
  "creator_id": "verified-test-user",
  "creator_credential": "verified-human",
  "verified_human": true
}
```

A later submission from the same creator also returned the `verified-human` credential, and the verification event is stored in `logs/audit.jsonl`.

## How I Used AI

**Moment 1**

- *What I asked for:* I asked AI to check whether the acceptance-criterion targets I was considering were actually measurable and testable.
- *What came back:* The review pointed out that allowing 9 or 10 false positives out of 10 would make the false-positive criterion meaningless, and that a score difference of 5 or 10 was impossible because the confidence scale only runs from 0 to 1.
- *What I changed:* I made the final choices myself and changed the targets to a maximum of 1 false positive out of 10 and a minimum score spread of 0.40. I also chose 3/3 reachable labels, 5/5 successful appeals, and 4/5 malformed-input cases handled safely.

**Moment 2**

- *What I asked for:* I asked AI to review the starter files and help me trace how a submission should move through the service, including identifying the blind spots of the two required signals.
- *What came back:* It described the path from `/submit` through the model signal, stylometry signal, combined score, label mapping, audit log, and appeal path. It also highlighted that model predictability is not the same as authorship and that stylometry can be changed by superficial edits.
- *What I changed:* I rewrote the ideas into the service description above and kept the two limitations explicit because they affect how I want the confidence thresholds and appeal process to behave.

---

## Unit 7 Stretch Features — Declared Before Building

I declared all three Unit 7 stretch features before building them, and all three are now implemented:

1. **Third signal:** add a third signal that measures a different property from the model and stylometry signals, and document how all three signals are weighted.
2. **GET /content/<id>:** add an endpoint that returns a submitted item's current status and relevant decision information.
3. **Verified-human path:** add an extra verification step through which a creator can earn a verified-human credential, and show that credential on their submitted content.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---
## Unit 8 Stretch Features — Declared Before Building

I plan to attempt all three Unit 8 stretch features before implementing them:

1. **Three attacks on another system:** I will write three original attacks against another team's Provenance Guard system, run them without changing that system, and report the outcome of each attack. I will only claim this stretch feature if I actually have access to another team's running system.

2. **Per-creator rate limiting:** I will key the `/submit` rate limit primarily to `creator_id` rather than only to the caller's network address. This should help catch repeated automated submissions from one creator identity, although a malicious caller could still rotate creator IDs.

3. **Second measured improvement:** After the required before-run diagnosis and first measured improvement, I will make a second diagnosis-driven change and measure it with another full comparable run.

---

## Rate Limiting

**My limits:** 10 submissions per minute and 200 submissions per day.

**Why those numbers and not others:**

A real writer should normally not need to submit more than 10 pieces of writing in one minute. A script attempting to map the detector's thresholds or repeatedly probe the service can send requests much faster than that.

The daily limit of 200 leaves substantial room for legitimate repeated use while putting a ceiling on sustained automated probing.

The limiter is keyed primarily by `creator_id` when a usable creator ID is present. Requests without a usable creator ID fall back to the caller's network address.

**What a caller counts as:**

For normal `/submit` requests, a caller is identified by `creator_id`. This catches a single creator rapidly sending repeated variations even when the service is accessed from a shared network.

The trade-off is that a malicious caller can rotate creator IDs, so this does not provide complete identity or abuse prevention.

**The run of status codes when I pushed past it:**

Produced by `run_attacks.py::run_flood` using 15 submissions from `flood_tester`:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

The first 10 requests were accepted and the final 5 were rejected with HTTP 429.

The rejected requests were also recorded in `logs/audit.jsonl` with `event: rejected`, `reason: rate_limited`, and `status: rejected`.

---
## Attack Run — Before

The complete staff attack set was run before changing the detector, signal weights, thresholds, or labels.

**Result:** 56 attacks total — **41 HELD, 15 BROKE**.

The table below is the real output from `run_attacks.py::main`, with each previously blank verdict manually judged from the attack target and service response.

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


### Ten audit log entries from the run

These entries include successful evasions, false-positive risk, malformed-input behavior, a successful AI detection, and a rate-limit rejection.

```json
[
  {
    "combined_score": 0.2478,
    "content_id": "2af41cfe-b49c-4dd4-81c9-0461319cbe60",
    "creator_credential": null,
    "creator_id": "attacker_EV01",
    "guess": "human",
    "label": "Our signals strongly suggest this writing was written by a person.",
    "model_score": 0.1635,
    "repetition_score": 0.0,
    "status": "decided",
    "style_score": 0.4978,
    "timestamp": "2026-11-08T16:13:41+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.2604,
    "content_id": "078f210d-e62b-4195-8130-dbff676a7b64",
    "creator_credential": null,
    "creator_id": "attacker_EV05",
    "guess": "human",
    "label": "Our signals strongly suggest this writing was written by a person.",
    "model_score": 0.3212,
    "repetition_score": 0.0,
    "status": "decided",
    "style_score": 0.3309,
    "timestamp": "2026-11-08T16:13:41+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.8588,
    "content_id": "fab9a640-7db0-4346-874e-f42c7a634a6e",
    "creator_credential": null,
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
    "model_score": 0.9792,
    "repetition_score": 0.85,
    "status": "decided",
    "style_score": 0.7091,
    "timestamp": "2026-11-08T16:13:42+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.6155,
    "content_id": "3eadea7b-56cd-4210-bff4-d98feea47908",
    "creator_credential": null,
    "creator_id": "attacker_FP05",
    "guess": "unsure",
    "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
    "model_score": 0.8005,
    "repetition_score": 0.084,
    "status": "decided",
    "style_score": 0.6813,
    "timestamp": "2026-11-08T16:13:42+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.6615,
    "content_id": "71960bbf-87e6-4f09-8991-96743a1849c0",
    "creator_credential": null,
    "creator_id": "attacker_FP07",
    "guess": "ai",
    "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
    "model_score": 0.8816,
    "repetition_score": 0.368,
    "status": "decided",
    "style_score": 0.5463,
    "timestamp": "2026-11-08T16:13:42+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.3455,
    "content_id": "6590c291-4a2e-4a02-a4a6-a3073e2a492f",
    "creator_credential": null,
    "creator_id": "attacker_PI05",
    "guess": "human",
    "label": "Our signals strongly suggest this writing was written by a person.",
    "model_score": 0.6401,
    "repetition_score": 0.0,
    "status": "decided",
    "style_score": 0.1643,
    "timestamp": "2026-11-08T16:13:42+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.168,
    "content_id": "bef992e3-692a-45e0-8883-7ae363561982",
    "creator_credential": null,
    "creator_id": "attacker_MF03",
    "guess": "human",
    "label": "Our signals strongly suggest this writing was written by a person.",
    "model_score": 0.0,
    "repetition_score": 0.0,
    "status": "decided",
    "style_score": 0.48,
    "timestamp": "2026-11-08T16:13:42+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.7566,
    "content_id": "3efc0aff-3399-4c0b-99df-f31debbbe00d",
    "creator_credential": null,
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
    "model_score": 0.9969,
    "repetition_score": 0.0,
    "status": "decided",
    "style_score": 0.88,
    "timestamp": "2026-11-08T16:13:43+00:00",
    "verified_human": false
  },
  {
    "combined_score": 0.7316,
    "content_id": "3d8c64e3-1c5c-4754-b6e1-ba2839d69289",
    "creator_credential": null,
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
    "model_score": 0.9064,
    "repetition_score": 0.0,
    "status": "decided",
    "style_score": 0.9248,
    "timestamp": "2026-11-08T16:13:43+00:00",
    "verified_human": false
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-08T16:13:43+00:00"
  }
]
```

### The single worst outcome

The worst result was **FP07**, a false-positive attack consisting of genuine human writing that deliberately repeated a phrase.

The service returned:

```text
guess: ai
combined score: 0.6615
model score: 0.8816
style score: 0.5463
repetition score: 0.3680
```

This is the outcome I would least want to explain to a real writer because the system crossed the high-confidence AI threshold and made an AI-facing authorship claim about writing that the attack set identifies as genuinely human.

The other seven false-positive attacks did not receive an AI label; they were either `human` or `unsure`.

---
## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | Maximum 1/10 clearly-human pieces labeled high-confidence AI |  |  |  |  |
| 2. Score spread | At least 0.40 difference between clearly-AI and clearly-human scores |  |  |  |  |
| 3. Label coverage | 3/3 labels reachable |  |  |  |  |
| 4. Appeal path | 5/5 valid appeals change status and are logged |  |  |  |  |
| 5. Bad input | At least 4/5 malformed inputs return controlled errors |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [x] criteria.md has five numbered criteria, each naming a target
       [x] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [x] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**