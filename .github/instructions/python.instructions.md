---
applyTo: "src/**/*.py"
---

# Python — CareerDEX Specifics

## Style (Ruff: E, F, I, B, UP, SIM, C90 — max complexity 8)
- Line length: 100 | `snake_case` functions/vars | `PascalCase` classes
- `from __future__ import annotations` in all source files
- Imports: stdlib → third-party → local (auto-sorted by ruff)
- Run `poe check-all` (lint + typecheck + test) before committing
- `mypy --strict` covers `src/careerdex/`

## Logging — Dual Stack
- API/middleware: `logger = structlog.get_logger(__name__)` → `logger.info("event", key=value)`
- ML/backend: `from loguru import logger` → `logger.info("message %s", arg)`
- `X-Request-ID` propagated via `structlog.contextvars`
- stdlib `logging` is intercepted → loguru (never use it directly)
