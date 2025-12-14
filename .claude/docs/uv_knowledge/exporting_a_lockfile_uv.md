---
# Smart Librarian Export (v2.0)
- Page Number: 21
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/projects/export
- Page Title: Exporting a lockfile | uv
- Semantic Filename: exporting_a_lockfile_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 4,381 characters
---

# Exporting a lockfile | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/projects/export/#exporting-a-lockfile)
# [Exporting a lockfile](https://docs.astral.sh/uv/concepts/projects/export/#exporting-a-lockfile)
uv can export a lockfile to different formats for integration with other tools and workflows. The `uv export` command supports multiple output formats, each suited to different use cases.
For more details on lockfiles and how they're created, see the [project layout](https://docs.astral.sh/uv/concepts/projects/layout/) and [locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) documentation.
## [Overview of export formats](https://docs.astral.sh/uv/concepts/projects/export/#overview-of-export-formats)
uv supports three export formats:
  * `requirements.txt`: The traditional pip-compatible 
  * `pylock.toml`: The standardized Python lockfile format defined in 
  * `CycloneDX`: An industry-standard 


The format can be specified with the `--format` flag:
```
[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-0-1)$ uvexport[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-0-2)$ uvexport[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-0-3)$ uvexport
```

Tip
By default, `uv export` prints to stdout. Use `--output-file` to write to a file for any format:
```
[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-1-1)$ uvexport[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-1-2)$ uvexport[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-1-3)$ uvexport
```

## [`requirements.txt` format](https://docs.astral.sh/uv/concepts/projects/export/#requirementstxt-format)
The `requirements.txt` format is the most widely supported format for Python dependencies. It can be used with `pip` and other Python package managers.
### [Basic usage](https://docs.astral.sh/uv/concepts/projects/export/#basic-usage)
```
[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-2-1)$ uvexport
```

The generated `requirements.txt` file can then be installed via `uv pip install`, or with other tools like `pip`.
Note
In general, we recommend against using both a `uv.lock` and a `requirements.txt` file. The `uv.lock` format is more powerful and includes features that cannot be expressed in `requirements.txt`. If you find yourself exporting a `uv.lock` file, consider opening an issue to discuss your use case.
## [`pylock.toml` format](https://docs.astral.sh/uv/concepts/projects/export/#pylocktoml-format)
### [Basic usage](https://docs.astral.sh/uv/concepts/projects/export/#basic-usage_1)
```
[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-3-1)$ uvexport
```

## [CycloneDX SBOM format](https://docs.astral.sh/uv/concepts/projects/export/#cyclonedx-sbom-format)
uv can export your project's dependency lockfile as a Software Bill of Materials (SBOM) in CycloneDX format. SBOMs provide a comprehensive inventory of all software components in your application, which is useful for security auditing, compliance, and supply chain transparency.
Important
Support for exporting to CycloneDX is in [preview](https://docs.astral.sh/uv/concepts/preview/), and may change in any future release.
### [What is CycloneDX?](https://docs.astral.sh/uv/concepts/projects/export/#what-is-cyclonedx)
### [Basic usage](https://docs.astral.sh/uv/concepts/projects/export/#basic-usage_2)
To export your project's lockfile as a CycloneDX SBOM:
```
[](https://docs.astral.sh/uv/concepts/projects/export/#__codelineno-4-1)$ uvexport
```

This will generate a JSON-encoded CycloneDX v1.5 document containing your project and all of its dependencies.
### [SBOM Structure](https://docs.astral.sh/uv/concepts/projects/export/#sbom-structure)
The generated SBOM follows the 
  * `uv:package:marker`: Environment markers (e.g., `python_version >= "3.8"`)
  * `uv:workspace:path`: Relative path for workspace members


## [Next steps](https://docs.astral.sh/uv/concepts/projects/export/#next-steps)
To learn more about lockfiles and exporting, see the [locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) documentation and the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-export).
Or, read on to learn how to [build and publish your project to a package index](https://docs.astral.sh/uv/guides/package/).
November 20, 2025
