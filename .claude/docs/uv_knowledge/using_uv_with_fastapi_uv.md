---
# Smart Librarian Export (v2.0)
- Page Number: 56
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/fastapi
- Page Title: Using uv with FastAPI | uv
- Semantic Filename: using_uv_with_fastapi_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 6,477 characters
---

# Using uv with FastAPI | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/fastapi/#using-uv-with-fastapi)
# [Using uv with FastAPI](https://docs.astral.sh/uv/guides/integration/fastapi/#using-uv-with-fastapi)
Note
You can view the source code for this guide in the 
## [Migrating an existing FastAPI project](https://docs.astral.sh/uv/guides/integration/fastapi/#migrating-an-existing-fastapi-project)
As an example, consider the sample application defined in the 
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-1)project
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-2)└── app
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-3)    ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-4)    ├── main.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-5)    ├── dependencies.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-6)    ├── routers
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-7)    │   ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-8)    │   ├── items.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-9)    │   └── users.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-10)    └── internal
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-11)        ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-0-12)        └── admin.py

```

To use uv with this application, inside the `project` directory run:
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-1-1)$ uv
```

This creates a [project with an application layout](https://docs.astral.sh/uv/concepts/projects/init/#applications) and a `pyproject.toml` file.
Then, add a dependency on FastAPI:
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-2-1)$ uv
```

You should now have the following structure:
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-1)project
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-2)├── pyproject.toml
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-3)└── app
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-4)    ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-5)    ├── main.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-6)    ├── dependencies.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-7)    ├── routers
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-8)    │   ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-9)    │   ├── items.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-10)    │   └── users.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-11)    └── internal
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-12)        ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-3-13)        └── admin.py

```

And the contents of the `pyproject.toml` file should look something like this:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-1)[project]
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-2)name="uv-fastapi-example"
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-3)version="0.1.0"
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-4)description="FastAPI project"
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-5)readme="README.md"
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-6)requires-python=">=3.12"
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-7)dependencies=[
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-8)"fastapi[standard]",
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-4-9)]

```

From there, you can run the FastAPI application with:
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-5-1)$ uv
```

`uv run` will automatically resolve and lock the project dependencies (i.e., create a `uv.lock` alongside the `pyproject.toml`), create a virtual environment, and run the command in that environment.
Test the app by opening 
## [Deployment](https://docs.astral.sh/uv/guides/integration/fastapi/#deployment)
To deploy the FastAPI application with Docker, you can use the following `Dockerfile`:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-1)FROMpython:3.12-slim
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-2)
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-3)# Install uv.
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-4)COPY=ghcr.io/astral-sh/uv:latest[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-5)
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-6)# Copy the application into the container.
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-7)COPY[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-8)
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-9)# Install the application dependencies.
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-10)WORKDIR/app
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-11)RUN[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-12)
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-13)# Run the application.
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-6-14)CMD["/app/.venv/bin/fastapi","run","app/main.py","--port","80","--host","0.0.0.0"]

```

Build the Docker image with:
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-7-1)$ docker
```

Run the Docker container locally with:
```
[](https://docs.astral.sh/uv/guides/integration/fastapi/#__codelineno-8-1)$ docker8000:80
```

Navigate to 
Tip
For more on using uv with Docker, see the [Docker guide](https://docs.astral.sh/uv/guides/integration/docker/).
November 17, 2025
