#!/usr/bin/env python3
"""
Provenance Guard — the web service.

Unit 7:
- POST /submit accepts writing and scores it with two different signals.
- POST /appeal is completed in Milestone 5.
- GET /log and GET /health expose service information.
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────

class _LimiterOff:
    """No-op limiter while Unit 8 rate limiting is disabled."""

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()

if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            return get_remote_address()

        creator = payload.get("creator_id")

        if isinstance(creator, str) and creator.strip():
            return creator

        return get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            payload = {}

        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )

        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── Starter routes ────────────────────────────────────────────────────────

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

    loaded = detector._model is not None

    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── Milestone 4: two signals and combined score ───────────────────────────

@app.post("/submit")
# @limiter.limit(
#     f"{config.RATE_LIMIT_PER_MINUTE}/minute;"
#     f"{config.RATE_LIMIT_PER_DAY}/day"
# )
def submit():
    """
    Accept text and creator_id.

    The route:
    1. validates the request
    2. runs the GPT-2 model signal
    3. runs the stylometry signal
    4. combines both scores
    5. logs all scores
    6. returns structured JSON

    Milestone 5 adds the final reader-facing label.
    """

    import detector
    import scoring
    import stylometry

    payload = request.get_json(silent=True)

    # JSON must be an object.
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
                creator_id
                if isinstance(creator_id, str)
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

    # Reject unusually large submissions.
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

    # ── Signal one: model predictability ──────────────────────────────

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
        return jsonify({
            "error": "detector_unavailable",
            "message": str(exc),
        }), 503

    # ── Signal two: writing style ─────────────────────────────────────

    style_score = stylometry.style_signal(text)

    # ── Combine both signals ──────────────────────────────────────────

    combined_score = scoring.combine_signals(
        model_score,
        style_score,
    )

    # The final guess and label are deliberately completed in Milestone 5.
    guess = "pending"
    label = "Final reader-facing label will be added in Milestone 5."

    # For this project, the combined 0–1 score is returned as confidence.
    confidence = combined_score

    # ── Audit log ─────────────────────────────────────────────────────

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined_score,
        label=label,
        status="decided",
    )

    # ── Response ──────────────────────────────────────────────────────

    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": confidence,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
    })


# ── Milestone 5: appeal ───────────────────────────────────────────────────

@app.post("/appeal")
def appeal():
    """
    Appeal remains intentionally unfinished until Milestone 5.
    """

    payload = request.get_json(silent=True) or {}

    return jsonify({
        "error": "not_implemented",
        "message": "POST /appeal is built in Milestone 5.",
        "you_sent": payload,
    }), 501


# ── Audit log ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)

    return jsonify({
        "count": len(entries),
        "entries": entries,
    })


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(
        f"  rate limiting:   "
        f"{'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}"
    )
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )


if __name__ == "__main__":
    main()