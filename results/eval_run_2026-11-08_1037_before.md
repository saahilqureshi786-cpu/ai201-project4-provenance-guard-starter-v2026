# Evaluation run — before

- Produced by: `run_eval.py::main`
- Service: `app.py::submit`
- Trials per criterion: **3**

## Run Log

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
|---|---|---|---|---|---|
| 1 | At most 1 of 10 clearly-human pieces labeled AI | PASS — 0/10 labeled AI | PASS — 0/10 labeled AI | PASS — 0/10 labeled AI | **MET** |
| 2 | At least 0.40 combined-score spread | PASS — score spread = 0.7041 | PASS — score spread = 0.7041 | PASS — score spread = 0.7041 | **MET** |
| 3 | All 3 labels reachable | FAIL — labels reached = ai, unsure | FAIL — labels reached = ai, unsure | FAIL — labels reached = ai, unsure | **MISSED** |
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
      "content_id": "b056d45b-91a3-4380-a976-b7fe508b9bb6",
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
      "content_id": "16c75497-e3df-478e-a0d9-324ddaa0fb0c",
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
      "content_id": "16749821-2dbf-4f71-a88b-7da69db0b920",
      "creator_credential": null,
      "guess": "unsure",
      "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
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
      "content_id": "ca1f3d24-300b-43e8-84c9-76c1bcbf7fa8",
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
      "content_id": "60481d4a-ffb2-4a2d-9e75-b164bdd09f47",
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
      "content_id": "09a2f1c0-145b-4a66-9499-45394466d0c7",
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
      "content_id": "533d9765-0be9-474d-b898-bd4f81cdc182",
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
      "content_id": "7c25b6e9-3696-4739-b64d-7109fffed094",
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
      "content_id": "a6ec526c-0d1a-4b4e-87a7-d6a28a107ee7",
      "creator_credential": null,
      "guess": "unsure",
      "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
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
      "content_id": "4b134396-edf7-4d01-9abd-675266c70b10",
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
      "content_id": "dd021832-af93-46eb-9e8b-706a069f2c2f",
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
      "content_id": "6c0eaa0a-f796-4764-8378-1db3fec6634c",
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

Trial 1 result: FAIL

Metric: `labels reached = ai, unsure`

```json
[
  {
    "item": 1,
    "creator_id": "eval_c3_t1_item1",
    "status_code": 200,
    "payload": {
      "confidence": 0.5221,
      "content_id": "2340bba1-2e5f-4bde-9fec-884e9f631cca",
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
      "content_id": "2394474f-f582-4791-9c74-0c116b83d37a",
      "creator_credential": null,
      "guess": "unsure",
      "label": "Our signals do not give a clear result, so we are not making an authorship claim about this writing.",
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
      "content_id": "48624bfd-16cf-4064-9ba0-1ff85830ba92",
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
        "content_id": "5122449c-0cb9-4f3b-b89a-daaa81279ac3",
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
          "content_id": "5122449c-0cb9-4f3b-b89a-daaa81279ac3",
          "creator_id": "eval_c4_t1_item1",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-08T16:37:09+00:00"
        },
        "content_id": "5122449c-0cb9-4f3b-b89a-daaa81279ac3",
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
        "content_id": "9d33a6b9-e30b-4a2e-a6a0-94550f07838a",
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
          "content_id": "9d33a6b9-e30b-4a2e-a6a0-94550f07838a",
          "creator_id": "eval_c4_t1_item2",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-08T16:37:09+00:00"
        },
        "content_id": "9d33a6b9-e30b-4a2e-a6a0-94550f07838a",
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
        "content_id": "d9ca6436-e343-4670-93e2-88d311c1c29c",
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
          "content_id": "d9ca6436-e343-4670-93e2-88d311c1c29c",
          "creator_id": "eval_c4_t1_item3",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-08T16:37:09+00:00"
        },
        "content_id": "d9ca6436-e343-4670-93e2-88d311c1c29c",
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
        "content_id": "16b29949-239a-4bac-b24e-719eb12c649e",
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
          "content_id": "16b29949-239a-4bac-b24e-719eb12c649e",
          "creator_id": "eval_c4_t1_item4",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-08T16:37:09+00:00"
        },
        "content_id": "16b29949-239a-4bac-b24e-719eb12c649e",
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
        "content_id": "f0c86a33-85df-4573-9a8f-f6cfd265495b",
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
          "content_id": "f0c86a33-85df-4573-9a8f-f6cfd265495b",
          "creator_id": "eval_c4_t1_item5",
          "event": "appeal",
          "reasoning": "Evaluation appeal: please review this decision.",
          "status": "under_review",
          "timestamp": "2026-11-08T16:37:09+00:00"
        },
        "content_id": "f0c86a33-85df-4573-9a8f-f6cfd265495b",
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

