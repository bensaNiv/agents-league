---
# Smart Librarian Export (v2.0)
- Page Number: 50
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/migration/pip-to-project
- Page Title: From pip to a uv project | uv
- Semantic Filename: from_pip_to_a_uv_project_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 25,946 characters
---

# From pip to a uv project | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-from-pip-to-a-uv-project)
# [Migrating from pip to a uv project](https://docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-from-pip-to-a-uv-project)
This guide will discuss converting from a `pip` and `pip-tools` workflow centered on `requirements` files to uv's project workflow using a `pyproject.toml` and `uv.lock` file.
Note
If you're looking to migrate from `pip` and `pip-tools` to uv's drop-in interface or from an existing workflow where you're already using a `pyproject.toml`, those guides are not yet written. See 
We'll start with an overview of developing with `pip`, then discuss migrating to uv.
Tip
If you're familiar with the ecosystem, you can jump ahead to the [requirements file import](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-requirements-files) instructions.
## [Understanding pip workflows](https://docs.astral.sh/uv/guides/migration/pip-to-project/#understanding-pip-workflows)
### [Project dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/#project-dependencies)
When you want to use a package in your project, you need to install it first. `pip` supports imperative installation of packages, e.g.:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-0-1)$ pip
```

This installs the package into the environment that `pip` is installed in. This may be a virtual environment, or, the global environment of your system's Python installation.
Then, you can run a Python script that requires the package:
example.py```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-1-1)import fastapi

```

It's best practice to create a virtual environment for each project, to avoid mixing packages between them. For example:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-2-1)$ python[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-2-2)$ source[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-2-3)$ pip
```

We will revisit this topic in the [project environments section](https://docs.astral.sh/uv/guides/migration/pip-to-project/#project-environments) below.
### [Requirements files](https://docs.astral.sh/uv/guides/migration/pip-to-project/#requirements-files)
When sharing projects with others, it's useful to declare all the packages you require upfront. `pip` supports installing requirements from a file, e.g.:
requirements.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-3-1)fastapi

```

```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-4-1)$ pip
```

Notice above that `fastapi` is not "locked" to a specific version — each person working on the project may have a different version of `fastapi` installed. `pip-tools` was created to improve this experience.
When using `pip-tools`, requirements files specify both the dependencies for your project and lock dependencies to a specific version — the file extension is used to differentiate between the two. For example, if you require `fastapi` and `pydantic`, you'd specify these in a `requirements.in` file:
requirements.in```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-5-1)fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-5-2)pydantic>2

```

Notice there's a version constraint on `pydantic` — this means only `pydantic` versions later than `2.0.0` can be used. In contrast, `fastapi` does not have a version constraint — any version can be used.
These dependencies can be compiled into a `requirements.txt` file:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-6-1)$ pip-compile
```

requirements.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-1)annotated-types==0.7.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-2)    # via pydantic
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-3)anyio==4.8.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-4)    # via starlette
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-5)fastapi==0.115.11
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-6)    # via -r requirements.in
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-7)idna==3.10
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-8)    # via anyio
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-9)pydantic==2.10.6
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-10)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-11)    #   -r requirements.in
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-12)    #   fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-13)pydantic-core==2.27.2
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-14)    # via pydantic
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-15)sniffio==1.3.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-16)    # via anyio
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-17)starlette==0.46.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-18)    # via fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-19)typing-extensions==4.12.2
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-20)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-21)    #   fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-22)    #   pydantic
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-7-23)    #   pydantic-core

```

Here, all the versions constraints are _exact_. Only a single version of each package can be used. The above example was generated with `uv pip compile`, but could also be generated with `pip-compile` from `pip-tools`.
Though less common, the `requirements.txt` can also be generated using `pip freeze`, by first installing the input dependencies into the environment then exporting the installed versions:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-8-1)$ pip[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-8-2)$ pip
```

requirements.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-1)annotated-types==0.7.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-2)anyio==4.8.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-3)fastapi==0.115.11
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-4)idna==3.10
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-5)pydantic==2.10.6
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-6)pydantic-core==2.27.2
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-7)sniffio==1.3.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-8)starlette==0.46.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-9-9)typing-extensions==4.12.2

```

After compiling dependencies into a locked set of versions, these files are committed to version control and distributed with the project.
Then, when someone wants to use the project, they install from the requirements file:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-10-1)$ pip
```

### [Development dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/#development-dependencies)
The requirements file format can only describe a single set of dependencies at once. This means if you have additional _groups_ of dependencies, such as development dependencies, they need separate files. For example, we'll create a `-dev` dependency file:
requirements-dev.in```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-11-1)-r requirements.in
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-11-2)-c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-11-3)
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-11-4)pytest

```

