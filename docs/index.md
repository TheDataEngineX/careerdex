# CareerDEX Documentation

**AI-powered career intelligence platform**

## Overview

CareerDEX is an intelligent job matching platform built on the [dataenginex](https://github.com/TheDataEngineX/dataenginex) framework. It combines real-time job ingestion, resume analysis, and ML-powered matching to help job seekers find their perfect role.

**Status**: Active development (v0.5.0)

## Key Components

- **Data Ingestion**: Multi-source pipeline (LinkedIn, Indeed, Glassdoor + local JSON/CSV connectors)
- **Storage**: Medallion architecture (Bronze → Silver → Gold)
- **ML Models**: Resume-job matching, salary prediction, skill gap analysis, career paths, churn prediction
- **API**: FastAPI endpoints for search, matching, and recommendations
- **Airflow DAGs**: Orchestrated job ingestion pipelines

## Documentation

- [Quickstart](quickstart.md) — Get running in 5 minutes
- [Architecture](ARCHITECTURE.md) — System design and component overview
- [Development](DEVELOPMENT.md) — Local setup and contributor workflow
- [Contributing](CONTRIBUTING.md) — How to contribute
- [Observability](OBSERVABILITY.md) — Metrics, logging, and tracing
- [ADR Template](adr/0000-template.md) — Architecture decision records

## Directory Structure

```
src/careerdex/
├── api/
│   ├── main.py              # FastAPI app with middleware stack
│   └── routers/
│       ├── ml.py             # ML model serving endpoints
│       └── v1.py             # Data pipeline & quality endpoints
├── core/
│   ├── exceptions.py         # Custom exception types
│   ├── notifier.py           # Slack notifications
│   ├── pipeline_config.py    # Pipeline configuration
│   ├── schemas.py            # Pydantic data models
│   ├── settings.py           # Pydantic-validated settings
│   └── validators.py         # Data quality validators
├── config/
│   └── job_config.json       # Pipeline configuration file
├── dags/
│   └── job_ingestion_dag.py  # Airflow DAG (10 tasks)
├── models/                   # ML model definitions
├── phases/
│   ├── phase1_foundation.py  # Config, schemas, medallion bootstrap
│   ├── phase2_job_ingestion.py  # Connectors, dedup, pipeline
│   ├── phase3_embeddings.py  # NLP, embeddings, vector store
│   ├── phase4_ml_models.py   # 5 ML models
│   ├── phase5_api_services.py  # API route definitions
│   └── phase6_testing_deployment.py  # Deploy config, monitoring
└── plugin.py                 # DataEngineX plugin entry point
```

## Quick Links

- **GitHub**: [TheDataEngineX/careerdex](https://github.com/TheDataEngineX/careerdex)
- **Part of**: [TheDataEngineX](https://github.com/TheDataEngineX) ecosystem
