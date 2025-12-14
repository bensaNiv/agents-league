---
# Smart Librarian Export (v2.0)
- Page Number: 18
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/projects/dependencies
- Page Title: Managing dependencies | uv
- Semantic Filename: managing_dependencies_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 53,111 characters
---

# Managing dependencies | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/projects/dependencies/#managing-dependencies)
# [Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#managing-dependencies)
## [Dependency fields](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-fields)
Dependencies of the project are defined in several fields:
  * [`project.dependencies`](https://docs.astral.sh/uv/concepts/projects/dependencies/#project-dependencies): Published dependencies.
  * [`project.optional-dependencies`](https://docs.astral.sh/uv/concepts/projects/dependencies/#optional-dependencies): Published optional dependencies, or "extras".
  * [`dependency-groups`](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-groups): Local dependencies for development.
  * [`tool.uv.sources`](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources): Alternative sources for dependencies during development.


Note
The `project.dependencies` and `project.optional-dependencies` fields can be used even if project isn't going to be published. `dependency-groups` are a recently standardized feature and may not be supported by all tools yet.
uv supports modifying the project's dependencies with `uv add` and `uv remove`, but dependency metadata can also be updated by editing the `pyproject.toml` directly.
## [Adding dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#adding-dependencies)
To add a dependency:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-0-1)$ uv
```

An entry will be added in the `project.dependencies` field:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-1-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-1-2)name="example"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-1-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-1-4)dependencies=["httpx>=0.27.2"]

```

The [`--dev`](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies), [`--group`](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-groups), or [`--optional`](https://docs.astral.sh/uv/concepts/projects/dependencies/#optional-dependencies) flags can be used to add dependencies to an alternative field.
The dependency will include a constraint, e.g., `>=0.27.2`, for the most recent, compatible version of the package. The kind of bound can be adjusted with [`--bounds`](https://docs.astral.sh/uv/reference/settings/#add-bounds), or the constraint can be provided directly:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-2-1)$ uv"httpx>=0.20"

```

When adding a dependency from a source other than a package registry, uv will add an entry in the sources field. For example, when adding `httpx` from GitHub:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-3-1)$ uv"httpx @ git+https://github.com/encode/httpx"

```

The `pyproject.toml` will include a [Git source entry](https://docs.astral.sh/uv/concepts/projects/dependencies/#git):
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-2)name="example"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-4)dependencies=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-5)"httpx",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-6)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-7)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-8)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-4-9)httpx={git="https://github.com/encode/httpx"}

```

If a dependency cannot be used, uv will display an error.:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-5-1)$ uv"httpx>9999"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-5-2)  × No solution found when resolving dependencies:
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-5-3)  ╰─▶ Because only httpx<=1.0.0b0 is available and your project depends on httpx>9999,
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-5-4)      we can conclude that your project's requirements are unsatisfiable.

```

### [Importing dependencies from requirements files](https://docs.astral.sh/uv/concepts/projects/dependencies/#importing-dependencies-from-requirements-files)
Dependencies declared in a `requirements.txt` file can be added to the project with the `-r` option:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-6-1)uv add -r requirements.txt

```

See the [pip migration guide](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-requirements-files) for more details.
## [Removing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#removing-dependencies)
To remove a dependency:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-7-1)$ uv
```

The `--dev`, `--group`, or `--optional` flags can be used to remove a dependency from a specific table.
If a [source](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources) is defined for the removed dependency, and there are no other references to the dependency, it will also be removed.
## [Changing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#changing-dependencies)
To change an existing dependency, e.g., to use a different constraint for `httpx`:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-8-1)$ uv"httpx>0.1.0"

```

Note
In this example, we are changing the constraints for the dependency in the `pyproject.toml`. The locked version of the dependency will only change if necessary to satisfy the new constraints. To force the package version to update to the latest within the constraints, use `--upgrade-package <name>`, e.g.:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-9-1)$ uv"httpx>0.1.0"
```