Notice the base requirements are included with `-r requirements.in`. This ensures your development environment considers _all_ of the dependencies together. The `-c requirements.txt` _constrains_ the package version to ensure that the `requirements-dev.txt` uses the same versions as `requirements.txt`.
Note
It's common to use `-r requirements.txt` directly instead of using both `-r requirements.in`, and `-c requirements.txt`. There's no difference in the resulting package versions, but using both files produces annotations which allow you to determine which dependencies are _direct_ (annotated with `-r requirements.in`) and which are _indirect_ (only annotated with `-c requirements.txt`).
The compiled development dependencies look like:
requirements-dev.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-1)annotated-types==0.7.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-2)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-3)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-4)    #   pydantic
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-5)anyio==4.8.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-6)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-7)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-8)    #   starlette
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-9)fastapi==0.115.11
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-10)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-11)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-12)    #   -r requirements.in
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-13)idna==3.10
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-14)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-15)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-16)    #   anyio
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-17)iniconfig==2.0.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-18)    # via pytest
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-19)packaging==24.2
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-20)    # via pytest
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-21)pluggy==1.5.0
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-22)    # via pytest
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-23)pydantic==2.10.6
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-24)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-25)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-26)    #   -r requirements.in
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-27)    #   fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-28)pydantic-core==2.27.2
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-29)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-30)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-31)    #   pydantic
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-32)pytest==8.3.5
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-33)    # via -r requirements-dev.in
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-34)sniffio==1.3.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-35)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-36)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-37)    #   anyio
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-38)starlette==0.46.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-39)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-40)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-41)    #   fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-42)typing-extensions==4.12.2
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-43)    # via
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-44)    #   -c requirements.txt
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-45)    #   fastapi
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-46)    #   pydantic
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-12-47)    #   pydantic-core

```

As with the base dependency files, these are committed to version control and distributed with the project. When someone wants to work on the project, they'll install from the requirements file:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-13-1)$ pip
```

### [Platform-specific dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/#platform-specific-dependencies)
When compiling dependencies with `pip` or `pip-tools`, the result is only usable on the same platform as it is generated on. This poses a problem for projects which need to be usable on multiple platforms, such as Windows and macOS.
For example, take a simple dependency:
requirements.in```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-14-1)tqdm

```

On Linux, this compiles to:
requirements-linux.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-15-1)tqdm==4.67.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-15-2)    # via -r requirements.in

```

While on Windows, this compiles to:
requirements-win.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-16-1)colorama==0.4.6
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-16-2)    # via tqdm
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-16-3)tqdm==4.67.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-16-4)    # via -r requirements.in

```

`colorama` is a Windows-only dependency of `tqdm`.
When using `pip` and `pip-tools`, a project needs to declare a requirements lock file for each supported platform.
Note
uv's resolver can compile dependencies for multiple platforms at once (see ["universal resolution"](https://docs.astral.sh/uv/concepts/resolution/#universal-resolution)), allowing you to use a single `requirements.txt` for all platforms:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-17-1)$ uv
```

requirements.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-18-1)colorama==0.4.6 ; sys_platform == 'win32'
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-18-2)    # via tqdm
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-18-3)tqdm==4.67.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-18-4)    # via -r requirements.in

```

This resolution mode is also used when using a `pyproject.toml` and `uv.lock`.
## [Migrating to a uv project](https://docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-to-a-uv-project)
### [The `pyproject.toml`](https://docs.astral.sh/uv/guides/migration/pip-to-project/#the-pyprojecttoml)
The `pyproject.toml` is a standardized file for Python project metadata. It replaces `requirements.in` files, allowing you to represent arbitrary groups of project dependencies. It also provides a centralized location for metadata about your project, such as the build system or tool settings.
For example, the `requirements.in` and `requirements-dev.in` files above can be translated to a `pyproject.toml` as follows:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-1)[project]
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-2)name="example"
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-3)version="0.0.1"
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-4)dependencies=[
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-5)"fastapi",
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-6)"pydantic>2"
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-7)]
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-8)
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-9)[dependency-groups]
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-19-10)dev=["pytest"]

