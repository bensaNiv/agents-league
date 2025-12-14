---
# Smart Librarian Export (v2.0)
- Page Number: 36
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/reference/settings
- Page Title: Settings | uv
- Semantic Filename: settings_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 144,130 characters
---

# Settings | uv

[ Skip to content ](https://docs.astral.sh/uv/reference/settings/#project-metadata)
# Settings
## [Project metadata](https://docs.astral.sh/uv/reference/settings/#project-metadata)
###  [](https://docs.astral.sh/uv/reference/settings/#build-constraint-dependencies)[`build-constraint-dependencies`](https://docs.astral.sh/uv/reference/settings/#build-constraint-dependencies)
Constraints to apply when solving build dependencies.
Build constraints are used to restrict the versions of build dependencies that are selected when building a package during resolution or installation.
Including a package as a constraint will _not_ trigger installation of the package during a build; instead, the package must be requested elsewhere in the project's build dependency graph.
Note
In `uv lock`, `uv sync`, and `uv run`, uv will only read `build-constraint-dependencies` from the `pyproject.toml` at the workspace root, and will ignore any declarations in other workspace members or `uv.toml` files.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-0-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-0-2)# Ensure that the setuptools v60.0.0 is used whenever a package has a build dependency
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-0-3)# on setuptools.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-0-4)build-constraint-dependencies=["setuptools==60.0.0"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#conflicts)[`conflicts`](https://docs.astral.sh/uv/reference/settings/#conflicts)
Declare collections of extras or dependency groups that are conflicting (i.e., mutually exclusive).
It's useful to declare conflicts when two or more extras have mutually incompatible dependencies. For example, extra `foo` might depend on `numpy==2.0.0` while extra `bar` depends on `numpy==2.1.0`. While these dependencies conflict, it may be the case that users are not expected to activate both `foo` and `bar` at the same time, making it possible to generate a universal resolution for the project despite the incompatibility.
By making such conflicts explicit, uv can generate a universal resolution for a project, taking into account that certain combinations of extras and groups are mutually exclusive. In exchange, installation will fail if a user attempts to activate both conflicting extras.
**Default value** : `[]`
**Type** : `list[list[dict]]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-2)# Require that `package[extra1]` and `package[extra2]` are resolved
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-3)# in different forks so that they cannot conflict with one another.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-4)conflicts=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-5)[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-6){extra="extra1"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-7){extra="extra2"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-8)]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-9)]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-10)
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-11)# Require that the dependency groups `group1` and `group2`
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-12)# are resolved in different forks so that they cannot conflict
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-13)# with one another.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-14)conflicts=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-15)[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-16){group="group1"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-17){group="group2"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-18)]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-1-19)]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#constraint-dependencies)[`constraint-dependencies`](https://docs.astral.sh/uv/reference/settings/#constraint-dependencies)
Constraints to apply when resolving the project's dependencies.
Constraints are used to restrict the versions of dependencies that are selected during resolution.
Including a package as a constraint will _not_ trigger installation of the package on its own; instead, the package must be requested elsewhere in the project's first-party or transitive dependencies.
Note
In `uv lock`, `uv sync`, and `uv run`, uv will only read `constraint-dependencies` from the `pyproject.toml` at the workspace root, and will ignore any declarations in other workspace members or `uv.toml` files.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-2-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-2-2)# Ensure that the grpcio version is always less than 1.65, if it's requested by a
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-2-3)# direct or transitive dependency.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-2-4)constraint-dependencies=["grpcio<1.65"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#default-groups)[`default-groups`](https://docs.astral.sh/uv/reference/settings/#default-groups)
The list of `dependency-groups` to install by default.
Can also be the literal `"all"` to default enable all groups.
**Default value** : `["dev"]`
**Type** : `str | list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-3-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-3-2)default-groups=["docs"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#dependency-groups)[`dependency-groups`](https://docs.astral.sh/uv/reference/settings/#dependency-groups)
Additional settings for `dependency-groups`.
Currently this can only be used to add `requires-python` constraints to dependency groups (typically to inform uv that your dev tooling has a higher python requirement than your actual project).
This cannot be used to define dependency groups, use the top-level `[dependency-groups]` table for that.
**Default value** : `[]`
**Type** : `dict`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-4-1)[tool.uv.dependency-groups]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-4-2)my-group={requires-python=">=3.12"}

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#dev-dependencies)[`dev-dependencies`](https://docs.astral.sh/uv/reference/settings/#dev-dependencies)
The project's development dependencies.
Development dependencies will be installed by default in `uv run` and `uv sync`, but will not appear in the project's published metadata.
Use of this field is not recommend anymore. Instead, use the `dependency-groups.dev` field which is a standardized way to declare development dependencies. The contents of `tool.uv.dev-dependencies` and `dependency-groups.dev` are combined to determine the final requirements of the `dev` dependency group.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-5-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-5-2)dev-dependencies=["ruff==0.5.0"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#environments)[`environments`](https://docs.astral.sh/uv/reference/settings/#environments)
A list of supported environments against which to resolve dependencies.
By default, uv will resolve for all possible environments during a `uv lock` operation. However, you can restrict the set of supported environments to improve performance and avoid unsatisfiable branches in the solution space.
These environments will also be respected when `uv pip compile` is invoked with the `--universal` flag.
**Default value** : `[]`
**Type** : `str | list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-6-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-6-2)# Resolve for macOS, but not for Linux or Windows.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-6-3)environments=["sys_platform == 'darwin'"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#exclude-dependencies)[`exclude-dependencies`](https://docs.astral.sh/uv/reference/settings/#exclude-dependencies)
Dependencies to exclude when resolving the project's dependencies.
Excludes are used to prevent a package from being selected during resolution, regardless of whether it's requested by any other package. When a package is excluded, it will be omitted from the dependency list entirely.
Including a package as an exclusion will prevent it from being installed, even if it's requested by transitive dependencies. This can be useful for removing optional dependencies or working around packages with broken dependencies.
Note
In `uv lock`, `uv sync`, and `uv run`, uv will only read `exclude-dependencies` from the `pyproject.toml` at the workspace root, and will ignore any declarations in other workspace members or `uv.toml` files.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-7-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-7-2)# Exclude Werkzeug from being installed, even if transitive dependencies request it.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-7-3)exclude-dependencies=["werkzeug"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#index)[`index`](https://docs.astral.sh/uv/reference/settings/#index)
The indexes to use when resolving dependencies.
Accepts either a repository compliant with 
Indexes are considered in the order in which they're defined, such that the first-defined index has the highest priority. Further, the indexes provided by this setting are given higher priority than any indexes specified via [`index_url`](https://docs.astral.sh/uv/reference/settings/#index-url) or [`extra_index_url`](https://docs.astral.sh/uv/reference/settings/#extra-index-url). uv will only consider the first index that contains a given package, unless an alternative [index strategy](https://docs.astral.sh/uv/reference/settings/#index-strategy) is specified.
If an index is marked as `explicit = true`, it will be used exclusively for the dependencies that select it explicitly via `[tool.uv.sources]`, as in:
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-2)name="pytorch"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-3)url="https://download.pytorch.org/whl/cu121"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-4)explicit=true
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-5)
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-6)[tool.uv.sources]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-8-7)torch={index="pytorch"}

```

If an index is marked as `default = true`, it will be moved to the end of the prioritized list, such that it is given the lowest priority when resolving packages. Additionally, marking an index as default will disable the PyPI default index.
**Default value** : `[]`
**Type** : `dict`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-9-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-9-2)name="pytorch"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-9-3)url="https://download.pytorch.org/whl/cu121"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#managed)[`managed`](https://docs.astral.sh/uv/reference/settings/#managed)
Whether the project is managed by uv. If `false`, uv will ignore the project when `uv run` is invoked.
**Default value** : `true`
**Type** : `bool`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-10-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-10-2)managed=false

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#override-dependencies)[`override-dependencies`](https://docs.astral.sh/uv/reference/settings/#override-dependencies)
Overrides to apply when resolving the project's dependencies.
Overrides are used to force selection of a specific version of a package, regardless of the version requested by any other package, and regardless of whether choosing that version would typically constitute an invalid resolution.
While constraints are _additive_ , in that they're combined with the requirements of the constituent packages, overrides are _absolute_ , in that they completely replace the requirements of any constituent packages.
Including a package as an override will _not_ trigger installation of the package on its own; instead, the package must be requested elsewhere in the project's first-party or transitive dependencies.
Note
In `uv lock`, `uv sync`, and `uv run`, uv will only read `override-dependencies` from the `pyproject.toml` at the workspace root, and will ignore any declarations in other workspace members or `uv.toml` files.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-11-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-11-2)# Always install Werkzeug 2.3.0, regardless of whether transitive dependencies request
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-11-3)# a different version.
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-11-4)override-dependencies=["werkzeug==2.3.0"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#package)[`package`](https://docs.astral.sh/uv/reference/settings/#package)
Whether the project should be considered a Python package, or a non-package ("virtual") project.
Packages are built and installed into the virtual environment in editable mode and thus require a build backend, while virtual projects are _not_ built or installed; instead, only their dependencies are included in the virtual environment.
Creating a package requires that a `build-system` is present in the `pyproject.toml`, and that the project adheres to a structure that adheres to the build backend's expectations (e.g., a `src` layout).
**Default value** : `true`
**Type** : `bool`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-12-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-12-2)package=false

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#required-environments)[`required-environments`](https://docs.astral.sh/uv/reference/settings/#required-environments)
A list of required platforms, for packages that lack source distributions.
When a package does not have a source distribution, it's availability will be limited to the platforms supported by its built distributions (wheels). For example, if a package only publishes wheels for Linux, then it won't be installable on macOS or Windows.
By default, uv requires each package to include at least one wheel that is compatible with the designated Python version. The `required-environments` setting can be used to ensure that the resulting resolution contains wheels for specific platforms, or fails if no such wheels are available.
While the `environments` setting _limits_ the set of environments that uv will consider when resolving dependencies, `required-environments` _expands_ the set of platforms that uv _must_ support when resolving dependencies.
For example, `environments = ["sys_platform == 'darwin'"]` would limit uv to solving for macOS (and ignoring Linux and Windows). On the other hand, `required-environments = ["sys_platform == 'darwin'"]` would _require_ that any package without a source distribution include a wheel for macOS in order to be installable.
**Default value** : `[]`
**Type** : `str | list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-13-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-13-2)# Require that the package is available for macOS ARM and x86 (Intel).
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-13-3)required-environments=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-13-4)"sys_platform == 'darwin' and platform_machine == 'arm64'",
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-13-5)"sys_platform == 'darwin' and platform_machine == 'x86_64'",
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-13-6)]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#sources)[`sources`](https://docs.astral.sh/uv/reference/settings/#sources)
The sources to use when resolving dependencies.
`tool.uv.sources` enriches the dependency metadata with additional sources, incorporated during development. A dependency source can be a Git repository, a URL, a local path, or an alternative registry.
See [Dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) for more.
**Default value** : `{}`
**Type** : `dict`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-14-1)[tool.uv.sources]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-14-2)httpx={git="https://github.com/encode/httpx",tag="0.27.0"}
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-14-3)pytest={url="https://files.pythonhosted.org/packages/6b/77/7440a06a8ead44c7757a64362dd22df5760f9b12dc5f11b6188cd2fc27a0/pytest-8.3.3-py3-none-any.whl"}
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-14-4)pydantic={path="/path/to/pydantic",editable=true}

```