See the [lockfile](https://docs.astral.sh/uv/concepts/projects/sync/#upgrading-locked-package-versions) documentation for more details on upgrading packages.
Requesting a different dependency source will update the `tool.uv.sources` table, e.g., to use `httpx` from a local path during development:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-10-1)$ uv"httpx @ ../httpx"

```

## [Platform-specific dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#platform-specific-dependencies)
To ensure that a dependency is only installed on a specific platform or on specific Python versions, use 
For example, to install `jax` on Linux, but not on Windows or macOS:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-11-1)$ uv"jax; sys_platform == 'linux'"

```

The resulting `pyproject.toml` will then include the environment marker in the dependency definition:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-12-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-12-2)name="project"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-12-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-12-4)requires-python=">=3.11"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-12-5)dependencies=["jax; sys_platform == 'linux'"]

```

Similarly, to include `numpy` on Python 3.11 and later:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-13-1)$ uv"numpy; python_version >= '3.11'"

```

See Python's 
Tip
Dependency sources can also be [changed per-platform](https://docs.astral.sh/uv/concepts/projects/dependencies/#platform-specific-sources).
## [Project dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#project-dependencies)
The `project.dependencies` table represents the dependencies that are used when uploading to PyPI or building a wheel. Individual dependencies are specified using 
`project.dependencies` defines the list of packages that are required for the project, along with the version constraints that should be used when installing them. Each entry includes a dependency name and version. An entry may include extras or environment markers for platform-specific packages. For example:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-2)name="albatross"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-4)dependencies=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-5)# Any version in this range
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-6)"tqdm >=4.66.2,<5",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-7)# Exactly this version of torch
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-8)"torch ==2.2.2",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-9)# Install transformers with the torch extra
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-10)"transformers[torch] >=4.39.3,<5",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-11)# Only install this package on older python versions
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-12)# See "Environment Markers" for more information
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-13)"importlib_metadata >=7.1.0,<8; python_version < '3.10'",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-14)"mollymawk ==0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-14-15)]

```

## [Dependency sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources)
The `tool.uv.sources` table extends the standard dependency tables with alternative dependency sources, which are used during development.
Dependency sources add support for common patterns that are not supported by the `project.dependencies` standard, like editable installations and relative paths. For example, to install `foo` from a directory relative to the project root:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-2)name="example"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-4)dependencies=["foo"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-5)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-6)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-15-7)foo={path="./packages/foo"}

```

The following dependency sources are supported by uv:
  * [Index](https://docs.astral.sh/uv/concepts/projects/dependencies/#index): A package resolved from a specific package index.
  * [Git](https://docs.astral.sh/uv/concepts/projects/dependencies/#git): A Git repository.
  * [URL](https://docs.astral.sh/uv/concepts/projects/dependencies/#url): A remote wheel or source distribution.
  * [Path](https://docs.astral.sh/uv/concepts/projects/dependencies/#path): A local wheel, source distribution, or project directory.
  * [Workspace](https://docs.astral.sh/uv/concepts/projects/dependencies/#workspace-member): A member of the current workspace.


Important
Sources are only respected by uv. If another tool is used, only the definitions in the standard project tables will be used. If another tool is being used for development, any metadata provided in the source table will need to be re-specified in the other tool's format.
### [Index](https://docs.astral.sh/uv/concepts/projects/dependencies/#index)
To add Python package from a specific index, use the `--index` option:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-16-1)$ uvpytorch=https://download.pytorch.org/whl/cpu

```

uv will store the index in `[[tool.uv.index]]` and add a `[tool.uv.sources]` entry:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-2)dependencies=["torch"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-5)torch={index="pytorch"}
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-6)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-7)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-8)name="pytorch"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-17-9)url="https://download.pytorch.org/whl/cpu"

```

Tip
The above example will only work on x86-64 Linux, due to the specifics of the PyTorch index. See the [PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/) for more information about setting up PyTorch.
Using an `index` source _pins_ a package to the given index — it will not be downloaded from other indexes.
When defining an index, an `explicit` flag can be included to indicate that the index should _only_ be used for packages that explicitly specify it in `tool.uv.sources`. If `explicit` is not set, other packages may be resolved from the index, if not found elsewhere.
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-18-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-18-2)name="pytorch"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-18-3)url="https://download.pytorch.org/whl/cpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-18-4)explicit=true

```

### [Git](https://docs.astral.sh/uv/concepts/projects/dependencies/#git)
To add a Git dependency source, prefix a Git-compatible URL with `git+`.
For example:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-19-1)$ # Install over HTTP(S).
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-19-2)$ uv[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-19-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-19-4)$ # Install over SSH.
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-19-5)$ uv
```

pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-20-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-20-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-20-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-20-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-20-5)httpx={git="https://github.com/encode/httpx"}

```

Specific Git references can be requested, e.g., a tag:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-21-1)$ uv0.27.0

```

pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-22-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-22-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-22-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-22-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-22-5)httpx={git="https://github.com/encode/httpx",tag="0.27.0"}

