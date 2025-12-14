---
# Smart Librarian Export (v2.0)
- Page Number: 24
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/docker
- Page Title: Using uv in Docker | uv
- Semantic Filename: using_uv_in_docker_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 32,685 characters
---

# Using uv in Docker | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/docker/#using-uv-in-docker)
# [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/#using-uv-in-docker)
## [Getting started](https://docs.astral.sh/uv/guides/integration/docker/#getting-started)
Tip
Check out the 
uv provides both _distroless_ Docker images, which are useful for [copying uv binaries](https://docs.astral.sh/uv/guides/integration/docker/#installing-uv) into your own image builds, and images derived from popular base images, which are useful for using uv in a container. The distroless images do not contain anything but the uv binaries. In contrast, the derived images include an operating system with uv pre-installed.
As an example, to run uv in a container using a Debian-based image:
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-0-1)$ docker
```

### [Available images](https://docs.astral.sh/uv/guides/integration/docker/#available-images)
The following distroless images are available:
  * `ghcr.io/astral-sh/uv:latest`
  * `ghcr.io/astral-sh/uv:{major}.{minor}.{patch}`, e.g., `ghcr.io/astral-sh/uv:0.9.17`
  * `ghcr.io/astral-sh/uv:{major}.{minor}`, e.g., `ghcr.io/astral-sh/uv:0.8` (the latest patch version)


And the following derived images are available:
  * Based on `alpine:3.22`:
    * `ghcr.io/astral-sh/uv:alpine`
    * `ghcr.io/astral-sh/uv:alpine3.22`
  * Based on `alpine:3.21`:
    * `ghcr.io/astral-sh/uv:alpine3.21`
  * Based on `debian:trixie-slim`:
    * `ghcr.io/astral-sh/uv:debian-slim`
    * `ghcr.io/astral-sh/uv:trixie-slim`
  * Based on `debian:bookworm-slim`:
    * `ghcr.io/astral-sh/uv:bookworm-slim`
  * Based on `buildpack-deps:trixie`:
    * `ghcr.io/astral-sh/uv:debian`
    * `ghcr.io/astral-sh/uv:trixie`
  * Based on `buildpack-deps:bookworm`:
    * `ghcr.io/astral-sh/uv:bookworm`
  * Based on `python3.x-alpine`:
    * `ghcr.io/astral-sh/uv:python3.14-alpine`
    * `ghcr.io/astral-sh/uv:python3.13-alpine`
    * `ghcr.io/astral-sh/uv:python3.12-alpine`
    * `ghcr.io/astral-sh/uv:python3.11-alpine`
    * `ghcr.io/astral-sh/uv:python3.10-alpine`
    * `ghcr.io/astral-sh/uv:python3.9-alpine`
    * `ghcr.io/astral-sh/uv:python3.8-alpine`
  * Based on `python3.x-trixie`:
    * `ghcr.io/astral-sh/uv:python3.14-trixie`
    * `ghcr.io/astral-sh/uv:python3.13-trixie`
    * `ghcr.io/astral-sh/uv:python3.12-trixie`
    * `ghcr.io/astral-sh/uv:python3.11-trixie`
    * `ghcr.io/astral-sh/uv:python3.10-trixie`
    * `ghcr.io/astral-sh/uv:python3.9-trixie`
  * Based on `python3.x-slim-trixie`:
    * `ghcr.io/astral-sh/uv:python3.14-trixie-slim`
    * `ghcr.io/astral-sh/uv:python3.13-trixie-slim`
    * `ghcr.io/astral-sh/uv:python3.12-trixie-slim`
    * `ghcr.io/astral-sh/uv:python3.11-trixie-slim`
    * `ghcr.io/astral-sh/uv:python3.10-trixie-slim`
    * `ghcr.io/astral-sh/uv:python3.9-trixie-slim`
  * Based on `python3.x-bookworm`:
    * `ghcr.io/astral-sh/uv:python3.14-bookworm`
    * `ghcr.io/astral-sh/uv:python3.13-bookworm`
    * `ghcr.io/astral-sh/uv:python3.12-bookworm`
    * `ghcr.io/astral-sh/uv:python3.11-bookworm`
    * `ghcr.io/astral-sh/uv:python3.10-bookworm`
    * `ghcr.io/astral-sh/uv:python3.9-bookworm`
    * `ghcr.io/astral-sh/uv:python3.8-bookworm`
  * Based on `python3.x-slim-bookworm`:
    * `ghcr.io/astral-sh/uv:python3.14-bookworm-slim`
    * `ghcr.io/astral-sh/uv:python3.13-bookworm-slim`
    * `ghcr.io/astral-sh/uv:python3.12-bookworm-slim`
    * `ghcr.io/astral-sh/uv:python3.11-bookworm-slim`
    * `ghcr.io/astral-sh/uv:python3.10-bookworm-slim`
    * `ghcr.io/astral-sh/uv:python3.9-bookworm-slim`
    * `ghcr.io/astral-sh/uv:python3.8-bookworm-slim`


As with the distroless image, each derived image is published with uv version tags as `ghcr.io/astral-sh/uv:{major}.{minor}.{patch}-{base}` and `ghcr.io/astral-sh/uv:{major}.{minor}-{base}`, e.g., `ghcr.io/astral-sh/uv:0.9.17-alpine`.
In addition, starting with `0.8` each derived image also sets `UV_TOOL_BIN_DIR` to `/usr/local/bin` to allow `uv tool install` to work as expected with the default user.
For more details, see the 
### [Installing uv](https://docs.astral.sh/uv/guides/integration/docker/#installing-uv)
Use one of the above images with uv pre-installed or install uv by copying the binary from the official distroless Docker image:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-1-1)FROMpython:3.12-slim-trixie
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-1-2)COPY=ghcr.io/astral-sh/uv:latest
```

