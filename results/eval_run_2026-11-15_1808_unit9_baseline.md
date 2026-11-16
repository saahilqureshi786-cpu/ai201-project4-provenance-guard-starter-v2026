# Evaluation run — unit9_baseline

- Produced by: `run_eval.py::main`
- Service: `app.py::submit`
- Trials per criterion: **3**

## Run Log

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
|---|---|---|---|---|---|
| 1 | At most 1 of 10 clearly-human pieces labeled AI | PASS — 0/10 labeled AI | PASS — 0/10 labeled AI | PASS — 0/10 labeled AI | **MET** |
| 2 | At least 0.40 combined-score spread | PASS — score spread = 0.7041 | PASS — score spread = 0.7041 | PASS — score spread = 0.7041 | **MET** |
| 3 | All 3 labels reachable | PASS — labels reached = ai, human, unsure | PASS — labels reached = ai, human, unsure | PASS — labels reached = ai, human, unsure | **MET** |
| 4 | 5 of 5 appeals under_review and logged | PASS — 5/5 appeals under_review and logged | PASS — 5/5 appeals under_review and logged | PASS — 5/5 appeals under_review and logged | **MET** |
| 5 | At least 4 of 5 malformed requests return controlled errors | PASS — 5/5 controlled errors | PASS — 5/5 controlled errors | PASS — 5/5 controlled errors | **MET** |

## Real output from each criterion

### Criterion 1

Trial 1 result: PASS

Metric: `0/10 labeled AI`

```json
[
  {
    "item": 1,
    "creator_id": "eval_c1_t1_item1",
    "status_code": 200,
    "payload": {
      "confidence": 0.2186,
      "content_id": "fe5e1168-1118-4561-b3aa-5a489e0212c5",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.0394,
      "repetition_score": 0.0,
      "style_score": 0.574,
      "verified_human": false
    }
  },
  {
    "item": 2,
    "creator_id": "eval_c1_t1_item2",
    "status_code": 200,
    "payload": {
      "confidence": 0.2989,
      "content_id": "5005bdf1-c9fb-4558-8a57-109c8dc5efff",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.2328,
      "repetition_score": 0.0,
      "style_score": 0.5547,
      "verified_human": false
    }
  },
  {
    "item": 3,
    "creator_id": "eval_c1_t1_item3",
    "status_code": 200,
    "payload": {
      "confidence": 0.3802,
      "content_id": "b0de673c-9fc7-44ab-846c-4da319105562",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.4184,
      "repetition_score": 0.0,
      "style_score": 0.5484,
      "verified_human": false
    }
  },
  {
    "item": 4,
    "creator_id": "eval_c1_t1_item4",
    "status_code": 200,
    "payload": {
      "confidence": 0.3035,
      "content_id": "8a2ef64b-88d4-49c8-8c3d-810f8367626c",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.2127,
      "repetition_score": 0.0,
      "style_score": 0.5937,
      "verified_human": false
    }
  },
  {
    "item": 5,
    "creator_id": "eval_c1_t1_item5",
    "status_code": 200,
    "payload": {
      "confidence": 0.2752,
      "content_id": "775d4432-ab80-4364-99da-612857a08622",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.149,
      "repetition_score": 0.0,
      "style_score": 0.5947,
      "verified_human": false
    }
  },
  {
    "item": 6,
    "creator_id": "eval_c1_t1_item6",
    "status_code": 200,
    "payload": {
      "confidence": 0.1883,
      "content_id": "a9fad793-3a95-4fc9-855a-0d5a5a60fd17",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.0041,
      "repetition_score": 0.0,
      "style_score": 0.5328,
      "verified_human": false
    }
  },
  {
    "item": 7,
    "creator_id": "eval_c1_t1_item7",
    "status_code": 200,
    "payload": {
      "confidence": 0.2165,
      "content_id": "a0b4d59b-ac89-4f6b-b6b6-522ed9d8bda2",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.0437,
      "repetition_score": 0.0,
      "style_score": 0.5624,
      "verified_human": false
    }
  },
  {
    "item": 8,
    "creator_id": "eval_c1_t1_item8",
    "status_code": 200,
    "payload": {
      "confidence": 0.2893,
      "content_id": "b6b427e5-010e-402a-9204-c44f0cda0882",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.1788,
      "repetition_score": 0.0,
      "style_score": 0.5968,
      "verified_human": false
    }
  },
  {
    "item": 9,
    "creator_id": "eval_c1_t1_item9",
    "status_code": 200,
    "payload": {
      "confidence": 0.4073,
      "content_id": "61454e1e-954a-440e-b62c-0d5a8e5cffe9",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.465,
      "repetition_score": 0.0,
      "style_score": 0.566,
      "verified_human": false
    }
  },
  {
    "item": 10,
    "creator_id": "eval_c1_t1_item10",
    "status_code": 200,
    "payload": {
      "confidence": 0.2278,
      "content_id": "2b46276b-698e-45c3-b375-acccbbac557d",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.0678,
      "repetition_score": 0.0,
      "style_score": 0.5636,
      "verified_human": false
    }
  }
]
```

