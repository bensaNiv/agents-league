"""{{PROJECT_NAME}} package.

A Python project created following modern best practices.
"""

__version__ = "0.1.0"
__author__ = "{{AUTHOR_NAME}}"
__email__ = "{{AUTHOR_EMAIL}}"

# Public API - what gets imported with "from myproject import *"
__all__ = [
    "main",
    "core_function",
]

# Import main functions to make them available at package level
from .main import main
from .core import core_function