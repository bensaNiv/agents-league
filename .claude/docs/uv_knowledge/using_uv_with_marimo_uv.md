---
# Smart Librarian Export (v2.0)
- Page Number: 49
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/marimo
- Page Title: Using uv with marimo | uv
- Semantic Filename: using_uv_with_marimo_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 4,190 characters
---

# Using uv with marimo | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/marimo/#using-uv-with-marimo)
# [Using uv with marimo](https://docs.astral.sh/uv/guides/integration/marimo/#using-uv-with-marimo)
You can readily use marimo as a standalone tool, as self-contained scripts, in projects, and in non-project environments.
## [Using marimo as a standalone tool](https://docs.astral.sh/uv/guides/integration/marimo/#using-marimo-as-a-standalone-tool)
For ad-hoc access to marimo notebooks, start a marimo server at any time in an isolated environment with:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-0-1)$ uvx
```

Start a specific notebook with:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-1-1)$ uvx
```

## [Using marimo with inline script metadata](https://docs.astral.sh/uv/guides/integration/marimo/#using-marimo-with-inline-script-metadata)
Because marimo notebooks are stored as Python scripts, they can encapsulate their own dependencies using inline script metadata, via uv's [support for scripts](https://docs.astral.sh/uv/guides/scripts/). For example, to add `numpy` as a dependency to your notebook, use this command:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-2-1)$ uv
```

To interactively edit a notebook containing inline script metadata, use:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-3-1)$ uvx
```

marimo will automatically use uv to start your notebook in an isolated virtual environment with your script's dependencies. Packages installed from the marimo UI will automatically be added to the notebook's script metadata.
You can optionally run these notebooks as Python scripts, without opening an interactive session:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-4-1)$ uv
```

## [Using marimo within a project](https://docs.astral.sh/uv/guides/integration/marimo/#using-marimo-within-a-project)
If you're working within a [project](https://docs.astral.sh/uv/concepts/projects/), you can start a marimo notebook with access to the project's virtual environment via the following command (assuming marimo is a project dependency):
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-5-1)$ uv
```

To make additional packages available to your notebook, either add them to your project with `uv add`, or use marimo's built-in package installation UI, which will invoke `uv add` on your behalf.
If marimo is not a project dependency, you can still run a notebook with the following command:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-6-1)$ uv
```

This will let you import your project's modules while editing your notebook. However, packages installed via marimo's UI when running in this way will not be added to your project, and may disappear on subsequent marimo invocations.
## [Using marimo in a non-project environment](https://docs.astral.sh/uv/guides/integration/marimo/#using-marimo-in-a-non-project-environment)
To run marimo in a virtual environment that isn't associated with a [project](https://docs.astral.sh/uv/concepts/projects/), add marimo to the environment directly:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-7-1)$ uv[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-7-2)$ uv[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-7-3)$ uv[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-7-4)$ uv
```

From here, `import numpy` will work within the notebook, and marimo's UI installer will add packages to the environment with `uv pip install` on your behalf.
## [Running marimo notebooks as scripts](https://docs.astral.sh/uv/guides/integration/marimo/#running-marimo-notebooks-as-scripts)
Regardless of how your dependencies are managed (with inline script metadata, within a project, or with a non-project environment), you can run marimo notebooks as scripts with:
```
[](https://docs.astral.sh/uv/guides/integration/marimo/#__codelineno-8-1)$ uv
```

This executes your notebook as a Python script, without opening an interactive session in your browser.
May 27, 2025