### Criterion 2

Trial 1 result: PASS

Metric: `score spread = 0.7041`

```json
[
  {
    "item": 1,
    "creator_id": "eval_c2_t1_item1",
    "status_code": 200,
    "payload": {
      "confidence": 0.2658,
      "content_id": "77b6606d-2437-4405-b049-99443a8dd0ad",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.2654,
      "repetition_score": 0.0,
      "style_score": 0.4182,
      "verified_human": false
    }
  },
  {
    "item": 2,
    "creator_id": "eval_c2_t1_item2",
    "status_code": 200,
    "payload": {
      "confidence": 0.9699,
      "content_id": "e5af39c6-f2b2-420b-8dea-3b90c16e8de4",
      "creator_credential": null,
      "guess": "ai",
      "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
      "model_score": 0.951,
      "repetition_score": 0.9625,
      "style_score": 0.9984,
      "verified_human": false
    }
  }
]
```

### Criterion 3

Trial 1 result: PASS

Metric: `labels reached = ai, human, unsure`

```json
[
  {
    "item": 1,
    "creator_id": "eval_c3_t1_item1",
    "status_code": 200,
    "payload": {
      "confidence": 0.5221,
      "content_id": "a53504bb-3ee2-409d-a2ba-eec9f653e2bb",
      "creator_credential": null,
      "guess": "unsure",
      "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
      "model_score": 0.6472,
      "repetition_score": 0.0,
      "style_score": 0.6595,
      "verified_human": false
    }
  },
  {
    "item": 2,
    "creator_id": "eval_c3_t1_item2",
    "status_code": 200,
    "payload": {
      "confidence": 0.4093,
      "content_id": "a7672fe8-aca5-45fc-91d9-ab383051d52b",
      "creator_credential": null,
      "guess": "human",
      "label": "Our signals strongly suggest this writing was written by a person.",
      "model_score": 0.5555,
      "repetition_score": 0.0,
      "style_score": 0.4553,
      "verified_human": false
    }
  },
  {
    "item": 3,
    "creator_id": "eval_c3_t1_item3",
    "status_code": 200,
    "payload": {
      "confidence": 0.9699,
      "content_id": "69cf99e9-2c40-4032-8940-d144949ced11",
      "creator_credential": null,
      "guess": "ai",
      "label": "Our signals strongly suggest this writing may be AI-generated. This result is not proof of authorship, and the writer can appeal the decision.",
      "model_score": 0.951,
      "repetition_score": 0.9625,
      "style_score": 0.9984,
      "verified_human": false
    }
  }
]
```

### Criterion 4

Trial 1 result: PASS

Metric: `5/5 appeals under_review and logged`

