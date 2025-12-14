#!/usr/bin/env python3
"""
Development Tools Configuration Script

Configures and installs common Python development tools (ruff, mypy, pytest)
with standardized settings using uv.

Usage:
    python configure_dev_tools.py [--tools ruff,mypy,pytest] [--update-pyproject]
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional
import tomllib
import tomli_w


TOOL_CONFIGS = {
    "ruff": {
        "package": "ruff>=0.1.0",
        "pyproject_config": {
            "tool": {
                "ruff": {
                    "line-length": 88,
                    "target-version": "py311",
                    "src": ["src", "tests"],
                    "lint": {
                        "select": [
                            "E",   # pycodestyle errors
                            "W",   # pycodestyle warnings
                            "F",   # pyflakes
                            "I",   # isort
                            "B",   # flake8-bugbear
                            "C4",  # flake8-comprehensions
                            "UP",  # pyupgrade
                            "N",   # pep8-naming
                            "S",   # flake8-bandit
                        ],
                        "ignore": ["S101"]  # Allow assert statements
                    },
                    "format": {
                        "quote-style": "double",
                        "indent-style": "space"
                    }
                }
            }
        }
    },
    "mypy": {
        "package": "mypy>=1.0",
        "pyproject_config": {
            "tool": {
                "mypy": {
                    "python_version": "3.11",
                    "warn_return_any": True,
                    "warn_unused_configs": True,
                    "disallow_untyped_defs": True,
                    "disallow_incomplete_defs": True,
                    "check_untyped_defs": True,
                    "disallow_untyped_decorators": True,
                    "no_implicit_optional": True,
                    "warn_redundant_casts": True,
                    "warn_unused_ignores": True,
                    "warn_no_return": True,
                    "warn_unreachable": True,
                    "strict_equality": True,
                    "overrides": [
                        {
                            "module": "tests.*",
                            "disallow_untyped_defs": False
                        }
                    ]
                }
            }
        }
    },
    "pytest": {
        "package": "pytest>=7.0",
        "extra_packages": ["pytest-cov>=4.0"],
        "pyproject_config": {
            "tool": {
                "pytest": {
                    "ini_options": {
                        "testpaths": ["tests"],
                        "python_files": ["test_*.py", "*_test.py"],
                        "python_classes": ["Test*"],
                        "python_functions": ["test_*"],
                        "addopts": "--cov=src --cov-report=term-missing --cov-report=html --strict-markers",
                        "markers": [
                            "slow: marks tests as slow (deselect with '-m \"not slow\"')",
                            "integration: marks tests as integration tests"
                        ]
                    }
                },
                "coverage": {
                    "run": {
                        "source": ["src"],
                        "omit": ["*/tests/*", "*/__pycache__/*"]
                    },
                    "report": {
                        "exclude_lines": [
                            "pragma: no cover",
                            "def __repr__",
                            "if self.debug:",
                            "if settings.DEBUG",
                            "raise AssertionError",
                            "raise NotImplementedError",
                            "if 0:",
                            "if __name__ == .__main__.:"
                        ]
                    }
                }
            }
        }
    },
    "bandit": {
        "package": "bandit>=1.7.0",
        "pyproject_config": {
            "tool": {
                "bandit": {
                    "exclude_dirs": ["tests"],
                    "tests": ["B201", "B301"],
                    "skips": ["B101", "B601"]
                }
            }
        }
    }
}


def run_uv_command(cmd: List[str], cwd: Optional[Path] = None) -> bool:
    """Run a uv command and return success status."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ {' '.join(cmd)}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {' '.join(cmd)}")
        print(f"   Error: {e.stderr}")
        return False


