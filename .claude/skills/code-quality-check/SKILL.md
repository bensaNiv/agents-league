---
name: code-quality-check
description: Automated Python code quality analysis with comprehensive tooling, generating detailed markdown reports
---

# Code Quality Check Skill

## Overview

The Code Quality Check skill provides automated, comprehensive code quality analysis for Python projects using industry-standard tools. It runs linting, type checking, security scanning, complexity analysis, dead code detection, and dependency validation, then generates detailed markdown reports with actionable recommendations.

This skill integrates seamlessly with uv-based Python projects and follows established patterns for consistent, reliable code quality assessment across different codebases.

## When to Use This Skill

Use this skill when you need to:

- **Before committing code**: Ensure code meets quality standards before version control
- **During code reviews**: Generate comprehensive quality reports for review discussions
- **Setting up CI/CD**: Establish baseline quality metrics for automated pipelines
- **Onboarding new projects**: Assess existing code quality and establish improvement roadmap
- **Regular maintenance**: Periodic code quality audits to prevent technical debt accumulation
- **Pre-release validation**: Comprehensive quality check before production deployments
- **Refactoring guidance**: Identify areas of code that need attention and improvement

## Core Quality Check Principles

### 1. **Comprehensive Analysis**
Run multiple complementary tools to get complete code quality picture:
- **Linting**: Code style, imports, and basic issues (ruff)
- **Type Safety**: Static type analysis (mypy)
- **Security**: Vulnerability scanning (bandit)
- **Complexity**: Maintainability metrics (radon)
- **Dead Code**: Unused code detection (vulture)
- **Dependencies**: Package validation (deptry)

### 2. **Auto-Fix First Approach**
Automatically fix what can be safely corrected, then report remaining issues:
```bash
# Auto-fix what's possible
uv run ruff check --fix .

# Then analyze what remains
uv run ruff check .
```

### 3. **Actionable Reporting**
Generate reports with:
- Clear categorization of issues by severity and type
- Specific file locations and line numbers
- Concrete commands to fix issues
- Prioritized recommendations for manual fixes

### 4. **Tool Integration via UV**
Use uv for consistent, isolated tool execution:
```bash
# Install all quality tools as dev dependencies
uv add --dev bandit radon vulture deptry

# Run tools through uv for consistency
uv run <tool> <args>
```

## Quality Check Workflow

### Step 1: Environment Setup and Validation

**Verify uv availability:**
```bash
uv --version
```

**Install missing quality tools:**
```bash
uv add --dev bandit radon vulture deptry
```

**Create output directory:**
```bash
mkdir -p .claude/project_code_quality
```

**Verify project structure:**
- Confirm Python source code locations (src/, tests/, etc.)
- Check for existing pyproject.toml
- Identify main code directories to analyze

### Step 2: Ruff Linting and Auto-Fixing

**Run auto-fixes first:**
```bash
uv run ruff check --fix .
```
*This automatically fixes imports, formatting, and style issues that can be safely corrected.*

**Analyze remaining issues:**
```bash
uv run ruff check .
```

**Categorize findings:**
- **Fixed**: Issues automatically resolved
- **Remaining**: Manual fixes required
- **Ignored**: Issues marked for exclusion

### Step 3: MyPy Type Checking

**Run type analysis:**
```bash
uv run mypy .
```

**Handle common scenarios:**
- Missing library stubs: Suggest `pip install types-<package>`
- Type compatibility issues: Identify specific code fixes needed
- Configuration missing: Recommend pyproject.toml type settings

**Parse and categorize:**
- **Critical**: Type safety violations requiring immediate attention
- **Missing Stubs**: Third-party libraries without type information
- **Configuration**: Settings that could improve type coverage

### Step 4: Security and Quality Analysis

**Security scanning (JSON format for parsing):**
```bash
uv run bandit -r src/ -f json
```

**Complexity analysis:**
```bash
uv run radon cc src/ -a
```

**Dead code detection:**
```bash
uv run vulture src/
```

**Dependency validation:**
```bash
uv run deptry .
```

**Process results:**
- Parse JSON/text outputs into structured data
- Apply severity filtering (High/Medium/Low for security)
- Identify complexity hotspots (functions graded D or F)
- Validate vulture findings against known dynamic usage patterns

### Step 5: Report Generation

**Create comprehensive markdown report at:**
`.claude/project_code_quality/LINTING_REPORT.md`

**Report structure:**
1. Executive summary with counts and priorities
2. Auto-fix results showing what was corrected
3. Detailed findings by tool with tables
4. Actionable recommendations with specific commands
5. Long-term improvement suggestions

### Step 6: Summary and Next Steps