Or, with the installer:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-1)FROMpython:3.12-slim-trixie
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-2)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-3)# The installer requires curl (and certificates) to download the release archive
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-4)RUN&&[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-5)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-6)# Download the latest installer
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-7)ADD[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-8)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-9)# Run the installer then remove it
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-10)RUN&&[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-11)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-12)# Ensure the installed binary is on the `PATH`
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-2-13)ENVPATH="/root/.local/bin/:$PATH"

```

Note this requires `curl` to be available.
In either case, it is best practice to pin to a specific uv version, e.g., with:
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-3-1)COPY=ghcr.io/astral-sh/uv:0.9.17
```

Tip
While the Dockerfile example above pins to a specific tag, it's also possible to pin a specific SHA256. Pinning a specific SHA256 is considered best practice in environments that require reproducible builds as tags can be moved across different commit SHAs.
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-4-1)# e.g., using a hash from a previous release
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-4-2)COPY=ghcr.io/astral-sh/uv@sha256:2381d6aa60c326b71fd40023f921a0a3b8f91b14d5db6b90402e65a635053709
```

Or, with the installer:
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-5-1)ADD
```

### [Installing a project](https://docs.astral.sh/uv/guides/integration/docker/#installing-a-project)
If you're using uv to manage your project, you can copy it into the image and install it:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-1)# Copy the project into the image
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-2)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-3)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-4)# Disable development dependencies
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-5)ENVUV_NO_DEV=1
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-6)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-7)# Sync the project into a new environment, asserting the lockfile is up to date
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-8)WORKDIR/app
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-6-9)RUN
```

Important
It is best practice to add `.venv` to a 
Then, to start your application by default:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-7-1)# Presuming there is a `my_app` command provided by the project
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-7-2)CMD["uv","run","my_app"]

```

Tip
It is best practice to use [intermediate layers](https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers) separating installation of dependencies and the project itself to improve Docker image build times.
See a complete example in the 
### [Using the environment](https://docs.astral.sh/uv/guides/integration/docker/#using-the-environment)
Once the project is installed, you can either _activate_ the project virtual environment by placing its binary directory at the front of the path:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-8-1)ENVPATH="/app/.venv/bin:$PATH"

```

Or, you can use `uv run` for any commands that require the environment:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-9-1)RUN
```

