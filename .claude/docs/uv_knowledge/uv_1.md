---
# Smart Librarian Export (v2.0)
- Page Number: 2
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv
- Page Title: uv
- Semantic Filename: uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 11,066 characters
---

# uv

[ Skip to content ](https://docs.astral.sh/uv/#uv)
# [uv](https://docs.astral.sh/uv/#uv)
An extremely fast Python package and project manager, written in Rust.
![Shows a bar chart with benchmark results.](https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d#only-light)
![Shows a bar chart with benchmark results.](https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310#only-dark)
_Installing_
## [Highlights](https://docs.astral.sh/uv/#highlights)
  * 🚀 A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.
  * ⚡️ `pip`.
  * 🗂️ Provides [comprehensive project management](https://docs.astral.sh/uv/#projects), with a [universal lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile).
  * ❇️ [Runs scripts](https://docs.astral.sh/uv/#scripts), with support for [inline dependency metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).
  * 🐍 [Installs and manages](https://docs.astral.sh/uv/#python-versions) Python versions.
  * 🛠️ [Runs and installs](https://docs.astral.sh/uv/#tools) tools published as Python packages.
  * 🔩 Includes a [pip-compatible interface](https://docs.astral.sh/uv/#the-pip-interface) for a performance boost with a familiar CLI.
  * 🏢 Supports Cargo-style [workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) for scalable projects.
  * 💾 Disk-space efficient, with a [global cache](https://docs.astral.sh/uv/concepts/cache/) for dependency deduplication.
  * ⏬ Installable without Rust or Python via `curl` or `pip`.
  * 🖥️ Supports macOS, Linux, and Windows.


uv is backed by [Astral](https://astral.sh), the creators of 
## [Installation](https://docs.astral.sh/uv/#installation)
Install uv with our official standalone installer:
[macOS and Linux](https://docs.astral.sh/uv/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/#__tabbed_1_2)
```
[](https://docs.astral.sh/uv/#__codelineno-0-1)$ curl|
```

```
[](https://docs.astral.sh/uv/#__codelineno-1-1)PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

```

Then, check out the [first steps](https://docs.astral.sh/uv/getting-started/first-steps/) or read on for a brief overview.
Tip
uv may also be installed with pip, Homebrew, and more. See all of the methods on the [installation page](https://docs.astral.sh/uv/getting-started/installation/).
## [Projects](https://docs.astral.sh/uv/#projects)
uv manages project dependencies and environments, with support for lockfiles, workspaces, and more, similar to `rye` or `poetry`:
```
[](https://docs.astral.sh/uv/#__codelineno-2-1)$ uv[](https://docs.astral.sh/uv/#__codelineno-2-2)Initialized project `example` at `/home/user/example`
[](https://docs.astral.sh/uv/#__codelineno-2-3)
[](https://docs.astral.sh/uv/#__codelineno-2-4)$ cd[](https://docs.astral.sh/uv/#__codelineno-2-5)
[](https://docs.astral.sh/uv/#__codelineno-2-6)$ uv[](https://docs.astral.sh/uv/#__codelineno-2-7)Creating virtual environment at: .venv
[](https://docs.astral.sh/uv/#__codelineno-2-8)Resolved 2 packages in 170ms
[](https://docs.astral.sh/uv/#__codelineno-2-9)   Built example @ file:///home/user/example
[](https://docs.astral.sh/uv/#__codelineno-2-10)Prepared 2 packages in 627ms
[](https://docs.astral.sh/uv/#__codelineno-2-11)Installed 2 packages in 1ms
[](https://docs.astral.sh/uv/#__codelineno-2-12) + example==0.1.0 (from file:///home/user/example)
[](https://docs.astral.sh/uv/#__codelineno-2-13) + ruff==0.5.4
[](https://docs.astral.sh/uv/#__codelineno-2-14)
[](https://docs.astral.sh/uv/#__codelineno-2-15)$ uv[](https://docs.astral.sh/uv/#__codelineno-2-16)All checks passed!
[](https://docs.astral.sh/uv/#__codelineno-2-17)
[](https://docs.astral.sh/uv/#__codelineno-2-18)$ uv[](https://docs.astral.sh/uv/#__codelineno-2-19)Resolved 2 packages in 0.33ms
[](https://docs.astral.sh/uv/#__codelineno-2-20)
[](https://docs.astral.sh/uv/#__codelineno-2-21)$ uv[](https://docs.astral.sh/uv/#__codelineno-2-22)Resolved 2 packages in 0.70ms
[](https://docs.astral.sh/uv/#__codelineno-2-23)Audited 1 package in 0.02ms

```

See the [project guide](https://docs.astral.sh/uv/guides/projects/) to get started.
uv also supports building and publishing projects, even if they're not managed with uv. See the [packaging guide](https://docs.astral.sh/uv/guides/package/) to learn more.
## [Scripts](https://docs.astral.sh/uv/#scripts)
uv manages dependencies and environments for single-file scripts.
Create a new script and add inline metadata declaring its dependencies:
```
[](https://docs.astral.sh/uv/#__codelineno-3-1)$ echo'import requests; print(requests.get("https://astral.sh"))'[](https://docs.astral.sh/uv/#__codelineno-3-2)
[](https://docs.astral.sh/uv/#__codelineno-3-3)$ uv[](https://docs.astral.sh/uv/#__codelineno-3-4)Updated `example.py`

```

Then, run the script in an isolated virtual environment:
```
[](https://docs.astral.sh/uv/#__codelineno-4-1)$ uv[](https://docs.astral.sh/uv/#__codelineno-4-2)Reading inline script metadata from: example.py
[](https://docs.astral.sh/uv/#__codelineno-4-3)Installed 5 packages in 12ms
[](https://docs.astral.sh/uv/#__codelineno-4-4)<Response [200]>

```

See the [scripts guide](https://docs.astral.sh/uv/guides/scripts/) to get started.
## [Tools](https://docs.astral.sh/uv/#tools)
uv executes and installs command-line tools provided by Python packages, similar to `pipx`.
Run a tool in an ephemeral environment using `uvx` (an alias for `uv tool run`):
```
[](https://docs.astral.sh/uv/#__codelineno-5-1)$ uvx'hello world!'
[](https://docs.astral.sh/uv/#__codelineno-5-2)Resolved 1 package in 167ms
[](https://docs.astral.sh/uv/#__codelineno-5-3)Installed 1 package in 9ms
[](https://docs.astral.sh/uv/#__codelineno-5-4) + pycowsay==0.0.0.2
[](https://docs.astral.sh/uv/#__codelineno-5-5)  """
[](https://docs.astral.sh/uv/#__codelineno-5-6)
[](https://docs.astral.sh/uv/#__codelineno-5-7)  ------------
[](https://docs.astral.sh/uv/#__codelineno-5-8)< hello world! >
[](https://docs.astral.sh/uv/#__codelineno-5-9)  ------------
[](https://docs.astral.sh/uv/#__codelineno-5-10)   \   ^__^
[](https://docs.astral.sh/uv/#__codelineno-5-11)    \  (oo)\_______
[](https://docs.astral.sh/uv/#__codelineno-5-12)       (__)\       )\/\
[](https://docs.astral.sh/uv/#__codelineno-5-13)           ||----w |
[](https://docs.astral.sh/uv/#__codelineno-5-14)           ||     ||

```

Install a tool with `uv tool install`:
```
[](https://docs.astral.sh/uv/#__codelineno-6-1)$ uv[](https://docs.astral.sh/uv/#__codelineno-6-2)Resolved 1 package in 6ms
[](https://docs.astral.sh/uv/#__codelineno-6-3)Installed 1 package in 2ms
[](https://docs.astral.sh/uv/#__codelineno-6-4) + ruff==0.5.4
[](https://docs.astral.sh/uv/#__codelineno-6-5)Installed 1 executable: ruff
[](https://docs.astral.sh/uv/#__codelineno-6-6)
[](https://docs.astral.sh/uv/#__codelineno-6-7)$ ruff[](https://docs.astral.sh/uv/#__codelineno-6-8)ruff 0.5.4

```

See the [tools guide](https://docs.astral.sh/uv/guides/tools/) to get started.
## [Python versions](https://docs.astral.sh/uv/#python-versions)
uv installs Python and allows quickly switching between versions.
Install multiple Python versions:
```
[](https://docs.astral.sh/uv/#__codelineno-7-1)$ uv3.103.113.12
[](https://docs.astral.sh/uv/#__codelineno-7-2)Searching for Python versions matching: Python 3.10
[](https://docs.astral.sh/uv/#__codelineno-7-3)Searching for Python versions matching: Python 3.11
[](https://docs.astral.sh/uv/#__codelineno-7-4)Searching for Python versions matching: Python 3.12
[](https://docs.astral.sh/uv/#__codelineno-7-5)Installed 3 versions in 3.42s
[](https://docs.astral.sh/uv/#__codelineno-7-6) + cpython-3.10.14-macos-aarch64-none
[](https://docs.astral.sh/uv/#__codelineno-7-7) + cpython-3.11.9-macos-aarch64-none
[](https://docs.astral.sh/uv/#__codelineno-7-8) + cpython-3.12.4-macos-aarch64-none

```

Download Python versions as needed:
```
[](https://docs.astral.sh/uv/#__codelineno-8-1)$ uv3.12.0
[](https://docs.astral.sh/uv/#__codelineno-8-2)Using CPython 3.12.0
[](https://docs.astral.sh/uv/#__codelineno-8-3)Creating virtual environment at: .venv
[](https://docs.astral.sh/uv/#__codelineno-8-4)Activate with: source .venv/bin/activate
[](https://docs.astral.sh/uv/#__codelineno-8-5)
[](https://docs.astral.sh/uv/#__codelineno-8-6)$ uv[](https://docs.astral.sh/uv/#__codelineno-8-7)Python 3.8.16 (a9dbdca6fc3286b0addd2240f11d97d8e8de187a, Dec 29 2022, 11:45:30)
[](https://docs.astral.sh/uv/#__codelineno-8-8)[PyPy 7.3.11 with GCC Apple LLVM 13.1.6 (clang-1316.0.21.2.5)] on darwin
[](https://docs.astral.sh/uv/#__codelineno-8-9)Type "help", "copyright", "credits" or "license" for more information.
[](https://docs.astral.sh/uv/#__codelineno-8-10)>>>>

```

Use a specific Python version in the current directory:
```
[](https://docs.astral.sh/uv/#__codelineno-9-1)$ uv3.11
[](https://docs.astral.sh/uv/#__codelineno-9-2)Pinned `.python-version` to `3.11`

```

See the [installing Python guide](https://docs.astral.sh/uv/guides/install-python/) to get started.
## [The pip interface](https://docs.astral.sh/uv/#the-pip-interface)
uv provides a drop-in replacement for common `pip`, `pip-tools`, and `virtualenv` commands.
uv extends their interfaces with advanced features, such as dependency version overrides, platform-independent resolutions, reproducible resolutions, alternative resolution strategies, and more.
Migrate to uv without changing your existing workflows — and experience a 10-100x speedup — with the `uv pip` interface.
Compile requirements into a platform-independent requirements file:
```
[](https://docs.astral.sh/uv/#__codelineno-10-1)$ uv\
[](https://docs.astral.sh/uv/#__codelineno-10-2)\
[](https://docs.astral.sh/uv/#__codelineno-10-3)[](https://docs.astral.sh/uv/#__codelineno-10-4)Resolved 43 packages in 12ms

```

Create a virtual environment:
```
[](https://docs.astral.sh/uv/#__codelineno-11-1)$ uv[](https://docs.astral.sh/uv/#__codelineno-11-2)Using CPython 3.12.3
[](https://docs.astral.sh/uv/#__codelineno-11-3)Creating virtual environment at: .venv
[](https://docs.astral.sh/uv/#__codelineno-11-4)Activate with: source .venv/bin/activate

```

Install the locked requirements:
```
[](https://docs.astral.sh/uv/#__codelineno-12-1)$ uv[](https://docs.astral.sh/uv/#__codelineno-12-2)Resolved 43 packages in 11ms
[](https://docs.astral.sh/uv/#__codelineno-12-3)Installed 43 packages in 208ms
[](https://docs.astral.sh/uv/#__codelineno-12-4) + babel==2.15.0
[](https://docs.astral.sh/uv/#__codelineno-12-5) + black==24.4.2
[](https://docs.astral.sh/uv/#__codelineno-12-6) + certifi==2024.7.4
[](https://docs.astral.sh/uv/#__codelineno-12-7) ...

```

See the [pip interface documentation](https://docs.astral.sh/uv/pip/) to get started.
## [Learn more](https://docs.astral.sh/uv/#learn-more)
See the [first steps](https://docs.astral.sh/uv/getting-started/first-steps/) or jump straight to the [guides](https://docs.astral.sh/uv/guides/) to start using uv.
May 18, 2025
