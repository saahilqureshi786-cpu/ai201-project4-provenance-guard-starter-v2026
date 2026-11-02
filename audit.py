"""
The audit log.

Every decision, appeal, rejection, and verification event is stored as
one JSON object per line.
"""

import json
import threading
from datetime import datetime, timezone

import config

_lock = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def log_decision(
    content_id: str,
    creator_id: str,
    guess: str | None = None,
    model_score: float | None = None,
    style_score: float | None = None,
    combined_score: float | None = None,
    label: str | None = None,
    status: str = "decided",
    **extra,
) -> dict:
    """Write one content decision to the audit log."""

    entry = {
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score,
        "label": label,
        "status": status,
    }

    entry.update(extra)

    return _append(entry)


def log_appeal(
    content_id: str,
    creator_id: str,
    reasoning: str,
) -> dict:
    """Record an appeal without overwriting the original decision."""

    return _append({
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": creator_id,
        "event": "appeal",
        "status": "under_review",
        "reasoning": reasoning,
    })


def log_verification(
    creator_id: str,
    method: str = "creator_confirmation",
) -> dict:
    """
    Record completion of the Unit 7 verified-human demo step.

    This is a project credential showing that the creator completed the
    additional verification workflow. It is not real-world identity proof.
    """

    return _append({
        "timestamp": _now(),
        "creator_id": creator_id,
        "event": "human_verification",
        "status": "verified",
        "credential": "verified-human",
        "verification_method": method,
    })


def creator_credential(creator_id: str) -> str | None:
    """
    Return the creator's latest verified-human credential, if one exists.
    """

    for entry in reversed(read_entries()):
        if (
            entry.get("creator_id") == creator_id
            and entry.get("event") == "human_verification"
            and entry.get("status") == "verified"
            and entry.get("credential") == "verified-human"
        ):
            return "verified-human"

    return None


def is_verified_human(creator_id: str) -> bool:
    """Return True if this creator completed the verification step."""

    return creator_credential(creator_id) == "verified-human"


def log_rejection(
    creator_id: str,
    reason: str,
    **extra,
) -> dict:
    """Record a request rejected before a normal decision was produced."""

    return _append({
        "timestamp": _now(),
        "creator_id": creator_id,
        "event": "rejected",
        "status": "rejected",
        "reason": reason,
        **extra,
    })


def _append(entry: dict) -> dict:
    """Append one JSON object to the audit log."""

    config.LOG_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    line = json.dumps(
        entry,
        ensure_ascii=False,
    )

    with _lock:
        with config.AUDIT_LOG.open(
            "a",
            encoding="utf-8",
        ) as file:
            file.write(line + "\n")

    return entry


def read_entries(limit: int | None = None) -> list[dict]:
    """Read audit entries oldest first."""

    if not config.AUDIT_LOG.exists():
        return []

    entries = []

    for line in config.AUDIT_LOG.read_text(
        encoding="utf-8",
    ).splitlines():
        line = line.strip()

        if not line:
            continue

        try:
            entries.append(
                json.loads(line)
            )
        except json.JSONDecodeError:
            continue

    return entries[-limit:] if limit else entries


def clear() -> int:
    """Delete the audit log and return the number of entries removed."""

    count = len(read_entries())

    if config.AUDIT_LOG.exists():
        config.AUDIT_LOG.unlink()

    return count


def entries_for(content_id: str) -> list[dict]:
    """Return every audit entry for one content ID."""

    return [
        entry
        for entry in read_entries()
        if entry.get("content_id") == content_id
    ]