Tip
Alternatively, the [`UV_PROJECT_ENVIRONMENT` setting](https://docs.astral.sh/uv/concepts/projects/config/#project-environment-path) can be set before syncing to install to the system Python environment and skip environment activation entirely.
### [Using installed tools](https://docs.astral.sh/uv/guides/integration/docker/#using-installed-tools)
To use installed tools, ensure the [tool bin directory](https://docs.astral.sh/uv/concepts/tools/#tool-executables) is on the path:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-10-1)ENVPATH=/root/.local/bin:$PATH
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-10-2)RUN
```

```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-1)$ docker$(docker)"cowsay -t hello"
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-2)  _____
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-3)| hello |
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-4)  =====
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-5)     \
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-6)      \
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-7)        ^__^
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-8)        (oo)\_______
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-9)        (__)\       )\/\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-10)            ||----w |
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-11-11)            ||     ||

```

Note
The tool bin directory's location can be determined by running the `uv tool dir --bin` command in the container.
Alternatively, it can be set to a constant location:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-12-1)ENVUV_TOOL_BIN_DIR=/opt/uv-bin/

```

### [Installing Python in ARM musl images](https://docs.astral.sh/uv/guides/integration/docker/#installing-python-in-arm-musl-images)
While uv will attempt to [install a compatible Python version](https://docs.astral.sh/uv/guides/install-python/) if no such version is available in the image, uv does not yet support installing Python for musl Linux on ARM. For example, if you are using an Alpine Linux base image on an ARM machine, you may need to add it with the system package manager:
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-13-1)apk=3.12

```

## [Developing in a container](https://docs.astral.sh/uv/guides/integration/docker/#developing-in-a-container)
When developing, it's useful to mount the project directory into a container. With this setup, changes to the project can be immediately reflected in a containerized service without rebuilding the image. However, it is important _not_ to include the project virtual environment (`.venv`) in the mount, because the virtual environment is platform specific and the one built for the image should be kept.
### [Mounting the project with `docker run`](https://docs.astral.sh/uv/guides/integration/docker/#mounting-the-project-with-docker-run)
Bind mount the project (in the working directory) to `/app` while retaining the `.venv` directory with an 
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-14-1)$ docker[...]

```

Tip
The `--rm` flag is included to ensure the container and anonymous volume are cleaned up when the container exits.
See a complete example in the 
### [Configuring `watch` with `docker compose`](https://docs.astral.sh/uv/guides/integration/docker/#configuring-watch-with-docker-compose)
When using Docker compose, more sophisticated tooling is available for container development. The 
Note
This feature requires Compose 2.22.0 which is bundled with Docker Desktop 4.24.
Configure `watch` in your 
compose.yaml```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-1)services:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-2)example:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-3)build:.
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-4)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-5)# ...
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-6)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-7)develop:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-8)# Create a `watch` configuration to update the app
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-9)#
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-10)watch:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-11)# Sync the working directory with the `/app` directory in the container
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-12)-action:sync
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-13)path:.
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-14)target:/app
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-15)# Exclude the project virtual environment
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-16)ignore:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-17)-.venv/
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-18)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-19)# Rebuild the image on changes to the `pyproject.toml`
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-20)-action:rebuild
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-15-21)path:./pyproject.toml

```

Then, run `docker compose watch` to run the container with the development setup.
See a complete example in the 
## [Optimizations](https://docs.astral.sh/uv/guides/integration/docker/#optimizations)
### [Compiling bytecode](https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode)
Compiling Python source files to bytecode is typically desirable for production images as it tends to improve startup time (at the cost of increased installation time).
To enable bytecode compilation, use the `--compile-bytecode` flag:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-16-1)RUN
```

Alternatively, you can set the `UV_COMPILE_BYTECODE` environment variable to ensure that all commands within the Dockerfile compile bytecode:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-17-1)ENVUV_COMPILE_BYTECODE=1

```

