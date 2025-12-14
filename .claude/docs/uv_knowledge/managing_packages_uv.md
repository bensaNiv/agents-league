---
# Smart Librarian Export (v2.0)
- Page Number: 41
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/pip/packages
- Page Title: Managing packages | uv
- Semantic Filename: managing_packages_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 4,636 characters
---

# Managing packages | uv

[ Skip to content ](https://docs.astral.sh/uv/pip/packages/#managing-packages)
# [Managing packages](https://docs.astral.sh/uv/pip/packages/#managing-packages)
## [Installing a package](https://docs.astral.sh/uv/pip/packages/#installing-a-package)
To install a package into the virtual environment, e.g., Flask:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-0-1)$ uv
```

To install a package with optional dependencies enabled, e.g., Flask with the "dotenv" extra:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-1-1)$ uv"flask[dotenv]"

```

To install multiple packages, e.g., Flask and Ruff:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-2-1)$ uv
```

To install a package with a constraint, e.g., Ruff v0.2.0 or newer:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-3-1)$ uv'ruff>=0.2.0'

```

To install a package at a specific version, e.g., Ruff v0.3.0:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-4-1)$ uv'ruff==0.3.0'

```

To install a package from the disk:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-5-1)$ uv"ruff @ ./projects/ruff"

```

To install a package from GitHub:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-6-1)$ uv"git+https://github.com/astral-sh/ruff"

```

To install a package from GitHub at a specific reference:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-1)$ # Install a tag
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-2)$ uv"git+https://github.com/astral-sh/ruff@v0.2.0"
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-3)
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-4)$ # Install a commit
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-5)$ uv"git+https://github.com/astral-sh/ruff@1fadefa67b26508cc59cf38e6130bde2243c929d"
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-6)
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-7)$ # Install a branch
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-7-8)$ uv"git+https://github.com/astral-sh/ruff@main"

```

See the [Git authentication](https://docs.astral.sh/uv/concepts/authentication/git/) documentation for installation from a private repository.
## [Editable packages](https://docs.astral.sh/uv/pip/packages/#editable-packages)
Editable packages do not need to be reinstalled for changes to their source code to be active.
To install the current project as an editable package
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-8-1)$ uv
```

To install a project in another directory as an editable package:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-9-1)$ uv"ruff @ ./project/ruff"

```

## [Installing packages from files](https://docs.astral.sh/uv/pip/packages/#installing-packages-from-files)
Multiple packages can be installed at once from standard file formats.
Install from a `requirements.txt` file:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-10-1)$ uv
```

See the [`uv pip compile`](https://docs.astral.sh/uv/pip/compile/) documentation for more information on `requirements.txt` files.
Install from a `pyproject.toml` file:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-11-1)$ uv
```

Install from a `pyproject.toml` file with optional dependencies enabled, e.g., the "foo" extra:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-12-1)$ uv
```

Install from a `pyproject.toml` file with all optional dependencies enabled:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-13-1)$ uv
```

To install dependency groups in the current project directory's `pyproject.toml`, for example the group `foo`:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-14-1)$ uv
```

To specify the project directory where groups should be sourced from:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-15-1)$ uv
```

Alternatively, you can specify a path to a `pyproject.toml` for each group:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-16-1)$ uv
```

Note
As in pip, `--group` flags do not apply to other sources specified with flags like `-r` or `-e`. For instance, `uv pip install -r some/path/pyproject.toml --group foo` sources `foo` from `./pyproject.toml` and **not** `some/path/pyproject.toml`.
## [Uninstalling a package](https://docs.astral.sh/uv/pip/packages/#uninstalling-a-package)
To uninstall a package, e.g., Flask:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-17-1)$ uv
```

To uninstall multiple packages, e.g., Flask and Ruff:
```
[](https://docs.astral.sh/uv/pip/packages/#__codelineno-18-1)$ uv
```

August 28, 2025
