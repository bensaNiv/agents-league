---
# Smart Librarian Export (v2.0)
- Page Number: 23
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/getting-started/help
- Page Title: Getting help | uv
- Semantic Filename: getting_help_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,751 characters
---

# Getting help | uv

[ Skip to content ](https://docs.astral.sh/uv/getting-started/help/#getting-help)
# [Getting help](https://docs.astral.sh/uv/getting-started/help/#getting-help)
## [Help menus](https://docs.astral.sh/uv/getting-started/help/#help-menus)
The `--help` flag can be used to view the help menu for a command, e.g., for `uv`:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-0-1)$ uv
```

To view the help menu for a specific command, e.g., for `uv init`:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-1-1)$ uv
```

When using the `--help` flag, uv displays a condensed help menu. To view a longer help menu for a command, use `uv help`:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-2-1)$ uvhelp

```

To view the long help menu for a specific command, e.g., for `uv init`:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-3-1)$ uvhelp
```

When using the long help menu, uv will attempt to use `less` or `more` to "page" the output so it is not all displayed at once. To exit the pager, press `q`.
## [Displaying verbose output](https://docs.astral.sh/uv/getting-started/help/#displaying-verbose-output)
The `-v` flag can be used to display verbose output for a command, e.g., for `uv sync`:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-4-1)$ uv
```

The `-v` flag can be repeated to increase verbosity, e.g.:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-5-1)$ uv
```

Often, the verbose output will include additional information about why uv is behaving in a certain way.
## [Viewing the version](https://docs.astral.sh/uv/getting-started/help/#viewing-the-version)
When seeking help, it's important to determine the version of uv that you're using — sometimes the problem is already solved in a newer version.
To check the installed version:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-6-1)$ uv
```

The following are also valid:
```
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-7-1)$ uv# Same output as `uv self version`
[](https://docs.astral.sh/uv/getting-started/help/#__codelineno-7-2)$ uv# Will not include the build commit and date

```

Note
Before uv 0.7.0, `uv version` was used instead of `uv self version`.
## [Troubleshooting issues](https://docs.astral.sh/uv/getting-started/help/#troubleshooting-issues)
The reference documentation contains a [troubleshooting guide](https://docs.astral.sh/uv/reference/troubleshooting/) for common issues.
## [Open an issue on GitHub](https://docs.astral.sh/uv/getting-started/help/#open-an-issue-on-github)
The 
## [Chat on Discord](https://docs.astral.sh/uv/getting-started/help/#chat-on-discord)
Astral has a 
September 17, 2025