```json
[
  {
    "item": 1,
    "creator_id": "eval_c4_t1_item1",
    "submission": {
      "status_code": 200,
      "payload": {
        "confidence": 0.234,
        "content_id": "e60b48e4-1336-4ae1-82e5-aa2c30b825f3",
        "creator_credential": null,
        "guess": "human",
        "label": "Our signals strongly suggest this writing was written by a person.",
        "model_score": 0.1057,
        "repetition_score": 0.0,
        "style_score": 0.5328,
        "verified_human": false
      }
    },
    "appeal": {
      "status_code": 200,
      "payload": {
        "appeal": {
          "content_id": "e60b48e4-1336-4ae1-82e5-aa2c30b825f3",
          "creator_id": "eval_c4_t1_item1",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:08:56+00:00"
        },
        "content_id": "e60b48e4-1336-4ae1-82e5-aa2c30b825f3",
        "message": "Your appeal was recorded and the item is now under review.",
        "status": "under_review"
      }
    },
    "response_under_review": true,
    "logged_under_review": true
  },
  {
    "item": 2,
    "creator_id": "eval_c4_t1_item2",
    "submission": {
      "status_code": 200,
      "payload": {
        "confidence": 0.2128,
        "content_id": "d8e57cf5-5ed9-47cb-9216-c6d690a54c22",
        "creator_credential": null,
        "guess": "human",
        "label": "Our signals strongly suggest this writing was written by a person.",
        "model_score": 0.0592,
        "repetition_score": 0.0,
        "style_score": 0.532,
        "verified_human": false
      }
    },
    "appeal": {
      "status_code": 200,
      "payload": {
        "appeal": {
          "content_id": "d8e57cf5-5ed9-47cb-9216-c6d690a54c22",
          "creator_id": "eval_c4_t1_item2",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:08:56+00:00"
        },
        "content_id": "d8e57cf5-5ed9-47cb-9216-c6d690a54c22",
        "message": "Your appeal was recorded and the item is now under review.",
        "status": "under_review"
      }
    },
    "response_under_review": true,
    "logged_under_review": true
  },
  {
    "item": 3,
    "creator_id": "eval_c4_t1_item3",
    "submission": {
      "status_code": 200,
      "payload": {
        "confidence": 0.2501,
        "content_id": "7564e2d7-3a92-4916-b378-b604d5b9a3e3",
        "creator_credential": null,
        "guess": "human",
        "label": "Our signals strongly suggest this writing was written by a person.",
        "model_score": 0.0895,
        "repetition_score": 0.0,
        "style_score": 0.5996,
        "verified_human": false
      }
    },
    "appeal": {
      "status_code": 200,
      "payload": {
        "appeal": {
          "content_id": "7564e2d7-3a92-4916-b378-b604d5b9a3e3",
          "creator_id": "eval_c4_t1_item3",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:08:56+00:00"
        },
        "content_id": "7564e2d7-3a92-4916-b378-b604d5b9a3e3",
        "message": "Your appeal was recorded and the item is now under review.",
        "status": "under_review"
      }
    },
    "response_under_review": true,
    "logged_under_review": true
  },
  {
    "item": 4,
    "creator_id": "eval_c4_t1_item4",
    "submission": {
      "status_code": 200,
      "payload": {
        "confidence": 0.2154,
        "content_id": "626a5941-8ff6-408b-bf64-24e2f17b3846",
        "creator_credential": null,
        "guess": "human",
        "label": "Our signals strongly suggest this writing was written by a person.",
        "model_score": 0.0235,
        "repetition_score": 0.0,
        "style_score": 0.5852,
        "verified_human": false
      }
    },
    "appeal": {
      "status_code": 200,
      "payload": {
        "appeal": {
          "content_id": "626a5941-8ff6-408b-bf64-24e2f17b3846",
          "creator_id": "eval_c4_t1_item4",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:08:56+00:00"
        },
        "content_id": "626a5941-8ff6-408b-bf64-24e2f17b3846",
        "message": "Your appeal was recorded and the item is now under review.",
        "status": "under_review"
      }
    },
    "response_under_review": true,
    "logged_under_review": true
  },
  {
    "item": 5,
    "creator_id": "eval_c4_t1_item5",
    "submission": {
      "status_code": 200,
      "payload": {
        "confidence": 0.2016,
        "content_id": "9f11d057-5c1d-4be1-9545-382317b4e3eb",
        "creator_credential": null,
        "guess": "human",
        "label": "Our signals strongly suggest this writing was written by a person.",
        "model_score": 0.039,
        "repetition_score": 0.0,
        "style_score": 0.526,
        "verified_human": false
      }
    },
    "appeal": {
      "status_code": 200,
      "payload": {
        "appeal": {
          "content_id": "9f11d057-5c1d-4be1-9545-382317b4e3eb",
          "creator_id": "eval_c4_t1_item5",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:08:56+00:00"
        },
        "content_id": "9f11d057-5c1d-4be1-9545-382317b4e3eb",
        "message": "Your appeal was recorded and the item is now under review.",
        "status": "under_review"
      }
    },
    "response_under_review": true,
    "logged_under_review": true
  }
]
```

### Criterion 5

Trial 1 result: PASS

Metric: `5/5 controlled errors`

```json
[
  {
    "item": 1,
    "body_summary": {
      "text": "",
      "creator_id": "eval_bad_empty_t1"
    },
    "controlled_error": true,
    "status_code": 400,
    "payload": {
      "error": "invalid_text",
      "message": "text must be a non-empty string."
    }
  },
  {
    "item": 2,
    "body_summary": {
      "creator_id": "eval_bad_missing_t1"
    },
    "controlled_error": true,
    "status_code": 400,
    "payload": {
      "error": "invalid_text",
      "message": "text must be a non-empty string."
    }
  },
  {
    "item": 3,
    "body_summary": {
      "text": null,
      "creator_id": "eval_bad_null_t1"
    },
    "controlled_error": true,
    "status_code": 400,
    "payload": {
      "error": "invalid_text",
      "message": "text must be a non-empty string."
    }
  },
  {
    "item": 4,
    "body_summary": {
      "text": 12345,
      "creator_id": "eval_bad_number_t1"
    },
    "controlled_error": true,
    "status_code": 400,
    "payload": {
      "error": "invalid_text",
      "message": "text must be a non-empty string."
    }
  },
  {
    "item": 5,
    "body_summary": {
      "text": "<string length 25000>",
      "creator_id": "eval_bad_large_t1"
    },
    "controlled_error": true,
    "status_code": 413,
    "payload": {
      "error": "text_too_large",
      "message": "text must contain 20,000 characters or fewer."
    }
  }
]
```
