---
applyTo: "tests/**/*.py"
---

# Testing — CareerDEX Specifics

## Commands
- `uv run poe test` — All tests
- `uv run poe test-unit` — Unit tests only
- `uv run poe test-integration` — Integration tests only
- `uv run poe test-cov` — With coverage report

## Structure
- `tests/unit/` — Isolated unit tests
- `tests/integration/` — Live uvicorn server tests
- `tests/fixtures/` — Sample data files (JSON, CSV, factory helpers)

## Rules
- `asyncio_mode = "auto"` — no `@pytest.mark.asyncio` needed
- Arrange-Act-Assert pattern
- Mock external services, not code under test
- 80%+ coverage target
