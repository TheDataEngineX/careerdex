# CLAUDE.md — CareerDEX Project Context

> This file is automatically loaded by Claude Code at session start.

## Project Overview

**CareerDEX** — AI-powered career intelligence platform (job matching, resume analysis, salary prediction, career paths).

**Stack:** Python 3.12+ · FastAPI (via dataenginex[api]) · uv · Ruff · mypy strict · pytest · Docker

**Version:** 0.5.0

## Build & Run Commands

```bash
# Quality
uv run poe lint           # Ruff lint
uv run poe lint-fix       # Auto-fix
uv run poe typecheck      # mypy --strict
uv run poe check-all      # lint + typecheck + test

# Test
uv run poe test           # All tests
uv run poe test-unit      # Unit tests
uv run poe test-cov       # With coverage

# Run
uv run poe dev            # Dev server (port 8003)
uv run poe docker-up      # Full stack
```

## Key Files

| File | Purpose |
|------|---------|
| `src/careerdex/api/main.py` | FastAPI app entry point |
| `src/careerdex/cli.py` | Click CLI |
| `src/careerdex/phases/` | Phased implementation (1-6) |
| `src/careerdex/core/` | Business logic, schemas, validators |
| `pyproject.toml` | Project configuration |
| `poe_tasks.toml` | Task runner definitions |

## Coding Standards

- `from __future__ import annotations` in all source files
- Ruff: E, F, I, B, UP, SIM, C90 · line-length 100
- `mypy --strict` on `src/careerdex/`
- API logging: `structlog.get_logger(__name__)` · ML: `from loguru import logger`
- Never: `print()`, bare `except:`, f-strings in log calls
- Tests: Arrange-Act-Assert, `asyncio_mode = "auto"`, 80%+ coverage

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

## Dependencies

- `dataenginex[api]>=0.6.0` — Core framework (FastAPI, auth, metrics, tracing)
- `click`, `rich` — CLI
- `pyyaml` — Config parsing
