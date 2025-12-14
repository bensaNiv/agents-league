---
# Smart Librarian Export (v2.0)
- Page Number: 47
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/alternative-indexes
- Page Title: Using alternative package indexes | uv
- Semantic Filename: using_alternative_package_indexes_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 21,014 characters
---

# Using alternative package indexes | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#using-alternative-package-indexes)
# [Using alternative package indexes](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#using-alternative-package-indexes)
While uv uses the official Python Package Index (PyPI) by default, it also supports [alternative package indexes](https://docs.astral.sh/uv/concepts/indexes/). Most alternative indexes require various forms of authentication, which require some initial setup.
Important
If using the pip interface, please read the documentation on [using multiple indexes](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes) in uv — the default behavior is different from pip to prevent dependency confusion attacks, but this means that uv may not find the versions of a package as you'd expect.
## [Azure Artifacts](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#azure-artifacts)
uv can install packages from 
To use Azure Artifacts, add the index to your project:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-0-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-0-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-0-3)url="https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"

```

### [Authenticate with an Azure access token](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-an-azure-access-token)
If there is a personal access token (PAT) available (e.g., 
For example, with the token stored in the `$AZURE_ARTIFACTS_TOKEN` environment variable, set credentials for the index with:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-1-1)exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=dummy
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-1-2)exportUV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AZURE_ARTIFACTS_TOKEN"

```

Note
`PRIVATE_REGISTRY` should match the name of the index defined in your `pyproject.toml`.
### [Authenticate with `keyring` and `artifacts-keyring`](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-keyring-and-artifacts-keyring)
You can also authenticate to Artifacts using 
The `artifacts-keyring` plugin wraps the 
uv only supports using the `keyring` package in [subprocess mode](https://docs.astral.sh/uv/reference/settings/#keyring-provider). The `keyring` executable must be in the `PATH`, i.e., installed globally or in the active environment. The `keyring` CLI requires a username in the URL, and it must be `VssSessionToken`.
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-1)# Pre-install keyring and the Artifacts plugin from the public PyPI
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-2)uv[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-3)
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-4)# Enable keyring authentication
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-5)exportUV_KEYRING_PROVIDER=subprocess
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-6)
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-7)# Set the username for the index
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-2-8)exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=VssSessionToken

```

Note
The [`tool.uv.keyring-provider`](https://docs.astral.sh/uv/reference/settings/#keyring-provider) setting can be used to enable keyring in your `uv.toml` or `pyproject.toml`.
Similarly, the username for the index can be added directly to the index URL.
### [Publishing packages to Azure Artifacts](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#publishing-packages-to-azure-artifacts)
If you also want to publish your own packages to Azure Artifacts, you can use `uv publish` as described in the [Building and publishing guide](https://docs.astral.sh/uv/guides/package/).
First, add a `publish-url` to the index you want to publish packages to. For example:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-3-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-3-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-3-3)url="https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-3-4)publish-url="https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/"

```

Then, configure credentials (if not using keyring):
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-4-1)$ exportUV_PUBLISH_USERNAME=dummy
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-4-2)$ exportUV_PUBLISH_PASSWORD="$AZURE_ARTIFACTS_TOKEN"

```

And publish the package:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-5-1)$ uv
```

To use `uv publish` without adding the `publish-url` to the project, you can set `UV_PUBLISH_URL`:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-6-1)$ exportUV_PUBLISH_URL=https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-6-2)$ uv
```

Note this method is not preferable because uv cannot check if the package is already published before uploading artifacts.
## [Google Artifact Registry](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#google-artifact-registry)
uv can install packages from 
Note
This guide assumes that 
To use Google Artifact Registry, add the index to your project:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-7-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-7-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-7-3)url="https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"

```

### [Authenticate with a Google access token](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-a-google-access-token)
Credentials can be provided via "Basic" HTTP authentication scheme. Include access token in the password field of the URL. Username must be `oauth2accesstoken`, otherwise authentication will fail.
Generate a token with `gcloud`:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-8-1)exportARTIFACT_REGISTRY_TOKEN=$(
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-8-2)[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-8-3))

