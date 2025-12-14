---
# Smart Librarian Export (v2.0)
- Page Number: 22
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/projects/build
- Page Title: Building distributions | uv
- Semantic Filename: building_distributions_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 3,499 characters
---

# Building distributions | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/projects/build/#building-distributions)
# [Building distributions](https://docs.astral.sh/uv/concepts/projects/build/#building-distributions)
To distribute your project to others (e.g., to upload it to an index like PyPI), you'll need to build it into a distributable format.
Python projects are typically distributed as both source distributions (sdists) and binary distributions (wheels). The former is typically a `.tar.gz` or `.zip` file containing the project's source code along with some additional metadata, while the latter is a `.whl` file containing pre-built artifacts that can be installed directly.
Important
When using `uv build`, uv acts as a [`[build-system]`](https://docs.astral.sh/uv/concepts/projects/config/#build-systems). Information about build configuration can be found in the respective tool's documentation.
## [Using `uv build`](https://docs.astral.sh/uv/concepts/projects/build/#using-uv-build)
`uv build` can be used to build both source distributions and binary distributions for your project. By default, `uv build` will build the project in the current directory, and place the built artifacts in a `dist/` subdirectory:
```
[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-0-1)$ uv[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-0-2)$ ls[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-0-3)example-0.1.0-py3-none-any.whl
[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-0-4)example-0.1.0.tar.gz

```

You can build the project in a different directory by providing a path to `uv build`, e.g., `uv build path/to/project`.
`uv build` will first build a source distribution, and then build a binary distribution (wheel) from that source distribution.
You can limit `uv build` to building a source distribution with `uv build --sdist`, a binary distribution with `uv build --wheel`, or build both distributions from source with `uv build --sdist --wheel`.
## [Build constraints](https://docs.astral.sh/uv/concepts/projects/build/#build-constraints)
`uv build` accepts `--build-constraint`, which can be used to constrain the versions of any build requirements during the build process. When coupled with `--require-hashes`, uv will enforce that the requirement used to build the project match specific, known hashes, for reproducibility.
For example, given the following `constraints.txt`:
```
[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-1-1)setuptools==68.2.2 --hash=sha256:b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a

```

Running the following would build the project with the specified version of `setuptools`, and verify that the downloaded `setuptools` distribution matches the specified hash:
```
[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-2-1)$ uv
```

## [Preventing publish to PyPI](https://docs.astral.sh/uv/concepts/projects/build/#preventing-publish-to-pypi)
If you have internal packages that you do not want to be published, you can mark them as private:
```
[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-3-1)[project]
[](https://docs.astral.sh/uv/concepts/projects/build/#__codelineno-3-2)classifiers=["Private :: Do Not Upload"]

```

This setting makes PyPI reject your uploaded package from publishing. It does not affect security or privacy settings on alternative registries.
We also recommend only generating 
November 20, 2025
