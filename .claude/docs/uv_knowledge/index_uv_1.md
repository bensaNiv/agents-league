---
# Smart Librarian Export (v2.0)
- Page Number: 13
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/pip
- Page Title: Index | uv
- Semantic Filename: index_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 1,613 characters
---

# Index | uv

[ Skip to content ](https://docs.astral.sh/uv/pip/#the-pip-interface)
# [The pip interface](https://docs.astral.sh/uv/pip/#the-pip-interface)
uv provides a drop-in replacement for common `pip`, `pip-tools`, and `virtualenv` commands. These commands work directly with the virtual environment, in contrast to uv's primary interfaces where the virtual environment is managed automatically. The `uv pip` interface exposes the speed and functionality of uv to power users and projects that are not ready to transition away from `pip` and `pip-tools`.
The following sections discuss the basics of using `uv pip`:
  * [Creating and using environments](https://docs.astral.sh/uv/pip/environments/)
  * [Installing and managing packages](https://docs.astral.sh/uv/pip/packages/)
  * [Inspecting environments and packages](https://docs.astral.sh/uv/pip/inspection/)
  * [Declaring package dependencies](https://docs.astral.sh/uv/pip/dependencies/)
  * [Locking and syncing environments](https://docs.astral.sh/uv/pip/compile/)


Please note these commands do not _exactly_ implement the interfaces and behavior of the tools they are based on. The further you stray from common workflows, the more likely you are to encounter differences. Consult the [pip-compatibility guide](https://docs.astral.sh/uv/pip/compatibility/) for details.
Important
uv does not rely on or invoke pip. The pip interface is named as such to highlight its dedicated purpose of providing low-level commands that match pip's interface and to separate it from the rest of uv's commands which operate at a higher level of abstraction.
August 8, 2024