```

Or, a branch:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-23-1)$ uv
```

pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-24-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-24-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-24-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-24-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-24-5)httpx={git="https://github.com/encode/httpx",branch="main"}

```

Or, a revision (commit):
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-25-1)$ uv
```

pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-26-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-26-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-26-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-26-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-26-5)httpx={git="https://github.com/encode/httpx",rev="326b9431c761e1ef1e00b9f760d1f654c8db48c6"}

```

A `subdirectory` may be specified if the package isn't in the repository root:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-27-1)$ uv=libs/langchain

```

pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-28-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-28-2)dependencies=["langchain"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-28-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-28-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-28-5)langchain={git="https://github.com/langchain-ai/langchain",subdirectory="libs/langchain"}

```

Support for 
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-29-1)$ uv
```

pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-30-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-30-2)dependencies=["lfs-cowsay"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-30-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-30-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-30-5)lfs-cowsay={git="https://github.com/astral-sh/lfs-cowsay",lfs=true}

```

  * When `lfs = true`, uv will always fetch LFS objects for this Git source.
  * When `lfs = false`, uv will never fetch LFS objects for this Git source.
  * When omitted, the `UV_GIT_LFS` environment variable is used for all Git sources without an explicit `lfs` configuration.


Important
Ensure Git LFS is installed and configured on your system before attempting to install sources using Git LFS, otherwise a build failure can occur.
### [URL](https://docs.astral.sh/uv/concepts/projects/dependencies/#url)
To add a URL source, provide a `https://` URL to either a wheel (ending in `.whl`) or a source distribution (typically ending in `.tar.gz` or `.zip`; see [here](https://docs.astral.sh/uv/concepts/resolution/#source-distribution) for all supported formats).
For example:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-31-1)$ uv"https://files.pythonhosted.org/packages/5c/2d/3da5bdf4408b8b2800061c339f240c1802f2e82d55e50bd39c5a881f47f0/httpx-0.27.0.tar.gz"

```

Will result in a `pyproject.toml` with:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-32-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-32-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-32-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-32-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-32-5)httpx={url="https://files.pythonhosted.org/packages/5c/2d/3da5bdf4408b8b2800061c339f240c1802f2e82d55e50bd39c5a881f47f0/httpx-0.27.0.tar.gz"}

```

URL dependencies can also be manually added or edited in the `pyproject.toml` with the `{ url = <url> }` syntax. A `subdirectory` may be specified if the source distribution isn't in the archive root.
### [Path](https://docs.astral.sh/uv/concepts/projects/dependencies/#path)
To add a path source, provide the path of a wheel (ending in `.whl`), a source distribution (typically ending in `.tar.gz` or `.zip`; see [here](https://docs.astral.sh/uv/concepts/resolution/#source-distribution) for all supported formats), or a directory containing a `pyproject.toml`.
For example:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-33-1)$ uv
```

Will result in a `pyproject.toml` with:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-34-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-34-2)dependencies=["foo"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-34-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-34-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-34-5)foo={path="/example/foo-0.1.0-py3-none-any.whl"}

```

The path may also be a relative path:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-35-1)$ uv
```

Or, a path to a project directory:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-36-1)$ uv
```

