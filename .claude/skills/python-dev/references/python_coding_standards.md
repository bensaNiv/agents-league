# Python Coding Standards and Best Practices

Comprehensive guide to Python coding standards based on PEPs, community best practices, and modern development patterns.

## Core Principles

1. **Readability Counts** - Code is read more often than written
2. **Explicit is Better Than Implicit** - Clear intent over clever tricks
3. **Simple is Better Than Complex** - Prefer straightforward solutions
4. **Consistency** - Follow established patterns within the codebase
5. **Pythonic** - Use Python's idioms and built-in features effectively

## PEP Standards

### PEP 8 - Style Guide for Python Code

#### Naming Conventions

```python
# Variables and functions: snake_case
user_name = "john_doe"
def get_user_profile():
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30

# Classes: PascalCase
class UserProfile:
    pass

class DatabaseConnection:
    pass

# Private attributes/methods: single underscore prefix
class MyClass:
    def __init__(self):
        self._internal_value = None

    def _helper_method(self):
        pass

# Name mangling: double underscore prefix (rare)
class BaseClass:
    def __init__(self):
        self.__private = "truly private"

# Module names: lowercase with underscores
# file: user_manager.py
# file: database_utils.py

# Package names: lowercase without underscores
# package: mypackage
# package: webutils
```

#### Indentation and Formatting

```python
# Use 4 spaces per indentation level
def my_function():
    if True:
        print("Properly indented")

# Line length: 88 characters (Black/Ruff default) or 79 (PEP 8)
def long_function_name(
    parameter_one: str,
    parameter_two: int,
    parameter_three: bool = False
) -> dict[str, Any]:
    """Function with long parameter list."""
    return {}

# Hanging indents
result = some_function_call(
    argument_one,
    argument_two,
    argument_three,
    argument_four,
)

# Binary operators
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

#### Import Organization

```python
# 1. Standard library imports
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# 2. Related third-party imports
import requests
import click
from fastapi import FastAPI

# 3. Local application imports
from myapp.models import User
from myapp.utils import helper_function
from .local_module import LocalClass

# Avoid wildcard imports
# Bad
from module import *

# Good
from module import specific_function, SpecificClass
```

### PEP 257 - Docstring Conventions

```python
def function_with_docstring(param1: str, param2: int) -> bool:
    """One-line summary of function purpose.

    More detailed description if needed. Explain the function's behavior,
    side effects, exceptions raised, etc.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value

    Raises:
        ValueError: When param2 is negative
        TypeError: When param1 is not a string

    Example:
        >>> function_with_docstring("test", 42)
        True
    """
    if param2 < 0:
        raise ValueError("param2 must be non-negative")
    return len(param1) > param2

class ExampleClass:
    """Brief description of the class purpose.

    Longer description explaining the class's role, usage patterns,
    and any important implementation details.

    Attributes:
        public_attr: Description of public attribute

    Example:
        >>> obj = ExampleClass()
        >>> obj.method()
    """

    def __init__(self, value: int):
        """Initialize the class with a value."""
        self.public_attr = value
```

### PEP 484/526 - Type Hints

```python
from typing import Any, Dict, List, Optional, Union, Callable, TypeVar, Generic

# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Collections
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Optional and Union
def find_user(user_id: int) -> Optional[User]:
    """Return user or None if not found."""
    return database.get_user(user_id)

def parse_value(value: str) -> Union[int, float]:
    """Parse string to int or float."""
    try:
        return int(value)
    except ValueError:
        return float(value)

# Callable type hints
def apply_function(func: Callable[[int], str], value: int) -> str:
    return func(value)

# Generic types
T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value

# Class attributes
class DataClass:
    items: list[str]
    count: int

    def __init__(self) -> None:
        self.items = []
        self.count = 0
```

## Modern Python Best Practices

### Exception Handling

```python
# Specific exception handling
try:
    value = int(user_input)
except ValueError as e:
    logger.error(f"Invalid input: {e}")
    return None

# Multiple exceptions
try:
    result = risky_operation()
except (ValueError, TypeError) as e:
    handle_error(e)

# Exception chaining
try:
    external_api_call()
except requests.RequestException as e:
    raise ApplicationError("API call failed") from e

# Context managers for resource management
with open("file.txt", "r") as f:
    content = f.read()

# Custom context managers
from contextlib import contextmanager

@contextmanager
def database_transaction():
    conn = get_connection()
    trans = conn.begin()
    try:
        yield conn
        trans.commit()
    except Exception:
        trans.rollback()
        raise
    finally:
        conn.close()
```

### Data Classes and Structures

```python
from dataclasses import dataclass, field
from typing import List
from enum import Enum, auto

@dataclass
class User:
    """User data with automatic methods."""
    name: str
    email: str
    age: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Validation after initialization."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# Enums for constants
class Status(Enum):
    """User status enumeration."""
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()

# NamedTuple for immutable data
from typing import NamedTuple

