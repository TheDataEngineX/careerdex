# CareerDEX

[![CI](https://github.com/TheDataEngineX/careerdex/actions/workflows/ci.yml/badge.svg)](https://github.com/TheDataEngineX/careerdex/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/TheDataEngineX/careerdex)](https://github.com/TheDataEngineX/careerdex/releases)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**AI-powered career intelligence platform** — job matching, resume analysis, salary prediction, and career path recommendations.

Built on [dataenginex](https://github.com/TheDataEngineX/dataenginex) and [datadex](https://github.com/TheDataEngineX/datadex).

______________________________________________________________________

## Quick Start

```bash
git clone https://github.com/TheDataEngineX/careerdex && cd careerdex
uv sync
uv run poe dev                       # Start API → http://localhost:8003
```

## CLI

```bash
careerdex serve --port 8003          # Start CareerDEX API server
careerdex ingest --source linkedin   # Run job ingestion pipeline
careerdex match resume.pdf           # Match resume against job database
careerdex predict-salary resume.pdf  # Predict salary range
careerdex career-path "Data Analyst" # Show career progression paths
```

## Features

| Feature | Description |
|---|---|
| **Multi-source ingestion** | Pull jobs from LinkedIn, Indeed, Glassdoor + local JSON/CSV connectors |
| **Resume intelligence** | NLP-based skill extraction and experience normalization |
| **Semantic matching** | Embedding-based cosine similarity + skill overlap scoring |
| **Salary prediction** | XGBoost models with percentile ranges and confidence scores |
| **Skill gap analysis** | TF-IDF based recommendations for target roles |
| **Career paths** | Graph-based career trajectory recommendations |
| **Churn prediction** | Logistic regression for user engagement risk scoring |
| **Real-time alerts** | Slack notifications for pipeline events |

## API Endpoints

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

## Architecture

```
LinkedIn / Indeed / Glassdoor APIs
Local JSON / CSV Files
         ↓
  Job Ingestion Pipeline (Phase 2)
  Connectors → Normalization → Dedup → Quality Scoring
         ↓
  Bronze (raw) → Silver (cleaned) → Gold (enriched)
         ↓
  ML Models (Phase 4)
  ┌──────────────────────────────────────┐
  │  Resume-Job Matcher · Salary Pred.   │
  │  Skill Gaps · Career Paths · Churn   │
  └──────────────────────────────────────┘
         ↓
  FastAPI Service (:8003)
```

## Project Structure

```
careerdex/
├── src/careerdex/
│   ├── api/                 # FastAPI app + routers
│   │   ├── main.py          # App entry point with middleware stack
│   │   └── routers/         # ML serving + v1 data endpoints
│   ├── core/                # Schemas, validators, settings, exceptions
│   ├── config/              # Pipeline configuration (job_config.json)
│   ├── dags/                # Airflow DAGs
│   ├── phases/              # Phased implementation (1-6)
│   ├── cli.py               # Click CLI
│   └── plugin.py            # DataEngineX plugin entry point
├── tests/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests (live server)
│   └── fixtures/            # Test data files
├── docs/                    # MkDocs documentation
├── .github/workflows/       # CI/CD pipelines
├── pyproject.toml           # Project configuration
├── poe_tasks.toml           # Task runner (25+ tasks)
├── Dockerfile               # Multi-stage container (port 8003)
└── docker-compose.yml       # Full stack with observability
```

## Development

```bash
git clone https://github.com/TheDataEngineX/careerdex && cd careerdex
uv sync

# Quality checks
uv run poe lint              # Ruff lint
uv run poe typecheck         # mypy --strict
uv run poe check-all         # lint + typecheck + test

# Testing
uv run poe test              # All tests
uv run poe test-cov          # With coverage

# Run
uv run poe dev               # Dev server (port 8003)
uv run poe docker-up         # Full stack (API + Prometheus + Grafana + Jaeger)
```

## Docker

```bash
uv run poe docker-build      # Build image
uv run poe docker-up         # Start full stack
uv run poe docker-down       # Stop everything
```

Services: CareerDEX API (:8003), Prometheus (:9090), Grafana (:3000), Jaeger (:16686)

______________________________________________________________________

**Part of [TheDataEngineX](https://github.com/TheDataEngineX) ecosystem** | **License**: MIT
