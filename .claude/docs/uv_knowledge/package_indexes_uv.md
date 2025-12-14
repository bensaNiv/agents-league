---
# Smart Librarian Export (v2.0)
- Page Number: 31
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/indexes
- Page Title: Package indexes | uv
- Semantic Filename: package_indexes_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 17,491 characters
---

# Package indexes | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/indexes/#package-indexes)
# [Package indexes](https://docs.astral.sh/uv/concepts/indexes/#package-indexes)
By default, uv uses the `[[tool.uv.index]]` configuration option (and `--index`, the analogous command-line option).
## [Defining an index](https://docs.astral.sh/uv/concepts/indexes/#defining-an-index)
To include an additional index when resolving dependencies, add a `[[tool.uv.index]]` entry to your `pyproject.toml`:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-0-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-0-2)# Optional name for the index.
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-0-3)name="pytorch"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-0-4)# Required URL for the index.
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-0-5)url="https://download.pytorch.org/whl/cpu"

```

Indexes are prioritized in the order in which they’re defined, such that the first index listed in the configuration file is the first index consulted when resolving dependencies, with indexes provided via the command line taking precedence over those in the configuration file.
By default, uv includes the Python Package Index (PyPI) as the "default" index, i.e., the index used when a package is not found on any other index. To exclude PyPI from the list of indexes, set `default = true` on another index entry (or use the `--default-index` command-line option):
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-1-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-1-2)name="pytorch"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-1-3)url="https://download.pytorch.org/whl/cpu"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-1-4)default=true

```

The default index is always treated as lowest priority, regardless of its position in the list of indexes.
Index names may only contain alphanumeric characters, dashes, underscores, and periods, and must be valid ASCII.
When providing an index on the command line (with `--index` or `--default-index`) or through an environment variable (`UV_INDEX` or `UV_DEFAULT_INDEX`), names are optional but can be included using the `<name>=<url>` syntax, as in:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-2-1)# On the command line.
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-2-2)$pytorch=https://download.pytorch.org/whl/cpu
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-2-3)# Via an environment variable.
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-2-4)$UV_INDEX=pytorch=https://download.pytorch.org/whl/cpu
```

## [Pinning a package to an index](https://docs.astral.sh/uv/concepts/indexes/#pinning-a-package-to-an-index)
A package can be pinned to a specific index by specifying the index in its `tool.uv.sources` entry. For example, to ensure that `torch` is _always_ installed from the `pytorch` index, add the following to your `pyproject.toml`:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-3-1)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-3-2)torch={index="pytorch"}
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-3-3)
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-3-4)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-3-5)name="pytorch"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-3-6)url="https://download.pytorch.org/whl/cpu"

```

Similarly, to pull from a different index based on the platform, you can provide a list of sources disambiguated by environment markers:
pyproject.toml```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-1)[project]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-2)dependencies=["torch"]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-3)
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-4)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-5)torch=[
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-6){index="pytorch-cu118",marker="sys_platform == 'darwin'"},
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-7){index="pytorch-cu124",marker="sys_platform != 'darwin'"},
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-8)]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-9)
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-10)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-11)name="pytorch-cu118"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-12)url="https://download.pytorch.org/whl/cu118"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-13)
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-14)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-15)name="pytorch-cu124"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-4-16)url="https://download.pytorch.org/whl/cu124"

```

An index can be marked as `explicit = true` to prevent packages from being installed from that index unless explicitly pinned to it. For example, to ensure that `torch` is installed from the `pytorch` index, but all other packages are installed from PyPI, add the following to your `pyproject.toml`:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-1)[tool.uv.sources]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-2)torch={index="pytorch"}
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-3)
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-4)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-5)name="pytorch"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-6)url="https://download.pytorch.org/whl/cpu"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-5-7)explicit=true

