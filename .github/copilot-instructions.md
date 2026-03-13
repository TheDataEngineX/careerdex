# CareerDEX — Copilot Instructions

These standards apply to **all code** in the CareerDEX project.

---

## Project Overview

**CareerDEX** — AI-powered career intelligence platform built on [dataenginex](https://github.com/TheDataEngineX/dataenginex).

**Stack:** Python 3.12+ · FastAPI (via dataenginex[api]) · uv · Ruff · mypy strict · pytest · Docker

**Port:** 8003

## Commands

```bash
uv run poe lint          # Ruff lint
uv run poe typecheck     # mypy --strict
uv run poe test          # pytest
uv run poe check-all     # lint + typecheck + test
uv run poe dev           # Dev server (port 8003)
```

## Coding Standards

- `from __future__ import annotations` in all source files
- Ruff: E, F, I, B, UP, SIM, C90 · line-length 100 · max complexity 8
- `mypy --strict` on `src/careerdex/`
- Functions: under 50 lines, max 4 parameters
- Type hints on all public functions (params + return)
- Pydantic models for API boundaries

## Logging

- **API/middleware:** `structlog.get_logger(__name__)` with `logger.info("event", key=value)`
- **ML/backend:** `from loguru import logger` with `logger.info("message %s", arg)`
- **NEVER:** `print()`, stdlib `logging`, or f-strings in log calls

## Testing

- 80%+ coverage target
- Arrange-Act-Assert pattern
- Mock external services, not code under test
- `asyncio_mode = "auto"` — no `@pytest.mark.asyncio` needed

## Security

- Never hardcode secrets, API keys, passwords, tokens
- Parameterized queries only
- Never log PII or credentials
- Validate inputs at system boundaries (Pydantic)

## Git

- Branches: `main` (prod), `dev` (integration), `feature/<desc>`, `fix/<desc>`
- Conventional commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`

## Red Flags

- Hardcoded secrets or `pickle.loads` on untrusted data
- Bare `except:`, silent error swallowing
- New feature with no tests
- API contract changes without versioning
