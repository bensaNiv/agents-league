"""Command-line interface for {{PROJECT_NAME}}.

This module provides a command-line interface using Click or argparse.
"""

import argparse
import sys
from typing import Optional, Sequence

from .main import main as app_main


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="{{PROJECT_NAME}}",
        description="{{PROJECT_DESCRIPTION}}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version="{{PROJECT_NAME}} 0.1.0",
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    parser.add_argument(
        "input",
        nargs="?",
        help="Input value to process",
    )

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main CLI entry point.

    Args:
        argv: Command line arguments (defaults to sys.argv)

    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = create_parser()
    args = parser.parse_args(argv)

    if args.verbose:
        print("Running in verbose mode")

    if args.input:
        print(f"Processing input: {args.input}")

    return app_main()


if __name__ == "__main__":
    sys.exit(main())