Important
When using a directory as a path dependency, uv will attempt to build and install the target as a package by default. See the [virtual dependency](https://docs.astral.sh/uv/concepts/projects/dependencies/#virtual-dependencies) documentation for details.
An [editable installation](https://docs.astral.sh/uv/concepts/projects/dependencies/#editable-dependencies) is not used for path dependencies by default. An editable installation may be requested for project directories:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-37-1)$ uv
```

Which will result in a `pyproject.toml` with:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-38-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-38-2)dependencies=["bar"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-38-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-38-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-38-5)bar={path="../projects/bar",editable=true}

```

Tip
For multiple packages in the same repository, [_workspaces_](https://docs.astral.sh/uv/concepts/projects/workspaces/) may be a better fit.
### [Workspace member](https://docs.astral.sh/uv/concepts/projects/dependencies/#workspace-member)
To declare a dependency on a workspace member, add the member name with `{ workspace = true }`. All workspace members must be explicitly stated. Workspace members are always [editable](https://docs.astral.sh/uv/concepts/projects/dependencies/#editable-dependencies) . See the [workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/) documentation for more details on workspaces.
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-2)dependencies=["foo==0.1.0"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-5)foo={workspace=true}
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-6)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-7)[tool.uv.workspace]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-8)members=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-9)"packages/foo"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-39-10)]

```

### [Platform-specific sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#platform-specific-sources)
You can limit a source to a given platform or Python version by providing 
For example, to pull `httpx` from GitHub, but only on macOS, use the following:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-40-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-40-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-40-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-40-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-40-5)httpx={git="https://github.com/encode/httpx",tag="0.27.2",marker="sys_platform == 'darwin'"}

```

By specifying the marker on the source, uv will still include `httpx` on all platforms, but will download the source from GitHub on macOS, and fall back to PyPI on all other platforms.
### [Multiple sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#multiple-sources)
You can specify multiple sources for a single dependency by providing a list of sources, disambiguated by 
For example, to pull in different `httpx` tags on macOS vs. Linux:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-2)dependencies=["httpx"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-5)httpx=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-6){git="https://github.com/encode/httpx",tag="0.27.2",marker="sys_platform == 'darwin'"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-7){git="https://github.com/encode/httpx",tag="0.24.1",marker="sys_platform == 'linux'"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-41-8)]

```

This strategy extends to using different indexes based on environment markers. For example, to install `torch` from different PyTorch indexes based on the platform:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-2)dependencies=["torch"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-5)torch=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-6){index="torch-cpu",marker="platform_system == 'Darwin'"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-7){index="torch-gpu",marker="platform_system == 'Linux'"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-8)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-9)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-10)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-11)name="torch-cpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-12)url="https://download.pytorch.org/whl/cpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-13)explicit=true
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-14)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-15)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-16)name="torch-gpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-17)url="https://download.pytorch.org/whl/cu124"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-42-18)explicit=true

```

