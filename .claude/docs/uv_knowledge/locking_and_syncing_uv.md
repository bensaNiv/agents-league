---
# Smart Librarian Export (v2.0)
- Page Number: 34
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/projects/sync
- Page Title: Locking and syncing | uv
- Semantic Filename: locking_and_syncing_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 9,396 characters
---

# Locking and syncing | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/projects/sync/#locking-and-syncing)
# [Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/#locking-and-syncing)
Locking is the process of resolving your project's dependencies into a [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile). Syncing is the process of installing a subset of packages from the lockfile into the [project environment](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment).
## [Automatic lock and sync](https://docs.astral.sh/uv/concepts/projects/sync/#automatic-lock-and-sync)
Locking and syncing are _automatic_ in uv. For example, when `uv run` is used, the project is locked and synced before invoking the requested command. This ensures the project environment is always up-to-date. Similarly, commands which read the lockfile, such as `uv tree`, will automatically update it before running.
To disable automatic locking, use the `--locked` option:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-0-1)$ uv
```

If the lockfile is not up-to-date, uv will raise an error instead of updating the lockfile.
To use the lockfile without checking if it is up-to-date, use the `--frozen` option:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-1-1)$ uv
```

Similarly, to run a command without checking if the environment is up-to-date, use the `--no-sync` option:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-2-1)$ uv
```

## [Checking the lockfile](https://docs.astral.sh/uv/concepts/projects/sync/#checking-the-lockfile)
When considering if the lockfile is up-to-date, uv will check if it matches the project metadata. For example, if you add a dependency to your `pyproject.toml`, the lockfile will be considered outdated. Similarly, if you change the version constraints for a dependency such that the locked version is excluded, the lockfile will be considered outdated. However, if you change the version constraints such that the existing locked version is still included, the lockfile will still be considered up-to-date.
You can check if the lockfile is up-to-date by passing the `--check` flag to `uv lock`:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-3-1)$ uv
```

This is equivalent to the `--locked` flag for other commands.
Important
uv will not consider lockfiles outdated when new versions of packages are released — the lockfile needs to be explicitly updated if you want to upgrade dependencies. See the documentation on [upgrading locked package versions](https://docs.astral.sh/uv/concepts/projects/sync/#upgrading-locked-package-versions) for details.
## [Creating the lockfile](https://docs.astral.sh/uv/concepts/projects/sync/#creating-the-lockfile)
While the lockfile is created [automatically](https://docs.astral.sh/uv/concepts/projects/sync/#automatic-lock-and-sync), the lockfile may also be explicitly created or updated using `uv lock`:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-4-1)$ uv
```

## [Syncing the environment](https://docs.astral.sh/uv/concepts/projects/sync/#syncing-the-environment)
While the environment is synced [automatically](https://docs.astral.sh/uv/concepts/projects/sync/#automatic-lock-and-sync), it may also be explicitly synced using `uv sync`:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-5-1)$ uv
```

Syncing the environment manually is especially useful for ensuring your editor has the correct versions of dependencies.
### [Editable installation](https://docs.astral.sh/uv/concepts/projects/sync/#editable-installation)
When the environment is synced, uv will install the project (and other workspace members) as _editable_ packages, such that re-syncing is not necessary for changes to be reflected in the environment.
To opt-out of this behavior, use the `--no-editable` option.
Note
If the project does not define a build system, it will not be installed. See the [build systems](https://docs.astral.sh/uv/concepts/projects/config/#build-systems) documentation for details.
### [Retaining extraneous packages](https://docs.astral.sh/uv/concepts/projects/sync/#retaining-extraneous-packages)
Syncing is "exact" by default, which means it will remove any packages that are not present in the lockfile.
To retain extraneous packages, use the `--inexact` option:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-6-1)$ uv
```

### [Syncing optional dependencies](https://docs.astral.sh/uv/concepts/projects/sync/#syncing-optional-dependencies)
uv reads optional dependencies from the `[project.optional-dependencies]` table. These are frequently referred to as "extras".
uv does not sync extras by default. Use the `--extra` option to include an extra.
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-7-1)$ uv
```

To quickly enable all extras, use the `--all-extras` option.
See the [optional dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#optional-dependencies) documentation for details on how to manage optional dependencies.
### [Syncing development dependencies](https://docs.astral.sh/uv/concepts/projects/sync/#syncing-development-dependencies)
uv reads development dependencies from the `[dependency-groups]` table (as defined in 
The `dev` group is special-cased and synced by default. See the [default groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#default-groups) documentation for details on changing the defaults.
The `--no-dev` flag can be used to exclude the `dev` group.
The `--only-dev` flag can be used to install the `dev` group _without_ the project and its dependencies.
Additional groups can be included or excluded with the `--all-groups`, `--no-default-groups`, `--group <name>`, `--only-group <name>`, and `--no-group <name>` options. The semantics of `--only-group` are the same as `--only-dev`, the project will not be included. However, `--only-group` will also exclude default groups.
Group exclusions always take precedence over inclusions, so given the command:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-8-1)$ uv sync --no-group foo --group foo

```

The `foo` group would not be installed.
See the [development dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies) documentation for details on how to manage development dependencies.
## [Upgrading locked package versions](https://docs.astral.sh/uv/concepts/projects/sync/#upgrading-locked-package-versions)
With an existing `uv.lock` file, uv will prefer the previously locked versions of packages when running `uv sync` and `uv lock`. Package versions will only change if the project's dependency constraints exclude the previous, locked version.
To upgrade all packages:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-9-1)$ uv
```

To upgrade a single package to the latest version, while retaining the locked versions of all other packages:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-10-1)$ uv
```

To upgrade a single package to a specific version:
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-11-1)$ uv==<version>

```

In all cases, upgrades are limited to the project's dependency constraints. For example, if the project defines an upper bound for a package then an upgrade will not go beyond that version.
Note
uv applies similar logic to Git dependencies. For example, if a Git dependency references the `main` branch, uv will prefer the locked commit SHA in an existing `uv.lock` file over the latest commit on the `main` branch, unless the `--upgrade` or `--upgrade-package` flags are used.
These flags can also be provided to `uv sync` or `uv run` to update the lockfile _and_ the environment.
## [Exporting the lockfile](https://docs.astral.sh/uv/concepts/projects/sync/#exporting-the-lockfile)
If you need to integrate uv with other tools or workflows, you can export `uv.lock` to different formats including `requirements.txt`, `pylock.toml` (PEP 751), and CycloneDX SBOM.
```
[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-12-1)$ uvexport[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-12-2)$ uvexport[](https://docs.astral.sh/uv/concepts/projects/sync/#__codelineno-12-3)$ uvexport
```

See the [export guide](https://docs.astral.sh/uv/concepts/projects/export/) for comprehensive documentation on all export formats and their use cases.
## [Partial installations](https://docs.astral.sh/uv/concepts/projects/sync/#partial-installations)
Sometimes it's helpful to perform installations in multiple steps, e.g., for optimal layer caching while building a Docker image. `uv sync` has several flags for this purpose.
  * `--no-install-project`: Do not install the current project
  * `--no-install-workspace`: Do not install any workspace members, including the root project
  * `--no-install-package <NO_INSTALL_PACKAGE>`: Do not install the given package(s)


When these options are used, all the dependencies of the target are still installed. For example, `--no-install-project` will omit the _project_ but not any of its dependencies.
If used improperly, these flags can result in a broken environment since a package can be missing its dependencies.
November 24, 2025