### [Caching](https://docs.astral.sh/uv/guides/integration/docker/#caching)
A 
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-18-1)ENVUV_LINK_MODE=copy
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-18-2)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-18-3)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-18-4)
```

Changing the default [`UV_LINK_MODE`](https://docs.astral.sh/uv/reference/settings/#link-mode) silences warnings about not being able to use hard links since the cache and sync target are on separate file systems.
If you're not mounting the cache, image size can be reduced by using the `--no-cache` flag or setting `UV_NO_CACHE`.
By default, managed Python installations are not cached before being installed. Setting `UV_PYTHON_CACHE_DIR` can be used in combination with a cache mount:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-19-1)ENVUV_PYTHON_CACHE_DIR=/root/.cache/uv/python
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-19-2)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-19-3)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-19-4)
```

Note
The cache directory's location can be determined by running the `uv cache dir` command in the container.
Alternatively, the cache can be set to a constant location:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-20-1)ENVUV_CACHE_DIR=/opt/uv-cache/

```

### [Intermediate layers](https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers)
If you're using uv to manage your project, you can improve build times by moving your transitive dependency installation into its own layer via the `--no-install` options.
`uv sync --no-install-project` will install the dependencies of the project but not the project itself. Since the project changes frequently, but its dependencies are generally static, this can be a big time saver.
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-1)# Install uv
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-2)FROMpython:3.12-slim
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-3)COPY=ghcr.io/astral-sh/uv:latest[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-4)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-5)# Change the working directory to the `app` directory
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-6)WORKDIR/app
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-7)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-8)# Install dependencies
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-9)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-10)=type=bind,source=uv.lock,target=uv.lock\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-11)=type=bind,source=pyproject.toml,target=pyproject.toml\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-12)[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-13)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-14)# Copy the project into the image
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-15)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-16)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-17)# Sync the project
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-18)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-21-19)
```

Note that the `pyproject.toml` is required to identify the project root and name, but the project _contents_ are not copied into the image until the final `uv sync` command.
Tip
If you want to remove additional, specific packages from the sync, use `--no-install-package <name>`.
#### [Intermediate layers in workspaces](https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers-in-workspaces)
If you're using a [workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/), then a couple changes are needed:
  * Use `--frozen` instead of `--locked` during the initially sync.
  * Use the `--no-install-workspace` flag which excludes the project _and_ any workspace members.


Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-1)# Install uv
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-2)FROMpython:3.12-slim
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-3)COPY=ghcr.io/astral-sh/uv:latest[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-4)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-5)WORKDIR/app
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-6)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-7)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-8)=type=bind,source=uv.lock,target=uv.lock\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-9)=type=bind,source=pyproject.toml,target=pyproject.toml\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-10)[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-11)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-12)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-13)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-14)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-22-15)
```

uv cannot assert that the `uv.lock` file is up-to-date without each of the workspace member `pyproject.toml` files, so we use `--frozen` instead of `--locked` to skip the check during the initial sync. The next sync, after all the workspace members have been copied, can still use `--locked` and will validate that the lockfile is correct for all workspace members.
### [Non-editable installs](https://docs.astral.sh/uv/guides/integration/docker/#non-editable-installs)
By default, uv installs projects and workspace members in editable mode, such that changes to the source code are immediately reflected in the environment.
`uv sync` and `uv run` both accept a `--no-editable` flag, which instructs uv to install the project in non-editable mode, removing any dependency on the source code.
In the context of a multi-stage Docker image, `--no-editable` can be used to include the project in the synced virtual environment from one stage, then copy the virtual environment alone (and not the source code) into the final image.
For example:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-1)# Install uv
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-2)FROMpython:3.12-slimASbuilder
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-3)COPY=ghcr.io/astral-sh/uv:latest[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-4)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-5)# Change the working directory to the `app` directory
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-6)WORKDIR/app
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-7)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-8)# Install dependencies
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-9)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-10)=type=bind,source=uv.lock,target=uv.lock\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-11)=type=bind,source=pyproject.toml,target=pyproject.toml\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-12)[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-13)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-14)# Copy the project into the intermediate image
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-15)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-16)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-17)# Sync the project
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-18)RUN=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-19)[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-20)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-21)FROMpython:3.12-slim
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-22)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-23)# Copy the environment, but not the source code
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-24)COPY=builder=app:app[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-25)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-26)# Run the application
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-23-27)CMD["/app/.venv/bin/hello"]

```