### [Disabling sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#disabling-sources)
To instruct uv to ignore the `tool.uv.sources` table (e.g., to simulate resolving with the package's published metadata), use the `--no-sources` flag:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-43-1)$ uv
```

The use of `--no-sources` will also prevent uv from discovering any [workspace members](https://docs.astral.sh/uv/concepts/projects/dependencies/#workspace-member) that could satisfy a given dependency.
## [Optional dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#optional-dependencies)
It is common for projects that are published as libraries to make some features optional to reduce the default dependency tree. For example, Pandas has an `matplotlib` unless someone explicitly requires them. Extras are requested with the `package[<extra>]` syntax, e.g., `pandas[plot, excel]`.
Optional dependencies are specified in `[project.optional-dependencies]`, a TOML table that maps from extra name to its dependencies, following [dependency specifiers](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-specifiers) syntax.
Optional dependencies can have entries in `tool.uv.sources` the same as normal dependencies.
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-2)name="pandas"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-3)version="1.0.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-4)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-5)[project.optional-dependencies]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-6)plot=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-7)"matplotlib>=3.6.3"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-8)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-9)excel=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-10)"odfpy>=1.4.1",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-11)"openpyxl>=3.1.0",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-12)"python-calamine>=0.1.7",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-13)"pyxlsb>=1.0.10",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-14)"xlrd>=2.0.1",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-15)"xlsxwriter>=3.0.5"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-44-16)]

```

To add an optional dependency, use the `--optional <extra>` option:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-45-1)$ uv
```

Note
If you have optional dependencies that conflict with one another, resolution will fail unless you explicitly [declare them as conflicting](https://docs.astral.sh/uv/concepts/projects/config/#conflicting-dependencies).
Sources can also be declared as applying only to a specific optional dependency. For example, to pull `torch` from different PyTorch indexes based on an optional `cpu` or `gpu` extra:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-2)dependencies=[]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-4)[project.optional-dependencies]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-5)cpu=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-6)"torch",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-7)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-8)gpu=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-9)"torch",
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-10)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-11)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-12)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-13)torch=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-14){index="torch-cpu",extra="cpu"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-15){index="torch-gpu",extra="gpu"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-16)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-17)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-18)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-19)name="torch-cpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-20)url="https://download.pytorch.org/whl/cpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-21)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-22)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-23)name="torch-gpu"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-46-24)url="https://download.pytorch.org/whl/cu124"

```

## [Development dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies)
Unlike optional dependencies, development dependencies are local-only and will _not_ be included in the project requirements when published to PyPI or other indexes. As such, development dependencies are not included in the `[project]` table.
Development dependencies can have entries in `tool.uv.sources` the same as normal dependencies.
To add a development dependency, use the `--dev` flag:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-47-1)$ uv
```

uv uses the `[dependency-groups]` table (as defined in `dev` group:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-48-1)[dependency-groups]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-48-2)dev=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-48-3)"pytest >=8.1.1,<9"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-48-4)]

```

The `dev` group is special-cased; there are `--dev`, `--only-dev`, and `--no-dev` flags to toggle inclusion or exclusion of its dependencies. See `--no-default-groups` to disable all default groups instead. Additionally, the `dev` group is [synced by default](https://docs.astral.sh/uv/concepts/projects/dependencies/#default-groups).
### [Dependency groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-groups)
Development dependencies can be divided into multiple groups, using the `--group` flag.
For example, to add a development dependency in the `lint` group:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-49-1)$ uv
```

Which results in the following `[dependency-groups]` definition:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-1)[dependency-groups]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-2)dev=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-3)"pytest"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-4)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-5)lint=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-6)"ruff"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-50-7)]

```

Once groups are defined, the `--all-groups`, `--no-default-groups`, `--group`, `--only-group`, and `--no-group` options can be used to include or exclude their dependencies.
Tip
The `--dev`, `--only-dev`, and `--no-dev` flags are equivalent to `--group dev`, `--only-group dev`, and `--no-group dev` respectively.
uv requires that all dependency groups are compatible with each other and resolves all groups together when creating the lockfile.
If dependencies declared in one group are not compatible with those in another group, uv will fail to resolve the requirements of the project with an error.
Note
If you have dependency groups that conflict with one another, resolution will fail unless you explicitly [declare them as conflicting](https://docs.astral.sh/uv/concepts/projects/config/#conflicting-dependencies).
### [Nesting groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#nesting-groups)
A dependency group can include other dependency groups, e.g.:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-1)[dependency-groups]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-2)dev=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-3){include-group="lint"},
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-4){include-group="test"}
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-5)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-6)lint=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-7)"ruff"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-8)]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-9)test=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-10)"pytest"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-51-11)]

