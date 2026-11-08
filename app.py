#!/usr/bin/env python3
"""
Provenance Guard — the web service.

Unit 7:
- POST /submit
- three signals
- combined confidence
- three reader-facing labels
- POST /appeal
- GET /content/<id>
- POST /verify-human
- audit logging

Unit 8:
- rate limiting on /submit
- per-creator limiting when creator_id is available
- rejected requests logged
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config

app = Flask(__name__)

VERIFICATION_STATEMENT = (
    "I confirm that I am the author submitting my own work."
)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────

class _LimiterOff:
    """No-op limiter if rate limiting is disabled."""

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()


if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Use creator_id as the caller identity whenever possible.

        If the request has no usable creator_id, fall back to the
        caller's network address.
        """

        payload = request.get_json(silent=True)

        if isinstance(payload, dict):
            creator_id = payload.get("creator_id")

            if isinstance(creator_id, str) and creator_id.strip():
                return creator_id.strip()

        return get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        Return a controlled JSON response and record the rejection
        in the audit log.
        """

        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            payload = {}

        creator_id = payload.get("creator_id")

        if not isinstance(creator_id, str) or not creator_id.strip():
            creator_id = "unknown"
        else:
            creator_id = creator_id.strip()

        audit.log_rejection(
            creator_id=creator_id,
            reason="rate_limited",
            limit=str(exc.description),
        )

        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── Basic routes ──────────────────────────────────────────────────────────

@app.post("/ping")
def ping():
    payload = request.get_json(silent=True) or {}

    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    import detector

    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": detector._model is not None,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "rate_limit_per_minute": config.RATE_LIMIT_PER_MINUTE,
        "rate_limit_per_day": config.RATE_LIMIT_PER_DAY,
        "log_entries": len(audit.read_entries()),
    })


# ── Verified-human path — Unit 7 stretch ─────────────────────────────────

@app.post("/verify-human")
def verify_human():
    """
    Give a creator the demo verified-human credential after
    completing an explicit confirmation step.

    This demonstrates a provenance path.
    It is not real-world identity proof.
    """

    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_json",
            "message": "Request body must be a JSON object.",
        }), 400

    creator_id = payload.get("creator_id")
    statement = payload.get("statement")

    if not isinstance(creator_id, str) or not creator_id.strip():
        return jsonify({
            "error": "invalid_creator_id",
            "message": "creator_id must be a non-empty string.",
        }), 400

    if not isinstance(statement, str):
        return jsonify({
            "error": "invalid_statement",
            "message": "A verification statement is required.",
        }), 400

    creator_id = creator_id.strip()
    statement = statement.strip()

    if statement != VERIFICATION_STATEMENT:
        return jsonify({
            "error": "verification_failed",
            "message": (
                "The verification statement did not match the "
                "required confirmation."
            ),
            "required_statement": VERIFICATION_STATEMENT,
        }), 400

    verification = audit.log_verification(
        creator_id=creator_id,
        method="creator_confirmation",
    )

    return jsonify({
        "creator_id": creator_id,
        "verified_human": True,
        "creator_credential": "verified-human",
        "message": (
            "Verification step completed. Future submissions from "
            "this creator will display the verified-human credential."
        ),
        "verification": verification,
    })


# ── Submission route ──────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(
    f"{config.RATE_LIMIT_PER_MINUTE}/minute;"
    f"{config.RATE_LIMIT_PER_DAY}/day"
)
def submit():
    """
    Run the three provenance signals and return a decision.

    Unit 8 adds rate limiting around this route, but the detector,
    scoring weights, thresholds, signals, and labels remain unchanged
    during the before-testing phase.
    """

    import detector
    import repetition_signal
    import scoring
    import stylometry

    payload = request.get_json(silent=True)

    # Request body must be JSON.
    if not isinstance(payload, dict):
        audit.log_rejection(
            creator_id="unknown",
            reason="invalid_json",
        )

        return jsonify({
            "error": "invalid_json",
            "message": "Request body must be a JSON object.",
        }), 400

    text = payload.get("text")
    creator_id = payload.get("creator_id")

    # Validate text.
    if not isinstance(text, str) or not text.strip():
        audit.log_rejection(
            creator_id=(
                creator_id.strip()
                if isinstance(creator_id, str) and creator_id.strip()
                else "unknown"
            ),
            reason="missing_or_empty_text",
        )

        return jsonify({
            "error": "invalid_text",
            "message": "text must be a non-empty string.",
        }), 400

    # Validate creator ID.
    if not isinstance(creator_id, str) or not creator_id.strip():
        audit.log_rejection(
            creator_id="unknown",
            reason="missing_creator_id",
        )

        return jsonify({
            "error": "invalid_creator_id",
            "message": "creator_id must be a non-empty string.",
        }), 400

    text = text.strip()
    creator_id = creator_id.strip()

    # Reject extremely large submissions.
    if len(text) > 20000:
        audit.log_rejection(
            creator_id=creator_id,
            reason="text_too_large",
            text_length=len(text),
        )

        return jsonify({
            "error": "text_too_large",
            "message": "text must contain 20,000 characters or fewer.",
        }), 413

    content_id = str(uuid.uuid4())

    # ── Signal 1: GPT-2 predictability ────────────────────────────────

    try:
        model_score = detector.model_signal(text)

    except ValueError as exc:
        audit.log_rejection(
            creator_id=creator_id,
            reason="text_too_short",
        )

        return jsonify({
            "error": "text_too_short",
            "message": str(exc),
        }), 400

    except detector.DetectorUnavailable as exc:
        audit.log_rejection(
            creator_id=creator_id,
            reason="detector_unavailable",
        )

        return jsonify({
            "error": "detector_unavailable",
            "message": str(exc),
        }), 503

    # ── Signal 2: stylometry ──────────────────────────────────────────

    style_score = stylometry.style_signal(text)

    # ── Signal 3: repetition ──────────────────────────────────────────

    repetition_score = repetition_signal.repetition_signal(text)

    # ── Combine signals ───────────────────────────────────────────────

    combined_score = scoring.combine_signals(
        model_score,
        style_score,
        repetition_score,
    )

    guess, label = scoring.score_to_label(combined_score)

    # ── Creator credential ────────────────────────────────────────────

    creator_credential = audit.creator_credential(creator_id)
    verified_human = creator_credential == "verified-human"

    # ── Audit decision ────────────────────────────────────────────────

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        label=label,
        status="decided",
        repetition_score=repetition_score,
        verified_human=verified_human,
        creator_credential=creator_credential,
    )

    # ── Response ──────────────────────────────────────────────────────

    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": combined_score,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "repetition_score": repetition_score,
        "verified_human": verified_human,
        "creator_credential": creator_credential,
    })


# ── Appeal route ──────────────────────────────────────────────────────────

@app.post("/appeal")
def appeal():
    """Allow a writer to challenge a decision."""

    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_json",
            "message": "Request body must be a JSON object.",
        }), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")

    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify({
            "error": "invalid_content_id",
            "message": "content_id must be a non-empty string.",
        }), 400

    if not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify({
            "error": "invalid_reasoning",
            "message": "reasoning must be a non-empty string.",
        }), 400

    content_id = content_id.strip()
    reasoning = reasoning.strip()

    entries = audit.entries_for(content_id)

    if not entries:
        return jsonify({
            "error": "content_not_found",
            "message": "No submitted content exists with that content_id.",
        }), 404

    original_decision = next(
        (
            entry
            for entry in entries
            if entry.get("guess") is not None
        ),
        None,
    )

    if original_decision is None:
        return jsonify({
            "error": "decision_not_found",
            "message": "No original decision was found.",
        }), 404

    creator_id = original_decision.get(
        "creator_id",
        "unknown",
    )

    appeal_entry = audit.log_appeal(
        content_id=content_id,
        creator_id=creator_id,
        reasoning=reasoning,
    )

    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "message": (
            "Your appeal was recorded and the item is now under review."
        ),
        "appeal": appeal_entry,
    })


# ── Content lookup — Unit 7 stretch ───────────────────────────────────────

@app.get("/content/<content_id>")
def get_content(content_id):
    """Return the current status and provenance information."""

    entries = audit.entries_for(content_id)

    if not entries:
        return jsonify({
            "error": "content_not_found",
            "message": "No submitted content exists with that content_id.",
        }), 404

    original_decision = next(
        (
            entry
            for entry in entries
            if entry.get("guess") is not None
        ),
        None,
    )

    if original_decision is None:
        return jsonify({
            "error": "decision_not_found",
            "message": "No original decision exists for this content.",
        }), 404

    latest_entry = entries[-1]
    creator_id = original_decision.get("creator_id")

    current_credential = audit.creator_credential(
        creator_id
    )

    response = {
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": original_decision.get("guess"),
        "confidence": original_decision.get(
            "combined_score"
        ),
        "label": original_decision.get("label"),
        "model_score": original_decision.get(
            "model_score"
        ),
        "style_score": original_decision.get(
            "style_score"
        ),
        "repetition_score": original_decision.get(
            "repetition_score"
        ),
        "status": latest_entry.get(
            "status",
            original_decision.get(
                "status",
                "decided",
            ),
        ),
        "verified_human": (
            current_credential == "verified-human"
        ),
        "creator_credential": current_credential,
    }

    if latest_entry.get("event") == "appeal":
        response["appeal_reasoning"] = (
            latest_entry.get("reasoning")
        )

    return jsonify(response)


# ── Audit log ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    limit = request.args.get(
        "limit",
        type=int,
    )

    entries = audit.read_entries(
        limit=limit
    )

    return jsonify({
        "count": len(entries),
        "entries": entries,
    })


# ── Run service ───────────────────────────────────────────────────────────

def main():
    print(
        f"Provenance Guard on "
        f"http://{config.HOST}:{config.PORT}"
    )

    print(
        f"  detector model:      "
        f"{config.DETECTOR_MODEL}"
    )

    print(
        f"  rate limiting:       "
        f"{'ON' if config.RATE_LIMITING_ENABLED else 'OFF'}"
    )

    print(
        f"  per-minute limit:    "
        f"{config.RATE_LIMIT_PER_MINUTE}"
    )

    print(
        f"  per-day limit:       "
        f"{config.RATE_LIMIT_PER_DAY}"
    )

    print(
        f"  audit log:           "
        f"{config.AUDIT_LOG}"
    )

    print()

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )


if __name__ == "__main__":
    main()