### [Using uv temporarily](https://docs.astral.sh/uv/guides/integration/docker/#using-uv-temporarily)
If uv isn't needed in the final image, the binary can be mounted in each invocation:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-24-1)RUN=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-24-2)
```

## [Using the pip interface](https://docs.astral.sh/uv/guides/integration/docker/#using-the-pip-interface)
### [Installing a package](https://docs.astral.sh/uv/guides/integration/docker/#installing-a-package)
The system Python environment is safe to use this context, since a container is already isolated. The `--system` flag can be used to install in the system environment:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-25-1)RUN
```

To use the system Python environment by default, set the `UV_SYSTEM_PYTHON` variable:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-26-1)ENVUV_SYSTEM_PYTHON=1

```

Alternatively, a virtual environment can be created and activated:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-27-1)RUN[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-27-2)# Use the virtual environment automatically
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-27-3)ENVVIRTUAL_ENV=/opt/venv
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-27-4)# Place entry points in the environment at the front of the path
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-27-5)ENVPATH="/opt/venv/bin:$PATH"

```

When using a virtual environment, the `--system` flag should be omitted from uv invocations:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-28-1)RUN
```

### [Installing requirements](https://docs.astral.sh/uv/guides/integration/docker/#installing-requirements)
To install requirements files, copy them into the container:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-29-1)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-29-2)RUN
```

### [Installing a project](https://docs.astral.sh/uv/guides/integration/docker/#installing-a-project_1)
When installing a project alongside requirements, it is best practice to separate copying the requirements from the rest of the source code. This allows the dependencies of the project (which do not change often) to be cached separately from the project itself (which changes very frequently).
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-30-1)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-30-2)RUN[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-30-3)COPY[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-30-4)RUN
```

## [Verifying image provenance](https://docs.astral.sh/uv/guides/integration/docker/#verifying-image-provenance)
The Docker images are signed during the build process to provide proof of their origin. These attestations can be used to verify that an image was produced from an official channel.
For example, you can verify the attestations with the 
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-1)$ gh[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-2)Loaded digest sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx for oci://ghcr.io/astral-sh/uv:latest
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-3)Loaded 1 attestation from GitHub API
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-4)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-5)The following policy criteria will be enforced:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-6)- OIDC Issuer must match:................... https://token.actions.githubusercontent.com
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-7)- Source Repository Owner URI must match:... https://github.com/astral-sh
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-8)- Predicate type must match:................ https://slsa.dev/provenance/v1
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-9)- Subject Alternative Name must match regex: (?i)^https://github.com/astral-sh/
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-10)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-11)✓ Verification succeeded!
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-12)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-13)sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx was attested by:
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-14)REPO          PREDICATE_TYPE                  WORKFLOW
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-31-15)astral-sh/uv  https://slsa.dev/provenance/v1  .github/workflows/build-docker.yml@refs/heads/main

```

This tells you that the specific Docker image was built by the official uv GitHub release workflow and hasn't been tampered with since.
GitHub attestations build on the `uv`:
```
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-1)$ REPO=astral-sh/uv
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-2)$ gh$REPO${REPO}:latest
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-3)Wrote attestations to file sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.jsonl.
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-4)Any previous content has been overwritten
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-5)
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-6)The trusted metadata is now available at sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.jsonl
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-7)$ docker${REPO}:latest"{{json .Manifest}}"[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-8)$ cosign\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-9)\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-10)"$(jq).jsonl"\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-11)="https://token.actions.githubusercontent.com"\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-12)="^https://github\.com/${REPO}/.*"\
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-13)(jq'.|del(.digest,.size)')
[](https://docs.astral.sh/uv/guides/integration/docker/#__codelineno-32-14)Verified OK

```

Tip
These examples use `latest`, but best practice is to verify the attestation for a specific version tag, e.g., `ghcr.io/astral-sh/uv:0.9.17`, or (even better) the specific image digest, such as `ghcr.io/astral-sh/uv:0.5.27@sha256:5adf09a5a526f380237408032a9308000d14d5947eafa687ad6c6a2476787b4f`.
December 9, 2025
