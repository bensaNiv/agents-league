---
# Smart Librarian Export (v2.0)
- Page Number: 35
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/pip/compile
- Page Title: Locking environments | uv
- Semantic Filename: locking_environments_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 8,350 characters
---

# Locking environments | uv

[ Skip to content ](https://docs.astral.sh/uv/pip/compile/#locking-environments)
# [Locking environments](https://docs.astral.sh/uv/pip/compile/#locking-environments)
Locking is to take a dependency, e.g., `ruff`, and write an exact version to use to a file. When working with many dependencies, it is useful to lock the exact versions so the environment can be reproduced. Without locking, the versions of dependencies could change over time, when using a different tool, or across platforms.
## [Locking requirements](https://docs.astral.sh/uv/pip/compile/#locking-requirements)
uv allows dependencies to be locked in the `requirements.txt` format. It is recommended to use the standard `pyproject.toml` to define dependencies, but other dependency formats are supported as well. See the documentation on [declaring dependencies](https://docs.astral.sh/uv/pip/dependencies/) for more details on how to define dependencies.
To lock dependencies declared in a `pyproject.toml`:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-0-1)$ uv
```

Note by default the `uv pip compile` output is just displayed and `--output-file` / `-o` argument is needed to write to a file.
To lock dependencies declared in a `requirements.in`:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-1-1)$ uv
```

To lock dependencies declared in multiple files:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-2-1)$ uv
```

uv also supports legacy `setup.py` and `setup.cfg` formats. To lock dependencies declared in a `setup.py`:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-3-1)$ uv
```

To lock dependencies from stdin, use `-`:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-4-1)$ echo"ruff"|
```

To lock with optional dependencies enabled, e.g., the "foo" extra:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-5-1)$ uv
```

To lock with all optional dependencies enabled:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-6-1)$ uv
```

Note extras are not supported with the `requirements.in` format.
To lock a dependency group in the current project directory's `pyproject.toml`, for example the group `foo`:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-7-1)$ uv
```

Important
A `--group` flag has to be added to pip-tools' `pip compile`, 
To specify the project directory where groups should be sourced from:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-8-1)$ uv
```

Alternatively, you can specify a path to a `pyproject.toml` for each group:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-9-1)$ uv
```

Note
`--group` flags do not apply to other specified sources. For instance, `uv pip compile some/path/pyproject.toml --group foo` sources `foo` from `./pyproject.toml` and **not** `some/path/pyproject.toml`.
## [Upgrading requirements](https://docs.astral.sh/uv/pip/compile/#upgrading-requirements)
When using an output file, uv will consider the versions pinned in an existing output file. If a dependency is pinned it will not be upgraded on a subsequent compile run. For example:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-10-1)$ echo"ruff==0.3.0"[](https://docs.astral.sh/uv/pip/compile/#__codelineno-10-2)$ echo"ruff"|[](https://docs.astral.sh/uv/pip/compile/#__codelineno-10-3)# This[](https://docs.astral.sh/uv/pip/compile/#__codelineno-10-4)#    uv[](https://docs.astral.sh/uv/pip/compile/#__codelineno-10-5)ruff==0.3.0

```

To upgrade a dependency, use the `--upgrade-package` flag:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-11-1)$ uv
```

To upgrade all dependencies, there is an `--upgrade` flag.
## [Syncing an environment](https://docs.astral.sh/uv/pip/compile/#syncing-an-environment)
Dependencies can be installed directly from their definition files or from compiled `requirements.txt` files with `uv pip install`. See the documentation on [installing packages from files](https://docs.astral.sh/uv/pip/packages/#installing-packages-from-files) for more details.
When installing with `uv pip install`, packages that are already installed will not be removed unless they conflict with the lockfile. This means that the environment can have dependencies that aren't declared in the lockfile, which isn't great for reproducibility. To ensure the environment exactly matches the lockfile, use `uv pip sync` instead.
To sync an environment with a `requirements.txt` file:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-12-1)$ uv
```

To sync an environment with a `pylock.toml` file:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-13-1)$ uv
```

## [Adding constraints](https://docs.astral.sh/uv/pip/compile/#adding-constraints)
Constraints files are `requirements.txt`-like files that only control the _version_ of a requirement that's installed. However, including a package in a constraints file will _not_ trigger the installation of that package. Constraints can be used to add bounds to dependencies that are not dependencies of the current project.
To define a constraint, define a bound for a package:
constraints.txt```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-14-1)pydantic<2.0

```

To use a constraints file:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-15-1)$ uv
```

Note that multiple constraints can be defined in each file and multiple files can be used.
uv will also read `constraint-dependencies` from the `pyproject.toml` at the workspace root, and append them to those specified in the constraints file.
## [Adding build constraints](https://docs.astral.sh/uv/pip/compile/#adding-build-constraints)
Similar to `constraints`, but specifically for build-time dependencies, including those required when building runtime dependencies.
Build constraint files are `requirements.txt`-like files that only control the _version_ of a build-time requirement. However, including a package in a build constraints file will _not_ trigger its installation at build time; instead, constraints apply only when the package is required as a direct or transitive build-time dependency. Build constraints can be used to add bounds to dependencies that are not explicitly declared as build-time dependencies of the current project.
For example, if a package defines its build dependencies as follows:
pyproject.toml```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-16-1)[build-system]
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-16-2)requires=["setuptools"]
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-16-3)build-backend="setuptools.build_meta"

```

Build constraints could be used to ensure that a specific version of `setuptools` is used for every package in the workspace:
build-constraints.txt```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-17-1)setuptools==75.0.0

```

uv will also read `build-constraint-dependencies` from the `pyproject.toml` at the workspace root, and append them to those specified in the build constraints file.
## [Overriding dependency versions](https://docs.astral.sh/uv/pip/compile/#overriding-dependency-versions)
Overrides files are `requirements.txt`-like files that force a specific version of a requirement to be installed, regardless of the requirements declared by any constituent package, and regardless of whether this would be considered an invalid resolution.
While constraints are _additive_ , in that they're combined with the requirements of the constituent packages, overrides are _absolute_ , in that they completely replace the requirements of the constituent packages.
Overrides are most often used to remove upper bounds from a transitive dependency. For example, if `a` requires `c>=1.0,<2.0` and `b` requires `c>=2.0` and the current project requires `a` and `b` then the dependencies cannot be resolved.
To define an override, define the new requirement for the problematic package:
overrides.txt```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-18-1)c>=2.0

```

To use an overrides file:
```
[](https://docs.astral.sh/uv/pip/compile/#__codelineno-19-1)$ uv
```

Now, resolution can succeed. However, note that if `a` is _correct_ that it does not support `c>=2.0` then a runtime error will likely be encountered when using the packages.
Note that multiple overrides can be defined in each file and multiple files can be used.
July 8, 2025
