---
# Smart Librarian Export (v2.0)
- Page Number: 11
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/getting-started/installation
- Page Title: Installation | uv
- Semantic Filename: installation_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 10,335 characters
---

# Installation | uv

[ Skip to content ](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)
# [Installing uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)
## [Installation methods](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
Install uv with our standalone installers or your package manager of choice.
### [Standalone installer](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
uv provides a standalone installer to download and install uv:
[macOS and Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)
Use `curl` to download the script and execute it with `sh`:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-0-1)$ curl|
```

If your system doesn't have `curl`, you can use `wget`:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-1-1)$ wget|
```

Request a specific version by including it in the URL:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-2-1)$ curl|
```

Use `irm` to download the script and execute it with `iex`:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-3-1)PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

```

Changing the 
Request a specific version by including it in the URL:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-4-1)PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.17/install.ps1 | iex"

```

Tip
The installation script may be inspected before use:
[macOS and Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_2_1)[Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_2_2)
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-5-1)$ curl|
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-6-1)PS> powershell -c "irm https://astral.sh/uv/install.ps1 | more"

```

Alternatively, the installer or binaries can be downloaded directly from [GitHub](https://docs.astral.sh/uv/getting-started/installation/#github-releases).
See the reference documentation on the [installer](https://docs.astral.sh/uv/reference/installer/) for details on customizing your uv installation.
### [PyPI](https://docs.astral.sh/uv/getting-started/installation/#pypi)
For convenience, uv is published to 
If installing from PyPI, we recommend installing uv into an isolated environment, e.g., with `pipx`:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-7-1)$ pipx
```

However, `pip` can also be used:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-8-1)$ pip
```

Note
uv ships with prebuilt distributions (wheels) for many platforms; if a wheel is not available for a given platform, uv will be built from source, which requires a Rust toolchain. See the 
### [Homebrew](https://docs.astral.sh/uv/getting-started/installation/#homebrew)
uv is available in the core Homebrew packages.
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-9-1)$ brew
```

### [MacPorts](https://docs.astral.sh/uv/getting-started/installation/#macports)
uv is available via 
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-10-1)$ sudo
```

### [WinGet](https://docs.astral.sh/uv/getting-started/installation/#winget)
uv is available via 
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-11-1)$ winget=astral-sh.uv
```

### [Scoop](https://docs.astral.sh/uv/getting-started/installation/#scoop)
uv is available via 
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-12-1)$ scoop
```

### [Docker](https://docs.astral.sh/uv/getting-started/installation/#docker)
uv provides a Docker image at 
See our guide on [using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/) for more details.
### [GitHub Releases](https://docs.astral.sh/uv/getting-started/installation/#github-releases)
uv release artifacts can be downloaded directly from 
Each release page includes binaries for all supported platforms as well as instructions for using the standalone installer via `github.com` instead of `astral.sh`.
### [Cargo](https://docs.astral.sh/uv/getting-started/installation/#cargo)
uv is available via 
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-13-1)$ cargo
```

Note
This method builds uv from source, which requires a compatible Rust toolchain.
## [Upgrading uv](https://docs.astral.sh/uv/getting-started/installation/#upgrading-uv)
When uv is installed via the standalone installer, it can update itself on-demand:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-14-1)$ uv
```

Tip
Updating uv will re-run the installer and can modify your shell profiles. To disable this behavior, set `UV_NO_MODIFY_PATH=1`.
When another installation method is used, self-updates are disabled. Use the package manager's upgrade method instead. For example, with `pip`:
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-15-1)$ pip
```

## [Shell autocompletion](https://docs.astral.sh/uv/getting-started/installation/#shell-autocompletion)
Tip
You can run `echo $SHELL` to help you determine your shell.
To enable shell autocompletion for uv commands, run one of the following:
[Bash](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_3_1)[Zsh](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_3_2)[fish](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_3_3)[Elvish](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_3_4)[PowerShell / pwsh](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_3_5)
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-16-1)echo'eval "$(uv generate-shell-completion bash)"'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-17-1)echo'eval "$(uv generate-shell-completion zsh)"'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-18-1)echo'uv generate-shell-completion fish | source'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-19-1)echo'eval (uv generate-shell-completion elvish | slurp)'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-20-1)if (!(Test-Path -Path $PROFILE)) {
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-20-2)  New-Item -ItemType File -Path $PROFILE -Force
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-20-3)}
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-20-4)Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'

```

To enable shell autocompletion for uvx, run one of the following:
[Bash](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_4_1)[Zsh](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_4_2)[fish](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_4_3)[Elvish](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_4_4)[PowerShell / pwsh](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_4_5)
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-21-1)echo'eval "$(uvx --generate-shell-completion bash)"'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-22-1)echo'eval "$(uvx --generate-shell-completion zsh)"'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-23-1)echo'uvx --generate-shell-completion fish | source'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-24-1)echo'eval (uvx --generate-shell-completion elvish | slurp)'
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-25-1)if (!(Test-Path -Path $PROFILE)) {
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-25-2)  New-Item -ItemType File -Path $PROFILE -Force
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-25-3)}
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-25-4)Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'

```

Then restart the shell or source the shell config file.
## [Uninstallation](https://docs.astral.sh/uv/getting-started/installation/#uninstallation)
If you need to remove uv from your system, follow these steps:
  1. Clean up stored data (optional):
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-26-1)$ uv[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-26-2)$ rm"$(uv)"
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-26-3)$ rm"$(uv)"

```

Tip
Before removing the binaries, you may want to remove any data that uv has stored. See the [storage reference](https://docs.astral.sh/uv/reference/storage/) for details on where uv stores data.
  2. Remove the uv, uvx, and uvw binaries:
[macOS and Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_5_1)[Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_5_2)
```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-27-1)$ rm
```

```
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-28-1)PS> rm $HOME\.local\bin\uv.exe
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-28-2)PS> rm $HOME\.local\bin\uvx.exe
[](https://docs.astral.sh/uv/getting-started/installation/#__codelineno-28-3)PS> rm $HOME\.local\bin\uvw.exe

```

Note
Prior to 0.5.0, uv was installed into `~/.cargo/bin`. The binaries can be removed from there to uninstall. Upgrading from an older version will not automatically remove the binaries from `~/.cargo/bin`.


## [Next steps](https://docs.astral.sh/uv/getting-started/installation/#next-steps)
See the [first steps](https://docs.astral.sh/uv/getting-started/first-steps/) or jump straight to the [guides](https://docs.astral.sh/uv/guides/) to start using uv.
December 9, 2025