* * *
### [`build-backend`](https://docs.astral.sh/uv/reference/settings/#build-backend)
Settings for the uv build backend (`uv_build`).
Note that those settings only apply when using the `uv_build` backend, other build backends (such as hatchling) have their own configuration.
All options that accept globs use the portable glob patterns from 
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_data)[`data`](https://docs.astral.sh/uv/reference/settings/#build-backend_data)
Data includes for wheels.
Each entry is a directory, whose contents are copied to the matching directory in the wheel in `<name>-<version>.data/(purelib|platlib|headers|scripts|data)`. Upon installation, this data is moved to its target location, as defined by 
  * `scripts`: Installed to the directory for executables, `<venv>/bin` on Unix or `<venv>\Scripts` on Windows. This directory is added to `PATH` when the virtual environment is activated or when using `uv run`, so this data type can be used to install additional binaries. Consider using `project.scripts` instead for Python entrypoints.
  * `data`: Installed over the virtualenv environment root.
Warning: This may override existing files!
  * `headers`: Installed to the include directory. Compilers building Python packages with this package as build requirement use the include directory to find additional header files.
  * `purelib` and `platlib`: Installed to the `site-packages` directory. It is not recommended to use these two options.


**Default value** : `{}`
**Type** : `dict[str, str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-15-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-15-2)data={headers="include/headers",scripts="bin"}

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_default-excludes)[`default-excludes`](https://docs.astral.sh/uv/reference/settings/#build-backend_default-excludes)
If set to `false`, the default excludes aren't applied.
Default excludes: `__pycache__`, `*.pyc`, and `*.pyo`.
**Default value** : `true`
**Type** : `bool`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-16-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-16-2)default-excludes=false

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_module-name)[`module-name`](https://docs.astral.sh/uv/reference/settings/#build-backend_module-name)
The name of the module directory inside `module-root`.
The default module name is the package name with dots and dashes replaced by underscores.
Package names need to be valid Python identifiers, and the directory needs to contain a `__init__.py`. An exception are stubs packages, whose name ends with `-stubs`, with the stem being the module name, and which contain a `__init__.pyi` file.
For namespace packages with a single module, the path can be dotted, e.g., `foo.bar` or `foo-stubs.bar`.
For namespace packages with multiple modules, the path can be a list, e.g., `["foo", "bar"]`. We recommend using a single module per package, splitting multiple packages into a workspace.
Note that using this option runs the risk of creating two packages with different names but the same module names. Installing such packages together leads to unspecified behavior, often with corrupted files or directory trees.
**Default value** : `None`
**Type** : `str | list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-17-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-17-2)module-name="sklearn"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_module-root)[`module-root`](https://docs.astral.sh/uv/reference/settings/#build-backend_module-root)
The directory that contains the module directory.
Common values are `src` (src layout, the default) or an empty path (flat layout).
**Default value** : `"src"`
**Type** : `str`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-18-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-18-2)module-root=""

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_namespace)[`namespace`](https://docs.astral.sh/uv/reference/settings/#build-backend_namespace)
Build a namespace package.
Build a PEP 420 implicit namespace package, allowing more than one root `__init__.py`.
Use this option when the namespace package contains multiple root `__init__.py`, for namespace packages with a single root `__init__.py` use a dotted `module-name` instead.
To compare dotted `module-name` and `namespace = true`, the first example below can be expressed with `module-name = "cloud.database"`: There is one root `__init__.py` `database`. In the second example, we have three roots (`cloud.database`, `cloud.database_pro`, `billing.modules.database_pro`), so `namespace = true` is required.
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-1)src
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-2)└── cloud
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-3)    └── database
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-4)        ├── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-5)        ├── query_builder
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-6)        │   └── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-7)        └── sql
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-8)            ├── parser.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-19-9)            └── __init__.py

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-1)src
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-2)├── cloud
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-3)│   ├── database
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-4)│   │   ├── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-5)│   │   ├── query_builder
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-6)│   │   │   └── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-7)│   │   └── sql
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-8)│   │       ├── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-9)│   │       └── parser.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-10)│   └── database_pro
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-11)│       ├── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-12)│       └── query_builder.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-13)└── billing
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-14)    └── modules
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-15)        └── database_pro
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-16)            ├── __init__.py
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-20-17)            └── sql.py

```

**Default value** : `false`
**Type** : `bool`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-21-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-21-2)namespace=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_source-exclude)[`source-exclude`](https://docs.astral.sh/uv/reference/settings/#build-backend_source-exclude)
Glob expressions which files and directories to exclude from the source distribution.
These exclusions are also applied to wheels to ensure that a wheel built from a source tree is consistent with a wheel built from a source distribution.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-22-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-22-2)source-exclude=["*.bin"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_source-include)[`source-include`](https://docs.astral.sh/uv/reference/settings/#build-backend_source-include)
Glob expressions which files and directories to additionally include in the source distribution.
`pyproject.toml` and the contents of the module directory are always included.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-23-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-23-2)source-include=["tests/**"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#build-backend_wheel-exclude)[`wheel-exclude`](https://docs.astral.sh/uv/reference/settings/#build-backend_wheel-exclude)
Glob expressions which files and directories to exclude from the wheel.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-24-1)[tool.uv.build-backend]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-24-2)wheel-exclude=["*.bin"]

```

* * *
### [`workspace`](https://docs.astral.sh/uv/reference/settings/#workspace)
####  [](https://docs.astral.sh/uv/reference/settings/#workspace_exclude)[`exclude`](https://docs.astral.sh/uv/reference/settings/#workspace_exclude)
Packages to exclude as workspace members. If a package matches both `members` and `exclude`, it will be excluded.
Supports both globs and explicit paths.
For more information on the glob syntax, refer to the 
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-25-1)[tool.uv.workspace]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-25-2)exclude=["member1","path/to/member2","libs/*"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#workspace_members)[`members`](https://docs.astral.sh/uv/reference/settings/#workspace_members)
Packages to include as workspace members.
Supports both globs and explicit paths.
For more information on the glob syntax, refer to the 
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
pyproject.toml```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-26-1)[tool.uv.workspace]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-26-2)members=["member1","path/to/member2","libs/*"]

```

* * *
## [Configuration](https://docs.astral.sh/uv/reference/settings/#configuration)
###  [](https://docs.astral.sh/uv/reference/settings/#add-bounds)[`add-bounds`](https://docs.astral.sh/uv/reference/settings/#add-bounds)
The default version specifier when adding a dependency.
When adding a dependency to the project, if no constraint or URL is provided, a constraint is added based on the latest compatible version of the package. By default, a lower bound constraint is used, e.g., `>=1.2.3`.
When `--frozen` is provided, no resolution is performed, and dependencies are always added without constraints.
This option is in preview and may change in any future release.
**Default value** : `"lower"`
**Possible values** :
  * `"lower"`: Only a lower bound, e.g., `>=1.2.3`
  * `"major"`: Allow the same major version, similar to the semver caret, e.g., `>=1.2.3, <2.0.0`
  * `"minor"`: Allow the same minor version, similar to the semver tilde, e.g., `>=1.2.3, <1.3.0`
  * `"exact"`: Pin the exact version, e.g., `==1.2.3`


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_1_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_1_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-27-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-27-2)add-bounds="major"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-28-1)add-bounds="major"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#allow-insecure-host)[`allow-insecure-host`](https://docs.astral.sh/uv/reference/settings/#allow-insecure-host)
Allow insecure connections to host.
Expects to receive either a hostname (e.g., `localhost`), a host-port pair (e.g., `localhost:8080`), or a URL (e.g., `https://localhost`).
WARNING: Hosts included in this list will not be verified against the system's certificate store. Only use `--allow-insecure-host` in a secure network with verified sources, as it bypasses SSL verification and could expose you to MITM attacks.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_2_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_2_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-29-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-29-2)allow-insecure-host=["localhost:8080"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-30-1)allow-insecure-host=["localhost:8080"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#cache-dir)[`cache-dir`](https://docs.astral.sh/uv/reference/settings/#cache-dir)
Path to the cache directory.
Defaults to `$XDG_CACHE_HOME/uv` or `$HOME/.cache/uv` on Linux and macOS, and `%LOCALAPPDATA%\uv\cache` on Windows.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_3_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_3_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-31-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-31-2)cache-dir="./.uv_cache"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-32-1)cache-dir="./.uv_cache"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#cache-keys)[`cache-keys`](https://docs.astral.sh/uv/reference/settings/#cache-keys)
The keys to consider when caching builds for the project.
Cache keys enable you to specify the files or directories that should trigger a rebuild when modified. By default, uv will rebuild a project whenever the `pyproject.toml`, `setup.py`, or `setup.cfg` files in the project directory are modified, or if a `src` directory is added or removed, i.e.:
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-33-1)cache-keys=[{file="pyproject.toml"},{file="setup.py"},{file="setup.cfg"},{dir="src"}]

