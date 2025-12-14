# Project Structure Template

This directory demonstrates the recommended Python project structure following modern best practices.

## Directory Layout

```
myproject/
├── src/                          # Source code (src layout)
│   └── myproject/               # Main package
│       ├── __init__.py         # Package initialization
│       ├── main.py             # Application entry point
│       ├── cli.py              # Command-line interface
│       ├── core.py             # Core business logic
│       ├── models.py           # Data models
│       ├── utils.py            # Utility functions
│       └── py.typed            # Type checking marker
├── tests/                       # Test suite
│   ├── __init__.py             # Test package
│   ├── conftest.py             # pytest configuration
│   ├── test_main.py            # Main module tests
│   ├── test_core.py            # Core logic tests
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── fixtures/               # Test fixtures and data
├── docs/                        # Documentation
│   ├── conf.py                 # Sphinx configuration
│   ├── index.rst               # Documentation index
│   ├── api.rst                 # API documentation
│   └── user_guide.rst          # User guide
├── scripts/                     # Development scripts
│   ├── setup.py               # Project setup script
│   ├── lint.sh                # Linting script
│   └── deploy.sh              # Deployment script
├── pyproject.toml              # Project configuration
├── uv.lock                     # Dependency lock file
├── README.md                   # Project README
├── LICENSE                     # License file
├── CHANGELOG.md                # Change log
├── .gitignore                  # Git ignore rules
├── .pre-commit-config.yaml     # Pre-commit hooks
└── Makefile                    # Development commands
```

## Key Benefits of src/ Layout

1. **Import Safety**: Prevents accidental imports of local modules during development
2. **Test Isolation**: Forces tests to run against installed package
3. **Build Clarity**: Clear separation between source and build artifacts
4. **Distribution Ready**: Matches PyPI package structure expectations

## Naming Conventions

- **Package names**: lowercase, no underscores (mypackage)
- **Module names**: lowercase with underscores (my_module.py)
- **Class names**: PascalCase (MyClass)
- **Function/variable names**: snake_case (my_function)
- **Constants**: UPPER_SNAKE_CASE (MAX_SIZE)

## File Purposes

- `__init__.py`: Package initialization, public API definition
- `main.py`: Application entry point and main logic
- `cli.py`: Command-line interface implementation
- `core.py`: Core business logic and algorithms
- `models.py`: Data structures and domain models
- `utils.py`: Utility functions and helpers
- `py.typed`: Indicates package supports type checking