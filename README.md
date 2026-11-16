
---

## Unit 9 — Final Results and Operational Report

### 1. Project Overview

For Unit 9, I extended my existing Provenance Guard application from Units 7 and 8.

The application analyzes writing using three signals:
- GPT-2 model predictability
- Stylometry
- Repetition analysis

It combines these signals to classify writing as human, unsure, or AI. The system also supports creator verification, appeals, audit logging, and rate limiting.

For this capstone, I selected **Shape A — Deploy and Instrument**, using **Path B — Local with Logs**.

My goal was to understand how the application performs in real operation, identify bottlenecks, make measurable improvements, and verify that existing functionality remained correct.

I did not change the underlying GPT-2 model, detection signals, scoring weights, or classification thresholds.

### 2. Operational Logging

I created `operational_log.py` and connected it to the Flask application in `app.py`.

The operational logger records:

- Timestamp
- HTTP request method and endpoint
- Summarized request information
- Summarized response information
- HTTP status code
- Request success or failure
- Total request execution time
- Stage-level latency measurements

Logs are stored locally in:

`logs/run_log.jsonl`

The stage-level measurements cover:

1. GPT-2 inference
2. Stylometry
3. Repetition analysis
4. Final scoring

Logging was tested using successful submissions and invalid requests.

The application correctly recorded both HTTP 200 responses and controlled HTTP 400 errors.

Operational logs may contain creator identifiers and text previews, so raw log files should be treated as potentially sensitive information.

### 3. Baseline Evaluation

Before making performance improvements, I ran the existing acceptance tests.

The evaluation consisted of five criteria, with three trials per criterion.

| Criterion | Target | Baseline Result |
|---|---|---|
| 1. False positives | At most 1/10 human samples labeled AI | PASS — 0/10 |
| 2. Score separation | At least 0.40 difference | PASS — 0.7041 |
| 3. Label reachability | Human, unsure, and AI labels reachable | PASS |
| 4. Appeals | 5/5 recorded and under review | PASS |
| 5. Controlled errors | At least 4/5 handled correctly | PASS — 5/5 |

All five criteria were met across all three trials.

Baseline evidence:

`results/eval_run_2026-11-15_1808_unit9_baseline.md`

### 4. Baseline Performance and Diagnosis

I examined operational logs to identify which part of the application consumed the most processing time.

The provisional baseline measurements were:

| Metric | Value |
|---|---:|
| Successful requests | 61 |
| Average latency | 91.29 ms |
| Median latency | 24.32 ms |
| Slowest observed request | 4,039.512 ms |
| GPT-2 time in slowest request | 4,031.518 ms |

Most requests completed quickly, but one request took approximately four seconds.

Nearly all of that request's duration occurred in the GPT-2 stage.

After reviewing `detector.py`, I found that GPT-2 uses lazy initialization. The model is loaded when the application first needs it and then cached for subsequent requests.

This suggested that model initialization was responsible for the unusually slow first request.

### 5. Improvement 1 — GPT-2 Preloading

My first improvement was to preload GPT-2 before starting the Flask server.

The detector already provided a `warm_up()` function, so I reused that function rather than changing the detection algorithm.

I started the application using:

```bash
python -c "import detector; print(detector.warm_up()); from app import app; app.run(host='127.0.0.1', port=5001, debug=False)"
```

The observed first-request performance was:

| Metric | Before | After Preloading |
|---|---:|---:|
| Total request duration | 4,039.512 ms | 31.805 ms |
| GPT-2 stage | 4,031.518 ms | 28.882 ms |

The observed first-request latency decreased by approximately **99.2%**.

This improvement moves model-loading time into application startup rather than eliminating the cost completely.

The change also depends on starting the server with the preloading command.

### 6. Improvement 2 — PyTorch Inference Mode

For my second improvement, I investigated GPT-2 inference overhead.

The existing implementation used:

```python
with torch.no_grad():
    output = model(input_ids, labels=input_ids)
```

I changed it to:

```python
with torch.inference_mode():
    output = model(input_ids, labels=input_ids)
```

The purpose was to reduce inference overhead while preserving the model and scoring behavior.

I then reran all five acceptance criteria.

The results remained unchanged, confirming that the tested functionality was preserved.

### 7. Comparison of Three Configurations

I compared the baseline, the preloaded version, and the version using PyTorch inference mode.

| Configuration | Requests | Median Latency | Average Latency |
|---|---:|---:|---:|
| Baseline | 61 | 24.32 ms | 91.29 ms |
| After Improvement 1 | 61 | 24.93 ms | 25.79 ms |
| After Improvement 2 | 60 | 23.55 ms | 24.85 ms |

The average latency decreased by approximately 71.8% after Improvement 1.

After Improvement 2, the observed average was approximately 3.6% lower than after Improvement 1.

These measurements were grouped using approximate evaluation time windows rather than explicit run identifiers. They may contain warm-up or other test requests.

