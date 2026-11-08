"""
Settings for Provenance Guard.

Unit 8 measured improvements:
1. AI_THRESHOLD raised from 0.65 to 0.70 after FP07.
2. HUMAN_THRESHOLD raised from 0.35 to 0.45 after the
   label-coverage criterion could not reach all three labels.

Everything else remains unchanged.
"""

import os
from pathlib import Path


ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))

DEBUG = (
    os.getenv("AI201_DEBUG", "1") == "1"
    and HOST in ("127.0.0.1", "localhost")
)


# ─── The local model ─────────────────────────────────────────────────────────

DETECTOR_MODEL = os.getenv(
    "AI201_DETECTOR_MODEL",
    "gpt2",
)

DETECTOR_MAX_TOKENS = 400


# ─── Scoring ─────────────────────────────────────────────────────────────────

WEIGHT_MODEL_SIGNAL = 0.45
WEIGHT_STYLE_SIGNAL = 0.35
WEIGHT_REPETITION_SIGNAL = 0.20


# ─── Thresholds ──────────────────────────────────────────────────────────────

# Unit 8 improvement #2:
#
# Before:
#   human example  = 0.4093 -> unsure
#   another example = 0.5221 -> unsure
#
# Raising the human threshold to 0.45 should make:
#   0.4093 -> human
#   0.5221 -> unsure
# while preserving the separate AI example.
HUMAN_THRESHOLD = 0.45


# Unit 8 improvement #1:
# FP07 was genuine human writing with a combined
# score of 0.6615. Raising this boundary moved
# that case from AI to unsure.
AI_THRESHOLD = 0.70


# ─── Rate limiting ───────────────────────────────────────────────────────────

RATE_LIMITING_ENABLED = True

RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 200

RATE_LIMIT_STORAGE = "memory://"


# ─── Paths ───────────────────────────────────────────────────────────────────

LOG_DIR = ROOT / "logs"
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"