```

Named indexes referenced via `tool.uv.sources` must be defined within the project's `pyproject.toml` file; indexes provided via the command-line, environment variables, or user-level configuration will not be recognized.
If an index is marked as both `default = true` and `explicit = true`, it will be treated as an explicit index (i.e., only usable via `tool.uv.sources`) while also removing PyPI as the default index.
## [Searching across multiple indexes](https://docs.astral.sh/uv/concepts/indexes/#searching-across-multiple-indexes)
By default, uv will stop at the first index on which a given package is available, and limit resolutions to those present on that first index (`first-index`).
For example, if an internal index is specified via `[[tool.uv.index]]`, uv's behavior is such that if a package exists on that internal index, it will _always_ be installed from that internal index, and never from PyPI. The intent is to prevent "dependency confusion" attacks, in which an attacker publishes a malicious package on PyPI with the same name as an internal package, thus causing the malicious package to be installed instead of the internal package. See, for example, 
To opt in to alternate index behaviors, use the`--index-strategy` command-line option, or the `UV_INDEX_STRATEGY` environment variable, which supports the following values:
  * `first-index` (default): Search for each package across all indexes, limiting the candidate versions to those present in the first index that contains the package.
  * `unsafe-first-match`: Search for each package across all indexes, but prefer the first index with a compatible version, even if newer versions are available on other indexes.
  * `unsafe-best-match`: Search for each package across all indexes, and select the best version from the combined set of candidate versions.


While `unsafe-best-match` is the closest to pip's behavior, it exposes users to the risk of "dependency confusion" attacks.
## [Authentication](https://docs.astral.sh/uv/concepts/indexes/#authentication)
Most private package indexes require authentication to access packages, typically via a username and password (or access token).
Tip
See the [alternative index guide](https://docs.astral.sh/uv/guides/integration/alternative-indexes/) for details on authenticating with specific private index providers, e.g., from AWS, Azure, or GCP.
### [Providing credentials directly](https://docs.astral.sh/uv/concepts/indexes/#providing-credentials-directly)
Credentials can be provided directly via environment variables or by embedding them in the URL.
For example, given an index named `internal-proxy` that requires a username (`public`) and password (`koala`), define the index (without credentials) in your `pyproject.toml`:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-6-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-6-2)name="internal-proxy"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-6-3)url="https://example.com/simple"

```

From there, you can set the `UV_INDEX_INTERNAL_PROXY_USERNAME` and `UV_INDEX_INTERNAL_PROXY_PASSWORD` environment variables, where `INTERNAL_PROXY` is the uppercase version of the index name, with non-alphanumeric characters replaced by underscores:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-7-1)exportUV_INDEX_INTERNAL_PROXY_USERNAME=public
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-7-2)exportUV_INDEX_INTERNAL_PROXY_PASSWORD=koala

```

By providing credentials via environment variables, you can avoid storing sensitive information in the plaintext `pyproject.toml` file.
Alternatively, credentials can be embedded directly in the index definition:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-8-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-8-2)name="internal"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-8-3)url="https://public:koala@pypi-proxy.corp.dev/simple"

```

For security purposes, credentials are _never_ stored in the `uv.lock` file; as such, uv _must_ have access to the authenticated URL at installation time.
### [Using credential providers](https://docs.astral.sh/uv/concepts/indexes/#using-credential-providers)
In addition to providing credentials directly, uv supports discovery of credentials from netrc and keyring. See the [HTTP authentication](https://docs.astral.sh/uv/concepts/authentication/http/) documentation for details on setting up specific credential providers.
By default, uv will attempt an unauthenticated request before querying providers. If the request fails, uv will search for credentials. If credentials are found, an authenticated request will be attempted.
Note
If a username is set, uv will search for credentials before making an unauthenticated request.
Some indexes (e.g., GitLab) will forward unauthenticated requests to a public index, like PyPI — which means that uv will not search for credentials. This behavior can be changed per-index, using the `authenticate` setting. For example, to always search for credentials:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-9-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-9-2)name="example"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-9-3)url="https://example.com/simple"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-9-4)authenticate="always"

