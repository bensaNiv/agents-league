# Development Tools Configuration Reference

Comprehensive guide to configuring Python development tools including ruff, mypy, pytest, bandit, and other essential tools for code quality and testing.

## Tool Overview

### Code Quality Stack
- **ruff** - Fast Python linter and formatter (replaces flake8, isort, black)
- **mypy** - Static type checker
- **pytest** - Testing framework with coverage
- **bandit** - Security linter
- **pre-commit** - Git hooks for quality gates

### Configuration Philosophy
- **pyproject.toml** - Single source of configuration
- **Strict by default** - Catch issues early
- **Team consistency** - Shared standards across projects
- **CI/CD ready** - Reliable automation

## Ruff Configuration

### Complete pyproject.toml Configuration

```toml
[tool.ruff]
# Python version compatibility
target-version = "py311"
line-length = 88
indent-width = 4

# Source code directories
src = ["src", "tests"]

# File patterns to include/exclude
include = ["*.py", "*.pyi", "**/pyproject.toml"]
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "venv",
]

[tool.ruff.lint]
# Rule selection
select = [
    # Pyflakes
    "F",
    # pycodestyle
    "E", "W",
    # isort
    "I",
    # pep8-naming
    "N",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-comprehensions
    "C4",
    # flake8-bandit
    "S",
    # flake8-simplify
    "SIM",
    # flake8-use-pathlib
    "PTH",
    # Pylint
    "PL",
]

ignore = [
    # Allow assert statements in tests
    "S101",
    # Allow subprocess calls (bandit)
    "S603", "S607",
    # Allow broad exception catching in some cases
    "BLE001",
    # Magic value comparison
    "PLR2004",
]

# Per-file ignores
[tool.ruff.lint.per-file-ignores]
"tests/**/*" = [
    "S101",    # Allow assertions
    "PLR2004", # Allow magic values in tests
    "S106",    # Allow hardcoded passwords in tests
]
"scripts/**/*" = [
    "T201",    # Allow print statements
]

[tool.ruff.lint.flake8-pytest-style]
fixture-parentheses = false
mark-parentheses = false

[tool.ruff.lint.isort]
known-first-party = ["myapp"]  # Replace with your package name
force-single-line = false
lines-after-imports = 2

[tool.ruff.lint.mccabe]
max-complexity = 10

[tool.ruff.format]
# Formatting options
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```

### Ruff Commands

```bash
# Check code for issues
uv run --no-sync --offline ruff check

# Fix auto-fixable issues
uv run --no-sync --offline ruff check --fix

# Format code
uv run --no-sync --offline ruff format

# Check formatting without changing files
uv run --no-sync --offline ruff format --check

# Run on specific files/directories
uv run --no-sync --offline ruff check src/
uv run --no-sync --offline ruff format tests/

# Show statistics
uv run --no-sync --offline ruff check --statistics

# Generate configuration
uv run --no-sync --offline ruff config
```

## MyPy Configuration

### Complete pyproject.toml Configuration

```toml
[tool.mypy]
# Python version and behavior
python_version = "3.11"
platform = "linux"
warn_return_any = true
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
extra_checks = true

# Strictness settings
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
strict_optional = true
disallow_any_generics = true
disallow_subclassing_any = true

# Error reporting
show_error_codes = true
show_column_numbers = true
show_error_context = true
color_output = true
error_summary = true

# Import discovery
mypy_path = ["src"]
packages = ["myapp"]  # Replace with your package name
namespace_packages = true

# Cache and performance
cache_dir = ".mypy_cache"
sqlite_cache = true
incremental = true

# Per-module overrides
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = false

[[tool.mypy.overrides]]
module = [
    "requests.*",
    "numpy.*",
    "pandas.*",
]
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = "scripts.*"
ignore_errors = true
```

### MyPy Commands

```bash
# Check entire project
uv run --no-sync --offline mypy src

# Check specific files
uv run --no-sync --offline mypy src/myapp/main.py

# Check with reports
uv run --no-sync --offline mypy --html-report mypy-report src
uv run --no-sync --offline mypy --txt-report mypy-report src

# Incremental checking
uv run --no-sync --offline mypy --incremental src

# Show coverage
uv run --no-sync --offline mypy --html-report mypy-report --show-missing-imports src
```

## Pytest Configuration

### Complete pyproject.toml Configuration

```toml
[tool.pytest.ini_options]
# Test discovery
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

# Output and reporting
addopts = [
    # Coverage
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html:htmlcov",
    "--cov-report=xml",

    # Output control
    "--strict-config",
    "--strict-markers",
    "--tb=short",
    "--verbose",

    # Warnings
    "--disable-warnings",

    # Performance
    "--durations=10",
]

# Test markers
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
    "api: marks tests as API tests",
    "database: marks tests that require database",
    "external: marks tests that call external services",
]

# Minimum version
minversion = "7.0"

# Timeout for hanging tests
timeout = 300

# Filter warnings
filterwarnings = [
    "error",
    "ignore::UserWarning",
    "ignore::DeprecationWarning",
]

# Test collection
collect_ignore = [
    "setup.py",
    "build",
    "dist",
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/test_*",
    "*/__pycache__/*",
    "*/migrations/*",
    "*/venv/*",
    "*/virtualenv/*",
    "*/.venv/*",
]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod",
]
ignore_errors = true
show_missing = true
skip_covered = false
precision = 2

[tool.coverage.html]
directory = "htmlcov"

[tool.coverage.xml]
output = "coverage.xml"
```

