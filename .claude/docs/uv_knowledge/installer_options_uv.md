---
# Smart Librarian Export (v2.0)
- Page Number: 40
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/reference/installer
- Page Title: Installer options | uv
- Semantic Filename: installer_options_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,677 characters
---

# Installer options | uv

[ Skip to content ](https://docs.astral.sh/uv/reference/installer/#the-uv-installer)
# [The uv installer](https://docs.astral.sh/uv/reference/installer/#the-uv-installer)
## [Changing the installation path](https://docs.astral.sh/uv/reference/installer/#changing-the-installation-path)
By default, uv is installed in the user [executable directory](https://docs.astral.sh/uv/reference/storage/#executable-directory).
To change the installation path, use `UV_INSTALL_DIR`:
[macOS and Linux](https://docs.astral.sh/uv/reference/installer/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/reference/installer/#__tabbed_1_2)
```
[](https://docs.astral.sh/uv/reference/installer/#__codelineno-0-1)$ curl|UV_INSTALL_DIR="/custom/path"
```

```
[](https://docs.astral.sh/uv/reference/installer/#__codelineno-1-1)PS> powershell -ExecutionPolicy ByPass -c {$env:UV_INSTALL_DIR = "C:\Custom\Path";irm https://astral.sh/uv/install.ps1 | iex}

```

Note
Changing the installation path only affects where the uv binary is installed. uv will still store its data (cache, Python installations, tools, etc.) in the default locations. See the [storage reference](https://docs.astral.sh/uv/reference/storage/) for details on these locations and how to customize them.
## [Disabling shell modifications](https://docs.astral.sh/uv/reference/installer/#disabling-shell-modifications)
The installer may also update your shell profiles to ensure the uv binary is on your `PATH`. To disable this behavior, use `UV_NO_MODIFY_PATH`. For example:
```
[](https://docs.astral.sh/uv/reference/installer/#__codelineno-2-1)$ curl|UV_NO_MODIFY_PATH=1
```

If installed with `UV_NO_MODIFY_PATH`, subsequent operations, like `uv self update`, will not modify your shell profiles.
## [Unmanaged installations](https://docs.astral.sh/uv/reference/installer/#unmanaged-installations)
In ephemeral environments like CI, use `UV_UNMANAGED_INSTALL` to install uv to a specific path while preventing the installer from modifying shell profiles or environment variables:
```
[](https://docs.astral.sh/uv/reference/installer/#__codelineno-3-1)$ curl|UV_UNMANAGED_INSTALL="/custom/path"
```

The use of `UV_UNMANAGED_INSTALL` will also disable self-updates (via `uv self update`).
## [Passing options to the installation script](https://docs.astral.sh/uv/reference/installer/#passing-options-to-the-installation-script)
Using environment variables is recommended because they are consistent across platforms. However, options can be passed directly to the installation script. For example, to see the available options:
```
[](https://docs.astral.sh/uv/reference/installer/#__codelineno-4-1)$ curl|
```

November 17, 2025
