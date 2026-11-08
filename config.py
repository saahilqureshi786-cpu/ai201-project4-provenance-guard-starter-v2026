"""
Settings for Provenance Guard.

Unit 8 improvement #1:
AI_THRESHOLD is raised from 0.65 to 0.70 in response to FP07.

Everything else stays unchanged so the before/after comparison remains valid.
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

HUMAN_THRESHOLD = 0.35

# Unit 8 improvement #1:
# FP07 was genuine human writing but scored 0.6615,
# slightly above the old 0.65 AI threshold.
# Raising the threshold to 0.70 should move that case
# from high-confidence AI to unsure.
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