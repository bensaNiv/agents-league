---
name: python-dev
description: Guide for writing Python code and using uv package manager with modern development practices. This skill should be used when developing Python scripts or packages, setting up Python projects, or working with Python development tools and workflows.
---

# Python Development Skill

This skill provides comprehensive guidance for Python development using modern tools and best practices, with emphasis on **uv** as the package manager and workflow orchestrator.

## When to Use This Skill

Use this skill when:
- Setting up new Python projects with proper structure
- Managing dependencies with uv
- Configuring development tools (ruff, mypy, pytest, bandit)
- Following Python coding standards and best practices
- Running development workflows with uv commands
- Troubleshooting Python project setup or tooling issues
- Converting existing projects to use uv

## Core Development Philosophy

1. **uv-first workflow** - Use `uv` with `--no-sync --offline` flags for reliable, reproducible execution
2. **src/ layout** - Modern package structure for better import safety and distribution
3. **Quality gates** - Automated linting, formatting, type checking, and testing
4. **Configuration as code** - Single `pyproject.toml` for all tool configurations
5. **Offline-ready** - Development workflows that work without network access

## Project Setup Workflows

### Creating New Projects

For new Python projects, use uv's built-in project initialization:

```bash
# Initialize new project with src/ layout
uv init myproject --package
cd myproject

# Set Python version
uv python pin 3.13

# Add basic development dependencies
uv add --dev pytest pytest-cov ruff mypy bandit

# Create src/ layout structure manually
mkdir -p src/myproject tests docs scripts
touch src/myproject/__init__.py src/myproject/main.py
touch tests/__init__.py tests/conftest.py
touch README.md
```

For a complete project setup, use the template assets provided in this skill:
- Copy `assets/pyproject_template.toml` as your `pyproject.toml` base
- Copy `assets/gitignore_template` as your `.gitignore`
- Reference `assets/project_structure_template/` for proper project layout
- Use the pre-commit configuration from the template

### Configuring Development Tools

After project creation, configure development tools:

```bash
# Install and configure all development tools
uv run --no-sync --offline python scripts/configure_dev_tools.py

# Install specific tools only
uv run --no-sync --offline python scripts/configure_dev_tools.py --tools ruff,mypy

# Update pyproject.toml with configurations
uv run --no-sync --offline python scripts/configure_dev_tools.py --update-pyproject

# Show usage examples
uv run --no-sync --offline python scripts/configure_dev_tools.py --examples
```

This script configures:
- **ruff** - Fast linting and formatting with strict rules
- **mypy** - Static type checking with strict mode
- **pytest** - Testing with coverage reporting (80%+ target)
- **bandit** - Security vulnerability scanning
- **pre-commit** - Git hooks for quality gates

## Essential uv Commands

### Project Management

**Always use `--no-sync --offline` flags for reproducible builds:**

```bash
# Initialize project
uv init myproject --python 3.13
cd myproject

# Add dependencies
uv add requests "fastapi>=0.104.0"

# Add development dependencies
uv add --dev pytest ruff mypy

# Sync environment
uv sync --dev

# Execute with offline mode (recommended)
uv run --no-sync --offline pytest
uv run --no-sync --offline ruff check --fix
uv run --no-sync --offline mypy src
```

### Development Workflow Commands

```bash
# Code quality checks
uv run --no-sync --offline ruff check          # Lint code
uv run --no-sync --offline ruff check --fix    # Fix auto-fixable issues
uv run --no-sync --offline ruff format         # Format code
uv run --no-sync --offline mypy src           # Type checking

# Testing
uv run --no-sync --offline pytest                    # Run tests
uv run --no-sync --offline pytest --cov=src         # With coverage
uv run --no-sync --offline pytest -m "not slow"    # Skip slow tests

# Security scanning
uv run --no-sync --offline bandit -r src

# Combined quality check
uv run --no-sync --offline ruff check --fix && \
uv run --no-sync --offline ruff format && \
uv run --no-sync --offline mypy src && \
uv run --no-sync --offline pytest
```

## Code Quality Standards

### Naming Conventions (PEP 8)

```python
# Variables and functions: snake_case
user_name = "john_doe"
def get_user_profile() -> dict:
    pass

# Classes: PascalCase
class UserProfile:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3

# Private attributes: single underscore prefix
class MyClass:
    def __init__(self):
        self._internal_value = None

# Module names: lowercase with underscores
# user_manager.py, database_utils.py
```

### Type Hints (Required)

```python
from typing import Optional, Union, Dict, List, Any

def process_data(items: list[str], config: dict[str, Any]) -> Optional[dict[str, int]]:
    """Process items according to configuration.

    Args:
        items: List of strings to process
        config: Configuration dictionary

    Returns:
        Processing results or None if failed

    Raises:
        ValueError: If configuration is invalid
    """
    if not config.get("enabled", True):
        return None

    results = {}
    for item in items:
        results[item] = len(item)

    return results
```

### Docstring Standards (PEP 257)

```python
def function_example(param1: str, param2: int) -> bool:
    """One-line summary of function purpose.

    Detailed description explaining behavior, side effects,
    and usage patterns.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value

    Raises:
        ValueError: When param2 is negative
        TypeError: When param1 is not a string

    Example:
        >>> function_example("test", 42)
        True
    """
```

## Project Structure

Use **src/ layout** for all Python projects:

```
myproject/
├── src/                          # Source code
│   └── myproject/               # Package directory
│       ├── __init__.py         # Package API
│       ├── main.py             # Entry point
│       ├── core.py             # Business logic
│       ├── models.py           # Data models
│       └── py.typed            # Type checking marker
├── tests/                       # Test suite
│   ├── __init__.py
│   ├── conftest.py             # pytest configuration
│   ├── test_main.py            # Tests
│   └── test_core.py
├── docs/                        # Documentation
├── scripts/                     # Development scripts
├── pyproject.toml              # Project configuration
├── uv.lock                     # Dependency lockfile
├── README.md
├── .gitignore
└── .pre-commit-config.yaml     # Quality gates
```

