---
# Smart Librarian Export (v2.0)
- Page Number: 33
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/pip/dependencies
- Page Title: Declaring dependencies | uv
- Semantic Filename: declaring_dependencies_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,537 characters
---

# Declaring dependencies | uv

[ Skip to content ](https://docs.astral.sh/uv/pip/dependencies/#declaring-dependencies)
# [Declaring dependencies](https://docs.astral.sh/uv/pip/dependencies/#declaring-dependencies)
It is best practice to declare dependencies in a static file instead of modifying environments with ad-hoc installations. Once dependencies are defined, they can be [locked](https://docs.astral.sh/uv/pip/compile/) to create a consistent, reproducible environment.
## [Using `pyproject.toml`](https://docs.astral.sh/uv/pip/dependencies/#using-pyprojecttoml)
The `pyproject.toml` file is the Python standard for defining configuration for a project.
To define project dependencies in a `pyproject.toml` file:
pyproject.toml```
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-0-1)[project]
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-0-2)dependencies=[
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-0-3)"httpx",
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-0-4)"ruff>=0.3.0"
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-0-5)]

```

To define optional dependencies in a `pyproject.toml` file:
pyproject.toml```
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-1-1)[project.optional-dependencies]
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-1-2)cli=[
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-1-3)"rich",
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-1-4)"click",
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-1-5)]

```

Each of the keys defines an "extra", which can be installed using the `--extra` and `--all-extras` flags or `package[<extra>]` syntax. See the documentation on [installing packages](https://docs.astral.sh/uv/pip/packages/#installing-packages-from-files) for more details.
See the official `pyproject.toml`.
## [Using `requirements.in`](https://docs.astral.sh/uv/pip/dependencies/#using-requirementsin)
It is also common to use a lightweight `requirements.txt` format to declare the dependencies for the project. Each requirement is defined on its own line. Commonly, this file is called `requirements.in` to distinguish it from `requirements.txt` which is used for the locked dependencies.
To define dependencies in a `requirements.in` file:
requirements.in```
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-2-1)httpx
[](https://docs.astral.sh/uv/pip/dependencies/#__codelineno-2-2)ruff>=0.3.0

```

Optional dependencies groups are not supported in this format.
August 27, 2024
