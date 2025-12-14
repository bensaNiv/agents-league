---
# Smart Librarian Export (v2.0)
- Page Number: 12
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/projects
- Page Title: Working on projects | uv
- Semantic Filename: working_on_projects_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 11,716 characters
---

# Working on projects | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/projects/#working-on-projects)
# [Working on projects](https://docs.astral.sh/uv/guides/projects/#working-on-projects)
uv supports managing Python projects, which define their dependencies in a `pyproject.toml` file.
## [Creating a new project](https://docs.astral.sh/uv/guides/projects/#creating-a-new-project)
You can create a new Python project using the `uv init` command:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-0-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-0-2)$ cd
```

Alternatively, you can initialize a project in the working directory:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-1-1)$ mkdir[](https://docs.astral.sh/uv/guides/projects/#__codelineno-1-2)$ cd[](https://docs.astral.sh/uv/guides/projects/#__codelineno-1-3)$ uv
```

uv will create the following files:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-2-1)├── .gitignore
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-2-2)├── .python-version
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-2-3)├── README.md
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-2-4)├── main.py
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-2-5)└── pyproject.toml

```

The `main.py` file contains a simple "Hello world" program. Try it out with `uv run`:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-3-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-3-2)Hello from hello-world!

```

## [Project structure](https://docs.astral.sh/uv/guides/projects/#project-structure)
A project consists of a few important parts that work together and allow uv to manage your project. In addition to the files created by `uv init`, uv will create a virtual environment and `uv.lock` file in the root of your project the first time you run a project command, i.e., `uv run`, `uv sync`, or `uv lock`.
A complete listing would look like:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-1).
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-2)├── .venv
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-3)│   ├── bin
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-4)│   ├── lib
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-5)│   └── pyvenv.cfg
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-6)├── .python-version
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-7)├── README.md
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-8)├── main.py
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-9)├── pyproject.toml
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-4-10)└── uv.lock

```

### [`pyproject.toml`](https://docs.astral.sh/uv/guides/projects/#pyprojecttoml)
The `pyproject.toml` contains metadata about your project:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-5-1)[project]
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-5-2)name="hello-world"
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-5-3)version="0.1.0"
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-5-4)description="Add your description here"
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-5-5)readme="README.md"
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-5-6)dependencies=[]

```

You'll use this file to specify dependencies, as well as details about the project such as its description or license. You can edit this file manually, or use commands like `uv add` and `uv remove` to manage your project from the terminal.
Tip
See the official `pyproject.toml` format.
You'll also use this file to specify uv [configuration options](https://docs.astral.sh/uv/concepts/configuration-files/) in a [`[tool.uv]`](https://docs.astral.sh/uv/reference/settings/) section.
### [`.python-version`](https://docs.astral.sh/uv/guides/projects/#python-version)
The `.python-version` file contains the project's default Python version. This file tells uv which Python version to use when creating the project's virtual environment.
### [`.venv`](https://docs.astral.sh/uv/guides/projects/#venv)
The `.venv` folder contains your project's virtual environment, a Python environment that is isolated from the rest of your system. This is where uv will install your project's dependencies.
See the [project environment](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment) documentation for more details.
### [`uv.lock`](https://docs.astral.sh/uv/guides/projects/#uvlock)
`uv.lock` is a cross-platform lockfile that contains exact information about your project's dependencies. Unlike the `pyproject.toml` which is used to specify the broad requirements of your project, the lockfile contains the exact resolved versions that are installed in the project environment. This file should be checked into version control, allowing for consistent and reproducible installations across machines.
`uv.lock` is a human-readable TOML file but is managed by uv and should not be edited manually.
See the [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) documentation for more details.
## [Managing dependencies](https://docs.astral.sh/uv/guides/projects/#managing-dependencies)
You can add dependencies to your `pyproject.toml` with the `uv add` command. This will also update the lockfile and project environment:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-6-1)$ uv
```

You can also specify version constraints or alternative sources:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-7-1)$ # Specify a version constraint
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-7-2)$ uv'requests==2.31.0'
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-7-3)
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-7-4)$ # Add a git dependency
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-7-5)$ uv
```

