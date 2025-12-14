---
# Smart Librarian Export (v2.0)
- Page Number: 19
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/tools
- Page Title: Tools | uv
- Semantic Filename: tools_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 11,629 characters
---

# Tools | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/tools/#tools)
# [Tools](https://docs.astral.sh/uv/concepts/tools/#tools)
Tools are Python packages that provide command-line interfaces.
Note
See the [tools guide](https://docs.astral.sh/uv/guides/tools/) for an introduction to working with the tools interface — this document discusses details of tool management.
## [The `uv tool` interface](https://docs.astral.sh/uv/concepts/tools/#the-uv-tool-interface)
uv includes a dedicated interface for interacting with tools. Tools can be invoked without installation using `uv tool run`, in which case their dependencies are installed in a temporary virtual environment isolated from the current project.
Because it is very common to run tools without installing them, a `uvx` alias is provided for `uv tool run` — the two commands are exactly equivalent. For brevity, the documentation will mostly refer to `uvx` instead of `uv tool run`.
Tools can also be installed with `uv tool install`, in which case their executables are [available on the `PATH`](https://docs.astral.sh/uv/concepts/tools/#tool-executables) — an isolated virtual environment is still used, but it is not removed when the command completes.
## [Execution vs installation](https://docs.astral.sh/uv/concepts/tools/#execution-vs-installation)
In most cases, executing a tool with `uvx` is more appropriate than installing the tool. Installing the tool is useful if you need the tool to be available to other programs on your system, e.g., if some script you do not control requires the tool, or if you are in a Docker image and want to make the tool available to users.
## [Tool environments](https://docs.astral.sh/uv/concepts/tools/#tool-environments)
When running a tool with `uvx`, a virtual environment is stored in the uv cache directory and is treated as disposable, i.e., if you run `uv cache clean` the environment will be deleted. The environment is only cached to reduce the overhead of repeated invocations. If the environment is removed, a new one will be created automatically.
When installing a tool with `uv tool install`, a virtual environment is created in the [uv tools directory](https://docs.astral.sh/uv/reference/storage/#tools). The environment will not be removed unless the tool is uninstalled. If the environment is manually deleted, the tool will fail to run.
Important
Tool environments are _not_ intended to be mutated directly. It is strongly recommended never to mutate a tool environment manually, e.g., with a `pip` operation.
## [Tool versions](https://docs.astral.sh/uv/concepts/tools/#tool-versions)
Unless a specific version is requested, `uv tool install` will install the latest available of the requested tool. `uvx` will use the latest available version of the requested tool _on the first invocation_. After that, `uvx` will use the cached version of the tool unless a different version is requested, the cache is pruned, or the cache is refreshed.
For example, to run a specific version of Ruff:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-0-1)$ uvx[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-0-2)ruff 0.6.0

```

A subsequent invocation of `uvx` will use the latest, not the cached, version.
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-1-1)$ uvx[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-1-2)ruff 0.6.2

```

But, if a new version of Ruff was released, it would not be used unless the cache was refreshed.
To request the latest version of Ruff and refresh the cache, use the `@latest` suffix:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-2-1)$ uvx[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-2-2)0.6.2

```

Once a tool is installed with `uv tool install`, `uvx` will use the installed version by default.
For example, after installing an older version of Ruff:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-3-1)$ uvruff==0.5.0

```

The version of `ruff` and `uvx ruff` is the same:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-4-1)$ ruff[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-4-2)ruff 0.5.0
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-4-3)$ uvx[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-4-4)ruff 0.5.0

```

However, you can ignore the installed version by requesting the latest version explicitly, e.g.:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-5-1)$ uvx[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-5-2)0.6.2

```

Or, by using the `--isolated` flag, which will avoid refreshing the cache but ignore the installed version:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-6-1)$ uvx[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-6-2)0.6.2

```

`uv tool install` will also respect the `{package}@{version}` and `{package}@latest` specifiers, as in:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-7-1)$ uv[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-7-2)$ uv
```

## [Upgrading tools](https://docs.astral.sh/uv/concepts/tools/#upgrading-tools)
Tool environments may be upgraded via `uv tool upgrade`, or re-created entirely via subsequent `uv tool install` operations.
To upgrade all packages in a tool environment
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-8-1)$ uv
```

To upgrade a single package in a tool environment:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-9-1)$ uv
```

Tool upgrades will respect the version constraints provided when installing the tool. For example, `uv tool install black >=23,<24` followed by `uv tool upgrade black` will upgrade Black to the latest version in the range `>=23,<24`.
To instead replace the version constraints, reinstall the tool with `uv tool install`:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-10-1)$ uv=24

