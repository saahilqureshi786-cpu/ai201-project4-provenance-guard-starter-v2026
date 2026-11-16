# Evaluation run — unit9_after2

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
      "content_id": "f864e46e-ae63-4fdb-90f3-5c968762180d",
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
      "content_id": "86c20f99-7dc0-4f50-9762-2b34dc34e99f",
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
      "content_id": "3e51b260-c2e6-413d-ae59-1936db7e13ae",
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
      "content_id": "082afb34-5092-4dca-9e3e-da6623103ad5",
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
      "content_id": "73ef2184-d111-46c0-adb3-195264a85dc4",
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
      "content_id": "ca96ca10-8d59-4dae-8ed2-47914f8b8ab2",
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
      "content_id": "73636cae-6230-4370-832a-a96dc16a7a19",
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
      "content_id": "228d5121-e671-49b4-9a7d-90d3472a1a37",
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
      "content_id": "dacdb0e3-1b2b-40f2-94be-f9fd8b55bd57",
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
      "content_id": "e8d21aa8-537c-4608-82b6-fed020e76123",
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
      "content_id": "aafe21ce-3de1-42c2-8b99-f54af613d55e",
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
      "content_id": "43c661ed-0882-42d5-b84a-f0c90fb98b9d",
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
      "content_id": "8c7ddc4f-1dcd-4249-b1e5-bad7283e0bc4",
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
      "content_id": "67b6e622-a1d7-4fb7-91f0-841bc9c7ab85",
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
      "content_id": "dcdd42af-18c7-404f-915d-bfcbcabd133d",
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
        "content_id": "642b2032-b6c1-4cbe-8c70-b4179262def0",
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
          "content_id": "642b2032-b6c1-4cbe-8c70-b4179262def0",
          "creator_id": "eval_c4_t1_item1",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:23:37+00:00"
        },
        "content_id": "642b2032-b6c1-4cbe-8c70-b4179262def0",
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
        "content_id": "8e540d97-e53a-4318-a97f-a6664ec87748",
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
          "content_id": "8e540d97-e53a-4318-a97f-a6664ec87748",
          "creator_id": "eval_c4_t1_item2",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:23:37+00:00"
        },
        "content_id": "8e540d97-e53a-4318-a97f-a6664ec87748",
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
        "content_id": "729a38f5-2b43-4f55-9d27-6c25e80c1053",
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
          "content_id": "729a38f5-2b43-4f55-9d27-6c25e80c1053",
          "creator_id": "eval_c4_t1_item3",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:23:37+00:00"
        },
        "content_id": "729a38f5-2b43-4f55-9d27-6c25e80c1053",
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
        "content_id": "298142da-ad37-4db3-b673-8a351bcaf0e4",
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
          "content_id": "298142da-ad37-4db3-b673-8a351bcaf0e4",
          "creator_id": "eval_c4_t1_item4",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:23:37+00:00"
        },
        "content_id": "298142da-ad37-4db3-b673-8a351bcaf0e4",
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
        "content_id": "2571dc89-b0a2-4fcd-a175-2ca14b8bdf84",
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
          "content_id": "2571dc89-b0a2-4fcd-a175-2ca14b8bdf84",
          "creator_id": "eval_c4_t1_item5",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:23:37+00:00"
        },
        "content_id": "2571dc89-b0a2-4fcd-a175-2ca14b8bdf84",
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
