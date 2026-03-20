# Development Setup Guide

## Prerequisites

| Package | Required | Purpose |
|---------|----------|---------|
| Python 3.12+ | Yes | Runtime (managed by uv) |
| uv | Yes | Python package & env manager |
| Git | Yes | Version control |
| Docker + Compose | Recommended | Full stack, integration tests |

## Quick Start

```bash
# 1. Clone and branch
git clone https://github.com/TheDataEngineX/careerdex.git
cd careerdex
git checkout -b feat/issue-XXX-description dev

# 2. Install dependencies
uv sync

# 3. Install pre-commit hooks
uv run poe pre-commit

# 4. Verify setup
uv run poe check-all
```

## Common Commands

```bash
# Development server
uv run poe dev                 # FastAPI on http://localhost:17003

# Quality checks
uv run poe lint                # Ruff lint
uv run poe lint-fix            # Ruff lint + auto-fix
uv run poe format              # Ruff format
uv run poe typecheck           # mypy --strict
uv run poe check-all           # lint + typecheck + test

# Testing
uv run poe test                # All tests
uv run poe test-unit           # Unit tests only
uv run poe test-integration    # Integration tests only
uv run poe test-cov            # Tests with coverage

# Docker
uv run poe docker-up           # Start full stack
uv run poe docker-down         # Stop stack
uv run poe docker-logs         # View logs

# Dependencies
uv run poe uv-sync             # Sync from lockfile
uv run poe uv-lock             # Regenerate lockfile
uv run poe security            # Audit for vulnerabilities
```

## Project Structure

```
careerdex/
├── src/careerdex/           # Application source
│   ├── api/                 # FastAPI app + routers
│   ├── core/                # Business logic, schemas, validators
│   ├── config/              # Configuration files
│   ├── dags/                # Airflow DAGs
│   ├── models/              # ML model definitions
│   ├── phases/              # Phased implementation modules
│   ├── cli.py               # Click CLI
│   └── plugin.py            # DataEngineX plugin
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests (live server)
│   └── fixtures/            # Test data files
├── docs/                    # Documentation (MkDocs)
├── .github/workflows/       # CI/CD pipelines
├── pyproject.toml           # Project configuration
├── poe_tasks.toml           # Task runner definitions
├── Dockerfile               # Container image
└── docker-compose.yml       # Full stack
```

## Validation Pipeline

Run after every code change:

```bash
# 1. Lint
uv run poe lint

# 2. Type check
uv run poe typecheck

# 3. Tests
uv run poe test

# 4. Manual verification
uv run poe dev
curl http://localhost:17003/health
curl http://localhost:17003/api/v1/careerdex/market/trends
```

## Git Conventions

- **Branches**: `main` (prod), `dev` (integration), `feature/<desc>`, `fix/<desc>`
- **Commits**: Conventional — `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`
- **Reference issues**: `feat: add drift detection (#42)`
