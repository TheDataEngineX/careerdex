# Quickstart

Get CareerDEX running in under five minutes.

## 1. Install

```bash
git clone https://github.com/TheDataEngineX/careerdex && cd careerdex
uv sync
```

## 2. Run the Dev Server

```bash
uv run poe dev     # Starts FastAPI on http://localhost:17003
```

Verify it works:

```bash
curl http://localhost:17003/health
# → {"status":"alive"}

curl http://localhost:17003/api/v1/careerdex/market/trends | python3 -m json.tool
```

## 3. Try the CLI

```bash
careerdex serve --port 17003          # Start API server
careerdex ingest --source linkedin   # Run job ingestion pipeline
careerdex match resume.pdf           # Match resume against job database
careerdex predict-salary resume.pdf  # Predict salary range
careerdex career-path "Data Analyst" # Show career progression paths
```

## 4. Run Tests

```bash
uv run poe test           # All tests
uv run poe test-unit      # Unit tests only
uv run poe test-cov       # With coverage report
```

## 5. API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/ready` | GET | Readiness probe |
| `/metrics` | GET | Prometheus metrics |
| `/api/v1/careerdex/salary/prediction` | POST | Salary prediction |
| `/api/v1/careerdex/insights/skill-gaps` | GET | Skill gap analysis |
| `/api/v1/careerdex/market/careers` | GET | Career path recommendations |
| `/api/v1/careerdex/insights/career-health` | GET | Career health score |
| `/api/v1/careerdex/market/trends` | GET | Market trends |
| `/api/v1/careerdex/jobs/recommendations` | GET | Job recommendations |
| `/api/v1/models` | GET | List ML models |
| `/api/v1/predict` | POST | Run ML prediction |

## 6. Docker

```bash
uv run poe docker-up      # Start full stack (API + Prometheus + Grafana + Jaeger)
uv run poe docker-down    # Stop everything
```

The API will be available at `http://localhost:17003`.
