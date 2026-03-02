# Project B — Coding Standards

## Stack
- Python 3
- unittest for testing

## Conventions
- Follow PEP 8 style
- Use type hints where practical
- Keep functions small and focused
- Use docstrings for public functions

## Testing
- All new functionality must have tests
- Run tests with `python -m pytest` or `python -m unittest discover`
- Test file naming: `test_*.py`

## PR Conventions
- Branch naming: `fix/issue-N-description`, `feat/issue-N-description`
- Commit style: `Fix #N: description` or `Feat #N: description`

## Things You Must Never Do
- Never commit secrets or API keys
- Never use `eval()` or `exec()` on user input
- Never ignore exceptions silently (no bare `except: pass`)
- Never push directly to `main` — always use PRs