```

An included group's dependencies cannot conflict with the other dependencies declared in a group.
### [Default groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#default-groups)
By default, uv includes the `dev` dependency group in the environment (e.g., during `uv run` or `uv sync`). The default groups to include can be changed using the `tool.uv.default-groups` setting.
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-52-1)[tool.uv]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-52-2)default-groups=["dev","foo"]

```

To enable all dependencies groups by default, use `"all"` instead of listing group names:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-53-1)[tool.uv]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-53-2)default-groups="all"

```

Tip
To disable this behaviour during `uv run` or `uv sync`, use `--no-default-groups`. To exclude a specific default group, use `--no-group <name>`.
### [Group `requires-python`](https://docs.astral.sh/uv/concepts/projects/dependencies/#group-requires-python)
By default, dependency groups must be compatible with your project's `requires-python` range.
If a dependency group requires a different range of Python versions than your project, you can specify a `requires-python` for the group in `[tool.uv.dependency-groups]`, e.g.:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-2)name="example"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-3)version="0.0.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-4)requires-python=">=3.10"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-5)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-6)[dependency-groups]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-7)dev=["pytest"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-8)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-9)[tool.uv.dependency-groups]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-54-10)dev={requires-python=">=3.12"}

```

### [Legacy `dev-dependencies`](https://docs.astral.sh/uv/concepts/projects/dependencies/#legacy-dev-dependencies)
Before `[dependency-groups]` was standardized, uv used the `tool.uv.dev-dependencies` field to specify development dependencies, e.g.:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-55-1)[tool.uv]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-55-2)dev-dependencies=[
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-55-3)"pytest"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-55-4)]

```

Dependencies declared in this section will be combined with the contents in the `dependency-groups.dev`. Eventually, the `dev-dependencies` field will be deprecated and removed.
Note
If a `tool.uv.dev-dependencies` field exists, `uv add --dev` will use the existing section instead of adding a new `dependency-groups.dev` section.
## [Build dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#build-dependencies)
If a project is structured as [Python package](https://docs.astral.sh/uv/concepts/projects/config/#build-systems), it may declare dependencies that are required to build the project, but not required to run it. These dependencies are specified in the `[build-system]` table under `build-system.requires`, following 
For example, if a project uses `setuptools` as its build backend, it should declare `setuptools` as a build dependency:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-2)name="pandas"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-4)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-5)[build-system]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-6)requires=["setuptools>=42"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-56-7)build-backend="setuptools.build_meta"

```

By default, uv will respect `tool.uv.sources` when resolving build dependencies. For example, to use a local version of `setuptools` for building, add the source to `tool.uv.sources`:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-2)name="pandas"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-3)version="0.1.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-4)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-5)[build-system]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-6)requires=["setuptools>=42"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-7)build-backend="setuptools.build_meta"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-8)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-9)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-57-10)setuptools={path="./packages/setuptools"}

```

When publishing a package, we recommend running `uv build --no-sources` to ensure that the package builds correctly when `tool.uv.sources` is disabled, as is the case when using other build tools, like 
## [Editable dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#editable-dependencies)
A regular installation of a directory with a Python package first builds a wheel and then installs that wheel into your virtual environment, copying all source files. When the package source files are edited, the virtual environment will contain outdated versions.
Editable installations solve this problem by adding a link to the project within the virtual environment (a `.pth` file), which instructs the interpreter to include the source files directly.
There are some limitations to editables (mainly: the build backend needs to support them, and native modules aren't recompiled before import), but they are useful for development, as the virtual environment will always use the latest changes to the package.
uv uses editable installation for workspace packages by default.
To add an editable dependency, use the `--editable` flag:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-58-1)$ uv
```

Or, to opt-out of using an editable dependency in a workspace:
```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-59-1)$ uv
```

