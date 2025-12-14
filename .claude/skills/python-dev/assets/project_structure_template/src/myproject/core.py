"""Core business logic for {{PROJECT_NAME}}.

This module contains the main business logic and algorithms.
"""

from typing import Any


def core_function(input_value: str) -> str:
    """Process input and return a result.

    Args:
        input_value: The input string to process

    Returns:
        Processed string result

    Raises:
        ValueError: If input_value is empty or None

    Example:
        >>> core_function("test")
        'Processed: test'
    """
    if not input_value:
        raise ValueError("Input value cannot be empty or None")

    return f"Processed: {input_value}"


class DataProcessor:
    """Example class for data processing.

    This class demonstrates proper class structure with type hints,
    docstrings, and error handling.
    """

    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize the data processor.

        Args:
            config: Configuration dictionary
        """
        self.config = config
        self._processed_count = 0

    def process(self, data: list[str]) -> list[str]:
        """Process a list of data items.

        Args:
            data: List of strings to process

        Returns:
            List of processed strings

        Example:
            >>> processor = DataProcessor({})
            >>> processor.process(["a", "b"])
            ['PROCESSED: a', 'PROCESSED: b']
        """
        results = []
        for item in data:
            processed = self._process_single(item)
            results.append(processed)
            self._processed_count += 1

        return results

    def _process_single(self, item: str) -> str:
        """Process a single data item.

        Args:
            item: Single string to process

        Returns:
            Processed string
        """
        return f"PROCESSED: {item.upper()}"

    @property
    def processed_count(self) -> int:
        """Get the number of processed items."""
        return self._processed_count