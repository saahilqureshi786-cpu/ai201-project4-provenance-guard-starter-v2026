# Evaluation run — unit9_after1

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
      "content_id": "80605602-642f-491a-99aa-992aa87116c4",
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
      "content_id": "566bcfc8-d5b2-4ca2-8f53-2b561cd189a5",
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
      "content_id": "57f4de02-083d-43e4-a65b-4f1b9b21c112",
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
      "content_id": "b90ebf16-bd9c-4ae0-82df-11dd99c8c255",
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
      "content_id": "cfc928bb-ba08-4f3d-a418-e49ab737adb8",
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
      "content_id": "a266be5d-2c4e-4939-b8f1-1bef37aecd8b",
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
      "content_id": "d6b7947d-1b21-4b47-9543-dc833d4d3815",
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
      "content_id": "3819ac17-8c49-44a5-b03e-876ade46791d",
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
      "content_id": "c1113cfd-2a99-4d5e-8305-5d6e5678f5f5",
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
      "content_id": "455d6efd-aa89-4b2a-82ad-c9d5bfc6b353",
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
      "content_id": "65f4366e-4029-4f68-9bd3-c9b1a6452be2",
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
      "content_id": "e209f38b-461b-47bb-8882-993449ba4db3",
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
      "content_id": "8b3b3f72-59ce-4776-bd5c-f8f289af0a55",
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
      "content_id": "195f5f01-ac8e-4b44-8179-b866dd9bf858",
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
      "content_id": "4195247c-064e-4c71-ae82-d5c2ecee841e",
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
        "content_id": "08c84ce1-40cc-41fb-b453-380f9acbc9fa",
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
          "content_id": "08c84ce1-40cc-41fb-b453-380f9acbc9fa",
          "creator_id": "eval_c4_t1_item1",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:19:46+00:00"
        },
        "content_id": "08c84ce1-40cc-41fb-b453-380f9acbc9fa",
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
        "content_id": "2720a121-e0c9-4432-909f-eb0581560960",
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
          "content_id": "2720a121-e0c9-4432-909f-eb0581560960",
          "creator_id": "eval_c4_t1_item2",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:19:46+00:00"
        },
        "content_id": "2720a121-e0c9-4432-909f-eb0581560960",
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
        "content_id": "a63364a5-a79b-4506-acc0-d17b3793e044",
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
          "content_id": "a63364a5-a79b-4506-acc0-d17b3793e044",
          "creator_id": "eval_c4_t1_item3",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:19:46+00:00"
        },
        "content_id": "a63364a5-a79b-4506-acc0-d17b3793e044",
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
        "content_id": "cd15ee49-ae94-4e24-936f-7881be40effb",
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
          "content_id": "cd15ee49-ae94-4e24-936f-7881be40effb",
          "creator_id": "eval_c4_t1_item4",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:19:46+00:00"
        },
        "content_id": "cd15ee49-ae94-4e24-936f-7881be40effb",
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
        "content_id": "d7f7d9a4-ddf3-4bbd-9ee0-c72934f5f9c4",
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
          "content_id": "d7f7d9a4-ddf3-4bbd-9ee0-c72934f5f9c4",
          "creator_id": "eval_c4_t1_item5",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-16T00:19:46+00:00"
        },
        "content_id": "d7f7d9a4-ddf3-4bbd-9ee0-c72934f5f9c4",
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