## [Virtual dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#virtual-dependencies)
uv allows dependencies to be "virtual", in which the dependency itself is not installed as a [package](https://docs.astral.sh/uv/concepts/projects/config/#project-packaging), but its dependencies are.
By default, dependencies are never virtual.
A dependency with a [`path` source](https://docs.astral.sh/uv/concepts/projects/dependencies/#path) can be virtual if it explicitly sets [`tool.uv.package = false`](https://docs.astral.sh/uv/reference/settings/#package). Unlike working _in_ the dependent project with uv, the package will be built even if a [build system](https://docs.astral.sh/uv/concepts/projects/config/#build-systems) is not declared.
To treat a dependency as virtual, set `package = false` on the source:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-60-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-60-2)dependencies=["bar"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-60-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-60-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-60-5)bar={path="../projects/bar",package=false}

```

If a dependency sets `tool.uv.package = false`, it can be overridden by declaring `package = true` on the source:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-61-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-61-2)dependencies=["bar"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-61-3)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-61-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-61-5)bar={path="../projects/bar",package=true}

```

Similarly, a dependency with a [`workspace` source](https://docs.astral.sh/uv/concepts/projects/dependencies/#workspace-member) can be virtual if it explicitly sets [`tool.uv.package = false`](https://docs.astral.sh/uv/reference/settings/#package). The workspace member will be built even if a [build system](https://docs.astral.sh/uv/concepts/projects/config/#build-systems) is not declared.
Workspace members that are _not_ dependencies can be virtual by default, e.g., if the parent `pyproject.toml` is:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-2)name="parent"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-3)version="1.0.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-4)dependencies=[]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-5)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-6)[tool.uv.workspace]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-62-7)members=["child"]

```

And the child `pyproject.toml` excluded a build system:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-63-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-63-2)name="child"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-63-3)version="1.0.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-63-4)dependencies=["anyio"]

```

Then the `child` workspace member would not be installed, but the transitive dependency `anyio` would be.
In contrast, if the parent declared a dependency on `child`:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-2)name="parent"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-3)version="1.0.0"
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-4)dependencies=["child"]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-5)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-6)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-7)child={workspace=true}
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-8)
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-9)[tool.uv.workspace]
[](https://docs.astral.sh/uv/concepts/projects/dependencies/#__codelineno-64-10)members=["child"]

```

Then `child` would be built and installed.
## [Dependency specifiers](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-specifiers)
uv uses standard 
  * The dependency name
  * The extras you want (optional)
  * The version specifier
  * An environment marker (optional)


The version specifiers are comma separated and added together, e.g., `foo >=1.2.3,<2,!=1.4.0` is interpreted as "a version of `foo` that's at least 1.2.3, but less than 2, and not 1.4.0".
Specifiers are padded with trailing zeros if required, so `foo ==2` matches foo 2.0.0, too.
A star can be used for the last digit with equals, e.g., `foo ==2.1.*` will accept any release from the 2.1 series. Similarly, `~=` matches where the last digit is equal or higher, e.g., `foo ~=1.2` is equal to `foo >=1.2,<2`, and `foo ~=1.2.3` is equal to `foo >=1.2.3,<1.3`.
Extras are comma-separated in square bracket between name and version, e.g., `pandas[excel,plot] ==2.2`. Whitespace between extra names is ignored.
Some dependencies are only required in specific environments, e.g., a specific Python version or operating system. For example to install the `importlib-metadata` backport for the `importlib.metadata` module, use `importlib-metadata >=7.1.0,<8; python_version < '3.10'`. To install `colorama` on Windows (but omit it on other platforms), use `colorama >=0.4.6,<5; platform_system == "Windows"`.
Markers are combined with `and`, `or`, and parentheses, e.g., `aiohttp >=3.7.4,<4; (sys_platform != 'win32' or implementation_name != 'pypy') and python_version >= '3.10'`. Note that versions within markers must be quoted, while versions _outside_ of markers must _not_ be quoted.
December 2, 2025
