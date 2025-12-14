---
# Smart Librarian Export (v2.0)
- Page Number: 4
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/install
- Page Title: Installation - Pydantic Validation
- Semantic Filename: installation_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,233 characters
---

# Installation - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/install/#optional-dependencies)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Installation
Installation is as simple as:
[pip](https://docs.pydantic.dev/latest/install/#__tabbed_1_1)[uv](https://docs.pydantic.dev/latest/install/#__tabbed_1_2)
```
pip
```

```
uv
```

Pydantic has a few dependencies:
If you've got Python 3.9+ and `pip` installed, you're good to go.
Pydantic is also available on 
```
conda
```

## Optional dependencies[¶](https://docs.pydantic.dev/latest/install/#optional-dependencies)
Pydantic has the following optional dependencies:
  * `email`: Email validation provided by the 
  * `timezone`: Fallback IANA time zone database provided by the 


To install optional dependencies along with Pydantic:
[pip](https://docs.pydantic.dev/latest/install/#__tabbed_2_1)[uv](https://docs.pydantic.dev/latest/install/#__tabbed_2_2)
```
# with the `email` extra:
pip'pydantic[email]'
# or with `email` and `timezone` extras:
pip'pydantic[email,timezone]'

```

```
# with the `email` extra:
uv'pydantic[email]'
# or with `email` and `timezone` extras:
uv'pydantic[email,timezone]'

```

Of course, you can also install requirements manually with `pip install email-validator tzdata`.
## Install from repository[¶](https://docs.pydantic.dev/latest/install/#install-from-repository)
And if you prefer to install Pydantic directly from the repository:
[pip](https://docs.pydantic.dev/latest/install/#__tabbed_3_1)[uv](https://docs.pydantic.dev/latest/install/#__tabbed_3_2)
```
pip'git+https://github.com/pydantic/pydantic@main'
# or with `email` and `timezone` extras:
pip'git+https://github.com/pydantic/pydantic@main#egg=pydantic[email,timezone]'

```

```
uv'git+https://github.com/pydantic/pydantic@main'
# or with `email` and `timezone` extras:
uv'git+https://github.com/pydantic/pydantic@main#egg=pydantic[email,timezone]'

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
