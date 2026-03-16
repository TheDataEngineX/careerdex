# CLAUDE.md — CareerDEX

> Repo-specific context. Workspace-level rules, coding standards, and git conventions are in `../CLAUDE.md`.

## Project Overview

**CareerDEX** — AI-powered career intelligence platform (job matching, resume analysis, salary prediction, career paths).

**Stack:** Python 3.12+ · FastAPI (via dataenginex[api]) · uv · Ruff · mypy strict · pytest · Port 8003

**Version:** `uv run poe version` | **Depends on:** dataenginex[api] (see `pyproject.toml`)

## Build & Run Commands

```bash
uv run poe lint           # Ruff lint
uv run poe lint-fix       # Auto-fix
uv run poe typecheck      # mypy --strict (src/careerdex/ only)
uv run poe check-all      # lint + typecheck + test

uv run poe test           # All tests
uv run poe test-unit      # Unit tests
uv run poe test-cov       # With coverage

uv run poe dev            # Dev server (port 8003)
uv run poe docker-up      # Full stack
```

## Key Files

| File | Purpose |
| --- | --- |
| `src/careerdex/api/main.py` | FastAPI app entry point |
| `src/careerdex/cli.py` | Click CLI |
| `src/careerdex/phases/` | Phased implementation (1–6) |
| `src/careerdex/core/` | Business logic, schemas, validators |
| `pyproject.toml` | Project configuration |
| `poe_tasks.toml` | Task runner definitions |

## API Endpoints

- `GET /health`, `/ready`, `/startup` — Health probes
- `GET /metrics` — Prometheus metrics
- `POST /api/v1/careerdex/salary/prediction` — Salary prediction
- `GET /api/v1/careerdex/insights/skill-gaps` — Skill gap analysis
- `GET /api/v1/careerdex/market/careers` — Career paths
- `GET /api/v1/careerdex/insights/career-health` — Career health
- `GET /api/v1/careerdex/market/trends` — Market trends
- `GET /api/v1/careerdex/jobs/recommendations` — Job recommendations
- `GET /api/v1/models`, `POST /api/v1/predict` — ML model serving
