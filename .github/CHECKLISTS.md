# CareerDEX Code Review Checklists

## PR Review Checklist

### Code Quality
- [ ] `from __future__ import annotations` present in all new/modified files
- [ ] Type hints on all public functions (params + return)
- [ ] Functions under 50 lines, max 4 parameters
- [ ] Clear naming — no `x`, `temp`, `data`
- [ ] Comments explain "why", not "what"

### Security
- [ ] No hardcoded secrets, API keys, or tokens
- [ ] Input validation at system boundaries
- [ ] No PII or credentials in logs

### Testing
- [ ] Tests written for new code
- [ ] Error scenarios covered
- [ ] Tests are independent (no shared state)
- [ ] 80%+ coverage for new code

### Logging
- [ ] structlog (API) or loguru (ML) — no print() or stdlib logging
- [ ] Structured key-value pairs, no f-strings in log calls
- [ ] Errors logged with full context

### Error Handling
- [ ] Specific exceptions caught (no bare `except:`)
- [ ] Errors re-raised with context
- [ ] No silent error swallowing

### API
- [ ] `response_model=` on every endpoint
- [ ] Pydantic models for request/response shapes
- [ ] Backwards compatible within major version

### CI/CD
- [ ] `uv run poe lint` passes
- [ ] `uv run poe typecheck` passes
- [ ] `uv run poe test` passes
- [ ] Real server tested (port 8003)
