## Development & Deployment

### Local Development
1. **Dependencies**
   - Python 3.11
   - Poetry (installed via `curl -sSL https://install.python-poetry.org | python3`)
2. **Setup**
   ```bash
   poetry install
   poetry run python main.py dev  # start development worker
   ```
3. **Testing & Quality**
   ```bash
   poetry run pytest
   poetry run black .
   ```
4. **Manual Console Testing**
   ```bash
   make console
   ```

### Environment Configuration
- `.env` for local; production uses environment variables injected via task definitions.
- Key variables: `BACKEND_API_URL`, `BACKEND_API_KEY`, `LIVEKIT_URL`, `WORKER_AGENT_NAME`, `ENABLE_DD_TRACING`, `RECORDING_S3_*`.
- Logging level adjustable through `VOXIRA_LOG_LEVEL` and module-specific overrides (e.g., `LOG_LEVEL_HTTPX`).

### Docker Images
- `Dockerfile` builds production image with Poetry-managed virtualenv, installs wscat for debugging, and sets up entrypoint/healthcheck scripts.
- `Makefile` targets:
  - `docker-dev` / `docker-prod` for building and running local containers.
  - `models` to download required model assets.

### LiveKit Worker Deployment
- `cli.run_app` in `main.py` reads `WORKER_AGENT_NAME` and registers `entrypoint`/`prewarm` functions.
- Scaling is managed by orchestrating multiple worker processes/containers pointing at the same LiveKit server.

### Infrastructure as Code
- Terraform files (`backend.tf`, `main.tf`, `variables.tf`, `outputs.tf`, `terraform/`) provision backend resources (e.g., LiveKit workers, networking, secrets).
- `deploy.sh` and `setup-*` scripts automate environment bootstrap and backend deployment.

### Monitoring & Logging
- Langfuse traces provide fine-grained observability for speech, LLM calls, tools, and session metadata.
- Structured logs (JSON in production) include `session_id` for correlation with backend dashboards.
- Optional Datadog tracing activated when `ENABLE_DD_TRACING` is true.

### Post-Call Analytics
- Webhook dispatch attaches transcripts, call analysis, and summary to the dashboard for QA and reporting.
- Call events stored in `UserData.call_events` supply HIPAA audit trails and conversation summaries.
