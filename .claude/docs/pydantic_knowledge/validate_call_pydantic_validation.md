---
# Smart Librarian Export (v2.0)
- Page Number: 42
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/validate_call
- Page Title: Validate Call - Pydantic Validation
- Semantic Filename: validate_call_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 3,538 characters
---

# Validate Call - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Validate Call
Decorator for validating function calls.
##  validate_call [¶](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call)
```
validate_call(
    *,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None = None,
    validate_return: = False
) -> [[AnyCallableT], AnyCallableT]

```

```
validate_call(func: AnyCallableT) -> AnyCallableT

```

```
validate_call(
    func: AnyCallableT | None = None,
    /,
    *,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None = None,
    validate_return: = False,
) -> AnyCallableT | [[AnyCallableT], AnyCallableT]

```

Usage Documentation
[Validation Decorator](https://docs.pydantic.dev/latest/concepts/validation_decorator/)
Returns a decorated wrapper around the function that validates the arguments and, optionally, the return value.
Usage may be either as a plain decorator `@validate_call` or with arguments `@validate_call(...)`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`func` |  `AnyCallableT | None` |  The function to be decorated. |  `None`  
`config` |  `ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | None` |  The configuration dictionary. |  `None`  
`validate_return` |  |  Whether to validate the return value. |  `False`  
Returns:
Type | Description  
---|---  
`AnyCallableT | AnyCallableT], AnyCallableT]` |  The decorated function.  
Source code in `pydantic/validate_call_decorator.py`
```
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
```
| ```
defvalidate_call(
    func: AnyCallableT | None = None,
    /,
    *,
    config: ConfigDict | None = None,
    validate_return: bool = False,
) -> AnyCallableT | Callable[[AnyCallableT], AnyCallableT]:
"""!!! abstract "Usage Documentation"
        [Validation Decorator](../concepts/validation_decorator.md)

    Returns a decorated wrapper around the function that validates the arguments and, optionally, the return value.

    Usage may be either as a plain decorator `@validate_call` or with arguments `@validate_call(...)`.

    Args:
        func: The function to be decorated.
        config: The configuration dictionary.
        validate_return: Whether to validate the return value.

    Returns:
        The decorated function.
    """
    parent_namespace = _typing_extra.parent_frame_namespace()

    defvalidate(function: AnyCallableT) -> AnyCallableT:
        _check_function_type(function)
        validate_call_wrapper = _validate_call.ValidateCallWrapper(
            cast(_generate_schema.ValidateCallSupportedTypes, function), config, validate_return, parent_namespace
        )
        return _validate_call.update_wrapper_attributes(function, validate_call_wrapper.__call__)  # type: ignore

    if func is not None:
        return validate(func)
    else:
        return validate

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
