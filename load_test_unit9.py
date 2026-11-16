
import requests
import time
import statistics

URL = "http://127.0.0.1:5001/submit"

TEXT = (
    "This is a controlled load testing request for Provenance Guard. "
    "The application evaluates writing using multiple signals and "
    "records performance metrics for operational analysis."
)


def run_test(name, count, interval):
    latencies = []
    statuses = {}

    print(f"\nRunning {name}...")

    start = time.perf_counter()

    for i in range(count):
        payload = {
            "text": TEXT,
            "creator_id": f"unit9-load-{name}-{i}",
        }

        request_start = time.perf_counter()

        try:
            response = requests.post(
                URL,
                json=payload,
                timeout=30,
            )
            status = response.status_code
        except requests.RequestException:
            status = "connection_error"

        elapsed = (
            time.perf_counter() - request_start
        ) * 1000

        latencies.append(elapsed)
        statuses[status] = statuses.get(status, 0) + 1

        if i < count - 1:
            time.sleep(interval)

    total_time = time.perf_counter() - start

    print("Requests:", count)
    print("Duration:", round(total_time, 2), "seconds")
    print("Observed request rate:", round(count / total_time, 2), "req/s")
    print("Mean latency:", round(statistics.mean(latencies), 2), "ms")
    print("Median latency:", round(statistics.median(latencies), 2), "ms")
    print("Status codes:", statuses)


if __name__ == "__main__":
    run_test("normal", 5, 1.0)
    run_test("10x", 50, 0.1)