Therefore, the results demonstrate observed performance changes but do not establish that inference mode alone caused the additional reduction.

### 8. Functional Verification After Both Improvements

I reran the existing acceptance tests after each improvement.

| Criterion | Baseline | After 1 | After 2 |
|---|---|---|---|
| False positives | 0/10 | 0/10 | 0/10 |
| Score spread | 0.7041 | 0.7041 | 0.7041 |
| Three labels reachable | PASS | PASS | PASS |
| Appeals | 5/5 | 5/5 | 5/5 |
| Controlled errors | 5/5 | 5/5 | 5/5 |

All five criteria passed across three trials for each configuration.

Evaluation evidence:

- `results/eval_run_2026-11-15_1808_unit9_baseline.md`
- `results/eval_run_2026-11-15_1819_unit9_after1.md`
- `results/eval_run_2026-11-15_1823_unit9_after2.md`

I also completed an additional reproduction evaluation, which again met all five criteria.

### 9. Load Observation

I created `load_test_unit9.py` to observe application performance under different request rates.

The normal workload submitted five requests with a one-second interval.

The higher-load workload submitted 50 requests with a 0.1-second interval, targeting a ten-times faster request schedule.

Initial results:

| Metric | Normal Load | Higher Load |
|---|---:|---:|
| Requests | 5 | 50 |
| Total duration | 4.21 sec | 6.60 sec |
| Achieved throughput | 1.19 req/sec | 7.57 req/sec |
| Average latency | 37.35 ms | 29.52 ms |
| Median latency | 31.36 ms | 29.12 ms |
| Successful requests | 5/5 | 50/50 |

I also repeated the load test.

The second observation produced 1.19 requests per second at normal load and 7.53 requests per second at higher load.

All 55 requests succeeded again.

The higher-load test achieved approximately 6.4 times the normal throughput, rather than the full ten-times target.

The test used sequential requests and unique creator identifiers. It does not demonstrate concurrent-user performance or the effectiveness of rate limiting against repeated requests from one creator.

### 10. Compute and Resource Measurements

The application was tested locally with the following environment:

| Component | Configuration |
|---|---|
| Operating system | macOS 26.5.2 ARM64 |
| CPU cores | 12 |
| PyTorch version | 2.15.0 |
| Apple Metal (MPS) | Available |
| Web framework | Flask |
| Detection model | GPT-2 |
| Deployment | Local |

Although Apple Metal acceleration was available, I did not verify that the detector actually used GPU acceleration.

I also measured a batch of ten HTTP requests.

Results:

| Metric | Value |
|---|---:|
| Successful submissions | 10/10 |
| Elapsed time | 0.41 sec |
| Client user CPU time | 0.06 sec |
| Client system CPU time | 0.02 sec |
| Maximum client resident memory | 36,831,232 bytes |

These results measure the HTTP client process, not the GPT-2 server.

A separate snapshot of the Flask server process showed approximately 290 MB of memory usage and 0% CPU while idle.

These measurements are useful local resource observations, but they do not establish peak inference memory, server CPU-seconds per request, electricity consumption, or an actual cloud hosting bill.

### 11. How to Reproduce Unit 9

First, follow the environment setup instructions in `RUNNING.md`.

Activate the project's virtual environment.

Start Flask with the GPT-2 model preloaded:

```bash
python -c "import detector; print(detector.warm_up()); from app import app; app.run(host='127.0.0.1', port=5001, debug=False)"
```

In a second terminal, run the existing evaluation configured for port 5001:

```bash
python run_eval_unit9.py --label unit9_reproduction
```

To repeat the load test:

```bash
python load_test_unit9.py
```

Operational measurements are written locally to:

`logs/run_log.jsonl`

### 12. Limitations

There are several limitations to these measurements.

First, the three performance comparison windows were based on approximate timestamps, so they are not perfectly controlled datasets.

Second, the preloading improvement was measured using first-request observations rather than repeated cold-start experiments.

Third, the PyTorch inference-mode optimization preserved functionality, but a controlled benchmark would be needed to confirm its independent speed benefit.

Fourth, the load test used sequential requests rather than a concurrent-user workload.

Finally, server-side peak memory consumption and CPU-seconds per request were not fully measured.

These limitations are important when interpreting the results.

### 13. Lessons Learned and Conclusion

Unit 9 helped me understand the difference between building an AI application and operating one.

My biggest finding was that the slowest request was caused mainly by GPT-2 initialization, rather than stylometry, repetition analysis, or final scoring.

Preloading GPT-2 moved that cost to application startup and substantially reduced observed first-request latency.

Stage-level logging made it possible to identify the bottleneck instead of guessing.

The second optimization showed that small implementation changes should always be evaluated rather than automatically assumed to improve performance.

The load observation also demonstrated why actual achieved throughput matters more than the configured request interval.

Most importantly, the application continued to meet all five existing acceptance criteria after both changes.

This project strengthened my understanding of observability, inference latency, system reliability, measurement limitations, and evidence-based performance optimization.
