# CareerDEX Architecture

## Overview

CareerDEX is an AI-powered career intelligence platform that combines job data ingestion, resume analysis, and ML-powered matching. It's built on the [dataenginex](https://github.com/TheDataEngineX/dataenginex) framework and follows a phased implementation approach.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   CareerDEX (v0.5.1)                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐     ┌──────────────┐    ┌──────────────┐ │
│  │  Ingestion    │     │  ML Models   │    │  API Layer   │ │
│  │  (Phase 2)    │     │  (Phase 4)   │    │  (Phase 5)   │ │
│  └──────────────┘     └──────────────┘    └──────────────┘ │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              DataEngineX Framework                    │   │
│  │  Auth · Rate Limit · Metrics · Tracing · Health       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  Observability: Prometheus + OpenTelemetry + structlog       │
│  Quality: Ruff + mypy + pytest + pre-commit                  │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│              Kubernetes + ArgoCD (GitOps)                    │
│   Environments: dev (1 pod), prod (3 pods)                   │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

```
LinkedIn / Indeed / Glassdoor APIs
Local JSON / CSV Files
         ↓
  Phase 2: Job Ingestion Pipeline
  (Connectors → Normalization → Dedup → Quality Scoring)
         ↓
  Bronze (raw) → Silver (cleaned) → Gold (enriched)
         ↓
  Phase 3: Feature Engineering
  (NLP Parsing → Skill Extraction → Embeddings → Vector Store)
         ↓
  Phase 4: ML Models
  ┌──────────────────────────────────────────┐
  │  Resume-Job Matcher (cosine + skills)    │
  │  Salary Predictor (XGBoost)              │
  │  Skill Gap Analyzer (TF-IDF)             │
  │  Career Path Recommender (graph)         │
  │  Churn Predictor (logistic regression)   │
  └──────────────────────────────────────────┘
         ↓
  Phase 5: FastAPI Service (:8003)
  • /api/v1/careerdex/salary/prediction
  • /api/v1/careerdex/insights/skill-gaps
  • /api/v1/careerdex/market/careers
  • /api/v1/careerdex/insights/career-health
  • /api/v1/careerdex/market/trends
  • /api/v1/careerdex/jobs/recommendations
```

## Implementation Phases

| Phase | Name | Status | Description |
|-------|------|--------|-------------|
| 0 | Settings & Exceptions | ✅ Done | Pydantic settings, custom exceptions |
| 1 | Foundation | ✅ Done | Config loading, schemas, validators, medallion bootstrap |
| 2 | Job Ingestion | ✅ Done | Multi-source connectors, dedup, quality scoring |
| 3 | Embeddings | ✅ Done | NLP parsing, skill extraction, vector store |
| 4 | ML Models | ✅ Done | 5 ML models (matcher, salary, gaps, paths, churn) |
| 5 | API Services | ✅ Done | 6 CareerDEX endpoints + ML serving |
| 6 | Deployment | ✅ Done | Deploy config, monitoring, security audit |

## Middleware Stack

Order matters (first added = outermost):

1. **RequestLoggingMiddleware** — Structured request/response logging
1. **PrometheusMetricsMiddleware** — HTTP metrics (`http_` prefix)
1. **AuthMiddleware** — JWT validation (HS256, configurable)
1. **RateLimitMiddleware** — Token bucket rate limiting

## Dependencies

- **dataenginex[api]** — Core framework (FastAPI, auth, rate limiting, metrics, tracing)
- **click + rich** — CLI framework
- **pyyaml** — Configuration parsing
- **numpy** (optional, ml group) — Numerical computing
- **requests** (optional, airflow group) — HTTP client for DAGs
