"""Main application module for {{PROJECT_NAME}}.

This module serves as the entry point for the application.
"""

import sys
from typing import Any

from .core import core_function


def main() -> int:
    """Main entry point for the application.

    Returns:
        Exit code (0 for success, non-zero for error)

    Example:
        >>> main()
        0
    """
    try:
        result = core_function("Hello, World!")
        print(f"Result: {result}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())