```

As an example: if a project uses dynamic metadata to read its dependencies from a `requirements.txt` file, you can specify `cache-keys = [{ file = "requirements.txt" }, { file = "pyproject.toml" }]` to ensure that the project is rebuilt whenever the `requirements.txt` file is modified (in addition to watching the `pyproject.toml`).
Globs are supported, following the syntax of the `.toml` file in the project directory or any of its subdirectories is modified, you can specify `cache-keys = [{ file = "**/*.toml" }]`. Note that the use of globs can be expensive, as uv may need to walk the filesystem to determine whether any files have changed.
Cache keys can also include version control information. For example, if a project uses `setuptools_scm` to read its version from a Git commit, you can specify `cache-keys = [{ git = { commit = true }, { file = "pyproject.toml" }]` to include the current Git commit hash in the cache key (in addition to the `pyproject.toml`). Git tags are also supported via `cache-keys = [{ git = { commit = true, tags = true } }]`.
Cache keys can also include environment variables. For example, if a project relies on `MACOSX_DEPLOYMENT_TARGET` or other environment variables to determine its behavior, you can specify `cache-keys = [{ env = "MACOSX_DEPLOYMENT_TARGET" }]` to invalidate the cache whenever the environment variable changes.
Cache keys only affect the project defined by the `pyproject.toml` in which they're specified (as opposed to, e.g., affecting all members in a workspace), and all paths and globs are interpreted as relative to the project directory.
**Default value** : `[{ file = "pyproject.toml" }, { file = "setup.py" }, { file = "setup.cfg" }]`
**Type** : `list[dict]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_4_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_4_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-34-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-34-2)cache-keys=[{file="pyproject.toml"},{file="requirements.txt"},{git={commit=true}}]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-35-1)cache-keys=[{file="pyproject.toml"},{file="requirements.txt"},{git={commit=true}}]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#check-url)[`check-url`](https://docs.astral.sh/uv/reference/settings/#check-url)
Check an index URL for existing files to skip duplicate uploads.
This option allows retrying publishing that failed after only some, but not all files have been uploaded, and handles error due to parallel uploads of the same file.
Before uploading, the index is checked. If the exact same file already exists in the index, the file will not be uploaded. If an error occurred during the upload, the index is checked again, to handle cases where the identical file was uploaded twice in parallel.
The exact behavior will vary based on the index. When uploading to PyPI, uploading the same file succeeds even without `--check-url`, while most other indexes error.
The index must provide one of the supported hashes (SHA-256, SHA-384, or SHA-512).
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_5_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_5_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-36-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-36-2)check-url="https://test.pypi.org/simple"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-37-1)check-url="https://test.pypi.org/simple"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#compile-bytecode)[`compile-bytecode`](https://docs.astral.sh/uv/reference/settings/#compile-bytecode)
Compile Python files to bytecode after installation.
By default, uv does not compile Python (`.py`) files to bytecode (`__pycache__/*.pyc`); instead, compilation is performed lazily the first time a module is imported. For use-cases in which start time is critical, such as CLI applications and Docker containers, this option can be enabled to trade longer installation times for faster start times.
When enabled, uv will process the entire site-packages directory (including packages that are not being modified by the current operation) for consistency. Like pip, it will also ignore errors.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_6_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_6_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-38-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-38-2)compile-bytecode=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-39-1)compile-bytecode=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#concurrent-builds)[`concurrent-builds`](https://docs.astral.sh/uv/reference/settings/#concurrent-builds)
The maximum number of source distributions that uv will build concurrently at any given time.
Defaults to the number of available CPU cores.
**Default value** : `None`
**Type** : `int`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_7_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_7_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-40-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-40-2)concurrent-builds=4

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-41-1)concurrent-builds=4

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#concurrent-downloads)[`concurrent-downloads`](https://docs.astral.sh/uv/reference/settings/#concurrent-downloads)
The maximum number of in-flight concurrent downloads that uv will perform at any given time.
**Default value** : `50`
**Type** : `int`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_8_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_8_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-42-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-42-2)concurrent-downloads=4

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-43-1)concurrent-downloads=4

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#concurrent-installs)[`concurrent-installs`](https://docs.astral.sh/uv/reference/settings/#concurrent-installs)
The number of threads used when installing and unzipping packages.
Defaults to the number of available CPU cores.
**Default value** : `None`
**Type** : `int`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_9_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_9_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-44-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-44-2)concurrent-installs=4

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-45-1)concurrent-installs=4

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#config-settings)[`config-settings`](https://docs.astral.sh/uv/reference/settings/#config-settings)
Settings to pass to the `KEY=VALUE` pairs.
**Default value** : `{}`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_10_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_10_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-46-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-46-2)config-settings={editable_mode="compat"}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-47-1)config-settings={editable_mode="compat"}

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#config-settings-package)[`config-settings-package`](https://docs.astral.sh/uv/reference/settings/#config-settings-package)
Settings to pass to the `KEY=VALUE` pairs.
Accepts a map from package names to string key-value pairs.
**Default value** : `{}`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_11_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_11_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-48-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-48-2)config-settings-package={numpy={editable_mode="compat"}}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-49-1)config-settings-package={numpy={editable_mode="compat"}}

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#dependency-metadata)[`dependency-metadata`](https://docs.astral.sh/uv/reference/settings/#dependency-metadata)
Pre-defined static metadata for dependencies of the project (direct or transitive). When provided, enables the resolver to use the specified metadata instead of querying the registry or building the relevant package from source.
Metadata should be provided in adherence with the 
  * `name`: The name of the package.
  * (Optional) `version`: The version of the package. If omitted, the metadata will be applied to all versions of the package.
  * (Optional) `requires-dist`: The dependencies of the package (e.g., `werkzeug>=0.14`).
  * (Optional) `requires-python`: The Python version required by the package (e.g., `>=3.10`).
  * (Optional) `provides-extra`: The extras provided by the package.


