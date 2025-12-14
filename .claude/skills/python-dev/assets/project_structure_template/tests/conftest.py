"""Pytest configuration and fixtures for {{PROJECT_NAME}}.

This file contains pytest configuration and reusable fixtures for tests.
"""

import pytest
from typing import Any, Dict

# Import your project modules for testing
from {{PROJECT_NAME}}.core import DataProcessor


@pytest.fixture
def sample_config() -> Dict[str, Any]:
    """Provide sample configuration for testing.

    Returns:
        Sample configuration dictionary
    """
    return {
        "debug": True,
        "max_items": 100,
        "timeout": 30,
    }


@pytest.fixture
def data_processor(sample_config: Dict[str, Any]) -> DataProcessor:
    """Create a DataProcessor instance for testing.

    Args:
        sample_config: Configuration fixture

    Returns:
        Configured DataProcessor instance
    """
    return DataProcessor(sample_config)


@pytest.fixture
def sample_data() -> list[str]:
    """Provide sample data for testing.

    Returns:
        List of sample strings
    """
    return ["item1", "item2", "item3"]


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment before each test.

    This fixture runs automatically before each test to ensure
    clean state.
    """
    # Setup code here
    yield
    # Cleanup code here


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line(
        "markers",
        "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers",
        "integration: mark test as integration test"
    )


# Custom test collection
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers."""
    for item in items:
        # Add slow marker to tests that take > 1 second
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)

        # Add integration marker to tests in integration/ directory
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)