# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives

Of 10 pieces of writing that I judge to be clearly human-written, no more than 1 should receive the high-confidence AI label.

**Why this target:**  
I chose this target because falsely accusing a real writer is more harmful than letting some AI-written text pass through. I want the system to be cautious before giving the strongest AI label.

---

## 2. Score spread

The combined score for clearly AI-written text and clearly human-written text should differ by at least 0.40.

**Why this target:**  
I chose a 0.40 difference because clearly different examples should not end up with almost the same confidence score. A noticeable gap shows that the signals are actually separating obvious cases.

---

## 3. Label coverage

I should be able to deliberately create test inputs that reach all 3 of the 3 possible labels: high-confidence human, unsure, and high-confidence AI.

**Why this target:**  
All three labels need to be reachable because each represents a different level of certainty. If one label can never appear, then part of the system is not actually useful.

---

## 4. Appeal path

For 5 out of 5 valid appeals, the content status should change to `under_review` and the appeal should also appear in the audit log.

**Why this target:**  
I chose 5 out of 5 because the appeal process is the writer's way to challenge a decision. A valid appeal should always be recorded and should never disappear without changing the item's status.

---

## 5. Bad input

At least 4 out of 5 malformed submission requests should return a controlled error response instead of crashing the service.

**Why this target:**  
I chose 4 out of 5 because the service should handle most common input mistakes safely. I am leaving room for one unusual edge case that may reveal something I need to improve during testing.

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