**Default value** : `[]`
**Type** : `list[dict]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_12_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_12_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-50-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-50-2)dependency-metadata=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-50-3){name="flask",version="1.0.0",requires-dist=["werkzeug"],requires-python=">=3.6"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-50-4)]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-51-1)dependency-metadata=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-51-2){name="flask",version="1.0.0",requires-dist=["werkzeug"],requires-python=">=3.6"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-51-3)]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#exclude-newer)[`exclude-newer`](https://docs.astral.sh/uv/reference/settings/#exclude-newer)
Limit candidate packages to those that were uploaded prior to a given point in time.
Accepts a superset of `2006-12-02T02:07:43Z`). A full timestamp is required to ensure that the resolver will behave consistently across timezones.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_13_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_13_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-52-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-52-2)exclude-newer="2006-12-02T02:07:43Z"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-53-1)exclude-newer="2006-12-02T02:07:43Z"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#exclude-newer-package)[`exclude-newer-package`](https://docs.astral.sh/uv/reference/settings/#exclude-newer-package)
Limit candidate packages for specific packages to those that were uploaded prior to the given date.
Accepts package-date pairs in a dictionary format.
**Default value** : `None`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_14_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_14_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-54-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-54-2)exclude-newer-package={tqdm="2022-04-04T00:00:00Z"}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-55-1)exclude-newer-package={tqdm="2022-04-04T00:00:00Z"}

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#extra-build-dependencies)[`extra-build-dependencies`](https://docs.astral.sh/uv/reference/settings/#extra-build-dependencies)
Additional build dependencies for packages.
This allows extending the PEP 517 build environment for the project's dependencies with additional packages. This is useful for packages that assume the presence of packages like `pip`, and do not declare them as build dependencies.
**Default value** : `[]`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_15_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_15_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-56-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-56-2)extra-build-dependencies={pytest=["setuptools"]}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-57-1)extra-build-dependencies={pytest=["setuptools"]}

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#extra-build-variables)[`extra-build-variables`](https://docs.astral.sh/uv/reference/settings/#extra-build-variables)
Extra environment variables to set when building certain packages.
Environment variables will be added to the environment when building the specified packages.
**Default value** : `{}`
**Type** : `dict[str, dict[str, str]]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_16_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_16_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-58-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-58-2)extra-build-variables={flash-attn={FLASH_ATTENTION_SKIP_CUDA_BUILD="TRUE"}}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-59-1)extra-build-variables={flash-attn={FLASH_ATTENTION_SKIP_CUDA_BUILD="TRUE"}}

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#extra-index-url)[`extra-index-url`](https://docs.astral.sh/uv/reference/settings/#extra-index-url)
Extra URLs of package indexes to use, in addition to `--index-url`.
Accepts either a repository compliant with 
All indexes provided via this flag take priority over the index specified by [`index_url`](https://docs.astral.sh/uv/reference/settings/#index-url) or [`index`](https://docs.astral.sh/uv/reference/settings/#index) with `default = true`. When multiple indexes are provided, earlier values take priority.
To control uv's resolution strategy when multiple indexes are present, see [`index_strategy`](https://docs.astral.sh/uv/reference/settings/#index-strategy).
(Deprecated: use `index` instead.)
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_17_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_17_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-60-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-60-2)extra-index-url=["https://download.pytorch.org/whl/cpu"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-61-1)extra-index-url=["https://download.pytorch.org/whl/cpu"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#find-links)[`find-links`](https://docs.astral.sh/uv/reference/settings/#find-links)
Locations to search for candidate distributions, in addition to those found in the registry indexes.
If a path, the target must be a directory that contains packages as wheel files (`.whl`) or source distributions (e.g., `.tar.gz` or `.zip`) at the top level.
If a URL, the page must contain a flat list of links to package files adhering to the formats described above.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_18_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_18_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-62-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-62-2)find-links=["https://download.pytorch.org/whl/torch_stable.html"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-63-1)find-links=["https://download.pytorch.org/whl/torch_stable.html"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#fork-strategy)[`fork-strategy`](https://docs.astral.sh/uv/reference/settings/#fork-strategy)
The strategy to use when selecting multiple versions of a given package across Python versions and platforms.
By default, uv will optimize for selecting the latest version of each package for each supported Python version (`requires-python`), while minimizing the number of selected versions across platforms.
Under `fewest`, uv will minimize the number of selected versions for each package, preferring older versions that are compatible with a wider range of supported Python versions or platforms.
**Default value** : `"requires-python"`
**Possible values** :
  * `"fewest"`: Optimize for selecting the fewest number of versions for each package. Older versions may be preferred if they are compatible with a wider range of supported Python versions or platforms
  * `"requires-python"`: Optimize for selecting latest supported version of each package, for each supported Python version


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_19_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_19_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-64-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-64-2)fork-strategy="fewest"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-65-1)fork-strategy="fewest"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#index)[`index`](https://docs.astral.sh/uv/reference/settings/#index)
The package indexes to use when resolving dependencies.
Accepts either a repository compliant with 
Indexes are considered in the order in which they're defined, such that the first-defined index has the highest priority. Further, the indexes provided by this setting are given higher priority than any indexes specified via [`index_url`](https://docs.astral.sh/uv/reference/settings/#index-url) or [`extra_index_url`](https://docs.astral.sh/uv/reference/settings/#extra-index-url). uv will only consider the first index that contains a given package, unless an alternative [index strategy](https://docs.astral.sh/uv/reference/settings/#index-strategy) is specified.
If an index is marked as `explicit = true`, it will be used exclusively for those dependencies that select it explicitly via `[tool.uv.sources]`, as in:
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-2)name="pytorch"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-3)url="https://download.pytorch.org/whl/cu121"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-4)explicit=true
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-5)
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-6)[tool.uv.sources]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-66-7)torch={index="pytorch"}