```

Similarly, tool upgrades will retain the settings provided when installing the tool. For example, `uv tool install black --prerelease allow` followed by `uv tool upgrade black` will retain the `--prerelease allow` setting.
Note
Tool upgrades will reinstall the tool executables, even if they have not changed.
To reinstall packages during upgrade, use the `--reinstall` and `--reinstall-package` options.
To reinstall all packages in a tool environment
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-11-1)$ uv
```

To reinstall a single package in a tool environment:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-12-1)$ uv
```

## [Including additional dependencies](https://docs.astral.sh/uv/concepts/tools/#including-additional-dependencies)
Additional packages can be included during tool execution:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-13-1)$ uvx
```

And, during tool installation:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-14-1)$ uv
```

The `--with` option can be provided multiple times to include additional packages.
The `--with` option supports package specifications, so a specific version can be requested:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-15-1)$ uvx==<version>
```

The `-w` shorthand can be used in place of the `--with` option:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-16-1)$ uvx
```

If the requested version conflicts with the requirements of the tool package, package resolution will fail and the command will error.
## [Installing executables from additional packages](https://docs.astral.sh/uv/concepts/tools/#installing-executables-from-additional-packages)
When installing a tool, you may want to include executables from additional packages in the same tool environment. This is useful when you have related tools that work together or when you want to install multiple executables that share dependencies.
The `--with-executables-from` option allows you to specify additional packages whose executables should be installed alongside the main tool:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-17-1)$ uv
```

For example, to install Ansible along with executables from `ansible-core` and `ansible-lint`:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-18-1)$ uv
```

This will install all executables from the `ansible`, `ansible-core`, and `ansible-lint` packages into the same tool environment, making them all available on the `PATH`.
The `--with-executables-from` option can be combined with other installation options:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-19-1)$ uv
```

Note that `--with-executables-from` differs from `--with` in that:
  * `--with` includes additional packages as dependencies but does not install their executables
  * `--with-executables-from` includes both the packages as dependencies and installs their executables


## [Python versions](https://docs.astral.sh/uv/concepts/tools/#python-versions)
Each tool environment is linked to a specific Python version. This uses the same Python version [discovery logic](https://docs.astral.sh/uv/concepts/python-versions/#discovery-of-python-versions) as other virtual environments created by uv, but will ignore non-global Python version requests like `.python-version` files and the `requires-python` value from a `pyproject.toml`.
The `--python` option can be used to request a specific version. See the [Python version](https://docs.astral.sh/uv/concepts/python-versions/) documentation for more details.
If the Python version used by a tool is _uninstalled_ , the tool environment will be broken and the tool may be unusable.
## [Tool executables](https://docs.astral.sh/uv/concepts/tools/#tool-executables)
Tool executables include all console entry points, script entry points, and binary scripts provided by a Python package. Tool executables are symlinked into the [executable directory](https://docs.astral.sh/uv/reference/storage/#tool-executables) on Unix and copied on Windows.
Note
Executables provided by dependencies of tool packages are not installed.
The [executable directory](https://docs.astral.sh/uv/reference/storage/#executable-directory) must be in the `PATH` variable for tool executables to be available from the shell. If it is not in the `PATH`, a warning will be displayed. The `uv tool update-shell` command can be used to add the executable directory to the `PATH` in common shell configuration files.
### [Overwriting executables](https://docs.astral.sh/uv/concepts/tools/#overwriting-executables)
Installation of tools will not overwrite executables in the executable directory that were not previously installed by uv. For example, if `pipx` has been used to install a tool, `uv tool install` will fail. The `--force` flag can be used to override this behavior.
## [Relationship to `uv run`](https://docs.astral.sh/uv/concepts/tools/#relationship-to-uv-run)
The invocation `uv tool run <name>` (or `uvx <name>`) is nearly equivalent to:
```
[](https://docs.astral.sh/uv/concepts/tools/#__codelineno-20-1)$ uv
```

However, there are a couple notable differences when using uv's tool interface:
  * The `--with` option is not needed — the required package is inferred from the command name.
  * The temporary environment is cached in a dedicated location.
  * The `--no-project` flag is not needed — tools are always run isolated from the project.
  * If a tool is already installed, `uv tool run` will use the installed version but `uv run` will not.


If the tool should not be isolated from the project, e.g., when running `pytest` or `mypy`, then `uv run` should be used instead of `uv tool run`.
November 24, 2025