```

When `authenticate` is set to `always`, uv will eagerly search for credentials and error if credentials cannot be found.
### [Ignoring error codes when searching across indexes](https://docs.astral.sh/uv/concepts/indexes/#ignoring-error-codes-when-searching-across-indexes)
When using the [first-index strategy](https://docs.astral.sh/uv/concepts/indexes/#searching-across-multiple-indexes), uv will stop searching across indexes if an HTTP 401 Unauthorized or HTTP 403 Forbidden status code is encountered. The one exception is that uv will ignore 403s when searching the `pytorch` index (since this index returns a 403 when a package is not present).
To configure which error codes are ignored for an index, use the `ignored-error-codes` setting. For example, to ignore 403s (but not 401s) for a private index:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-10-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-10-2)name="private-index"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-10-3)url="https://private-index.com/simple"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-10-4)authenticate="always"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-10-5)ignore-error-codes=[403]

```

uv will always continue searching across indexes when it encounters a `404 Not Found`. This cannot be overridden.
### [Disabling authentication](https://docs.astral.sh/uv/concepts/indexes/#disabling-authentication)
To prevent leaking credentials, authentication can be disabled for an index:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-11-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-11-2)name="example"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-11-3)url="https://example.com/simple"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-11-4)authenticate="never"

```

When `authenticate` is set to `never`, uv will never search for credentials for the given index and will error if credentials are provided directly.
### [Customizing cache control headers](https://docs.astral.sh/uv/concepts/indexes/#customizing-cache-control-headers)
By default, uv will respect the cache control headers provided by the index. For example, PyPI serves package metadata with a `max-age=600` header, thereby allowing uv to cache package metadata for 10 minutes; and wheels and source distributions with a `max-age=365000000, immutable` header, thereby allowing uv to cache artifacts indefinitely.
To override the cache control headers for an index, use the `cache-control` setting:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-12-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-12-2)name="example"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-12-3)url="https://example.com/simple"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-12-4)cache-control={api="max-age=600",files="max-age=365000000, immutable"}

```

The `cache-control` setting accepts an object with two optional keys:
  * `api`: Controls caching for Simple API requests (package metadata).
  * `files`: Controls caching for artifact downloads (wheels and source distributions).


The values for these keys are strings that follow the `api = "no-cache"`:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-13-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-13-2)name="example"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-13-3)url="https://example.com/simple"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-13-4)cache-control={api="no-cache"}

```

This setting is most commonly used to override the default cache control headers for private indexes that otherwise disable caching, often unintentionally. We typically recommend following PyPI's approach to caching headers, i.e., setting `api = "max-age=600"` and `files = "max-age=365000000, immutable"`.
## ["Flat" indexes](https://docs.astral.sh/uv/concepts/indexes/#flat-indexes)
By default, `[[tool.uv.index]]` entries are assumed to be PyPI-style registries that implement the `--find-links` option.
To define a flat index in your `pyproject.toml`, use the `format = "flat"` option:
```
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-14-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-14-2)name="example"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-14-3)url="/path/to/directory"
[](https://docs.astral.sh/uv/concepts/indexes/#__codelineno-14-4)format="flat"

```

Flat indexes support the same feature set as Simple Repository API indexes (e.g., `explicit = true`); you can also pin a package to a flat index using `tool.uv.sources`.
## [`--index-url` and `--extra-index-url`](https://docs.astral.sh/uv/concepts/indexes/#-index-url-and-extra-index-url)
In addition to the `[[tool.uv.index]]` configuration option, uv supports pip-style `--index-url` and `--extra-index-url` command-line options for compatibility, where `--index-url` defines the default index and `--extra-index-url` defines additional indexes.
These options can be used in conjunction with the `[[tool.uv.index]]` configuration option, and follow the same prioritization rules:
  * The default index is always treated as lowest priority, whether defined via the legacy `--index-url` argument, the recommended `--default-index` argument, or a `[[tool.uv.index]]` entry with `default = true`.
  * Indexes are consulted in the order in which they’re defined, either via the legacy `--extra-index-url` argument, the recommended `--index` argument, or `[[tool.uv.index]]` entries.


In effect, `--index-url` and `--extra-index-url` can be thought of as unnamed `[[tool.uv.index]]` entries, with `default = true` enabled for the former. In that context, `--index-url` maps to `--default-index`, and `--extra-index-url` maps to `--index`.
August 28, 2025
