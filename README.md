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

**A case where my two signals split, and what my rule does with it:**  
To be completed after I build the style signal and run both signals over the same calibration examples. I will use a real observed disagreement rather than inventing one before the second signal exists.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | Our signals strongly suggest this writing was written by a person. |
| unsure | above 0.35 and below 0.65 | Our signals do not give a clear result, so we are not making an authorship claim about this writing. |
| high-confidence AI | 0.65–1.00 | Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision. |

**Why I worded the "unsure" one this way:**  
I do not want an uncertain score to sound like an accusation. The label clearly says that the system does not have enough evidence to make an authorship claim, which is especially important because a real writer may be reading the result.

---

## Sample Run

The real submission, appeal, and log output will be pasted here after the endpoints are implemented and tested. I am leaving the outputs blank for now rather than inventing results that have not happened.

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

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

I plan to attempt all three Unit 7 stretch features:

1. **Third signal:** add a third signal that measures a different property from the model and stylometry signals, and document how all three signals are weighted.
2. **GET /content/<id>:** add an endpoint that returns a submitted item's current status and relevant decision information.
3. **Verified-human path:** add an extra verification step through which a creator can earn a verified-human credential, and show that credential on their submitted content.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



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