class Point(NamedTuple):
    """Immutable 2D point."""
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
```

### Function and Class Design

```python
# Single Responsibility Principle
class UserValidator:
    """Validates user data."""

    def validate_email(self, email: str) -> bool:
        """Validate email format."""
        return "@" in email and "." in email

    def validate_age(self, age: int) -> bool:
        """Validate age range."""
        return 0 <= age <= 150

class UserRepository:
    """Handles user data persistence."""

    def save(self, user: User) -> None:
        """Save user to database."""
        pass

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Find user by ID."""
        pass

# Dependency Injection
class UserService:
    """User business logic."""

    def __init__(
        self,
        validator: UserValidator,
        repository: UserRepository
    ) -> None:
        self.validator = validator
        self.repository = repository

    def create_user(self, user_data: dict) -> User:
        """Create and save a new user."""
        if not self.validator.validate_email(user_data["email"]):
            raise ValueError("Invalid email")

        user = User(**user_data)
        self.repository.save(user)
        return user
```

### Pythonic Patterns

```python
# List comprehensions
squares = [x ** 2 for x in range(10)]
filtered = [x for x in numbers if x > 0]
transformed = [process(item) for item in items if is_valid(item)]

# Dictionary comprehensions
word_lengths = {word: len(word) for word in words}
inverted = {v: k for k, v in original_dict.items()}

# Generator expressions for memory efficiency
total = sum(x ** 2 for x in large_list)
processed = (transform(item) for item in huge_dataset)

# Enumerate and zip
for i, item in enumerate(items):
    print(f"{i}: {item}")

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Unpacking
first, *middle, last = sequence
name, email, *extra = user_data

# Default dictionary
from collections import defaultdict

counts = defaultdict(int)
for item in items:
    counts[item] += 1

# Pathlib for file operations
from pathlib import Path

config_file = Path("config") / "settings.json"
if config_file.exists():
    content = config_file.read_text()
```

### Error Handling Patterns

```python
# Custom exceptions
class ValidationError(Exception):
    """Raised when validation fails."""
    pass

class BusinessLogicError(Exception):
    """Raised when business rules are violated."""
    pass

# Result pattern
from typing import Union

class Result:
    """Result wrapper for success/failure."""

    def __init__(self, success: bool, value: Any = None, error: str = None):
        self.success = success
        self.value = value
        self.error = error

    @classmethod
    def ok(cls, value: Any) -> 'Result':
        return cls(True, value=value)

    @classmethod
    def error(cls, message: str) -> 'Result':
        return cls(False, error=message)

def safe_divide(a: float, b: float) -> Result:
    """Safely divide two numbers."""
    if b == 0:
        return Result.error("Division by zero")
    return Result.ok(a / b)
```

## Testing Best Practices

```python
import pytest
from unittest.mock import Mock, patch

class TestUserService:
    """Test user service functionality."""

    def test_create_user_success(self):
        """Test successful user creation."""
        # Arrange
        validator = Mock()
        validator.validate_email.return_value = True
        repository = Mock()
        service = UserService(validator, repository)

        user_data = {"name": "John", "email": "john@example.com"}

        # Act
        result = service.create_user(user_data)

        # Assert
        assert result.name == "John"
        repository.save.assert_called_once()

    def test_create_user_invalid_email(self):
        """Test user creation with invalid email."""
        validator = Mock()
        validator.validate_email.return_value = False
        repository = Mock()
        service = UserService(validator, repository)

        with pytest.raises(ValueError, match="Invalid email"):
            service.create_user({"email": "invalid"})

    @pytest.mark.parametrize("age,expected", [
        (25, True),
        (-1, False),
        (151, False),
    ])
    def test_age_validation(self, age, expected):
        """Test age validation with different values."""
        validator = UserValidator()
        assert validator.validate_age(age) == expected

# Fixtures for reusable test data
@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return User(name="Test User", email="test@example.com", age=30)

@pytest.fixture
def mock_database():
    """Mock database connection."""
    with patch('myapp.database.get_connection') as mock:
        yield mock
```

## Code Quality Tools Configuration

### Ruff Configuration

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
    "N",   # pep8-naming
]

ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.format]
quote-style = "double"
```

### MyPy Configuration

```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

## Performance Considerations

```python
# Use appropriate data structures
# List for ordered, mutable sequences
# Tuple for immutable sequences
# Set for unique items, fast membership testing
# Dict for key-value mappings

# Generator for memory efficiency
def read_large_file(filename):
    """Generator for reading large files line by line."""
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Use built-in functions (implemented in C)
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # Faster than manual loop
maximum = max(numbers)  # Faster than manual comparison

# String operations
# Join for building strings from sequences
parts = ["hello", "world", "python"]
result = " ".join(parts)  # Efficient

# F-strings for formatting (Python 3.6+)
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."  # Fast and readable

# Avoid premature optimization
# Profile first, then optimize bottlenecks
import cProfile
cProfile.run('your_function()')
```

This comprehensive guide covers the essential Python coding standards and best practices for writing clean, maintainable, and efficient code.