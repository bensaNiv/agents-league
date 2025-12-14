---
# Smart Librarian Export (v2.0)
- Page Number: 52
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/preview
- Page Title: Preview features | uv
- Semantic Filename: preview_features_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 3,713 characters
---

# Preview features | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/preview/#preview-features)
# [Preview features](https://docs.astral.sh/uv/concepts/preview/#preview-features)
uv includes opt-in preview features to provide an opportunity for community feedback and increase confidence that changes are a net-benefit before enabling them for everyone.
## [Enabling preview features](https://docs.astral.sh/uv/concepts/preview/#enabling-preview-features)
To enable all preview features, use the `--preview` flag:
```
[](https://docs.astral.sh/uv/concepts/preview/#__codelineno-0-1)$ uv
```

Or, set the `UV_PREVIEW` environment variable:
```
[](https://docs.astral.sh/uv/concepts/preview/#__codelineno-1-1)$ UV_PREVIEW=1
```

To enable specific preview features, use the `--preview-features` flag:
```
[](https://docs.astral.sh/uv/concepts/preview/#__codelineno-2-1)$ uv
```

The `--preview-features` flag can be repeated to enable multiple features:
```
[](https://docs.astral.sh/uv/concepts/preview/#__codelineno-3-1)$ uv
```

Or, features can be provided in a comma separated list:
```
[](https://docs.astral.sh/uv/concepts/preview/#__codelineno-4-1)$ uv
```

The `UV_PREVIEW_FEATURES` environment variable can be used similarly, e.g.:
```
[](https://docs.astral.sh/uv/concepts/preview/#__codelineno-5-1)$ UV_PREVIEW_FEATURES=foo,bar
```

For backwards compatibility, enabling preview features that do not exist will warn, but not error.
## [Using preview features](https://docs.astral.sh/uv/concepts/preview/#using-preview-features)
Often, preview features can be used without changing any preview settings if the behavior change is gated by some sort of user interaction, For example, while `pylock.toml` support is in preview, you can use `uv pip install` with a `pylock.toml` file without additional configuration because specifying the `pylock.toml` file indicates you want to use the feature. However, a warning will be displayed that the feature is in preview. The preview feature can be enabled to silence the warning.
Other preview features change behavior without changes to your use of uv. For example, when the `python-upgrade` feature is enabled, the default behavior of `uv python install` changes to allow uv to upgrade Python versions transparently. This feature requires enabling the preview flag for proper usage.
## [Available preview features](https://docs.astral.sh/uv/concepts/preview/#available-preview-features)
The following preview features are available:
  * `add-bounds`: Allows configuring the [default bounds for `uv add`](https://docs.astral.sh/uv/reference/settings/#add-bounds) invocations.
  * `json-output`: Allows `--output-format json` for various uv commands.
  * `package-conflicts`: Allows defining workspace conflicts at the package level.
  * `pylock`: Allows installing from `pylock.toml` files.
  * `python-install-default`: Allows [installing `python` and `python3` executables](https://docs.astral.sh/uv/concepts/python-versions/#installing-python-executables).
  * `python-upgrade`: Allows [transparent Python version upgrades](https://docs.astral.sh/uv/concepts/python-versions/#upgrading-python-versions).
  * `format`: Allows using `uv format`.
  * `native-auth`: Enables storage of credentials in a [system-native location](https://docs.astral.sh/uv/concepts/authentication/http/#the-uv-credentials-store).
  * `workspace-metadata`: Allows using `uv workspace metadata`.
  * `workspace-dir`: Allows using `uv workspace dir`.
  * `workspace-list`: Allows using `uv workspace list`.


## [Disabling preview features](https://docs.astral.sh/uv/concepts/preview/#disabling-preview-features)
The `--no-preview` option can be used to disable preview features.
November 17, 2025
