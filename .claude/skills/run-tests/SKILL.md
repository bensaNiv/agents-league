---
name: run-tests
description: Run Python test suites using uv with offline mode and calculated timeouts. This skill should be used when executing pytest-based tests to avoid network issues, prevent hanging tests, and ensure reliable test execution in uv-managed Python projects.
---

# Run Tests

## Overview

Run Python test suites reliably using `uv run` with offline mode and proper timeout handling. This skill ensures tests execute without network dependencies and prevents indefinite hangs through calculated timeout enforcement.

## When to Use This Skill

Use this skill when:
- Running pytest test suites in uv-managed Python projects
- Tests previously hung or timed out unexpectedly
- Working in offline or network-restricted environments
- Need to prevent network-related test failures
- Running tests in CI/CD pipelines where reliability is critical

## Core Execution Principles

### Always Use Offline Mode

Always execute tests with `uv run --no-sync --offline` flags:

```bash
uv run --no-sync --offline pytest <path> -v
```

**Flags explained:**
- `--no-sync`: Skip dependency synchronization before running
- `--offline`: Prevent any network access during execution
- `-v`: Verbose output for better debugging

### Timeout Calculation Strategy

Calculate timeouts based on expected test duration:

1. **Initial Run**: If test duration unknown, start without timeout to establish baseline
2. **Estimate Duration**: For subsequent runs, use: `(test_count × avg_time_per_test) × 1.5`
3. **Apply Buffer**: Add 50% buffer to account for variability
4. **Minimum Timeout**: Never set timeout below 30 seconds

**Example calculation:**
- 50 tests × 0.2 seconds/test = 10 seconds baseline
- 10 seconds × 1.5 buffer = 15 seconds total
- Round up to 30 seconds (minimum)

For detailed timeout calculation guidelines, refer to `references/timeout-calculation.md`.

## Test Execution Workflow

Follow this workflow when running tests:

### 1. Determine Test Scope

Identify what to test:
- **All tests**: `pytest tests/ -v`
- **Specific file**: `pytest tests/test_cli.py -v`
- **Specific test**: `pytest tests/test_cli.py::TestCLI::test_help_command -v`
- **Test pattern**: `pytest tests/ -k "cli" -v`

### 2. Estimate Expected Duration

For first-time runs:
- Run without timeout to establish baseline
- Note the total execution time from output
- Use this for future timeout calculations

For subsequent runs:
- Use previous execution time as baseline
- Apply 1.5× buffer
- Minimum 30 seconds

### 3. Construct Command

Build the test command:

```bash
uv run --no-sync --offline pytest <test-path> -v
```

**Common pytest flags:**
- `-v`: Verbose output
- `-s`: Show print statements
- `-x`: Stop on first failure
- `-k <pattern>`: Run tests matching pattern
- `--tb=short`: Shorter traceback format

### 4. Execute and Monitor

Run the command and observe:
- **Initial output**: Verify pytest discovers tests correctly
- **Progress**: Watch for tests passing/failing
- **Completion**: Check final summary statistics
- **Duration**: Note execution time for future reference

### 5. Handle Results

Based on execution outcome:

**Success (all tests pass):**
- Note execution time for future timeout calculations
- Proceed with development

**Partial failure (some tests fail):**
- Review failure details in output
- Address failing tests before re-running

**Timeout or hang:**
- Identify which test is hanging (last test shown in output)
- Investigate the hanging test specifically
- Consider running with `-s` flag to see print output
- Check for infinite loops or blocking I/O

**Network errors:**
- Verify `--no-sync --offline` flags are used
- Check if tests require external services (should be mocked)
- Review test fixtures for network dependencies

## Common Issues and Solutions

### Tests Hang Indefinitely

**Symptoms:** Tests stop progressing, no output for extended period

**Solutions:**
1. Identify last test shown in output
2. Run that specific test with `-s` flag to see where it hangs
3. Common causes:
   - Waiting for user input (interactive prompts)
   - Unmocked external API calls
   - Infinite loops in test code
   - Deadlocks in concurrent code

### Network-Related Failures

**Symptoms:** Tests fail with connection errors, DNS resolution failures

**Solutions:**
1. Verify using `--no-sync --offline` flags
2. Check test fixtures for network dependencies
3. Mock external services (HTTP clients, API calls)
4. Use local test doubles instead of remote services

### Dependency Not Found

**Symptoms:** ImportError or ModuleNotFoundError during test execution

**Solutions:**
1. Verify dependencies installed: `uv sync`
2. Check `pyproject.toml` for correct test dependencies
3. Ensure running from correct directory
4. Verify virtual environment activated (uv handles this automatically)

## Quick Reference

### Basic Commands

```bash
# Run all tests offline
uv run --no-sync --offline pytest tests/ -v

# Run specific test file
uv run --no-sync --offline pytest tests/test_cli.py -v

# Run specific test
uv run --no-sync --offline pytest tests/test_cli.py::TestClass::test_method -v

# Run with pattern matching
uv run --no-sync --offline pytest tests/ -k "integration" -v

# Stop on first failure
uv run --no-sync --offline pytest tests/ -v -x
```

### Useful Pytest Options

- `-v, --verbose`: Increase verbosity
- `-s`: Disable output capturing (show prints)
- `-x, --exitfirst`: Exit on first failure
- `-k EXPRESSION`: Run tests matching expression
- `--tb=short`: Shorter traceback format
- `--tb=no`: No traceback (just show failures)
- `-q`: Quiet mode (less verbose)
- `--collect-only`: Show what tests would run without running them

## Resources

This skill includes reference documentation for advanced timeout calculation strategies:

### references/

- `timeout-calculation.md`: Detailed guidelines for estimating test duration, calculating appropriate timeouts, and adjusting based on test characteristics