```

Note
You might need to pass extra parameters to properly generate the token (like `--project`), this is a basic example.
Then set credentials for the index with:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-9-1)exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-9-2)exportUV_INDEX_PRIVATE_REGISTRY_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"

```

Note
`PRIVATE_REGISTRY` should match the name of the index defined in your `pyproject.toml`.
### [Authenticate with `keyring` and `keyrings.google-artifactregistry-auth`](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-keyring-and-keyringsgoogle-artifactregistry-auth)
You can also authenticate to Artifact Registry using 
The `keyrings.google-artifactregistry-auth` plugin wraps 
uv only supports using the `keyring` package in [subprocess mode](https://docs.astral.sh/uv/reference/settings/#keyring-provider). The `keyring` executable must be in the `PATH`, i.e., installed globally or in the active environment. The `keyring` CLI requires a username in the URL and it must be `oauth2accesstoken`.
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-1)# Pre-install keyring and Artifact Registry plugin from the public PyPI
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-2)uv[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-3)
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-4)# Enable keyring authentication
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-5)exportUV_KEYRING_PROVIDER=subprocess
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-6)
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-7)# Set the username for the index
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-10-8)exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken

```

Note
The [`tool.uv.keyring-provider`](https://docs.astral.sh/uv/reference/settings/#keyring-provider) setting can be used to enable keyring in your `uv.toml` or `pyproject.toml`.
Similarly, the username for the index can be added directly to the index URL.
### [Publishing packages to Google Artifact Registry](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#publishing-packages-to-google-artifact-registry)
If you also want to publish your own packages to Google Artifact Registry, you can use `uv publish` as described in the [Building and publishing guide](https://docs.astral.sh/uv/guides/package/).
First, add a `publish-url` to the index you want to publish packages to. For example:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-11-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-11-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-11-3)url="https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-11-4)publish-url="https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/"

```

Then, configure credentials (if not using keyring):
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-12-1)$ exportUV_PUBLISH_USERNAME=oauth2accesstoken
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-12-2)$ exportUV_PUBLISH_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"

```

And publish the package:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-13-1)$ uv
```

To use `uv publish` without adding the `publish-url` to the project, you can set `UV_PUBLISH_URL`:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-14-1)$ exportUV_PUBLISH_URL=https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-14-2)$ uv
```

Note this method is not preferable because uv cannot check if the package is already published before uploading artifacts.
## [AWS CodeArtifact](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#aws-codeartifact)
uv can install packages from 
Note
This guide assumes that 
The index can be declared like so:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-15-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-15-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-15-3)url="https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"

```

### [Authenticate with an AWS access token](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-an-aws-access-token)
Credentials can be provided via "Basic" HTTP authentication scheme. Include access token in the password field of the URL. Username must be `aws`, otherwise authentication will fail.
Generate a token with `awscli`:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-1)exportAWS_CODEARTIFACT_TOKEN="$(
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-2)\
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-3)\
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-4)\
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-5)\
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-6)[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-16-7))"

```

Note
You might need to pass extra parameters to properly generate the token (like `--region`), this is a basic example.
Then set credentials for the index with:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-17-1)exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-17-2)exportUV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AWS_CODEARTIFACT_TOKEN"

```

Note
`PRIVATE_REGISTRY` should match the name of the index defined in your `pyproject.toml`.
### [Authenticate with `keyring` and `keyrings.codeartifact`](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-keyring-and-keyringscodeartifact)
You can also authenticate to Artifact Registry using 
The `keyrings.codeartifact` plugin wraps 
uv only supports using the `keyring` package in [subprocess mode](https://docs.astral.sh/uv/reference/settings/#keyring-provider). The `keyring` executable must be in the `PATH`, i.e., installed globally or in the active environment. The `keyring` CLI requires a username in the URL and it must be `aws`.
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-1)# Pre-install keyring and AWS CodeArtifact plugin from the public PyPI
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-2)uv[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-3)
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-4)# Enable keyring authentication
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-5)exportUV_KEYRING_PROVIDER=subprocess
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-6)
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-7)# Set the username for the index
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-18-8)exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=aws

