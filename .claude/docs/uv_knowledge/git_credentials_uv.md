---
# Smart Librarian Export (v2.0)
- Page Number: 60
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/concepts/authentication/git
- Page Title: Git credentials | uv
- Semantic Filename: git_credentials_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 3,074 characters
---

# Git credentials | uv

[ Skip to content ](https://docs.astral.sh/uv/concepts/authentication/git/#git-credentials)
# [Git credentials](https://docs.astral.sh/uv/concepts/authentication/git/#git-credentials)
uv allows packages to be installed from private Git repositories using SSH or HTTP authentication.
## [SSH authentication](https://docs.astral.sh/uv/concepts/authentication/git/#ssh-authentication)
To authenticate using an SSH key, use the `ssh://` protocol:
  * `git+ssh://git@<hostname>/...` (e.g., `git+ssh://git@github.com/astral-sh/uv`)
  * `git+ssh://git@<host>/...` (e.g., `git+ssh://git@github.com-key-2/astral-sh/uv`)


SSH authentication requires using the username `git`.
See the 
### [HTTP authentication](https://docs.astral.sh/uv/concepts/authentication/git/#http-authentication)
To authenticate over HTTP Basic authentication using a password or token:
  * `git+https://<user>:<token>@<hostname>/...` (e.g., `git+https://git:github_pat_asdf@github.com/astral-sh/uv`)
  * `git+https://<token>@<hostname>/...` (e.g., `git+https://github_pat_asdf@github.com/astral-sh/uv`)
  * `git+https://<user>@<hostname>/...` (e.g., `git+https://git@github.com/astral-sh/uv`)


Note
When using a GitHub personal access token, the username is arbitrary. GitHub doesn't allow you to use your account name and password in URLs like this, although other hosts may.
If there are no credentials present in the URL and authentication is needed, the [Git credential helper](https://docs.astral.sh/uv/concepts/authentication/git/#git-credential-helpers) will be queried.
## [Persistence of credentials](https://docs.astral.sh/uv/concepts/authentication/git/#persistence-of-credentials)
When using `uv add`, uv _will not_ persist Git credentials to the `pyproject.toml` or `uv.lock`. These files are often included in source control and distributions, so it is generally unsafe to include credentials in them.
If you have a Git credential helper configured, your credentials may be automatically persisted, resulting in successful subsequent fetches of the dependency. However, if you do not have a Git credential helper or the project is used on a machine without credentials seeded, uv will fail to fetch the dependency.
You _may_ force uv to persist Git credentials by passing the `--raw` option to `uv add`. However, we strongly recommend setting up a [credential helper](https://docs.astral.sh/uv/concepts/authentication/git/#git-credential-helpers) instead.
## [Git credential helpers](https://docs.astral.sh/uv/concepts/authentication/git/#git-credential-helpers)
Git credential helpers are used to store and retrieve Git credentials. See the 
If you're using GitHub, the simplest way to set up a credential helper is to 
```
[](https://docs.astral.sh/uv/concepts/authentication/git/#__codelineno-0-1)$ gh
```

See the 
Note
When using `gh auth login` interactively, the credential helper will be configured automatically. But when using `gh auth login --with-token`, as in the uv [GitHub Actions guide](https://docs.astral.sh/uv/guides/integration/github/#private-repos), the 
August 28, 2025
