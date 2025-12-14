---
# Smart Librarian Export (v2.0)
- Page Number: 8
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/tools
- Page Title: Using tools | uv
- Semantic Filename: using_tools_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 9,724 characters
---

# Using tools | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/tools/#using-tools)
# [Using tools](https://docs.astral.sh/uv/guides/tools/#using-tools)
Many Python packages provide applications that can be used as tools. uv has specialized support for easily invoking and installing tools.
## [Running tools](https://docs.astral.sh/uv/guides/tools/#running-tools)
The `uvx` command invokes a tool without installing it.
For example, to run `ruff`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-0-1)$ uvx
```

Note
This is exactly equivalent to:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-1-1)$ uv
```

`uvx` is provided as an alias for convenience.
Arguments can be provided after the tool name:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-1)$ uvx[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-2)
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-3)  -------------
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-4)< hello from uv >
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-5)  -------------
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-6)   \   ^__^
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-7)    \  (oo)\_______
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-8)       (__)\       )\/\
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-9)           ||----w |
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-2-10)           ||     ||

```

Tools are installed into temporary, isolated environments when using `uvx`.
Note
If you are running a tool in a [_project_](https://docs.astral.sh/uv/concepts/projects/) and the tool requires that your project is installed, e.g., when using `pytest` or `mypy`, you'll want to use [`uv run`](https://docs.astral.sh/uv/guides/projects/#running-commands) instead of `uvx`. Otherwise, the tool will be run in a virtual environment that is isolated from your project.
If your project has a flat structure, e.g., instead of using a `src` directory for modules, the project itself does not need to be installed and `uvx` is fine. In this case, using `uv run` is only beneficial if you want to pin the version of the tool in the project's dependencies.
## [Commands with different package names](https://docs.astral.sh/uv/guides/tools/#commands-with-different-package-names)
When `uvx ruff` is invoked, uv installs the `ruff` package which provides the `ruff` command. However, sometimes the package and command names differ.
The `--from` option can be used to invoke a command from a specific package, e.g., `http` which is provided by `httpie`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-3-1)$ uvx
```

## [Requesting specific versions](https://docs.astral.sh/uv/guides/tools/#requesting-specific-versions)
To run a tool at a specific version, use `command@<version>`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-4-1)$ uvx
```

To run a tool at the latest version, use `command@latest`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-5-1)$ uvx
```

The `--from` option can also be used to specify package versions, as above:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-6-1)$ uvx'ruff==0.3.0'
```

Or, to constrain to a range of versions:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-7-1)$ uvx'ruff>0.2.0,<0.3.0'
```

Note the `@` syntax cannot be used for anything other than an exact version.
## [Requesting extras](https://docs.astral.sh/uv/guides/tools/#requesting-extras)
The `--from` option can be used to run a tool with extras:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-8-1)$ uvx'mypy[faster-cache,reports]'
```

This can also be combined with version selection:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-9-1)$ uvx'mypy[faster-cache,reports]==1.13.0'
```

## [Requesting different sources](https://docs.astral.sh/uv/guides/tools/#requesting-different-sources)
The `--from` option can also be used to install from alternative sources.
For example, to pull from git:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-10-1)$ uvx
```

You can also pull the latest commit from a specific named branch:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-11-1)$ uvx
```

Or pull a specific tag:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-12-1)$ uvx
```

Or even a specific commit:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-13-1)$ uvx
```

Or with 
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-14-1)$ uvx
```

## [Commands with plugins](https://docs.astral.sh/uv/guides/tools/#commands-with-plugins)
Additional dependencies can be included, e.g., to include `mkdocs-material` when running `mkdocs`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-15-1)$ uvx
```

## [Installing tools](https://docs.astral.sh/uv/guides/tools/#installing-tools)
If a tool is used often, it is useful to install it to a persistent environment and add it to the `PATH` instead of invoking `uvx` repeatedly.
Tip
`uvx` is a convenient alias for `uv tool run`. All of the other commands for interacting with tools require the full `uv tool` prefix.
To install `ruff`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-16-1)$ uv
```

When a tool is installed, its executables are placed in a `bin` directory in the `PATH` which allows the tool to be run without uv. If it's not on the `PATH`, a warning will be displayed and `uv tool update-shell` can be used to add it to the `PATH`.
After installing `ruff`, it should be available:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-17-1)$ ruff
```

Unlike `uv pip install`, installing a tool does not make its modules available in the current environment. For example, the following command will fail:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-18-1)$ python"import ruff"

```

This isolation is important for reducing interactions and conflicts between dependencies of tools, scripts, and projects.
Unlike `uvx`, `uv tool install` operates on a _package_ and will install all executables provided by the tool.
For example, the following will install the `http`, `https`, and `httpie` executables:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-19-1)$ uv
```

Additionally, package versions can be included without `--from`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-20-1)$ uv'httpie>0.1.0'

```

And, similarly, for package sources:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-21-1)$ uv
```

Or package sources with 
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-22-1)$ uv
```

As with `uvx`, installations can include additional packages:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-23-1)$ uv
```

Multiple related executables can be installed together in the same tool environment, using the `--with-executables-from` flag. For example, the following will install the executables from `ansible`, plus those ones provided by `ansible-core` and `ansible-lint`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-24-1)$ uv
```

## [Upgrading tools](https://docs.astral.sh/uv/guides/tools/#upgrading-tools)
To upgrade a tool, use `uv tool upgrade`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-25-1)$ uv
```

Tool upgrades will respect the version constraints provided when installing the tool. For example, `uv tool install ruff >=0.3,<0.4` followed by `uv tool upgrade ruff` will upgrade Ruff to the latest version in the range `>=0.3,<0.4`.
To instead replace the version constraints, re-install the tool with `uv tool install`:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-26-1)$ uv=0.4

```

To instead upgrade all tools:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-27-1)$ uv
```

## [Requesting Python versions](https://docs.astral.sh/uv/guides/tools/#requesting-python-versions)
By default, uv will use your default Python interpreter (the first it finds) when running, installing, or upgrading tools. You can specify the Python interpreter to use with the `--python` option.
For example, to request a specific Python version when running a tool:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-28-1)$ uvx3.10
```

Or, when installing a tool:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-29-1)$ uv3.10
```

Or, when upgrading a tool:
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-30-1)$ uv3.10
```

For more details on requesting Python versions, see the [Python version](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version) concept page.
## [Legacy Windows Scripts](https://docs.astral.sh/uv/guides/tools/#legacy-windows-scripts)
Tools also support running `$(uv tool dir)\<tool-name>\Scripts` when installed.
Currently only legacy scripts with the `.ps1`, `.cmd`, and `.bat` extensions are supported.
For example, below is an example running a Command Prompt script.
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-31-1)$ uvnuitka==2.6.7
```

In addition, you don't need to specify the extension. `uvx` will automatically look for files ending in `.ps1`, `.cmd`, and `.bat` in that order of execution on your behalf.
```
[](https://docs.astral.sh/uv/guides/tools/#__codelineno-32-1)$ uvnuitka==2.6.7
```

## [Next steps](https://docs.astral.sh/uv/guides/tools/#next-steps)
To learn more about managing tools with uv, see the [Tools concept](https://docs.astral.sh/uv/concepts/tools/) page and the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-tool).
Or, read on to learn how to [work on projects](https://docs.astral.sh/uv/guides/projects/).
December 2, 2025