If you're migrating from a `requirements.txt` file, you can use `uv add` with the `-r` flag to add all dependencies from the file:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-8-1)$ # Add all dependencies from `requirements.txt`.
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-8-2)$ uv
```

To remove a package, you can use `uv remove`:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-9-1)$ uv
```

To upgrade a package, run `uv lock` with the `--upgrade-package` flag:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-10-1)$ uv
```

The `--upgrade-package` flag will attempt to update the specified package to the latest compatible version, while keeping the rest of the lockfile intact.
See the documentation on [managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) for more details.
## [Viewing your version](https://docs.astral.sh/uv/guides/projects/#viewing-your-version)
The `uv version` command can be used to read your package's version.
To get the version of your package, run `uv version`:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-11-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-11-2)hello-world 0.7.0

```

To get the version without the package name, use the `--short` option:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-12-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-12-2)0.7.0

```

To get version information in a JSON format, use the `--output-format json` option:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-13-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-13-2){
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-13-3)    "package_name": "hello-world",
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-13-4)    "version": "0.7.0",
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-13-5)    "commit_info": null
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-13-6)}

```

See the [publishing guide](https://docs.astral.sh/uv/guides/package/#updating-your-version) for details on updating your package version.
## [Running commands](https://docs.astral.sh/uv/guides/projects/#running-commands)
`uv run` can be used to run arbitrary scripts or commands in your project environment.
Prior to every `uv run` invocation, uv will verify that the lockfile is up-to-date with the `pyproject.toml`, and that the environment is up-to-date with the lockfile, keeping your project in-sync without the need for manual intervention. `uv run` guarantees that your command is run in a consistent, locked environment.
For example, to use `flask`:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-14-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-14-2)$ uv3000

```

Or, to run a script:
example.py```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-15-1)# Require a project dependency
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-15-2)import flask
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-15-3)
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-15-4)print("hello world")

```

```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-16-1)$ uv
```

Alternatively, you can use `uv sync` to manually update the environment then activate it before executing a command:
[macOS and Linux](https://docs.astral.sh/uv/guides/projects/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/guides/projects/#__tabbed_1_2)
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-17-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-17-2)$ source[](https://docs.astral.sh/uv/guides/projects/#__codelineno-17-3)$ flask3000
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-17-4)$ python
```

```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-18-1)PS> uv sync
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-18-2)PS> .venv\Scripts\activate
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-18-3)PS> flask run -p 3000
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-18-4)PS> python example.py

```

Note
The virtual environment must be active to run scripts and commands in the project without `uv run`. Virtual environment activation differs per shell and platform.
See the documentation on [running commands and scripts](https://docs.astral.sh/uv/concepts/projects/run/) in projects for more details.
## [Building distributions](https://docs.astral.sh/uv/guides/projects/#building-distributions)
`uv build` can be used to build source distributions and binary distributions (wheel) for your project.
By default, `uv build` will build the project in the current directory, and place the built artifacts in a `dist/` subdirectory:
```
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-19-1)$ uv[](https://docs.astral.sh/uv/guides/projects/#__codelineno-19-2)$ ls[](https://docs.astral.sh/uv/guides/projects/#__codelineno-19-3)hello-world-0.1.0-py3-none-any.whl
[](https://docs.astral.sh/uv/guides/projects/#__codelineno-19-4)hello-world-0.1.0.tar.gz

```

See the documentation on [building projects](https://docs.astral.sh/uv/concepts/projects/build/) for more details.
## [Next steps](https://docs.astral.sh/uv/guides/projects/#next-steps)
To learn more about working on projects with uv, see the [projects concept](https://docs.astral.sh/uv/concepts/projects/) page and the [command reference](https://docs.astral.sh/uv/reference/cli/#uv).
Or, read on to learn how to [export a uv lockfile to different formats](https://docs.astral.sh/uv/concepts/projects/export/).
November 24, 2025