def load_pyproject_toml(path: Path) -> Dict:
    """Load pyproject.toml file."""
    if not path.exists():
        return {}

    try:
        with open(path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        print(f"Warning: Could not load {path}: {e}")
        return {}


def save_pyproject_toml(path: Path, data: Dict) -> bool:
    """Save pyproject.toml file."""
    try:
        with open(path, "wb") as f:
            tomli_w.dump(data, f)
        return True
    except Exception as e:
        print(f"Error: Could not save {path}: {e}")
        return False


def merge_config(base: Dict, update: Dict) -> Dict:
    """Deep merge configuration dictionaries."""
    result = base.copy()

    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_config(result[key], value)
        else:
            result[key] = value

    return result


def install_tool(tool: str) -> bool:
    """Install a development tool using uv."""
    if tool not in TOOL_CONFIGS:
        print(f"❌ Unknown tool: {tool}")
        return False

    config = TOOL_CONFIGS[tool]
    packages = [config["package"]]

    if "extra_packages" in config:
        packages.extend(config["extra_packages"])

    print(f"\n🔧 Installing {tool}...")
    success = True

    for package in packages:
        if not run_uv_command(["uv", "add", "--dev", package]):
            success = False

    return success


def configure_pyproject_toml(tools: List[str]) -> bool:
    """Update pyproject.toml with tool configurations."""
    pyproject_path = Path("pyproject.toml")

    print(f"\n📝 Updating {pyproject_path}...")

    # Load existing config
    config = load_pyproject_toml(pyproject_path)

    # Merge tool configurations
    for tool in tools:
        if tool in TOOL_CONFIGS:
            tool_config = TOOL_CONFIGS[tool]["pyproject_config"]
            config = merge_config(config, tool_config)

    # Ensure dev dependencies section exists
    if "project" not in config:
        config["project"] = {}
    if "optional-dependencies" not in config["project"]:
        config["project"]["optional-dependencies"] = {}
    if "dev" not in config["project"]["optional-dependencies"]:
        config["project"]["optional-dependencies"]["dev"] = []

    # Save updated config
    if save_pyproject_toml(pyproject_path, config):
        print(f"✅ Updated {pyproject_path}")
        return True
    else:
        return False


def show_usage_examples():
    """Show usage examples for the configured tools."""
    print("\n📚 Usage Examples:")
    print("\n  # Format and lint with ruff")
    print("  uv run --no-sync --offline ruff format")
    print("  uv run --no-sync --offline ruff check")
    print("  uv run --no-sync --offline ruff check --fix")

    print("\n  # Type checking with mypy")
    print("  uv run --no-sync --offline mypy src")
    print("  uv run --no-sync --offline mypy src tests")

    print("\n  # Testing with pytest")
    print("  uv run --no-sync --offline pytest")
    print("  uv run --no-sync --offline pytest --cov-report=html")
    print("  uv run --no-sync --offline pytest -m \"not slow\"")

    print("\n  # Security scanning with bandit")
    print("  uv run --no-sync --offline bandit -r src")

    print("\n  # Pre-commit workflow")
    print("  uv run --no-sync --offline ruff check --fix")
    print("  uv run --no-sync --offline ruff format")
    print("  uv run --no-sync --offline mypy src")
    print("  uv run --no-sync --offline pytest")


def main():
    parser = argparse.ArgumentParser(description="Configure Python development tools")
    parser.add_argument(
        "--tools",
        default="ruff,mypy,pytest",
        help="Comma-separated list of tools to install (default: ruff,mypy,pytest)"
    )
    parser.add_argument(
        "--update-pyproject",
        action="store_true",
        help="Update pyproject.toml with tool configurations"
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Show usage examples and exit"
    )

    args = parser.parse_args()

    if args.examples:
        show_usage_examples()
        return 0

    # Check if we're in a Python project
    if not Path("pyproject.toml").exists():
        print("❌ No pyproject.toml found. Run this in a Python project directory.")
        return 1

    tools = [tool.strip() for tool in args.tools.split(",")]

    print(f"🚀 Configuring development tools: {', '.join(tools)}")

    # Install tools
    all_success = True
    for tool in tools:
        if not install_tool(tool):
            all_success = False

    # Update pyproject.toml if requested
    if args.update_pyproject or all_success:
        if not configure_pyproject_toml(tools):
            all_success = False

    if all_success:
        print(f"\n✅ Successfully configured: {', '.join(tools)}")
        show_usage_examples()
        return 0
    else:
        print(f"\n❌ Some configuration steps failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())