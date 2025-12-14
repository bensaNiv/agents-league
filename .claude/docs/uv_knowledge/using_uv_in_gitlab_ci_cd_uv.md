---
# Smart Librarian Export (v2.0)
- Page Number: 45
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/gitlab
- Page Title: Using uv in GitLab CI/CD | uv
- Semantic Filename: using_uv_in_gitlab_ci_cd_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 4,721 characters
---

# Using uv in GitLab CI/CD | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/gitlab/#using-uv-in-gitlab-cicd)
# [Using uv in GitLab CI/CD](https://docs.astral.sh/uv/guides/integration/gitlab/#using-uv-in-gitlab-cicd)
## [Using the uv image](https://docs.astral.sh/uv/guides/integration/gitlab/#using-the-uv-image)
Astral provides [Docker images](https://docs.astral.sh/uv/guides/integration/docker/#available-images) with uv preinstalled. Select a variant that is suitable for your workflow.
gitlab-ci.yml```
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-1)variables:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-2)UV_VERSION:"0.9.17"
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-3)PYTHON_VERSION:"3.12"
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-4)BASE_LAYER:bookworm-slim
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-5)# GitLab CI creates a separate mountpoint for the build directory,
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-6)# so we need to copy instead of using hard links.
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-7)UV_LINK_MODE:copy
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-8)
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-9)uv:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-10)image:ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-11)script:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-0-12)# your `uv` commands

```

Note
If you are using a distroless image, you have to specify the entrypoint: 
```
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-1-1)uv:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-1-2)image:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-1-3)name:ghcr.io/astral-sh/uv:$UV_VERSION
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-1-4)entrypoint:[""]
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-1-5)# ...

```

## [Caching](https://docs.astral.sh/uv/guides/integration/gitlab/#caching)
Persisting the uv cache between workflow runs can improve performance.
```
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-1)uv-install:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-2)variables:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-3)UV_CACHE_DIR:.uv-cache
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-4)cache:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-5)-key:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-6)files:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-7)-uv.lock
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-8)paths:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-9)-$UV_CACHE_DIR
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-10)script:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-11)# Your `uv` commands
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-2-12)-uv cache prune --ci

```

See the 
Using `uv cache prune --ci` at the end of the job is recommended to reduce cache size. See the [uv cache documentation](https://docs.astral.sh/uv/concepts/cache/#caching-in-continuous-integration) for more details.
## [Using `uv pip`](https://docs.astral.sh/uv/guides/integration/gitlab/#using-uv-pip)
If using the `uv pip` interface instead of the uv project interface, uv requires a virtual environment by default. To allow installing packages into the system environment, use the `--system` flag on all uv invocations or set the `UV_SYSTEM_PYTHON` variable.
The `UV_SYSTEM_PYTHON` variable can be defined in at different scopes. You can read more about how 
Opt-in for the entire workflow by defining it at the top level:
gitlab-ci.yml```
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-3-1)variables:
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-3-2)UV_SYSTEM_PYTHON:1
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-3-3)
[](https://docs.astral.sh/uv/guides/integration/gitlab/#__codelineno-3-4)# [...]

```

To opt-out again, the `--no-system` flag can be used in any uv invocation.
When persisting the cache, you may want to use `requirements.txt` or `pyproject.toml` as your cache key files instead of `uv.lock`.
December 9, 2025
