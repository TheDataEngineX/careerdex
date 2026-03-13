# Contributing to CareerDEX

Thank you for contributing!

## Getting Started

1. Read [DEVELOPMENT.md](DEVELOPMENT.md) for setup instructions
2. Fork the repository
3. Create a feature branch from `dev`
4. Make your changes
5. Submit a pull request

## Commit Messages

Use conventional commit format:

- `feat(#123): add resume parser`
- `fix(#124): handle edge case in matching`
- `docs: update API docs`
- `test: add parsing tests`
- `chore: update dependencies`

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints on all public functions
- Max line length: 100 characters (Ruff)
- Add docstrings to public functions
- `from __future__ import annotations` in all source files

## Before Submitting PR

1. Run all checks locally:

   ```bash
   uv run poe lint
   uv run poe typecheck
   uv run poe test
   ```

2. Tests must pass with 80%+ coverage for new code

3. Update documentation if needed

4. Use PR template in `.github/PULL_REQUEST_TEMPLATE.md`

## Pull Request Process

- Reference issue: `Closes #123`
- Describe what changed and why
- Confirm all checklist items
- Wait for CI/CD to pass
- Get at least 1 approval before merging

## Testing Requirements

- Add unit tests for new code
- Test error scenarios
- Target 80%+ coverage: `uv run poe test-cov`
- Arrange-Act-Assert pattern
- Mock external services, not code under test