**Provide immediate feedback:**
- Total issues found vs. auto-fixed
- Critical security or type safety issues requiring immediate attention
- High-complexity functions needing refactoring priority

**Generate action plan:**
- Commands to run for immediate fixes
- Code changes requiring manual intervention
- Configuration improvements to prevent future issues

## Tool Configuration Guidelines

### Ruff Configuration (pyproject.toml)

**Basic setup:**
```toml
[tool.ruff]
target-version = "py312"
line-length = 88
select = [
    "E",   # pycodestyle errors
    "F",   # Pyflakes
    "W",   # pycodestyle warnings
    "I",   # isort
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "S",   # bandit (basic security)
]
ignore = [
    "E501",  # Line too long (handled by formatter)
]

[tool.ruff.isort]
known-first-party = ["your_package_name"]
```

**Security-focused configuration:**
```toml
[tool.ruff]
select = ["E", "F", "W", "I", "N", "UP", "S", "B", "A", "C90"]
ignore = ["S101"]  # Allow assert statements in tests

[tool.ruff.per-file-ignores]
"tests/*" = ["S101", "S106"]  # Allow assert and hardcoded passwords in tests
```

### MyPy Configuration (pyproject.toml)

**Strict type checking:**
```toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
```

**Gradual adoption:**
```toml
[tool.mypy]
python_version = "3.12"
ignore_missing_imports = true
warn_return_any = true
warn_unused_configs = true
# Start less strict, increase over time
disallow_untyped_defs = false
```

### Bandit Configuration (pyproject.toml)

```toml
[tool.bandit]
exclude_dirs = ["tests", ".venv"]
skips = ["B101", "B601"]  # Skip assert_used and shell_injection for specific cases

[tool.bandit.assert_used]
skips = ["*/test_*.py", "*/tests.py"]
```

## Report Generation Details

### Report Structure

The generated report follows this comprehensive structure:

```markdown
# Code Quality Report - [Date]

## Executive Summary
- **Total Issues**: X found, Y auto-fixed, Z remaining
- **Critical Security Issues**: N high-severity findings
- **Type Safety**: Coverage percentage and critical violations
- **Code Complexity**: Functions requiring refactoring attention

## Auto-Fix Results
### Ruff Auto-Fixes Applied (Y fixes)
| Category | Count | Examples |
|----------|--------|----------|
| Unused imports | X | `import os` removed from file.py:10 |
| Code formatting | X | Line spacing, quote consistency |
| Import sorting | X | Reorganized imports in module.py |

## Remaining Issues Requiring Manual Attention

### Ruff Linting Results (Z issues)
#### Unused Variables (count)
| File | Line | Variable | Suggestion |
|------|------|----------|------------|
| src/module.py | 45 | `unused_var` | Remove or prefix with _ |

#### Style and Convention Issues (count)
| File | Line | Issue | Fix |
|------|------|-------|-----|
| src/app.py | 120 | Line too long | Break into multiple lines |

### MyPy Type Checking Results (count issues)
#### Missing Library Stubs (count)
| Library | Install Command | Impact |
|---------|----------------|--------|
| aiofiles | `pip install types-aiofiles` | Medium |
| custom-lib | Add py.typed marker | High |

#### Type Compatibility Issues (count)
| File | Line | Issue | Recommended Fix |
|------|------|-------|-----------------|
| src/cli.py | 195 | int \| None → int expected | Add None check before passing |

### Security Analysis - Bandit Results (count issues)
#### High Severity Issues (count)
| File | Line | Issue | Risk Level | Recommendation |
|------|------|-------|------------|----------------|
| src/auth.py | 67 | Hardcoded password | HIGH | Use environment variables |

#### Medium/Low Severity Issues (count)
| File | Line | Issue | Risk Level | Action |
|------|------|-------|------------|--------|
| src/utils.py | 34 | subprocess.shell=True | MEDIUM | Use shell=False or validate input |

### Code Complexity - Radon Results (count functions)
#### Functions Needing Refactoring (Grade D/F)
| File | Function | Complexity | Grade | Suggestion |
|------|----------|------------|-------|------------|
| src/processor.py | process_data() | 15 | D | Break into smaller functions |
| src/analyzer.py | complex_analysis() | 23 | F | Extract helper methods, reduce nesting |

### Dead Code Detection - Vulture Results (count items)
| File | Item | Type | Confidence | Action |
|------|------|------|------------|--------|
| src/old_utils.py | legacy_function() | function | 90% | Review and remove if unused |
| src/models.py | UnusedClass | class | 80% | Verify usage patterns |

### Dependency Issues - Deptry Results
#### Missing Dependencies (count)
| Import | Used In | Suggested Package |
|--------|---------|------------------|
| requests | src/api.py | `uv add requests` |

#### Unused Dependencies (count)
| Package | Installed Version | Action |
|---------|------------------|--------|
| old-library | 2.1.0 | `uv remove old-library` |

## Recommended Actions

### Immediate Fixes (Run These Commands)
```bash
# Apply auto-fixes
uv run ruff check --fix .

