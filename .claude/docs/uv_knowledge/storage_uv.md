---
# Smart Librarian Export (v2.0)
- Page Number: 39
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/reference/storage
- Page Title: Storage | uv
- Semantic Filename: storage_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 7,879 characters
---

# Storage | uv

[ Skip to content ](https://docs.astral.sh/uv/reference/storage/#storage)
# [Storage](https://docs.astral.sh/uv/reference/storage/#storage)
## [Storage directories](https://docs.astral.sh/uv/reference/storage/#storage-directories)
uv uses the following high-level directories for storage.
For each location, uv checks for the existence of environment variables in the given order and uses the first path found.
The paths of storage directories are platform-specific. uv follows the 
### [Temporary directory](https://docs.astral.sh/uv/reference/storage/#temporary-directory)
The temporary directory is used for ephemeral data.
[Unix](https://docs.astral.sh/uv/reference/storage/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/reference/storage/#__tabbed_1_2)
  1. `$TMPDIR`
  2. `/tmp`


  1. `%TMP%`
  2. `%TEMP%`
  3. `%USERPROFILE%`


### [Cache directory](https://docs.astral.sh/uv/reference/storage/#cache-directory)
The cache directory is used for data that is disposable, but is useful to be long-lived.
[Unix](https://docs.astral.sh/uv/reference/storage/#__tabbed_2_1)[Windows](https://docs.astral.sh/uv/reference/storage/#__tabbed_2_2)
  1. `$XDG_CACHE_HOME/uv`
  2. `$HOME/.cache/uv`


  1. `%LOCALAPPDATA%\uv\cache`
  2. `uv\cache` within 


### [Persistent data directory](https://docs.astral.sh/uv/reference/storage/#persistent-data-directory)
The persistent data directory is used for non-disposable data.
[Unix](https://docs.astral.sh/uv/reference/storage/#__tabbed_3_1)[Windows](https://docs.astral.sh/uv/reference/storage/#__tabbed_3_2)
  1. `$XDG_DATA_HOME/uv`
  2. `$HOME/.local/share/uv`
  3. `$CWD/.uv`


  1. `%APPDATA%\uv\data`
  2. `.\.uv`


### [Configuration directories](https://docs.astral.sh/uv/reference/storage/#configuration-directories)
The configuration directories are used to store changes to uv's settings.
User-level configuration
[Unix](https://docs.astral.sh/uv/reference/storage/#__tabbed_4_1)[Windows](https://docs.astral.sh/uv/reference/storage/#__tabbed_4_2)
  1. `$XDG_CONFIG_HOME/uv`
  2. `$HOME/.config/uv`


  1. `%APPDATA%\uv`
  2. `uv` within 


System-level configuration
[Unix](https://docs.astral.sh/uv/reference/storage/#__tabbed_5_1)[Windows](https://docs.astral.sh/uv/reference/storage/#__tabbed_5_2)
  1. `$XDG_CONFIG_DIRS/uv`
  2. `/etc/uv`


  1. `%PROGRAMDATA%\uv`
  2. `uv` within 


### [Executable directory](https://docs.astral.sh/uv/reference/storage/#executable-directory)
The executable directory is used to store files that can be run by the user, i.e., a directory that should be on the `PATH`.
[Unix](https://docs.astral.sh/uv/reference/storage/#__tabbed_6_1)[Windows](https://docs.astral.sh/uv/reference/storage/#__tabbed_6_2)
  1. `$XDG_BIN_HOME`
  2. `$XDG_DATA_HOME/../bin`
  3. `$HOME/.local/bin`


  1. `%XDG_BIN_HOME%`
  2. `%XDG_DATA_HOME%\..\bin`
  3. `%USERPROFILE%\.local\bin`


## [Types of data](https://docs.astral.sh/uv/reference/storage/#types-of-data)
### [Dependency cache](https://docs.astral.sh/uv/reference/storage/#dependency-cache)
uv uses a local cache to avoid re-downloading and re-building dependencies.
By default, the cache is stored in the [cache directory](https://docs.astral.sh/uv/reference/storage/#cache-directory) but it can be overridden via command line arguments, environment variables, or settings as detailed in [the cache documentation](https://docs.astral.sh/uv/concepts/cache/#cache-directory). When the cache is disabled, the cache will be stored in a [temporary directory](https://docs.astral.sh/uv/reference/storage/#temporary-directory).
Use `uv cache dir` to show the current cache directory path.
Important
For optimal performance, the cache directory needs to be on the same filesystem as virtual environments.
### [Python versions](https://docs.astral.sh/uv/reference/storage/#python-versions)
uv can install managed [Python versions](https://docs.astral.sh/uv/concepts/python-versions/), e.g., with `uv python install`.
By default, Python versions managed by uv are stored in a `python/` subdirectory of the [persistent data directory](https://docs.astral.sh/uv/reference/storage/#persistent-data-directory), e.g., `~/.local/share/uv/python`.
Use `uv python dir` to show the Python installation directory.
Use the `UV_PYTHON_INSTALL_DIR` environment variable to override the installation directory.
Note
Changing where Python is installed will not be automatically reflected in existing virtual environments; they will keep referring to the old location, and will need to be updated manually (e.g. by re-creating them).
### [Python executables](https://docs.astral.sh/uv/reference/storage/#python-executables)
uv installs executables for [Python versions](https://docs.astral.sh/uv/reference/storage/#python-versions), e.g., `python3.13`.
By default, Python executables are stored in the [executable directory](https://docs.astral.sh/uv/reference/storage/#executable-directory).
Use `uv python dir --bin` to show the Python executable directory.
Use the `UV_PYTHON_BIN_DIR` environment variable to override the Python executable directory.
### [Tools](https://docs.astral.sh/uv/reference/storage/#tools)
uv can install Python packages as [command-line tools](https://docs.astral.sh/uv/concepts/tools/) using `uv tool install`.
By default, tools are installed in a `tools/` subdirectory of the [persistent data directory](https://docs.astral.sh/uv/reference/storage/#persistent-data-directory), e.g., `~/.local/share/uv/tools`.
Use `uv tool dir` to show the tool installation directory.
Use the `UV_TOOL_DIR` environment variable to configure the installation directory.
### [Tool executables](https://docs.astral.sh/uv/reference/storage/#tool-executables)
uv installs executables for installed [tools](https://docs.astral.sh/uv/reference/storage/#tools), e.g., `ruff`.
By default, tool executables are stored in the [executable directory](https://docs.astral.sh/uv/reference/storage/#executable-directory).
Use `uv tool dir --bin` to show the tool executable directory.
Use the `UV_TOOL_BIN_DIR` environment variable to configure the tool executable directory.
### [The uv executable](https://docs.astral.sh/uv/reference/storage/#the-uv-executable)
When using uv's [standalone installer](https://docs.astral.sh/uv/reference/installer/) to install uv, the `uv` and `uvx` executables are installed into the [executable directory](https://docs.astral.sh/uv/reference/storage/#executable-directory).
Use the `UV_INSTALL_DIR` environment variable to configure uv's installation directory.
### [Configuration files](https://docs.astral.sh/uv/reference/storage/#configuration-files)
uv's behavior can be configured through TOML files.
Configuration files are discovered in the [configuration directories](https://docs.astral.sh/uv/reference/storage/#configuration-directories).
For more details, see the [configuration files documentation](https://docs.astral.sh/uv/concepts/configuration-files/).
### [Project virtual environments](https://docs.astral.sh/uv/reference/storage/#project-virtual-environments)
When working on [projects](https://docs.astral.sh/uv/concepts/projects/), uv creates a dedicated virtual environment for each project.
By default, project virtual environments are created in `.venv` in the project or workspace root, i.e., next to the `pyproject.toml`.
Use the `UV_PROJECT_ENVIRONMENT` environment variable to override this location. For more details, see the [projects environment documentation](https://docs.astral.sh/uv/concepts/projects/config/#project-environment-path).
### [Script virtual environments](https://docs.astral.sh/uv/reference/storage/#script-virtual-environments)
When running [scripts with inline metadata](https://docs.astral.sh/uv/guides/scripts/), uv creates a dedicated virtual environment for each script in the [cache directory](https://docs.astral.sh/uv/reference/storage/#cache-directory).
November 17, 2025
