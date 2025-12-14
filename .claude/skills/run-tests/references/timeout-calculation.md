# Timeout Calculation Reference

## Overview

This document provides detailed guidelines for calculating appropriate test timeouts based on test suite characteristics, execution patterns, and reliability requirements.

## Basic Timeout Formula

```
timeout = (test_count × avg_time_per_test × buffer_multiplier) + setup_overhead
```

Where:
- `test_count`: Number of tests to execute
- `avg_time_per_test`: Average duration per test
- `buffer_multiplier`: Safety margin (typically 1.5-2.0)
- `setup_overhead`: Time for test discovery and setup (typically 5-10 seconds)

## Timeout Calculation Examples

### Fast Unit Tests

**Characteristics:**
- Pure Python logic tests
- No I/O operations
- No external dependencies
- Typical speed: 0.01-0.1 seconds per test

**Example calculation:**
```
100 tests × 0.05 sec/test × 1.5 buffer + 5 sec overhead = 12.5 seconds
Recommended timeout: 30 seconds (use minimum)
```

### Integration Tests

**Characteristics:**
- File I/O operations
- Database interactions (mocked or local)
- Subprocess execution
- Typical speed: 0.1-1 seconds per test

**Example calculation:**
```
50 tests × 0.5 sec/test × 1.5 buffer + 10 sec overhead = 47.5 seconds
Recommended timeout: 60 seconds
```

### End-to-End Tests

**Characteristics:**
- Full application workflows
- External process spawning
- Network operations (mocked)
- UI automation
- Typical speed: 1-10 seconds per test

**Example calculation:**
```
20 tests × 5 sec/test × 2.0 buffer + 15 sec overhead = 215 seconds
Recommended timeout: 240 seconds (4 minutes)
```

## Determining Average Time Per Test

### Method 1: Initial Baseline Run

1. Run tests without timeout first time
2. Note total execution time from pytest output
3. Divide by number of tests
4. Add to timeout calculation guidelines

Example pytest output:
```
======================== 15 passed in 5.89s =========================
```

Calculation:
```
avg_time_per_test = 5.89 seconds / 15 tests = 0.39 seconds/test
```

### Method 2: Sampling Approach

For large test suites:

1. Run representative subset of tests
2. Calculate average for subset
3. Extrapolate to full suite
4. Add extra buffer for variability

Example:
```bash
# Run 10% sample
uv run --no-sync --offline pytest tests/ -k "test_basic" -v

# If 10 tests take 5 seconds:
# avg = 0.5 sec/test
# Full suite: 100 tests × 0.5 × 1.5 = 75 seconds
```

### Method 3: Historical Data

If tests run regularly:

1. Track execution times over multiple runs
2. Calculate mean and standard deviation
3. Use mean + 2×std_dev as timeout
4. Accounts for natural variability

## Buffer Multiplier Guidelines

### When to Use Different Buffers

**1.5× buffer (standard):**
- Stable test suite
- Consistent execution environment
- Well-mocked dependencies
- Low system load

**2.0× buffer (safe):**
- New or changing test suite
- Shared test environment
- Some unmocked I/O
- Moderate system load

**3.0× buffer (conservative):**
- CI/CD pipelines
- Heavily loaded systems
- Flaky test history
- Critical test runs

## Special Considerations

### Test Parallelization

If using pytest-xdist for parallel execution:

```
timeout = (total_tests / num_workers) × avg_time × buffer + overhead
```

Example with 4 workers:
```
100 tests / 4 workers = 25 tests per worker
25 × 0.5 sec × 1.5 = 18.75 seconds
Timeout: 30 seconds
```

### Slow Test Identification

To find slow tests:

```bash
uv run --no-sync --offline pytest tests/ --durations=10 -v
```

This shows the 10 slowest tests. Consider:
- Optimizing slow tests
- Running slow tests separately
- Using different timeout tiers

### Dynamic Timeout Adjustment

For adaptive timeout calculation:

1. **First run**: No timeout (establish baseline)
2. **Second run**: baseline × 1.5
3. **Subsequent runs**: Use rolling average of last 3 runs × 1.5
4. **On timeout**: Increase by 50% for next run
5. **On consistent success**: Decrease by 20% (but not below baseline × 1.5)

## Timeout by Test Suite Size

Quick reference for typical test suites:

| Suite Size | Fast Tests | Medium Tests | Slow Tests |
|------------|-----------|--------------|------------|
| < 10 tests | 30 sec | 60 sec | 120 sec |
| 10-50 tests | 30 sec | 90 sec | 300 sec |
| 50-100 tests | 60 sec | 180 sec | 600 sec |
| 100-500 tests | 120 sec | 600 sec | 1800 sec |
| > 500 tests | Consider splitting or parallelization |

**Test speed categories:**
- **Fast**: < 0.1 sec/test (pure unit tests)
- **Medium**: 0.1-1 sec/test (integration tests)
- **Slow**: > 1 sec/test (E2E tests)

## Handling Timeout Failures

When tests exceed timeout:

### 1. Analyze the Failure

Check pytest output for:
- Last test that ran before timeout
- Whether tests are progressing or stuck
- Any error messages or warnings

### 2. Investigate Root Cause

Common timeout causes:
- **Hanging test**: Waiting for input, deadlock, infinite loop
- **Insufficient timeout**: Tests slower than expected
- **System overload**: Resource contention
- **External dependency**: Unmocked network call

### 3. Adjust Approach

Based on root cause:

**Hanging test:**
- Run specific test with `-s` to see output
- Add print statements to identify hang point
- Check for interactive prompts or blocking calls

**Insufficient timeout:**
- Increase timeout by 50-100%
- Re-evaluate test speed expectations
- Consider if tests need optimization

**System overload:**
- Run tests during off-peak hours
- Reduce parallel test execution
- Increase system resources

**External dependency:**
- Add proper mocking
- Use test fixtures
- Ensure `--offline` flag prevents network access

## Minimum Timeout Rule

Always enforce a minimum timeout of 30 seconds:

**Rationale:**
- Accounts for test discovery overhead
- Handles process startup time
- Provides buffer for system variability
- Prevents false timeout on slow startup

Even if calculated timeout is lower, use 30 seconds as floor value.

## CI/CD Pipeline Considerations

For automated test execution:

### Conservative Timeouts

Use higher buffer multipliers (2.0-3.0×) because:
- Shared runners may have variable performance
- System load unpredictable
- Timeout failures block deployment
- Extra time is less costly than false failures

### Tiered Timeout Strategy

Consider different timeouts by test type:

```bash
# Fast unit tests (30 second timeout)
uv run --no-sync --offline pytest tests/unit/ -v

# Integration tests (120 second timeout)
uv run --no-sync --offline pytest tests/integration/ -v

# E2E tests (300 second timeout)
uv run --no-sync --offline pytest tests/e2e/ -v
```

### Timeout Monitoring

Track timeout metrics:
- Frequency of timeout failures
- Tests that consistently approach timeout
- Average execution time trends
- Adjust timeouts based on data

## Advanced: Adaptive Timeout Script

For projects with varying test execution times, consider a script that:

1. Runs tests without timeout first time
2. Stores execution time in metadata file
3. Calculates timeout from historical data
4. Adjusts based on success/failure patterns

Example metadata structure:
```json
{
  "tests/test_cli.py": {
    "last_run": "2024-01-15T10:30:00Z",
    "avg_duration": 5.89,
    "timeout_used": 30,
    "recent_durations": [5.89, 6.12, 5.67, 5.94, 6.03]
  }
}
```

This enables intelligent timeout selection based on actual test behavior.