### Pytest Commands

```bash
# Basic test execution
uv run --no-sync --offline pytest

# Run with coverage
uv run --no-sync --offline pytest --cov=src

# Run specific test files/directories
uv run --no-sync --offline pytest tests/test_api.py
uv run --no-sync --offline pytest tests/unit/

# Run with markers
uv run --no-sync --offline pytest -m "not slow"
uv run --no-sync --offline pytest -m "integration"

# Verbose output
uv run --no-sync --offline pytest -v
uv run --no-sync --offline pytest -vv

# Stop on first failure
uv run --no-sync --offline pytest -x

# Run failed tests from last run
uv run --no-sync --offline pytest --lf

# Parallel execution (with pytest-xdist)
uv run --no-sync --offline pytest -n auto

# Generate reports
uv run --no-sync --offline pytest --html=report.html --self-contained-html
```

## Bandit Configuration

### Complete pyproject.toml Configuration

```toml
[tool.bandit]
# Directories to exclude from scanning
exclude_dirs = [
    "tests",
    ".venv",
    "venv",
    ".tox",
    ".git",
    "__pycache__",
]

# Files to skip
skips = [
    # Skip assert statements (handled by tests)
    "B101",
    # Skip subprocess with shell=True warnings in scripts
    "B602",
]

# Tests to run (empty means all)
tests = []

# Confidence levels: LOW, MEDIUM, HIGH
# Severity levels: LOW, MEDIUM, HIGH
severity = "medium"
confidence = "medium"

# Output format
format = "json"

[tool.bandit.assert_used]
skips = ["*/tests/*", "*/test_*.py"]
```

### Bandit Commands

```bash
# Scan entire project
uv run --no-sync --offline bandit -r src

# Scan with configuration
uv run --no-sync --offline bandit -r src -f json -o security-report.json

# Skip specific tests
uv run --no-sync --offline bandit -r src -s B101,B602

# Show only high severity issues
uv run --no-sync --offline bandit -r src -l -i
```

## Pre-commit Configuration

### .pre-commit-config.yaml

```yaml
repos:
  # Ruff
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  # MyPy
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  # Security
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-c, pyproject.toml]
        additional_dependencies: ["bandit[toml]"]

  # General
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-merge-conflict
      - id: check-added-large-files

  # Local hooks using uv
  - repo: local
    hooks:
      - id: tests
        name: tests
        entry: uv run --no-sync --offline pytest
        language: system
        pass_filenames: false
        always_run: true
```

### Pre-commit Commands

```bash
# Install pre-commit hooks
uv add --dev pre-commit
uv run pre-commit install

# Run on all files
uv run pre-commit run --all-files

# Run specific hook
uv run pre-commit run ruff

# Update hooks
uv run pre-commit autoupdate
```

## Makefile Integration

```makefile
# Makefile for development tasks
.PHONY: install test lint format type-check security check clean

# Installation
install:
	uv sync --dev

# Testing
test:
	uv run --no-sync --offline pytest

test-cov:
	uv run --no-sync --offline pytest --cov=src --cov-report=html

test-fast:
	uv run --no-sync --offline pytest -m "not slow"

# Code quality
lint:
	uv run --no-sync --offline ruff check

lint-fix:
	uv run --no-sync --offline ruff check --fix

format:
	uv run --no-sync --offline ruff format

format-check:
	uv run --no-sync --offline ruff format --check

type-check:
	uv run --no-sync --offline mypy src

security:
	uv run --no-sync --offline bandit -r src

# Combined checks
check: lint type-check security test

# Cleanup
clean:
	rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete

# Development server (example)
dev:
	uv run --no-sync --offline python -m myapp

# Build
build:
	uv build

# Install in development mode
dev-install:
	uv sync --dev --all-extras
```

## CI/CD Configuration Examples

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Test

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up uv
      run: curl -LsSf https://astral.sh/uv/install.sh | sh

    - name: Set up Python ${{ matrix.python-version }}
      run: uv python install ${{ matrix.python-version }}

    - name: Install dependencies
      run: uv sync --frozen --dev

    - name: Lint with ruff
      run: uv run --no-sync --offline ruff check

    - name: Check formatting
      run: uv run --no-sync --offline ruff format --check

    - name: Type check with mypy
      run: uv run --no-sync --offline mypy src

    - name: Security scan with bandit
      run: uv run --no-sync --offline bandit -r src

    - name: Test with pytest
      run: uv run --no-sync --offline pytest --cov=src --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

This comprehensive configuration reference provides standard, production-ready configurations for all major Python development tools with emphasis on uv integration and offline execution patterns.