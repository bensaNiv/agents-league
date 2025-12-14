"""Tests for {{PROJECT_NAME}}.core module.

This module contains unit tests for the core business logic.
"""

import pytest
from {{PROJECT_NAME}}.core import core_function, DataProcessor


class TestCoreFunction:
    """Tests for core_function."""

    def test_core_function_basic(self):
        """Test basic functionality of core_function."""
        # Arrange
        input_value = "test input"
        expected = "Processed: test input"

        # Act
        result = core_function(input_value)

        # Assert
        assert result == expected

    def test_core_function_empty_string(self):
        """Test core_function with empty string raises ValueError."""
        with pytest.raises(ValueError, match="Input value cannot be empty"):
            core_function("")

    def test_core_function_none(self):
        """Test core_function with None raises ValueError."""
        with pytest.raises(ValueError, match="Input value cannot be empty"):
            core_function(None)

    @pytest.mark.parametrize("input_val,expected", [
        ("hello", "Processed: hello"),
        ("world", "Processed: world"),
        ("123", "Processed: 123"),
        ("special chars !@#", "Processed: special chars !@#"),
    ])
    def test_core_function_parametrized(self, input_val, expected):
        """Test core_function with various inputs."""
        result = core_function(input_val)
        assert result == expected


class TestDataProcessor:
    """Tests for DataProcessor class."""

    def test_init(self, sample_config):
        """Test DataProcessor initialization."""
        processor = DataProcessor(sample_config)
        assert processor.config == sample_config
        assert processor.processed_count == 0

    def test_process_empty_list(self, data_processor):
        """Test processing empty list."""
        result = data_processor.process([])
        assert result == []
        assert data_processor.processed_count == 0

    def test_process_single_item(self, data_processor):
        """Test processing single item."""
        result = data_processor.process(["test"])
        assert result == ["PROCESSED: TEST"]
        assert data_processor.processed_count == 1

    def test_process_multiple_items(self, data_processor, sample_data):
        """Test processing multiple items."""
        expected = ["PROCESSED: ITEM1", "PROCESSED: ITEM2", "PROCESSED: ITEM3"]
        result = data_processor.process(sample_data)

        assert result == expected
        assert data_processor.processed_count == 3

    def test_process_accumulates_count(self, data_processor):
        """Test that processed count accumulates across calls."""
        # First processing
        data_processor.process(["a", "b"])
        assert data_processor.processed_count == 2

        # Second processing
        data_processor.process(["c"])
        assert data_processor.processed_count == 3

    def test_process_single_private_method(self, data_processor):
        """Test the private _process_single method."""
        # Note: Testing private methods is generally discouraged,
        # but sometimes necessary for complex logic
        result = data_processor._process_single("test")
        assert result == "PROCESSED: TEST"


class TestIntegration:
    """Integration tests combining multiple components."""

    @pytest.mark.integration
    def test_core_function_with_processor_output(self, data_processor):
        """Test using core_function with DataProcessor output."""
        # Process data first
        processed_data = data_processor.process(["hello"])

        # Use core_function on the result
        final_result = core_function(processed_data[0])

        assert final_result == "Processed: PROCESSED: HELLO"

    @pytest.mark.slow
    def test_large_data_processing(self, data_processor):
        """Test processing large amounts of data."""
        # Create large dataset
        large_data = [f"item_{i}" for i in range(1000)]

        # Process it
        result = data_processor.process(large_data)

        # Verify results
        assert len(result) == 1000
        assert all(item.startswith("PROCESSED: ITEM_") for item in result)
        assert data_processor.processed_count == 1000