```

If an index is marked as `default = true`, it will be moved to the end of the prioritized list, such that it is given the lowest priority when resolving packages. Additionally, marking an index as default will disable the PyPI default index.
**Default value** : `"[]"`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_20_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_20_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-67-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-67-2)name="pytorch"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-67-3)url="https://download.pytorch.org/whl/cu121"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-68-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-68-2)name="pytorch"
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-68-3)url="https://download.pytorch.org/whl/cu121"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#index-strategy)[`index-strategy`](https://docs.astral.sh/uv/reference/settings/#index-strategy)
The strategy to use when resolving against multiple index URLs.
By default, uv will stop at the first index on which a given package is available, and limit resolutions to those present on that first index (`first-index`). This prevents "dependency confusion" attacks, whereby an attacker can upload a malicious package under the same name to an alternate index.
**Default value** : `"first-index"`
**Possible values** :
  * `"first-index"`: Only use results from the first index that returns a match for a given package name
  * `"unsafe-first-match"`: Search for every package name across all indexes, exhausting the versions from the first index before moving on to the next
  * `"unsafe-best-match"`: Search for every package name across all indexes, preferring the "best" version found. If a package version is in multiple indexes, only look at the entry for the first index


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_21_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_21_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-69-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-69-2)index-strategy="unsafe-best-match"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-70-1)index-strategy="unsafe-best-match"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#index-url)[`index-url`](https://docs.astral.sh/uv/reference/settings/#index-url)
The URL of the Python package index (by default: 
Accepts either a repository compliant with 
The index provided by this setting is given lower priority than any indexes specified via [`extra_index_url`](https://docs.astral.sh/uv/reference/settings/#extra-index-url) or [`index`](https://docs.astral.sh/uv/reference/settings/#index).
(Deprecated: use `index` instead.)
**Default value** : `"https://pypi.org/simple"`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_22_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_22_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-71-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-71-2)index-url="https://test.pypi.org/simple"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-72-1)index-url="https://test.pypi.org/simple"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#keyring-provider)[`keyring-provider`](https://docs.astral.sh/uv/reference/settings/#keyring-provider)
Attempt to use `keyring` for authentication for index URLs.
At present, only `--keyring-provider subprocess` is supported, which configures uv to use the `keyring` CLI to handle authentication.
**Default value** : `"disabled"`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_23_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_23_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-73-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-73-2)keyring-provider="subprocess"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-74-1)keyring-provider="subprocess"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#link-mode)[`link-mode`](https://docs.astral.sh/uv/reference/settings/#link-mode)
The method to use when installing packages from the global cache.
Defaults to `clone` (also known as Copy-on-Write) on macOS, and `hardlink` on Linux and Windows.
WARNING: The use of symlink link mode is discouraged, as they create tight coupling between the cache and the target environment. For example, clearing the cache (`uv cache clean`) will break all installed packages by way of removing the underlying source files. Use symlinks with caution.
**Default value** : `"clone" (macOS) or "hardlink" (Linux, Windows)`
**Possible values** :
  * `"clone"`: Clone (i.e., copy-on-write) packages from the wheel into the `site-packages` directory
  * `"copy"`: Copy packages from the wheel into the `site-packages` directory
  * `"hardlink"`: Hard link packages from the wheel into the `site-packages` directory
  * `"symlink"`: Symbolically link packages from the wheel into the `site-packages` directory


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_24_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_24_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-75-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-75-2)link-mode="copy"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-76-1)link-mode="copy"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#native-tls)[`native-tls`](https://docs.astral.sh/uv/reference/settings/#native-tls)
Whether to load TLS certificates from the platform's native certificate store.
By default, uv loads certificates from the bundled `webpki-roots` crate. The `webpki-roots` are a reliable set of trust roots from Mozilla, and including them in uv improves portability and performance (especially on macOS).
However, in some cases, you may want to use the platform's native certificate store, especially if you're relying on a corporate trust root (e.g., for a mandatory proxy) that's included in your system's certificate store.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_25_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_25_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-77-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-77-2)native-tls=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-78-1)native-tls=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-binary)[`no-binary`](https://docs.astral.sh/uv/reference/settings/#no-binary)
Don't install pre-built wheels.
The given packages will be built and installed from source. The resolver will still use pre-built wheels to extract package metadata, if available.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_26_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_26_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-79-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-79-2)no-binary=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-80-1)no-binary=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-binary-package)[`no-binary-package`](https://docs.astral.sh/uv/reference/settings/#no-binary-package)
Don't install pre-built wheels for a specific package.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_27_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_27_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-81-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-81-2)no-binary-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-82-1)no-binary-package=["ruff"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-build)[`no-build`](https://docs.astral.sh/uv/reference/settings/#no-build)
Don't build source distributions.
When enabled, resolving will not run arbitrary Python code. The cached wheels of already-built source distributions will be reused, but operations that require building distributions will exit with an error.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_28_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_28_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-83-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-83-2)no-build=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-84-1)no-build=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-build-isolation)[`no-build-isolation`](https://docs.astral.sh/uv/reference/settings/#no-build-isolation)
Disable isolation when building source distributions.
Assumes that build dependencies specified by 
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_29_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_29_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-85-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-85-2)no-build-isolation=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-86-1)no-build-isolation=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-build-isolation-package)[`no-build-isolation-package`](https://docs.astral.sh/uv/reference/settings/#no-build-isolation-package)
Disable isolation when building source distributions for a specific package.
Assumes that the packages' build dependencies specified by 
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_30_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_30_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-87-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-87-2)no-build-isolation-package=["package1","package2"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-88-1)no-build-isolation-package=["package1","package2"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-build-package)[`no-build-package`](https://docs.astral.sh/uv/reference/settings/#no-build-package)
Don't build source distributions for a specific package.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_31_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_31_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-89-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-89-2)no-build-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-90-1)no-build-package=["ruff"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-cache)[`no-cache`](https://docs.astral.sh/uv/reference/settings/#no-cache)
Avoid reading from or writing to the cache, instead using a temporary directory for the duration of the operation.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_32_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_32_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-91-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-91-2)no-cache=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-92-1)no-cache=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-index)[`no-index`](https://docs.astral.sh/uv/reference/settings/#no-index)
Ignore all registry indexes (e.g., PyPI), instead relying on direct URL dependencies and those provided via `--find-links`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_33_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_33_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-93-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-93-2)no-index=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-94-1)no-index=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#no-sources)[`no-sources`](https://docs.astral.sh/uv/reference/settings/#no-sources)
Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any local or Git sources.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_34_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_34_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-95-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-95-2)no-sources=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-96-1)no-sources=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#offline)[`offline`](https://docs.astral.sh/uv/reference/settings/#offline)
Disable network access, relying only on locally cached data and locally available files.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_35_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_35_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-97-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-97-2)offline=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-98-1)offline=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#prerelease)[`prerelease`](https://docs.astral.sh/uv/reference/settings/#prerelease)
The strategy to use when considering pre-release versions.
By default, uv will accept pre-releases for packages that _only_ publish pre-releases, along with first-party requirements that contain an explicit pre-release marker in the declared specifiers (`if-necessary-or-explicit`).
**Default value** : `"if-necessary-or-explicit"`
**Possible values** :
  * `"disallow"`: Disallow all pre-release versions
  * `"allow"`: Allow all pre-release versions
  * `"if-necessary"`: Allow pre-release versions if all versions of a package are pre-release
  * `"explicit"`: Allow pre-release versions for first-party packages with explicit pre-release markers in their version requirements
  * `"if-necessary-or-explicit"`: Allow pre-release versions if all versions of a package are pre-release, or if the package has an explicit pre-release marker in its version requirements


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_36_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_36_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-99-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-99-2)prerelease="allow"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-100-1)prerelease="allow"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#preview)[`preview`](https://docs.astral.sh/uv/reference/settings/#preview)
Whether to enable experimental, preview features.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_37_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_37_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-101-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-101-2)preview=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-102-1)preview=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#publish-url)[`publish-url`](https://docs.astral.sh/uv/reference/settings/#publish-url)
The URL for publishing packages to the Python package index (by default: 
**Default value** : `"https://upload.pypi.org/legacy/"`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_38_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_38_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-103-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-103-2)publish-url="https://test.pypi.org/legacy/"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-104-1)publish-url="https://test.pypi.org/legacy/"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#pypy-install-mirror)[`pypy-install-mirror`](https://docs.astral.sh/uv/reference/settings/#pypy-install-mirror)
Mirror URL to use for downloading managed PyPy installations.
By default, managed PyPy installations are downloaded from `https://downloads.python.org/pypy` in, e.g., `https://downloads.python.org/pypy/pypy3.8-v7.3.7-osx64.tar.bz2`.
Distributions can be read from a local directory by using the `file://` URL scheme.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_39_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_39_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-105-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-105-2)pypy-install-mirror="https://downloads.python.org/pypy"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-106-1)pypy-install-mirror="https://downloads.python.org/pypy"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#python-downloads)[`python-downloads`](https://docs.astral.sh/uv/reference/settings/#python-downloads)
Whether to allow Python downloads.
**Default value** : `"automatic"`
**Possible values** :
  * `"automatic"`: Automatically download managed Python installations when needed
  * `"manual"`: Do not automatically download managed Python installations; require explicit installation
  * `"never"`: Do not ever allow Python downloads


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_40_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_40_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-107-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-107-2)python-downloads="manual"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-108-1)python-downloads="manual"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#python-downloads-json-url)[`python-downloads-json-url`](https://docs.astral.sh/uv/reference/settings/#python-downloads-json-url)
URL pointing to JSON of custom Python installations.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_41_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_41_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-109-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-109-2)python-downloads-json-url="/etc/uv/python-downloads.json"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-110-1)python-downloads-json-url="/etc/uv/python-downloads.json"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#python-install-mirror)[`python-install-mirror`](https://docs.astral.sh/uv/reference/settings/#python-install-mirror)
Mirror URL for downloading managed Python installations.
By default, managed Python installations are downloaded from `https://github.com/astral-sh/python-build-standalone/releases/download` in, e.g., `https://github.com/astral-sh/python-build-standalone/releases/download/20240713/cpython-3.12.4%2B20240713-aarch64-apple-darwin-install_only.tar.gz`.
Distributions can be read from a local directory by using the `file://` URL scheme.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_42_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_42_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-111-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-111-2)python-install-mirror="https://github.com/astral-sh/python-build-standalone/releases/download"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-112-1)python-install-mirror="https://github.com/astral-sh/python-build-standalone/releases/download"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#python-preference)[`python-preference`](https://docs.astral.sh/uv/reference/settings/#python-preference)
Whether to prefer using Python installations that are already present on the system, or those that are downloaded and installed by uv.
**Default value** : `"managed"`
**Possible values** :
  * `"only-managed"`: Only use managed Python installations; never use system Python installations
  * `"managed"`: Prefer managed Python installations over system Python installations
  * `"system"`: Prefer system Python installations over managed Python installations
  * `"only-system"`: Only use system Python installations; never use managed Python installations


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_43_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_43_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-113-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-113-2)python-preference="managed"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-114-1)python-preference="managed"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#reinstall)[`reinstall`](https://docs.astral.sh/uv/reference/settings/#reinstall)
Reinstall all packages, regardless of whether they're already installed. Implies `refresh`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_44_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_44_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-115-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-115-2)reinstall=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-116-1)reinstall=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#reinstall-package)[`reinstall-package`](https://docs.astral.sh/uv/reference/settings/#reinstall-package)
Reinstall a specific package, regardless of whether it's already installed. Implies `refresh-package`.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_45_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_45_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-117-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-117-2)reinstall-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-118-1)reinstall-package=["ruff"]

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#required-version)[`required-version`](https://docs.astral.sh/uv/reference/settings/#required-version)
Enforce a requirement on the version of uv.
If the version of uv does not meet the requirement at runtime, uv will exit with an error.
Accepts a `==0.5.0` or `>=0.5.0`.
**Default value** : `null`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_46_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_46_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-119-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-119-2)required-version=">=0.5.0"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-120-1)required-version=">=0.5.0"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#resolution)[`resolution`](https://docs.astral.sh/uv/reference/settings/#resolution)
The strategy to use when selecting between the different compatible versions for a given package requirement.
By default, uv will use the latest compatible version of each package (`highest`).
**Default value** : `"highest"`
**Possible values** :
  * `"highest"`: Resolve the highest compatible version of each package
  * `"lowest"`: Resolve the lowest compatible version of each package
  * `"lowest-direct"`: Resolve the lowest compatible version of any direct dependencies, and the highest compatible version of any transitive dependencies


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_47_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_47_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-121-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-121-2)resolution="lowest-direct"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-122-1)resolution="lowest-direct"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#trusted-publishing)[`trusted-publishing`](https://docs.astral.sh/uv/reference/settings/#trusted-publishing)
Configure trusted publishing.
By default, uv checks for trusted publishing when running in a supported environment, but ignores it if it isn't configured.
uv's supported environments for trusted publishing include GitHub Actions and GitLab CI/CD.
**Default value** : `automatic`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_48_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_48_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-123-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-123-2)trusted-publishing="always"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-124-1)trusted-publishing="always"

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#upgrade)[`upgrade`](https://docs.astral.sh/uv/reference/settings/#upgrade)
Allow package upgrades, ignoring pinned versions in any existing output file.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_49_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_49_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-125-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-125-2)upgrade=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-126-1)upgrade=true

```

* * *
###  [](https://docs.astral.sh/uv/reference/settings/#upgrade-package)[`upgrade-package`](https://docs.astral.sh/uv/reference/settings/#upgrade-package)
Allow upgrades for a specific package, ignoring pinned versions in any existing output file.
Accepts both standalone package names (`ruff`) and version specifiers (`ruff<0.5.0`).
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_50_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_50_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-127-1)[tool.uv]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-127-2)upgrade-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-128-1)upgrade-package=["ruff"]

```