**Benefits of src/ layout:**
- Import safety during development
- Forces tests to use installed package
- Clear separation of source vs. build artifacts
- Matches PyPI distribution expectations

## Configuration Management

### Single pyproject.toml Configuration

All tool configuration lives in `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py311"
line-length = 88
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP", "N", "S", "SIM", "PTH", "PL"]
ignore = ["S101", "PLR2004"]

[tool.mypy]
python_version = "3.11"
strict = true
mypy_path = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["--cov=src", "--cov-report=term-missing", "--cov-fail-under=80"]

[tool.coverage.run]
source = ["src"]
branch = true
```

### Development Scripts Integration

Create Makefile for common development tasks:

```makefile
.PHONY: install test lint format type-check security check

install:
	uv sync --dev

test:
	uv run --no-sync --offline pytest

lint:
	uv run --no-sync --offline ruff check

format:
	uv run --no-sync --offline ruff format

type-check:
	uv run --no-sync --offline mypy src

security:
	uv run --no-sync --offline bandit -r src

check: lint type-check security test
```

## Testing Best Practices

### Pytest Configuration and Patterns

```python
# conftest.py - Shared fixtures
import pytest
from myproject.core import DataProcessor

@pytest.fixture
def sample_config():
    return {"debug": True, "timeout": 30}

@pytest.fixture
def processor(sample_config):
    return DataProcessor(sample_config)

# test_core.py - Comprehensive testing
class TestDataProcessor:
    def test_process_success(self, processor):
        result = processor.process(["test"])
        assert result == ["PROCESSED: TEST"]

    def test_process_empty_raises_error(self, processor):
        with pytest.raises(ValueError, match="cannot be empty"):
            processor.process([])

    @pytest.mark.parametrize("input,expected", [
        ("hello", "HELLO"),
        ("world", "WORLD"),
    ])
    def test_process_parametrized(self, processor, input, expected):
        result = processor.process([input])
        assert expected in result[0]
```

### Test Execution Patterns

```bash
# Full test suite with coverage
uv run --no-sync --offline pytest --cov=src --cov-report=html

# Fast tests only
uv run --no-sync --offline pytest -m "not slow"

# Specific test files/classes/functions
uv run --no-sync --offline pytest tests/test_core.py::TestDataProcessor::test_process_success

# Parallel execution
uv run --no-sync --offline pytest -n auto

# Debug mode (stop on first failure)
uv run --no-sync --offline pytest -x -vv
```

## Common Development Patterns

### Error Handling

```python
# Custom exceptions
class ValidationError(Exception):
    """Raised when data validation fails."""
    pass

# Context managers for resources
from contextlib import contextmanager

@contextmanager
def database_transaction():
    conn = get_connection()
    trans = conn.begin()
    try:
        yield conn
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    finally:
        conn.close()

# Result pattern for error handling
from typing import Union, Optional

class Result:
    def __init__(self, success: bool, value: Any = None, error: str = None):
        self.success = success
        self.value = value
        self.error = error

    @classmethod
    def ok(cls, value: Any) -> 'Result':
        return cls(True, value=value)

    @classmethod
    def error(cls, message: str) -> 'Result':
        return cls(False, error=message)
```

### Data Classes and Type Safety

```python
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum, auto

@dataclass
class User:
    name: str
    email: str
    age: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

class Status(Enum):
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --frozen --dev
      - name: Run quality checks
        run: |
          uv run --no-sync --offline ruff check
          uv run --no-sync --offline ruff format --check
          uv run --no-sync --offline mypy src
          uv run --no-sync --offline bandit -r src
      - name: Run tests
        run: uv run --no-sync --offline pytest --cov=src --cov-report=xml
```

## Troubleshooting Common Issues

### Dependency Conflicts
```bash
# Clear cache and reinstall
uv cache clean
uv sync --refresh

# Force specific versions
uv add "requests>=2.31.0,<3.0"
```

### Import Issues
```bash
# Check Python path
uv run python -c "import sys; print(sys.path)"

# Install in development mode
uv sync --dev
```

### Type Checking Issues
```bash
# Verbose mypy output
uv run --no-sync --offline mypy --show-error-codes src

# Check specific module
uv run --no-sync --offline mypy src/myproject/main.py
```

## Reference Materials

The skill includes comprehensive reference materials:

- **`references/uv_commands_reference.md`** - Complete uv command guide with examples and common patterns
- **`references/python_coding_standards.md`** - Python PEPs, naming conventions, and modern best practices
- **`references/dev_tools_configuration.md`** - Standard configurations for ruff, mypy, pytest, bandit, and CI/CD

Load these references when you need detailed information about specific tools or patterns. For example, when configuring a complex mypy setup, read `references/dev_tools_configuration.md` for comprehensive configuration examples.

## Quick Start Template

For immediate project creation with all best practices:

1. **Initialize project**: `uv init myproject --package && cd myproject`
2. **Setup structure**: Create src/ layout and copy template files from skill assets
3. **Configure tools**: `uv run python scripts/configure_dev_tools.py --update-pyproject`
4. **Install pre-commit**: `uv add --dev pre-commit && uv run pre-commit install`
5. **Start developing**: Begin writing code in `src/myproject/`
6. **Run quality checks**: `make check` (or run individual uv commands)

This skill ensures Python development follows modern best practices with uv at the center of the workflow, emphasizing reproducible builds, comprehensive quality gates, and maintainable project structure.