```

We'll discuss the commands necessary to automate these imports below.
### [The uv lockfile](https://docs.astral.sh/uv/guides/migration/pip-to-project/#the-uv-lockfile)
uv uses a lockfile (`uv.lock`) file to lock package versions. The format of this file is specific to uv, allowing uv to support advanced features. It replaces `requirements.txt` files.
The lockfile will be automatically created and populated when adding dependencies, but you can explicitly create it with `uv lock`.
Unlike `requirements.txt` files, the `uv.lock` file can represent arbitrary groups of dependencies, so multiple files are not needed to lock development dependencies.
The uv lockfile is always [universal](https://docs.astral.sh/uv/concepts/resolution/#universal-resolution), so multiple files are not needed to [lock dependencies for each platform](https://docs.astral.sh/uv/guides/migration/pip-to-project/#platform-specific-dependencies). This ensures that all developers are using consistent, locked versions of dependencies regardless of their machine.
The uv lockfile also supports concepts like [pinning packages to specific indexes](https://docs.astral.sh/uv/concepts/indexes/#pinning-a-package-to-an-index), which is not representable in `requirements.txt` files.
Tip
If you only need to lock for a subset of platforms, use the [`tool.uv.environments`](https://docs.astral.sh/uv/concepts/resolution/#limited-resolution-environments) setting to limit the resolution and lockfile.
To learn more, see the [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) documentation.
### [Importing requirements files](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-requirements-files)
First, create a `pyproject.toml` if you have not already:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-20-1)$ uv
```

Then, the easiest way to import requirements is with `uv add`:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-21-1)$ uv
```

However, there is some nuance to this transition. Notice we used the `requirements.in` file, which does not pin to exact versions of packages so uv will solve for new versions of these packages. You may want to continue using your previously locked versions from your `requirements.txt` so, when switching over to uv, none of your dependency versions change.
The solution is to add your locked versions as _constraints_. uv supports using these on `add` to preserve locked versions:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-22-1)$ uv
```

Your existing versions will be retained when producing a `uv.lock` file.
#### [Importing platform-specific constraints](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-platform-specific-constraints)
If your platform-specific dependencies have been compiled into separate files, you can still transition to a universal lockfile. However, you cannot just use `-c` to specify constraints from your existing platform-specific `requirements.txt` files because they do not include markers describing the environment and will consequently conflict.
To add the necessary markers, use `uv pip compile` to convert your existing files. For example, given the following:
requirements-win.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-23-1)colorama==0.4.6
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-23-2)    # via tqdm
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-23-3)tqdm==4.67.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-23-4)    # via -r requirements.in

```

The markers can be added with:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-24-1)$ uv
```

Notice the resulting output includes a Windows marker on `colorama`:
requirements-win.txt```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-25-1)colorama==0.4.6 ; sys_platform == 'win32'
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-25-2)    # via tqdm
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-25-3)tqdm==4.67.1
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-25-4)    # via -r requirements.in

```

When using `-o`, uv will constrain the versions to match the existing output file, if it can.
Markers can be added for other platforms by changing the `--python-platform` and `-o` values for each requirements file you need to import, e.g., to `linux` and `macos`.
Once each `requirements.txt` file has been transformed, the dependencies can be imported to the `pyproject.toml` and `uv.lock` with `uv add`:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-26-1)$ uv
```

#### [Importing development dependency files](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-development-dependency-files)
As discussed in the [development dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/#development-dependencies) section, it's common to have groups of dependencies for development purposes.
To import development dependencies, use the `--dev` flag during `uv add`:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-27-1)$ uv
```

If the `requirements-dev.in` includes the parent `requirements.in` via `-r`, it will need to be stripped to avoid adding the base requirements to the `dev` dependency group. The following example uses `sed` to strip lines that start with `-r`, then pipes the result to `uv add`:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-28-1)$ sed'/^-r /d'|
```

In addition to the `dev` dependency group, uv supports arbitrary group names. For example, if you also have a dedicated set of dependencies for building your documentation, those can be imported to a `docs` group:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-29-1)$ uv
```

### [Project environments](https://docs.astral.sh/uv/guides/migration/pip-to-project/#project-environments)
Unlike `pip`, uv is not centered around the concept of an "active" virtual environment. Instead, uv uses a dedicated virtual environment for each project in a `.venv` directory. This environment is automatically managed, so when you run a command, like `uv add`, the environment is synced with the project dependencies.
The preferred way to execute commands in the environment is with `uv run`, e.g.:
```
[](https://docs.astral.sh/uv/guides/migration/pip-to-project/#__codelineno-30-1)$ uv
```

Prior to every `uv run` invocation, uv will verify that the lockfile is up-to-date with the `pyproject.toml`, and that the environment is up-to-date with the lockfile, keeping your project in-sync without the need for manual intervention. `uv run` guarantees that your command is run in a consistent, locked environment.
The project environment can also be explicitly created with `uv sync`, e.g., for use with editors.
Note
When in projects, uv will prefer a `.venv` in the project directory and ignore the active environment as declared by the `VIRTUAL_ENV` variable by default. You can opt-in to using the active environment with the `--active` flag.
To learn more, see the [project environment](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment) documentation.
## [Next steps](https://docs.astral.sh/uv/guides/migration/pip-to-project/#next-steps)
Now that you've migrated to uv, take a look at the [project concept](https://docs.astral.sh/uv/concepts/projects/) page for more details about uv projects.
July 3, 2025