```

Note
The [`tool.uv.keyring-provider`](https://docs.astral.sh/uv/reference/settings/#keyring-provider) setting can be used to enable keyring in your `uv.toml` or `pyproject.toml`.
Similarly, the username for the index can be added directly to the index URL.
### [Publishing packages to AWS CodeArtifact](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#publishing-packages-to-aws-codeartifact)
If you also want to publish your own packages to AWS CodeArtifact, you can use `uv publish` as described in the [Building and publishing guide](https://docs.astral.sh/uv/guides/package/).
First, add a `publish-url` to the index you want to publish packages to. For example:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-19-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-19-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-19-3)url="https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-19-4)publish-url="https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/"

```

Then, configure credentials (if not using keyring):
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-20-1)$ exportUV_PUBLISH_USERNAME=aws
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-20-2)$ exportUV_PUBLISH_PASSWORD="$AWS_CODEARTIFACT_TOKEN"

```

And publish the package:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-21-1)$ uv
```

To use `uv publish` without adding the `publish-url` to the project, you can set `UV_PUBLISH_URL`:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-22-1)$ exportUV_PUBLISH_URL=https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-22-2)$ uv
```

Note this method is not preferable because uv cannot check if the package is already published before uploading artifacts.
## [JFrog Artifactory](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#jfrog-artifactory)
uv can install packages from JFrog Artifactory, either by using a username and password or a JWT token.
To use it, add the index to your project:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-23-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-23-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-23-3)url="https://<organization>.jfrog.io/artifactory/api/pypi/<repository>/simple"

```

### [Authenticate with username and password](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-username-and-password)
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-24-1)$ exportUV_INDEX_PRIVATE_REGISTRY_USERNAME="<username>"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-24-2)$ exportUV_INDEX_PRIVATE_REGISTRY_PASSWORD="<password>"

```

### [Authenticate with JWT token](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#authenticate-with-jwt-token)
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-25-1)$ exportUV_INDEX_PRIVATE_REGISTRY_USERNAME=""
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-25-2)$ exportUV_INDEX_PRIVATE_REGISTRY_PASSWORD="$JFROG_JWT_TOKEN"

```

Note
Replace `PRIVATE_REGISTRY` in the environment variable names with the actual index name defined in your `pyproject.toml`.
### [Publishing packages to JFrog Artifactory](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#publishing-packages-to-jfrog-artifactory)
Add a `publish-url` to your index definition:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-26-1)[[tool.uv.index]]
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-26-2)name="private-registry"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-26-3)url="https://<organization>.jfrog.io/artifactory/api/pypi/<repository>/simple"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-26-4)publish-url="https://<organization>.jfrog.io/artifactory/api/pypi/<repository>"

```

Important
If you use `--token "$JFROG_TOKEN"` or `UV_PUBLISH_TOKEN` with JFrog, you will receive a 401 Unauthorized error as JFrog requires an empty username but uv passes `__token__` for as the username when `--token` is used.
To authenticate, pass your token as the password and set the username to an empty string:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-27-1)$ uv"""$JFROG_TOKEN"

```

Alternatively, you can set environment variables:
```
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-28-1)$ exportUV_PUBLISH_USERNAME=""
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-28-2)$ exportUV_PUBLISH_PASSWORD="$JFROG_TOKEN"
[](https://docs.astral.sh/uv/guides/integration/alternative-indexes/#__codelineno-28-3)$ uv
```

Note
The publish environment variables (`UV_PUBLISH_USERNAME` and `UV_PUBLISH_PASSWORD`) do not include the index name.
June 30, 2025
