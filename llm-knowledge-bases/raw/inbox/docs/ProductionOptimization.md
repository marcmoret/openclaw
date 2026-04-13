# Production Optimization Guide for LiveKit Agent Workers

This document distills best-practice guidance for running LiveKit Agent workers in **production**. Apply these recommendations when promoting a worker from "it runs on my laptop" to a fault-tolerant, observable, cost-efficient service that can run 24 × 7.

---
## 1. Identify the Role of the Worker

| Setting | Why it matters | Recommendation |
|---------|----------------|----------------|
| `agent_name` (required) | Routing key used by LiveKit Cloud to dispatch jobs. | Give every logical agent a **stable** name such as `inbound-agent`, `outbound-agent`, etc. |
| `job_queue_name` | Lets you isolate traffic per environment or tenant. | Use distinct queues like `inbound-prod`, `inbound-staging`, `inbound-dev`. |
| `worker_name` | Helps you spot individual processes in metrics & logs. | `worker_name = f"inbound-{socket.gethostname()}-{uuid.uuid4().hex[:6]}"`. |

---
## 2. Concurrency & Strategy

| Option | Description | Rule of thumb |
|--------|-------------|---------------|
| `concurrency` | Maximum simultaneous jobs **in one process**. | CPU-bound → keep small and scale replicas; I/O-bound (STT/TTS) → 2-4. |
| `concurrency_strategy` | How concurrency is implemented. | `BLOCKING` (safe default), `ASYNC` (all-async code), `THREAD` (mix of blocking + async). |

---
## 3. Keep Heavy Models Warm

Large models (Silero VAD, TTS) cause cold-start latency when reloaded for every job.

```python
WorkerOptions(
    ...,
    auto_unload=False,  # keep models in memory between jobs
)
```

Memory ↑, latency ↓.

---
## 4. Reliability: Error Handling & Retries

* `max_retries` / `retry_delay` – keep defaults (3 × 3 s) unless the job is **not** idempotent.
* **Never** set `max_retries = 0` in prod—transient 5xx errors will drop calls.
* Provide an `on_error` callback to forward exceptions to Sentry / Datadog and increment a fatal-error metric.

---
## 5. Observability Hooks

| Setting | Purpose |
|---------|---------|
| `metrics_interval_seconds` | Emit worker metrics every N seconds (≥15 s recommended). |
| `on_metrics_collected` | Central place to attach OpenTelemetry, Langfuse, etc. |
| `disable_status_updates` | Keep **False** so job progress events show in dashboards. |

---
## 6. Resource Selection

### Hosted Workers (LiveKit Cloud)
* Defaults (`connect_audio=True`, `connect_video=False`) are fine.
* If you need LiveKit to build the runtime image, set `project_source=Path(...)`.

### Self-hosted (Kubernetes / ECS)
* Health-checks: `/` (process), `/live` (agent event-loop).
* CPU & RAM limits: budget for `concurrency × (STT + TTS + buffering)`.

---
## 7. Sample Production Snippet

```python
# main.py – prod excerpt
from livekit.agents import WorkerOptions, ConcurrencyStrategy
import socket, uuid, multiprocessing


def _on_worker_error(exc: Exception):
    logger.exception("Worker-level failure", exc_info=exc)
    # send to Sentry / PagerDuty …


worker_options = WorkerOptions(
    entrypoint_fnc          = entrypoint,
    # Routing
    agent_name              = "inbound-agent",
    job_queue_name          = "inbound-prod",
    worker_name             = f"inbound-{socket.gethostname()}-{uuid.uuid4().hex[:6]}",

    # Capacity
    concurrency             = max(2, multiprocessing.cpu_count() // 2),
    concurrency_strategy    = ConcurrencyStrategy.THREAD,
    auto_unload             = False,   # keep models warm

    # Reliability
    max_retries             = 5,
    retry_delay             = 5.0,
    on_error                = _on_worker_error,

    # Observability
    metrics_interval_seconds = 30,
    on_metrics_collected     = _on_metrics_collected,

    # Performance
    polling_interval        = 0.5,     # faster queue pickup
)
cli.run_app(worker_options)
```

---
## 8. Operational Checklist

1. **Containerise** the worker; pin the LiveKit SDK version.
2. Use **separate queues** for dev / staging / prod.
3. Allocate **CPU & RAM** for `concurrency × (STT + TTS)`.
4. Emit **structured JSON logs** to a central aggregator.
5. Wire `on_error` and `on_metrics_collected` to Sentry / Datadog / OTLP.
6. Run **≥2 replicas** behind each queue for high availability.
7. Implement **readiness & liveness probes** so new Pods don't receive jobs until ready.

---
## 9. Key Take-aways

* Always set a **stable `agent_name`** – it *is* the routing key.
* Tune `concurrency` / `concurrency_strategy` to the workload type.
* Use `auto_unload=False` to avoid cold-starts when large models are involved.
* Provide unique `worker_name`s and rich metrics hooks for observability.
* Separate environments with dedicated queues and run at least two replicas for fault-tolerance.