* * *
### [`pip`](https://docs.astral.sh/uv/reference/settings/#pip)
Settings that are specific to the `uv pip` command-line interface.
These values will be ignored when running commands outside the `uv pip` namespace (e.g., `uv lock`, `uvx`).
####  [](https://docs.astral.sh/uv/reference/settings/#pip_all-extras)[`all-extras`](https://docs.astral.sh/uv/reference/settings/#pip_all-extras)
Include all optional dependencies.
Only applies to `pyproject.toml`, `setup.py`, and `setup.cfg` sources.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_51_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_51_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-129-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-129-2)all-extras=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-130-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-130-2)all-extras=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_allow-empty-requirements)[`allow-empty-requirements`](https://docs.astral.sh/uv/reference/settings/#pip_allow-empty-requirements)
Allow `uv pip sync` with empty requirements, which will clear the environment of all packages.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_52_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_52_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-131-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-131-2)allow-empty-requirements=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-132-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-132-2)allow-empty-requirements=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_annotation-style)[`annotation-style`](https://docs.astral.sh/uv/reference/settings/#pip_annotation-style)
The style of the annotation comments included in the output file, used to indicate the source of each package.
**Default value** : `"split"`
**Possible values** :
  * `"line"`: Render the annotations on a single, comma-separated line
  * `"split"`: Render each annotation on its own line


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_53_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_53_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-133-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-133-2)annotation-style="line"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-134-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-134-2)annotation-style="line"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_break-system-packages)[`break-system-packages`](https://docs.astral.sh/uv/reference/settings/#pip_break-system-packages)
Allow uv to modify an `EXTERNALLY-MANAGED` Python installation.
WARNING: `--break-system-packages` is intended for use in continuous integration (CI) environments, when installing into Python installations that are managed by an external package manager, like `apt`. It should be used with caution, as such Python installations explicitly recommend against modifications by other package managers (like uv or pip).
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_54_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_54_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-135-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-135-2)break-system-packages=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-136-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-136-2)break-system-packages=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_compile-bytecode)[`compile-bytecode`](https://docs.astral.sh/uv/reference/settings/#pip_compile-bytecode)
Compile Python files to bytecode after installation.
By default, uv does not compile Python (`.py`) files to bytecode (`__pycache__/*.pyc`); instead, compilation is performed lazily the first time a module is imported. For use-cases in which start time is critical, such as CLI applications and Docker containers, this option can be enabled to trade longer installation times for faster start times.
When enabled, uv will process the entire site-packages directory (including packages that are not being modified by the current operation) for consistency. Like pip, it will also ignore errors.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_55_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_55_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-137-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-137-2)compile-bytecode=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-138-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-138-2)compile-bytecode=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_config-settings)[`config-settings`](https://docs.astral.sh/uv/reference/settings/#pip_config-settings)
Settings to pass to the `KEY=VALUE` pairs.
**Default value** : `{}`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_56_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_56_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-139-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-139-2)config-settings={editable_mode="compat"}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-140-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-140-2)config-settings={editable_mode="compat"}

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_config-settings-package)[`config-settings-package`](https://docs.astral.sh/uv/reference/settings/#pip_config-settings-package)
Settings to pass to the `KEY=VALUE` pairs.
**Default value** : `{}`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_57_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_57_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-141-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-141-2)config-settings-package={numpy={editable_mode="compat"}}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-142-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-142-2)config-settings-package={numpy={editable_mode="compat"}}

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_custom-compile-command)[`custom-compile-command`](https://docs.astral.sh/uv/reference/settings/#pip_custom-compile-command)
The header comment to include at the top of the output file generated by `uv pip compile`.
Used to reflect custom build scripts and commands that wrap `uv pip compile`.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_58_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_58_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-143-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-143-2)custom-compile-command="./custom-uv-compile.sh"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-144-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-144-2)custom-compile-command="./custom-uv-compile.sh"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_dependency-metadata)[`dependency-metadata`](https://docs.astral.sh/uv/reference/settings/#pip_dependency-metadata)
Pre-defined static metadata for dependencies of the project (direct or transitive). When provided, enables the resolver to use the specified metadata instead of querying the registry or building the relevant package from source.
Metadata should be provided in adherence with the 
  * `name`: The name of the package.
  * (Optional) `version`: The version of the package. If omitted, the metadata will be applied to all versions of the package.
  * (Optional) `requires-dist`: The dependencies of the package (e.g., `werkzeug>=0.14`).
  * (Optional) `requires-python`: The Python version required by the package (e.g., `>=3.10`).
  * (Optional) `provides-extra`: The extras provided by the package.


**Default value** : `[]`
**Type** : `list[dict]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_59_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_59_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-145-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-145-2)dependency-metadata=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-145-3){name="flask",version="1.0.0",requires-dist=["werkzeug"],requires-python=">=3.6"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-145-4)]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-146-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-146-2)dependency-metadata=[
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-146-3){name="flask",version="1.0.0",requires-dist=["werkzeug"],requires-python=">=3.6"},
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-146-4)]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_emit-build-options)[`emit-build-options`](https://docs.astral.sh/uv/reference/settings/#pip_emit-build-options)
Include `--no-binary` and `--only-binary` entries in the output file generated by `uv pip compile`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_60_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_60_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-147-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-147-2)emit-build-options=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-148-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-148-2)emit-build-options=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_emit-find-links)[`emit-find-links`](https://docs.astral.sh/uv/reference/settings/#pip_emit-find-links)
Include `--find-links` entries in the output file generated by `uv pip compile`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_61_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_61_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-149-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-149-2)emit-find-links=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-150-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-150-2)emit-find-links=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_emit-index-annotation)[`emit-index-annotation`](https://docs.astral.sh/uv/reference/settings/#pip_emit-index-annotation)
Include comment annotations indicating the index used to resolve each package (e.g., `# from https://pypi.org/simple`).
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_62_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_62_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-151-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-151-2)emit-index-annotation=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-152-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-152-2)emit-index-annotation=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_emit-index-url)[`emit-index-url`](https://docs.astral.sh/uv/reference/settings/#pip_emit-index-url)
Include `--index-url` and `--extra-index-url` entries in the output file generated by `uv pip compile`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_63_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_63_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-153-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-153-2)emit-index-url=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-154-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-154-2)emit-index-url=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_emit-marker-expression)[`emit-marker-expression`](https://docs.astral.sh/uv/reference/settings/#pip_emit-marker-expression)
Whether to emit a marker string indicating the conditions under which the set of pinned dependencies is valid.
The pinned dependencies may be valid even when the marker expression is false, but when the expression is true, the requirements are known to be correct.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_64_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_64_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-155-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-155-2)emit-marker-expression=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-156-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-156-2)emit-marker-expression=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_exclude-newer)[`exclude-newer`](https://docs.astral.sh/uv/reference/settings/#pip_exclude-newer)
Limit candidate packages to those that were uploaded prior to a given point in time.
Accepts a superset of `2006-12-02T02:07:43Z`). A full timestamp is required to ensure that the resolver will behave consistently across timezones.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_65_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_65_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-157-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-157-2)exclude-newer="2006-12-02T02:07:43Z"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-158-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-158-2)exclude-newer="2006-12-02T02:07:43Z"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_exclude-newer-package)[`exclude-newer-package`](https://docs.astral.sh/uv/reference/settings/#pip_exclude-newer-package)
Limit candidate packages for specific packages to those that were uploaded prior to the given date.
Accepts package-date pairs in a dictionary format.
**Default value** : `None`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_66_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_66_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-159-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-159-2)exclude-newer-package={tqdm="2022-04-04T00:00:00Z"}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-160-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-160-2)exclude-newer-package={tqdm="2022-04-04T00:00:00Z"}

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_extra)[`extra`](https://docs.astral.sh/uv/reference/settings/#pip_extra)
Include optional dependencies from the specified extra; may be provided more than once.
Only applies to `pyproject.toml`, `setup.py`, and `setup.cfg` sources.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_67_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_67_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-161-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-161-2)extra=["dev","docs"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-162-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-162-2)extra=["dev","docs"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_extra-build-dependencies)[`extra-build-dependencies`](https://docs.astral.sh/uv/reference/settings/#pip_extra-build-dependencies)
Additional build dependencies for packages.
This allows extending the PEP 517 build environment for the project's dependencies with additional packages. This is useful for packages that assume the presence of packages like `pip`, and do not declare them as build dependencies.
**Default value** : `[]`
**Type** : `dict`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_68_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_68_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-163-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-163-2)extra-build-dependencies={pytest=["setuptools"]}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-164-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-164-2)extra-build-dependencies={pytest=["setuptools"]}

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_extra-build-variables)[`extra-build-variables`](https://docs.astral.sh/uv/reference/settings/#pip_extra-build-variables)
Extra environment variables to set when building certain packages.
Environment variables will be added to the environment when building the specified packages.
**Default value** : `{}`
**Type** : `dict[str, dict[str, str]]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_69_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_69_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-165-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-165-2)extra-build-variables={flash-attn={FLASH_ATTENTION_SKIP_CUDA_BUILD="TRUE"}}

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-166-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-166-2)extra-build-variables={flash-attn={FLASH_ATTENTION_SKIP_CUDA_BUILD="TRUE"}}

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_extra-index-url)[`extra-index-url`](https://docs.astral.sh/uv/reference/settings/#pip_extra-index-url)
Extra URLs of package indexes to use, in addition to `--index-url`.
Accepts either a repository compliant with 
All indexes provided via this flag take priority over the index specified by [`index_url`](https://docs.astral.sh/uv/reference/settings/#index-url). When multiple indexes are provided, earlier values take priority.
To control uv's resolution strategy when multiple indexes are present, see [`index_strategy`](https://docs.astral.sh/uv/reference/settings/#index-strategy).
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_70_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_70_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-167-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-167-2)extra-index-url=["https://download.pytorch.org/whl/cpu"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-168-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-168-2)extra-index-url=["https://download.pytorch.org/whl/cpu"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_find-links)[`find-links`](https://docs.astral.sh/uv/reference/settings/#pip_find-links)
Locations to search for candidate distributions, in addition to those found in the registry indexes.
If a path, the target must be a directory that contains packages as wheel files (`.whl`) or source distributions (e.g., `.tar.gz` or `.zip`) at the top level.
If a URL, the page must contain a flat list of links to package files adhering to the formats described above.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_71_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_71_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-169-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-169-2)find-links=["https://download.pytorch.org/whl/torch_stable.html"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-170-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-170-2)find-links=["https://download.pytorch.org/whl/torch_stable.html"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_fork-strategy)[`fork-strategy`](https://docs.astral.sh/uv/reference/settings/#pip_fork-strategy)
The strategy to use when selecting multiple versions of a given package across Python versions and platforms.
By default, uv will optimize for selecting the latest version of each package for each supported Python version (`requires-python`), while minimizing the number of selected versions across platforms.
Under `fewest`, uv will minimize the number of selected versions for each package, preferring older versions that are compatible with a wider range of supported Python versions or platforms.
**Default value** : `"requires-python"`
**Possible values** :
  * `"fewest"`: Optimize for selecting the fewest number of versions for each package. Older versions may be preferred if they are compatible with a wider range of supported Python versions or platforms
  * `"requires-python"`: Optimize for selecting latest supported version of each package, for each supported Python version


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_72_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_72_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-171-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-171-2)fork-strategy="fewest"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-172-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-172-2)fork-strategy="fewest"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_generate-hashes)[`generate-hashes`](https://docs.astral.sh/uv/reference/settings/#pip_generate-hashes)
Include distribution hashes in the output file.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_73_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_73_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-173-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-173-2)generate-hashes=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-174-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-174-2)generate-hashes=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_group)[`group`](https://docs.astral.sh/uv/reference/settings/#pip_group)
Include the following dependency groups.
**Default value** : `None`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_74_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_74_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-175-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-175-2)group=["dev","docs"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-176-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-176-2)group=["dev","docs"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_index-strategy)[`index-strategy`](https://docs.astral.sh/uv/reference/settings/#pip_index-strategy)
The strategy to use when resolving against multiple index URLs.
By default, uv will stop at the first index on which a given package is available, and limit resolutions to those present on that first index (`first-index`). This prevents "dependency confusion" attacks, whereby an attacker can upload a malicious package under the same name to an alternate index.
**Default value** : `"first-index"`
**Possible values** :
  * `"first-index"`: Only use results from the first index that returns a match for a given package name
  * `"unsafe-first-match"`: Search for every package name across all indexes, exhausting the versions from the first index before moving on to the next
  * `"unsafe-best-match"`: Search for every package name across all indexes, preferring the "best" version found. If a package version is in multiple indexes, only look at the entry for the first index


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_75_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_75_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-177-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-177-2)index-strategy="unsafe-best-match"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-178-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-178-2)index-strategy="unsafe-best-match"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_index-url)[`index-url`](https://docs.astral.sh/uv/reference/settings/#pip_index-url)
The URL of the Python package index (by default: 
Accepts either a repository compliant with 
The index provided by this setting is given lower priority than any indexes specified via [`extra_index_url`](https://docs.astral.sh/uv/reference/settings/#extra-index-url).
**Default value** : `"https://pypi.org/simple"`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_76_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_76_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-179-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-179-2)index-url="https://test.pypi.org/simple"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-180-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-180-2)index-url="https://test.pypi.org/simple"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_keyring-provider)[`keyring-provider`](https://docs.astral.sh/uv/reference/settings/#pip_keyring-provider)
Attempt to use `keyring` for authentication for index URLs.
At present, only `--keyring-provider subprocess` is supported, which configures uv to use the `keyring` CLI to handle authentication.
**Default value** : `disabled`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_77_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_77_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-181-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-181-2)keyring-provider="subprocess"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-182-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-182-2)keyring-provider="subprocess"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_link-mode)[`link-mode`](https://docs.astral.sh/uv/reference/settings/#pip_link-mode)
The method to use when installing packages from the global cache.
Defaults to `clone` (also known as Copy-on-Write) on macOS, and `hardlink` on Linux and Windows.
WARNING: The use of symlink link mode is discouraged, as they create tight coupling between the cache and the target environment. For example, clearing the cache (`uv cache clean`) will break all installed packages by way of removing the underlying source files. Use symlinks with caution.
**Default value** : `"clone" (macOS) or "hardlink" (Linux, Windows)`
**Possible values** :
  * `"clone"`: Clone (i.e., copy-on-write) packages from the wheel into the `site-packages` directory
  * `"copy"`: Copy packages from the wheel into the `site-packages` directory
  * `"hardlink"`: Hard link packages from the wheel into the `site-packages` directory
  * `"symlink"`: Symbolically link packages from the wheel into the `site-packages` directory


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_78_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_78_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-183-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-183-2)link-mode="copy"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-184-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-184-2)link-mode="copy"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-annotate)[`no-annotate`](https://docs.astral.sh/uv/reference/settings/#pip_no-annotate)
Exclude comment annotations indicating the source of each package from the output file generated by `uv pip compile`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_79_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_79_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-185-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-185-2)no-annotate=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-186-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-186-2)no-annotate=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-binary)[`no-binary`](https://docs.astral.sh/uv/reference/settings/#pip_no-binary)
Don't install pre-built wheels.
The given packages will be built and installed from source. The resolver will still use pre-built wheels to extract package metadata, if available.
Multiple packages may be provided. Disable binaries for all packages with `:all:`. Clear previously specified packages with `:none:`.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_80_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_80_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-187-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-187-2)no-binary=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-188-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-188-2)no-binary=["ruff"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-build)[`no-build`](https://docs.astral.sh/uv/reference/settings/#pip_no-build)
Don't build source distributions.
When enabled, resolving will not run arbitrary Python code. The cached wheels of already-built source distributions will be reused, but operations that require building distributions will exit with an error.
Alias for `--only-binary :all:`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_81_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_81_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-189-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-189-2)no-build=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-190-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-190-2)no-build=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-build-isolation)[`no-build-isolation`](https://docs.astral.sh/uv/reference/settings/#pip_no-build-isolation)
Disable isolation when building source distributions.
Assumes that build dependencies specified by 
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_82_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_82_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-191-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-191-2)no-build-isolation=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-192-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-192-2)no-build-isolation=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-build-isolation-package)[`no-build-isolation-package`](https://docs.astral.sh/uv/reference/settings/#pip_no-build-isolation-package)
Disable isolation when building source distributions for a specific package.
Assumes that the packages' build dependencies specified by 
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_83_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_83_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-193-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-193-2)no-build-isolation-package=["package1","package2"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-194-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-194-2)no-build-isolation-package=["package1","package2"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-deps)[`no-deps`](https://docs.astral.sh/uv/reference/settings/#pip_no-deps)
Ignore package dependencies, instead only add those packages explicitly listed on the command line to the resulting requirements file.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_84_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_84_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-195-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-195-2)no-deps=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-196-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-196-2)no-deps=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-emit-package)[`no-emit-package`](https://docs.astral.sh/uv/reference/settings/#pip_no-emit-package)
Specify a package to omit from the output resolution. Its dependencies will still be included in the resolution. Equivalent to pip-compile's `--unsafe-package` option.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_85_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_85_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-197-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-197-2)no-emit-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-198-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-198-2)no-emit-package=["ruff"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-extra)[`no-extra`](https://docs.astral.sh/uv/reference/settings/#pip_no-extra)
Exclude the specified optional dependencies if `all-extras` is supplied.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_86_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_86_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-199-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-199-2)all-extras=true
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-199-3)no-extra=["dev","docs"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-200-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-200-2)all-extras=true
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-200-3)no-extra=["dev","docs"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-header)[`no-header`](https://docs.astral.sh/uv/reference/settings/#pip_no-header)
Exclude the comment header at the top of output file generated by `uv pip compile`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_87_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_87_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-201-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-201-2)no-header=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-202-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-202-2)no-header=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-index)[`no-index`](https://docs.astral.sh/uv/reference/settings/#pip_no-index)
Ignore all registry indexes (e.g., PyPI), instead relying on direct URL dependencies and those provided via `--find-links`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_88_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_88_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-203-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-203-2)no-index=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-204-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-204-2)no-index=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-sources)[`no-sources`](https://docs.astral.sh/uv/reference/settings/#pip_no-sources)
Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to using any local or Git sources.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_89_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_89_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-205-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-205-2)no-sources=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-206-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-206-2)no-sources=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-strip-extras)[`no-strip-extras`](https://docs.astral.sh/uv/reference/settings/#pip_no-strip-extras)
Include extras in the output file.
By default, uv strips extras, as any packages pulled in by the extras are already included as dependencies in the output file directly. Further, output files generated with `--no-strip-extras` cannot be used as constraints files in `install` and `sync` invocations.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_90_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_90_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-207-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-207-2)no-strip-extras=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-208-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-208-2)no-strip-extras=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_no-strip-markers)[`no-strip-markers`](https://docs.astral.sh/uv/reference/settings/#pip_no-strip-markers)
Include environment markers in the output file generated by `uv pip compile`.
By default, uv strips environment markers, as the resolution generated by `compile` is only guaranteed to be correct for the target environment.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_91_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_91_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-209-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-209-2)no-strip-markers=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-210-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-210-2)no-strip-markers=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_only-binary)[`only-binary`](https://docs.astral.sh/uv/reference/settings/#pip_only-binary)
Only use pre-built wheels; don't build source distributions.
When enabled, resolving will not run code from the given packages. The cached wheels of already-built source distributions will be reused, but operations that require building distributions will exit with an error.
Multiple packages may be provided. Disable binaries for all packages with `:all:`. Clear previously specified packages with `:none:`.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_92_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_92_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-211-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-211-2)only-binary=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-212-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-212-2)only-binary=["ruff"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_output-file)[`output-file`](https://docs.astral.sh/uv/reference/settings/#pip_output-file)
Write the requirements generated by `uv pip compile` to the given `requirements.txt` file.
If the file already exists, the existing versions will be preferred when resolving dependencies, unless `--upgrade` is also specified.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_93_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_93_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-213-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-213-2)output-file="requirements.txt"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-214-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-214-2)output-file="requirements.txt"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_prefix)[`prefix`](https://docs.astral.sh/uv/reference/settings/#pip_prefix)
Install packages into `lib`, `bin`, and other top-level folders under the specified directory, as if a virtual environment were present at that location.
In general, prefer the use of `--python` to install into an alternate environment, as scripts and other artifacts installed via `--prefix` will reference the installing interpreter, rather than any interpreter added to the `--prefix` directory, rendering them non-portable.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_94_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_94_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-215-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-215-2)prefix="./prefix"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-216-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-216-2)prefix="./prefix"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_prerelease)[`prerelease`](https://docs.astral.sh/uv/reference/settings/#pip_prerelease)
The strategy to use when considering pre-release versions.
By default, uv will accept pre-releases for packages that _only_ publish pre-releases, along with first-party requirements that contain an explicit pre-release marker in the declared specifiers (`if-necessary-or-explicit`).
**Default value** : `"if-necessary-or-explicit"`
**Possible values** :
  * `"disallow"`: Disallow all pre-release versions
  * `"allow"`: Allow all pre-release versions
  * `"if-necessary"`: Allow pre-release versions if all versions of a package are pre-release
  * `"explicit"`: Allow pre-release versions for first-party packages with explicit pre-release markers in their version requirements
  * `"if-necessary-or-explicit"`: Allow pre-release versions if all versions of a package are pre-release, or if the package has an explicit pre-release marker in its version requirements


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_95_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_95_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-217-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-217-2)prerelease="allow"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-218-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-218-2)prerelease="allow"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_python)[`python`](https://docs.astral.sh/uv/reference/settings/#pip_python)
The Python interpreter into which packages should be installed.
By default, uv installs into the virtual environment in the current working directory or any parent directory. The `--python` option allows you to specify a different interpreter, which is intended for use in continuous integration (CI) environments or other automated workflows.
Supported formats: - `3.10` looks for an installed Python 3.10 in the registry on Windows (see `py --list-paths`), or `python3.10` on Linux and macOS. - `python3.10` or `python.exe` looks for a binary with the given name in `PATH`. - `/home/ferris/.local/bin/python3.10` uses the exact Python at the given path.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_96_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_96_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-219-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-219-2)python="3.10"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-220-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-220-2)python="3.10"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_python-platform)[`python-platform`](https://docs.astral.sh/uv/reference/settings/#pip_python-platform)
The platform for which requirements should be resolved.
Represented as a "target triple", a string that describes the target platform in terms of its CPU, vendor, and operating system name, like `x86_64-unknown-linux-gnu` or `aarch64-apple-darwin`.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_97_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_97_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-221-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-221-2)python-platform="x86_64-unknown-linux-gnu"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-222-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-222-2)python-platform="x86_64-unknown-linux-gnu"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_python-version)[`python-version`](https://docs.astral.sh/uv/reference/settings/#pip_python-version)
The minimum Python version that should be supported by the resolved requirements (e.g., `3.8` or `3.8.17`).
If a patch version is omitted, the minimum patch version is assumed. For example, `3.8` is mapped to `3.8.0`.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_98_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_98_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-223-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-223-2)python-version="3.8"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-224-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-224-2)python-version="3.8"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_reinstall)[`reinstall`](https://docs.astral.sh/uv/reference/settings/#pip_reinstall)
Reinstall all packages, regardless of whether they're already installed. Implies `refresh`.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_99_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_99_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-225-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-225-2)reinstall=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-226-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-226-2)reinstall=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_reinstall-package)[`reinstall-package`](https://docs.astral.sh/uv/reference/settings/#pip_reinstall-package)
Reinstall a specific package, regardless of whether it's already installed. Implies `refresh-package`.
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_100_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_100_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-227-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-227-2)reinstall-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-228-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-228-2)reinstall-package=["ruff"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_require-hashes)[`require-hashes`](https://docs.astral.sh/uv/reference/settings/#pip_require-hashes)
Require a matching hash for each requirement.
Hash-checking mode is all or nothing. If enabled, _all_ requirements must be provided with a corresponding hash or set of hashes. Additionally, if enabled, _all_ requirements must either be pinned to exact versions (e.g., `==1.0.0`), or be specified via direct URL.
Hash-checking mode introduces a number of additional constraints:
  * Git dependencies are not supported.
  * Editable installations are not supported.
  * Local dependencies are not supported, unless they point to a specific wheel (`.whl`) or source archive (`.zip`, `.tar.gz`), as opposed to a directory.


**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_101_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_101_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-229-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-229-2)require-hashes=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-230-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-230-2)require-hashes=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_resolution)[`resolution`](https://docs.astral.sh/uv/reference/settings/#pip_resolution)
The strategy to use when selecting between the different compatible versions for a given package requirement.
By default, uv will use the latest compatible version of each package (`highest`).
**Default value** : `"highest"`
**Possible values** :
  * `"highest"`: Resolve the highest compatible version of each package
  * `"lowest"`: Resolve the lowest compatible version of each package
  * `"lowest-direct"`: Resolve the lowest compatible version of any direct dependencies, and the highest compatible version of any transitive dependencies


**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_102_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_102_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-231-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-231-2)resolution="lowest-direct"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-232-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-232-2)resolution="lowest-direct"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_strict)[`strict`](https://docs.astral.sh/uv/reference/settings/#pip_strict)
Validate the Python environment, to detect packages with missing dependencies and other issues.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_103_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_103_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-233-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-233-2)strict=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-234-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-234-2)strict=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_system)[`system`](https://docs.astral.sh/uv/reference/settings/#pip_system)
Install packages into the system Python environment.
By default, uv installs into the virtual environment in the current working directory or any parent directory. The `--system` option instructs uv to instead use the first Python found in the system `PATH`.
WARNING: `--system` is intended for use in continuous integration (CI) environments and should be used with caution, as it can modify the system Python installation.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_104_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_104_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-235-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-235-2)system=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-236-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-236-2)system=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_target)[`target`](https://docs.astral.sh/uv/reference/settings/#pip_target)
Install packages into the specified directory, rather than into the virtual or system Python environment. The packages will be installed at the top-level of the directory.
**Default value** : `None`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_105_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_105_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-237-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-237-2)target="./target"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-238-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-238-2)target="./target"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_torch-backend)[`torch-backend`](https://docs.astral.sh/uv/reference/settings/#pip_torch-backend)
The backend to use when fetching packages in the PyTorch ecosystem.
When set, uv will ignore the configured index URLs for packages in the PyTorch ecosystem, and will instead use the defined backend.
For example, when set to `cpu`, uv will use the CPU-only PyTorch index; when set to `cu126`, uv will use the PyTorch index for CUDA 12.6.
The `auto` mode will attempt to detect the appropriate PyTorch index based on the currently installed CUDA drivers.
This option is in preview and may change in any future release.
**Default value** : `null`
**Type** : `str`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_106_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_106_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-239-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-239-2)torch-backend="auto"

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-240-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-240-2)torch-backend="auto"

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_universal)[`universal`](https://docs.astral.sh/uv/reference/settings/#pip_universal)
Perform a universal resolution, attempting to generate a single `requirements.txt` output file that is compatible with all operating systems, architectures, and Python implementations.
In universal mode, the current Python version (or user-provided `--python-version`) will be treated as a lower bound. For example, `--universal --python-version 3.7` would produce a universal resolution for Python 3.7 and later.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_107_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_107_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-241-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-241-2)universal=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-242-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-242-2)universal=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_upgrade)[`upgrade`](https://docs.astral.sh/uv/reference/settings/#pip_upgrade)
Allow package upgrades, ignoring pinned versions in any existing output file.
**Default value** : `false`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_108_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_108_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-243-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-243-2)upgrade=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-244-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-244-2)upgrade=true

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_upgrade-package)[`upgrade-package`](https://docs.astral.sh/uv/reference/settings/#pip_upgrade-package)
Allow upgrades for a specific package, ignoring pinned versions in any existing output file.
Accepts both standalone package names (`ruff`) and version specifiers (`ruff<0.5.0`).
**Default value** : `[]`
**Type** : `list[str]`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_109_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_109_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-245-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-245-2)upgrade-package=["ruff"]

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-246-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-246-2)upgrade-package=["ruff"]

```

* * *
####  [](https://docs.astral.sh/uv/reference/settings/#pip_verify-hashes)[`verify-hashes`](https://docs.astral.sh/uv/reference/settings/#pip_verify-hashes)
Validate any hashes provided in the requirements file.
Unlike `--require-hashes`, `--verify-hashes` does not require that all requirements have hashes; instead, it will limit itself to verifying the hashes of those requirements that do include them.
**Default value** : `true`
**Type** : `bool`
**Example usage** :
[pyproject.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_110_1)[uv.toml](https://docs.astral.sh/uv/reference/settings/#__tabbed_110_2)
```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-247-1)[tool.uv.pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-247-2)verify-hashes=true

```

```
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-248-1)[pip]
[](https://docs.astral.sh/uv/reference/settings/#__codelineno-248-2)verify-hashes=true

```

* * *
December 8, 2025
