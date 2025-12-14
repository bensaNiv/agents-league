---
# Smart Librarian Export (v2.0)
- Page Number: 42
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/pip/inspection
- Page Title: Inspecting environments | uv
- Semantic Filename: inspecting_environments_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 1,317 characters
---

# Inspecting environments | uv

[ Skip to content ](https://docs.astral.sh/uv/pip/inspection/#inspecting-environments)
# [Inspecting environments](https://docs.astral.sh/uv/pip/inspection/#inspecting-environments)
## [Listing installed packages](https://docs.astral.sh/uv/pip/inspection/#listing-installed-packages)
To list all the packages in the environment:
```
[](https://docs.astral.sh/uv/pip/inspection/#__codelineno-0-1)$ uv
```

To list the packages in a JSON format:
```
[](https://docs.astral.sh/uv/pip/inspection/#__codelineno-1-1)$ uv
```

To list all the packages in the environment in a `requirements.txt` format:
```
[](https://docs.astral.sh/uv/pip/inspection/#__codelineno-2-1)$ uv
```

## [Inspecting a package](https://docs.astral.sh/uv/pip/inspection/#inspecting-a-package)
To show information about an installed package, e.g., `numpy`:
```
[](https://docs.astral.sh/uv/pip/inspection/#__codelineno-3-1)$ uv
```

Multiple packages can be inspected at once.
## [Verifying an environment](https://docs.astral.sh/uv/pip/inspection/#verifying-an-environment)
It is possible to install packages with conflicting requirements into an environment if installed in multiple steps.
To check for conflicts or missing dependencies in the environment:
```
[](https://docs.astral.sh/uv/pip/inspection/#__codelineno-4-1)$ uv
```

June 10, 2025
