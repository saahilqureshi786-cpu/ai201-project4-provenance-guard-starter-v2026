"""
Unit 9 structured operational logging.
"""

import json
import threading
from datetime import datetime, timezone

import config

RUN_LOG = config.LOG_DIR / "run_log.jsonl"
_LOCK = threading.Lock()


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def summarize_input(payload):
    if not isinstance(payload, dict):
        return {"body_type": type(payload).__name__}

    text = payload.get("text")
    creator_id = payload.get("creator_id")

    result = {
        "creator_id": creator_id if isinstance(creator_id, str) else None,
    }

    if isinstance(text, str):
        result["text_length"] = len(text)
        result["text_preview"] = text.strip()[:80]
    else:
        result["text_type"] = type(text).__name__

    return result


def summarize_output(payload):
    if not isinstance(payload, dict):
        return {"body_type": type(payload).__name__}

    keys = [
        "content_id",
        "guess",
        "confidence",
        "status",
        "error",
        "message",
    ]

    return {key: payload.get(key) for key in keys if key in payload}


def log_run(
    *,
    method,
    path,
    input_data,
    output_data,
    status_code,
    duration_ms,
    stage_timings_ms=None,
    error=None,
):
    entry = {
        "timestamp": _now(),
        "method": method,
        "path": path,
        "input": input_data,
        "output": output_data,
        "status_code": status_code,
        "success": 200 <= status_code < 400,
        "duration_ms": round(float(duration_ms), 3),
    }

    if stage_timings_ms:
        entry["stage_timings_ms"] = {
            key: round(float(value), 3)
            for key, value in stage_timings_ms.items()
        }

    if error:
        entry["error_detail"] = error

    config.LOG_DIR.mkdir(parents=True, exist_ok=True)

    with _LOCK:
        with RUN_LOG.open("a", encoding="utf-8") as file:
            file.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return entry


def read_entries(limit=None):
    if not RUN_LOG.exists():
        return []

    entries = []

    for line in RUN_LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line:
            continue

        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return entries[-limit:] if limit else entries


def clear():
    count = len(read_entries())

    if RUN_LOG.exists():
        RUN_LOG.unlink()

    return count