# Install missing type stubs
pip install types-aiofiles types-requests

# Remove unused dependencies
uv remove old-library unused-package
```

### Manual Code Changes Required
1. **Security**: Replace hardcoded credentials in src/auth.py:67
2. **Type Safety**: Add None checks in src/cli.py:195-196
3. **Complexity**: Refactor process_data() function (15+ complexity)

### Long-term Improvements
1. **Configuration**: Add strict mypy settings to pyproject.toml
2. **CI/CD**: Integrate quality checks into automated pipelines
3. **Documentation**: Add type hints to remaining untyped functions
4. **Architecture**: Consider breaking down high-complexity modules
```

## Common Issues and Solutions

### Issue: "Command not found" for quality tools

**Cause**: Tools not installed or not in uv environment

**Solution**:
```bash
# Install all tools at once
uv add --dev bandit radon vulture deptry

# Verify installation
uv run bandit --help
uv run radon --help
```

### Issue: MyPy "Module has no attribute" errors

**Cause**: Missing type stubs for third-party libraries

**Solutions**:
```bash
# Install official type stubs
pip install types-requests types-aiofiles

# For libraries without stubs, ignore in pyproject.toml:
[tool.mypy]
ignore_missing_imports = true

# Or create stub files for critical libraries
```

### Issue: Vulture false positives (reports used code as dead)

**Cause**: Dynamic code usage, reflection, or framework patterns

**Solutions**:
```python
# Create whitelist file: vulture_whitelist.py
# Add false positives:
_.dynamic_method_name  # Django ORM methods
_.pytest_fixtures      # Test fixtures
```

**Run with whitelist:**
```bash
uv run vulture src/ vulture_whitelist.py
```

### Issue: Bandit security false positives

**Cause**: Legitimate use cases flagged as security risks

**Solutions**:
```python
# Suppress specific lines with comments:
subprocess.call(cmd, shell=True)  # nosec B602

# Or configure in pyproject.toml:
[tool.bandit]
skips = ["B602"]  # Skip subprocess with shell=True
```

### Issue: Radon complexity threshold configuration

**Customize complexity grading:**
```bash
# Set custom thresholds
uv run radon cc src/ -a --min=C  # Only show C grade and below
uv run radon cc src/ --json      # JSON output for parsing
```

### Issue: Deptry missing imports in dynamic code

**Configure exclusions:**
```toml
[tool.deptry]
ignore_notebooks = true
exclude = ["migrations", "test_*.py"]
ignore_missing = ["dynamic-import-lib"]
```

## Quick Reference

### Installation Commands
```bash
# Install all quality tools
uv add --dev bandit radon vulture deptry

# Verify installation
uv run ruff --version && uv run mypy --version
```

### Analysis Commands
```bash
# Full quality check sequence
uv run ruff check --fix .        # Auto-fix issues
uv run ruff check .              # Check remaining
uv run mypy .                    # Type checking
uv run bandit -r src/ -f json    # Security scan
uv run radon cc src/ -a          # Complexity
uv run vulture src/              # Dead code
uv run deptry .                  # Dependencies
```

### Report Generation
```bash
# Create output directory
mkdir -p .claude/project_code_quality

# Generate report (via this skill)
# Report saved to: .claude/project_code_quality/LINTING_REPORT.md
```

### Configuration Files
```bash
# Add tool configurations to pyproject.toml
[tool.ruff]
[tool.mypy]
[tool.bandit]
[tool.deptry]
```

## Resources

- **Ruff Documentation**: https://docs.astral.sh/ruff/
- **MyPy Documentation**: https://mypy.readthedocs.io/
- **Bandit Documentation**: https://bandit.readthedocs.io/
- **Radon Documentation**: https://radon.readthedocs.io/
- **Vulture Documentation**: https://pypi.org/project/vulture/
- **Deptry Documentation**: https://deptry.com/
- **UV Package Manager**: https://docs.astral.sh/uv/

### Configuration Examples
- **Python Type Checking**: https://mypy.readthedocs.io/en/stable/config_file.html
- **Ruff Configuration**: https://docs.astral.sh/ruff/configuration/
- **Security Scanning Setup**: https://bandit.readthedocs.io/en/latest/config.html