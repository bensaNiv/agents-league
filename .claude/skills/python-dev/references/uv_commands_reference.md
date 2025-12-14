# uv Commands Reference

Complete reference for uv (Python package and project manager) with common usage patterns and best practices.

## Core Philosophy

- **Always use offline flags** for reproducible builds: `--no-sync --offline`
- **Fast and reliable** dependency resolution
- **Modern Python workflows** with proper isolation
- **Compatible with pip/setuptools** ecosystem

## Project Lifecycle Commands

### Project Creation

```bash
# Initialize new project
uv init my-project
cd my-project

# Initialize in existing directory
uv init --name my-project

# Initialize with specific Python version
uv init --python 3.13

# Initialize library package (default)
uv init --lib my-library

# Initialize application
uv init --app my-app
```

### Dependencies Management

```bash
# Add runtime dependency
uv add requests
uv add "fastapi>=0.104.0"

# Add development dependency
uv add --dev pytest
uv add --dev "ruff>=0.1.0"

# Add optional dependency group
uv add --optional-group test pytest
uv add --optional-group docs sphinx

# Remove dependency
uv remove requests
uv remove --dev pytest

# Update dependencies
uv sync
uv sync --upgrade

# Install all dependencies (including dev)
uv sync --all-extras --dev

# Install specific groups
uv sync --extra test --extra docs
```

### Environment Management

```bash
# Sync environment with lockfile
uv sync

# Sync without updating lockfile
uv sync --frozen

# Sync for production (no dev deps)
uv sync --no-dev

# Clean sync (remove unused packages)
uv sync --exact
```

## Execution Commands

### Running Code

```bash
# Basic execution
uv run python script.py
uv run python -m mymodule

# Offline execution (recommended)
uv run --no-sync --offline python script.py
uv run --no-sync --offline pytest

# Run with specific Python version
uv run --python 3.13 python script.py

# Run entry point/console script
uv run my-cli-tool --help
```

### Tool Execution

```bash
# Run development tools (offline recommended)
uv run --no-sync --offline ruff check
uv run --no-sync --offline ruff format
uv run --no-sync --offline mypy src
uv run --no-sync --offline pytest
uv run --no-sync --offline bandit -r src

# Run with environment variables
uv run --env-file .env python app.py

# Run in specific directory
uv run --directory /path/to/project pytest
```

### Tool Installation

```bash
# Install global tool
uv tool install ruff
uv tool install --python 3.13 black

# Run tool without installing
uv tool run ruff check .
uv tool run --from "ruff>=0.1.0" ruff format

# List installed tools
uv tool list

# Upgrade tool
uv tool upgrade ruff
uv tool upgrade --all
```

## Python Version Management

```bash
# List available Python versions
uv python list

# Install specific Python version
uv python install 3.13
uv python install 3.12.1

# Pin Python version for project
uv python pin 3.13

# Find Python installations
uv python find 3.13
```

## Lock Files and Reproducibility

```bash
# Generate/update lock file
uv lock

# Update specific package in lock
uv lock --upgrade-package requests

# Verify lock file is up to date
uv lock --check

# Export requirements (for Docker/CI)
uv export --format requirements-txt > requirements.txt
uv export --dev --format requirements-txt > requirements-dev.txt
```

## Common Patterns and Best Practices

### Development Workflow

```bash
# Setup new project
uv init my-project --python 3.13
cd my-project

# Add basic dev tools
uv add --dev pytest ruff mypy

# Install and configure
uv sync --dev
uv run python scripts/configure_dev_tools.py

# Daily development
uv run --no-sync --offline ruff check --fix
uv run --no-sync --offline ruff format
uv run --no-sync --offline mypy src
uv run --no-sync --offline pytest
```

### CI/CD Patterns

```bash
# Fast CI install (use lockfile)
uv sync --frozen --no-dev

# Install with cache
uv sync --cache-dir .uv-cache

# Export for Docker
uv export --no-dev --format requirements-txt > requirements.txt

# Verify reproducibility
uv lock --check
```

### Docker Integration

```dockerfile
# Dockerfile example
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache --no-dev

# Copy application code
COPY . .

# Run application
CMD ["uv", "run", "--no-sync", "python", "-m", "myapp"]
```

### Performance Tips

```bash
# Use offline mode for reproducible builds
uv run --no-sync --offline <command>

# Use frozen sync for faster installs
uv sync --frozen

# Enable UV cache for repeated operations
export UV_CACHE_DIR=.uv-cache
uv sync --cache-dir .uv-cache

# Parallel installation
export UV_CONCURRENT_INSTALLS=4
```

## Configuration

### pyproject.toml Configuration

```toml
[project]
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1.0",
    "mypy>=1.0",
]
test = [
    "pytest-cov>=4.0",
    "pytest-mock>=3.0",
]

[tool.uv]
dev-dependencies = [
    "pre-commit>=3.0.0",
]

[tool.uv.sources]
# Use local/git dependencies
my-package = { path = "../my-package" }
other-package = { git = "https://github.com/user/repo.git" }
```

### Environment Variables

```bash
# Cache configuration
export UV_CACHE_DIR=~/.cache/uv
export UV_NO_CACHE=1

# Network configuration
export UV_INDEX_URL=https://pypi.org/simple
export UV_EXTRA_INDEX_URL=https://my-index.example.com/simple

# Behavior configuration
export UV_NO_SYNC=1
export UV_OFFLINE=1
export UV_CONCURRENT_DOWNLOADS=4
```

## Troubleshooting

### Common Issues

```bash
# Clear cache
uv cache clean

# Force sync
uv sync --refresh

# Verbose output
uv --verbose sync

# Check what would be installed
uv sync --dry-run

# Resolve conflicts
uv lock --resolution highest
uv lock --resolution lowest-direct
```

### Migration from pip

```bash
# Convert requirements.txt
uv add --requirement requirements.txt

# Import from setup.py/setup.cfg
uv init --package

# From pipenv
uv add $(cat Pipfile | grep -A 100 "\[packages\]" | grep "=" | cut -d'"' -f2)
```

## Integration Examples

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: ruff-check
        name: ruff-check
        entry: uv run --no-sync --offline ruff check --fix
        language: system
        types: [python]
      - id: ruff-format
        name: ruff-format
        entry: uv run --no-sync --offline ruff format
        language: system
        types: [python]
      - id: mypy
        name: mypy
        entry: uv run --no-sync --offline mypy
        language: system
        types: [python]
```

### Makefile Integration

```makefile
# Makefile
.PHONY: install test lint format type-check

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

check: lint type-check test
```

### GitHub Actions

```yaml
# .github/workflows/test.yml
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
      - name: Run tests
        run: uv run --no-sync --offline pytest
      - name: Run linting
        run: uv run --no-sync --offline ruff check
      - name: Run type checking
        run: uv run --no-sync --offline mypy src
```

This reference covers the most common uv usage patterns for Python development with emphasis on the `--no-sync --offline` flags for reliable, reproducible builds.