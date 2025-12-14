---
# Smart Librarian Export (v2.0)
- Page Number: 43
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/pydantic_core
- Page Title: pydantic_core - Pydantic Validation
- Semantic Filename: pydantic_core_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 51,980 characters
---

# pydantic_core - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# pydantic_core
##  __version__ `module-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.__version__)
```
__version__: 
```

##  SchemaValidator [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator)
```
SchemaValidator(
    schema: CoreSchema, config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
)

```

`SchemaValidator` is the Python wrapper for `pydantic-core`'s Rust validation logic, internally it owns one `CombinedValidator` which may in turn own more `CombinedValidator`s which make up the full schema validator.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The `CoreSchema` to use for validation. |  _required_  
`config` |  `CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None` |  Optionally a [`CoreConfig`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) to configure validation. |  `None`  
###  title `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.title)
```
title: 
```

The title of the schema, as used in the heading of [`ValidationError.__str__()`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError).
###  validate_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_python)
```
validate_python(
    input: ,
    *,
    strict: | None = None,
    extra: ExtraBehavior | None = None,
    from_attributes: | None = None,
    context: | None = None,
    self_instance: | None = None,
    allow_partial: (
        | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias: | None = None,
    by_name: | None = None
) -> 
```

Validate a Python object against the schema and return the validated object.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`input` |  |  The Python object to validate. |  _required_  
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`from_attributes` |  |  Whether to validate objects as inputs to models by extracting attributes. If `None`, the value of [`CoreConfig.from_attributes`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`  
`self_instance` |  |  An instance of a model set attributes on from validation, this is used when running validation from the `__init__` method of a model. |  `None`  
`allow_partial` |  |  Whether to allow partial validation; if `True` errors in the last element of sequences and mappings are ignored. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`  
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`  
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`  
Raises:
Type | Description  
---|---  
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails.  
|  Other error types maybe raised if internal errors occur.  
Returns:
Type | Description  
---|---  
|  The validated object.  
###  isinstance_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.isinstance_python)
```
isinstance_python(
    input: ,
    *,
    strict: | None = None,
    extra: ExtraBehavior | None = None,
    from_attributes: | None = None,
    context: | None = None,
    self_instance: | None = None,
    by_alias: | None = None,
    by_name: | None = None
) -> 
```

Similar to [`validate_python()`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_python) but returns a boolean.
Arguments match `validate_python()`. This method will not raise `ValidationError`s but will raise internal errors.
Returns:
Type | Description  
---|---  
|  `True` if validation succeeds, `False` if validation fails.  
###  validate_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_json)
```
validate_json(
    input: | | ,
    *,
    strict: | None = None,
    extra: ExtraBehavior | None = None,
    context: | None = None,
    self_instance: | None = None,
    allow_partial: (
        | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias: | None = None,
    by_name: | None = None
) -> 
```

Validate JSON data directly against the schema and return the validated Python object.
This method should be significantly faster than `validate_python(json.loads(json_data))` as it avoids the need to create intermediate Python objects
It also handles constructing the correct Python type even in strict mode, where `validate_python(json.loads(json_data))` would fail validation.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`input` |  |  The JSON data to validate. |  _required_  
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`  
`self_instance` |  |  An instance of a model set attributes on from validation. |  `None`  
`allow_partial` |  |  Whether to allow partial validation; if `True` incomplete JSON will be parsed successfully and errors in the last element of sequences and mappings are ignored. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`  
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`  
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`  
Raises:
Type | Description  
---|---  
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails or if the JSON data is invalid.  
|  Other error types maybe raised if internal errors occur.  
Returns:
Type | Description  
---|---  
|  The validated Python object.  
###  validate_strings [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_strings)
```
validate_strings(
    input: _StringInput,
    *,
    strict: | None = None,
    extra: ExtraBehavior | None = None,
    context: | None = None,
    allow_partial: (
        | ["off", "on", "trailing-strings"]
    ) = False,
    by_alias: | None = None,
    by_name: | None = None
) -> 
```

Validate a string against the schema and return the validated Python object.
This is similar to `validate_json` but applies to scenarios where the input will be a string but not JSON data, e.g. URL fragments, query parameters, etc.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`input` |  `_StringInput` |  The input as a string, or bytes/bytearray if `strict=False`. |  _required_  
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`  
`allow_partial` |  |  Whether to allow partial validation; if `True` errors in the last element of sequences and mappings are ignored. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`  
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`  
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`  
Raises:
Type | Description  
---|---  
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails or if the JSON data is invalid.  
|  Other error types maybe raised if internal errors occur.  
Returns:
Type | Description  
---|---  
|  The validated Python object.  
###  validate_assignment [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.validate_assignment)
```
validate_assignment(
    obj: ,
    field_name: ,
    field_value: ,
    *,
    strict: | None = None,
    extra: ExtraBehavior | None = None,
    from_attributes: | None = None,
    context: | None = None,
    by_alias: | None = None,
    by_name: | None = None
) -> (
    [, ]
    | [[, ], [, ] | None, []]
)

```

Validate an assignment to a field on a model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`obj` |  |  The model instance being assigned to. |  _required_  
`field_name` |  |  The name of the field to validate assignment for. |  _required_  
`field_value` |  |  The value to assign to the field. |  _required_  
`strict` |  |  Whether to validate the object in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`extra` |  `ExtraBehavior | None` |  Whether to ignore, allow, or forbid extra data during model validation. If `None`, the value of [`CoreConfig.extra_fields_behavior`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`from_attributes` |  |  Whether to validate objects as inputs to models by extracting attributes. If `None`, the value of [`CoreConfig.from_attributes`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`  
`by_alias` |  |  Whether to use the field's alias when validating against the provided input data. |  `None`  
`by_name` |  |  Whether to use the field's name when validating against the provided input data. |  `None`  
Raises:
Type | Description  
---|---  
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails.  
|  Other error types maybe raised if internal errors occur.  
Returns:
Type | Description  
---|---  
|  Either the model dict or a tuple of `(model_data, model_extra, fields_set)`  
###  get_default_value [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator.get_default_value)
```
get_default_value(
    *, strict: | None = None, context: = None
) -> Some[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some) | None

```

Get the default value for the schema, including running default value validation.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether to validate the default value in strict mode. If `None`, the value of [`CoreConfig.strict`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) is used. |  `None`  
`context` |  |  The context to use for validation, this is passed to functional validators as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context). |  `None`  
Raises:
Type | Description  
---|---  
`ValidationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)` |  If validation fails.  
|  Other error types maybe raised if internal errors occur.  
Returns:
Type | Description  
---|---  
`Some[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some) | None` |  `None` if the schema has no default value, otherwise a [`Some`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some) containing the default.  
##  SchemaSerializer [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer)
```
SchemaSerializer(
    schema: CoreSchema, config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
)

```

`SchemaSerializer` is the Python wrapper for `pydantic-core`'s Rust serialization logic, internally it owns one `CombinedSerializer` which may in turn own more `CombinedSerializer`s which make up the full schema serializer.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The `CoreSchema` to use for serialization. |  _required_  
`config` |  `CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None` |  Optionally a [`CoreConfig`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) to to configure serialization. |  `None`  
###  to_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_python)
```
to_python(
    value: ,
    *,
    mode: | None = None,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias: | None = None,
    exclude_unset: = False,
    exclude_defaults: = False,
    exclude_none: = False,
    exclude_computed_fields: = False,
    round_trip: = False,
    warnings: (
        | ["none", "warn", "error"]
    ) = True,
    fallback: [[], ] | None = None,
    serialize_as_any: = False,
    context: | None = None
) -> 
```

Serialize/marshal a Python object to a Python object including transforming and filtering data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The Python object to serialize. |  _required_  
`mode` |  |  The serialization mode to use, either `'python'` or `'json'`, defaults to `'python'`. In JSON mode, all values are converted to JSON compatible types, e.g. `None`, `int`, `float`, `str`, `list`, `dict`. |  `None`  
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`  
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`  
`by_alias` |  |  Whether to use the alias names of fields. |  `None`  
`exclude_unset` |  |  Whether to exclude fields that are not set, e.g. are not included in `__pydantic_fields_set__`. |  `False`  
`exclude_defaults` |  |  Whether to exclude fields that are equal to their default value. |  `False`  
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`  
`exclude_computed_fields` |  |  Whether to exclude computed fields. |  `False`  
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`  
`warnings` |  |  How to handle invalid fields. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`  
`fallback` |  |  A function to call when an unknown value is encountered, if `None` a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`  
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`  
`context` |  |  The context to use for serialization, this is passed to functional serializers as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context). |  `None`  
Raises:
Type | Description  
---|---  
`PydanticSerializationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)` |  If serialization fails and no `fallback` function is provided.  
Returns:
Type | Description  
---|---  
|  The serialized Python object.  
###  to_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_json)
```
to_json(
    value: ,
    *,
    indent: | None = None,
    ensure_ascii: = False,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias: | None = None,
    exclude_unset: = False,
    exclude_defaults: = False,
    exclude_none: = False,
    exclude_computed_fields: = False,
    round_trip: = False,
    warnings: (
        | ["none", "warn", "error"]
    ) = True,
    fallback: [[], ] | None = None,
    serialize_as_any: = False,
    context: | None = None
) -> 
```

Serialize a Python object to JSON including transforming and filtering data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The Python object to serialize. |  _required_  
`indent` |  |  If `None`, the JSON will be compact, otherwise it will be pretty-printed with the indent provided. |  `None`  
`ensure_ascii` |  |  If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |  `False`  
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`  
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`  
`by_alias` |  |  Whether to use the alias names of fields. |  `None`  
`exclude_unset` |  |  Whether to exclude fields that are not set, e.g. are not included in `__pydantic_fields_set__`. |  `False`  
`exclude_defaults` |  |  Whether to exclude fields that are equal to their default value. |  `False`  
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`  
`exclude_computed_fields` |  |  Whether to exclude computed fields. |  `False`  
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`  
`warnings` |  |  How to handle invalid fields. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |  `True`  
`fallback` |  |  A function to call when an unknown value is encountered, if `None` a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`  
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`  
`context` |  |  The context to use for serialization, this is passed to functional serializers as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context). |  `None`  
Raises:
Type | Description  
---|---  
`PydanticSerializationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)` |  If serialization fails and no `fallback` function is provided.  
Returns:
Type | Description  
---|---  
|  JSON bytes.  
##  ValidationError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
Bases: 
`ValidationError` is the exception raised by `pydantic-core` when validation fails, it contains a list of errors which detail why validation failed.
###  title `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.title)
```
title: 
```

The title of the error, as used in the heading of `str(validation_error)`.
###  from_exception_data `classmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.from_exception_data)
```
from_exception_data(
    title: ,
    line_errors: [InitErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails)],
    input_type: ["python", "json"] = "python",
    hide_input: = False,
) -> 
```

Python constructor for a Validation Error.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`title` |  |  The title of the error, as used in the heading of `str(validation_error)` |  _required_  
`line_errors` |  `InitErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails)]` |  A list of [`InitErrorDetails`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails) which contain information about errors that occurred during validation. |  _required_  
`input_type` |  |  Whether the error is for a Python object or JSON. |  `'python'`  
`hide_input` |  |  Whether to hide the input value in the error message. |  `False`  
###  error_count [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.error_count)
```
error_count() -> 
```

Returns:
Type | Description  
---|---  
|  The number of errors in the validation error.  
###  errors [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.errors)
```
errors(
    *,
    include_url: = True,
    include_context: = True,
    include_input: = True
) -> [ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]

```

Details about each error in the validation error.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`include_url` |  |  Whether to include a URL to documentation on the error each error. |  `True`  
`include_context` |  |  Whether to include the context of each error. |  `True`  
`include_input` |  |  Whether to include the input value of each error. |  `True`  
Returns:
Type | Description  
---|---  
`ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]` |  A list of [`ErrorDetails`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails) for each error in the validation error.  
###  json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.json)
```
json(
    *,
    indent: | None = None,
    include_url: = True,
    include_context: = True,
    include_input: = True
) -> 
```

Same as [`errors()`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError.errors) but returns a JSON string.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`indent` |  |  The number of spaces to indent the JSON by, or `None` for no indentation - compact JSON. |  `None`  
`include_url` |  |  Whether to include a URL to documentation on the error each error. |  `True`  
`include_context` |  |  Whether to include the context of each error. |  `True`  
`include_input` |  |  Whether to include the input value of each error. |  `True`  
Returns:
Type | Description  
---|---  
|  a JSON string.  
##  ErrorDetails [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)
Bases: 
###  type `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.type)
```
type: 
```

The type of error that occurred, this is an identifier designed for programmatic use that will change rarely or never.
`type` is unique for each error message, and can hence be used as an identifier to build custom error messages.
###  loc `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.loc)
```
loc: [| , ...]

```

Tuple of strings and ints identifying where in the schema the error occurred.
###  msg `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.msg)
```
msg: 
```

A human readable error message.
###  input `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.input)
```
input: 
```

The input data at this `loc` that caused the error.
###  ctx `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.ctx)
```
ctx: [[, ]]

```

Values which are required to render the error message, and could hence be useful in rendering custom error messages. Also useful for passing custom error data forward.
###  url `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails.url)
```
url: []

```

The documentation URL giving information about the error. No URL is available if a [`PydanticCustomError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError) is used.
##  InitErrorDetails [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails)
Bases: 
###  type `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.type)
```
type: | PydanticCustomError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError)

```

The type of error that occurred, this should be a "slug" identifier that changes rarely or never.
###  loc `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.loc)
```
loc: [[| , ...]]

```

Tuple of strings and ints identifying where in the schema the error occurred.
###  input `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.input)
```
input: 
```

The input data at this `loc` that caused the error.
###  ctx `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.InitErrorDetails.ctx)
```
ctx: [[, ]]

```

Values which are required to render the error message, and could hence be useful in rendering custom error messages. Also useful for passing custom error data forward.
##  SchemaError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaError)
Bases: 
Information about errors that occur while building a [`SchemaValidator`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator) or [`SchemaSerializer`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer).
###  error_count [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaError.error_count)
```
error_count() -> 
```

Returns:
Type | Description  
---|---  
|  The number of errors in the schema.  
###  errors [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaError.errors)
```
errors() -> [ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]

```

Returns:
Type | Description  
---|---  
`ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails)]` |  A list of [`ErrorDetails`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails) for each error in the schema.  
##  PydanticCustomError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError)
```
PydanticCustomError(
    error_type: ,
    message_template: ,
    context: [, ] | None = None,
)

```

Bases: 
A custom exception providing flexible error handling for Pydantic validators.
You can raise this error in custom validators when you'd like flexibility in regards to the error type, message, and context.
Example
```
frompydantic_coreimport PydanticCustomError

defcustom_validator(v) -> None:
    if v <= 10:
        raise PydanticCustomError('custom_value_error', 'Value must be greater than {value}', {'value': 10, 'extra_context': 'extra_data'})
    return v

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`error_type` |  |  The error type. |  _required_  
`message_template` |  |  The message template. |  _required_  
`context` |  |  The data to inject into the message template. |  `None`  
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.context)
```
context: [, ] | None

```

Values which are required to render the error message, and could hence be useful in passing error data forward.
###  type `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.type)
```
type: 
```

The error type associated with the error. For consistency with Pydantic, this is typically a snake_case string.
###  message_template `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.message_template)
```
message_template: 
```

The message template associated with the error. This is a string that can be formatted with context variables in `{curly_braces}`.
###  message [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError.message)
```
message() -> 
```

The formatted message associated with the error. This presents as the message template with context variables appropriately injected.
##  PydanticKnownError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError)
```
PydanticKnownError(
    error_type: ErrorType,
    context: [, ] | None = None,
)

```

Bases: 
A helper class for raising exceptions that mimic Pydantic's built-in exceptions, with more flexibility in regards to context.
Unlike [`PydanticCustomError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError), the `error_type` argument must be a known `ErrorType`.
Example
```
frompydantic_coreimport PydanticKnownError

defcustom_validator(v) -> None:
    if v <= 10:
        raise PydanticKnownError('greater_than', {'gt': 10})
    return v

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`error_type` |  `ErrorType` |  The error type. |  _required_  
`context` |  |  The data to inject into the message template. |  `None`  
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.context)
```
context: [, ] | None

```

Values which are required to render the error message, and could hence be useful in passing error data forward.
###  type `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.type)
```
type: ErrorType

```

The type of the error.
###  message_template `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.message_template)
```
message_template: 
```

The message template associated with the provided error type. This is a string that can be formatted with context variables in `{curly_braces}`.
###  message [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticKnownError.message)
```
message() -> 
```

The formatted message associated with the error. This presents as the message template with context variables appropriately injected.
##  PydanticOmit [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticOmit)
Bases: 
An exception to signal that a field should be omitted from a generated result.
This could span from omitting a field from a JSON Schema to omitting a field from a serialized result. Upcoming: more robust support for using PydanticOmit in custom serializers is still in development. Right now, this is primarily used in the JSON Schema generation process.
Example
```
fromtypingimport Callable

frompydantic_coreimport PydanticOmit

frompydanticimport BaseModel
frompydantic.json_schemaimport GenerateJsonSchema, JsonSchemaValue


classMyGenerateJsonSchema(GenerateJsonSchema):
    defhandle_invalid_for_json_schema(self, schema, error_info) -> JsonSchemaValue:
        raise PydanticOmit


classPredicate(BaseModel):
    name: str = 'no-op'
    func: Callable = lambda x: x


instance_example = Predicate()

validation_schema = instance_example.model_json_schema(schema_generator=MyGenerateJsonSchema, mode='validation')
print(validation_schema)
'''
{'properties': {'name': {'default': 'no-op', 'title': 'Name', 'type': 'string'}}, 'title': 'Predicate', 'type': 'object'}
'''

```

For a more in depth example / explanation, see the [customizing JSON schema](https://docs.pydantic.dev/latest/concepts/json_schema/#customizing-the-json-schema-generation-process) docs.
##  PydanticUseDefault [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticUseDefault)
Bases: 
An exception to signal that standard validation either failed or should be skipped, and the default value should be used instead.
This warning can be raised in custom valiation functions to redirect the flow of validation.
Example
```
frompydantic_coreimport PydanticUseDefault
fromdatetimeimport datetime
frompydanticimport BaseModel, field_validator


classEvent(BaseModel):
    name: str = 'meeting'
    time: datetime

    @field_validator('name', mode='plain')
    defname_must_be_present(cls, v) -> str:
        if not v or not isinstance(v, str):
            raise PydanticUseDefault()
        return v


event1 = Event(name='party', time=datetime(2024, 1, 1, 12, 0, 0))
print(repr(event1))
# > Event(name='party', time=datetime.datetime(2024, 1, 1, 12, 0))
event2 = Event(time=datetime(2024, 1, 1, 12, 0, 0))
print(repr(event2))
# > Event(name='meeting', time=datetime.datetime(2024, 1, 1, 12, 0))

```

For an additional example, see the [validating partial json data](https://docs.pydantic.dev/latest/concepts/json/#partial-json-parsing) section of the Pydantic documentation.
##  PydanticSerializationError [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)
```
PydanticSerializationError(message: )

```

Bases: 
An error raised when an issue occurs during serialization.
In custom serializers, this error can be used to indicate that serialization has failed.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`message` |  |  The message associated with the error. |  _required_  
##  PydanticSerializationUnexpectedValue [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationUnexpectedValue)
```
PydanticSerializationUnexpectedValue(message: )

```

Bases: 
An error raised when an unexpected value is encountered during serialization.
This error is often caught and coerced into a warning, as `pydantic-core` generally makes a best attempt at serializing values, in contrast with validation where errors are eagerly raised.
Example
```
frompydanticimport BaseModel, field_serializer
frompydantic_coreimport PydanticSerializationUnexpectedValue

classBasicPoint(BaseModel):
    x: int
    y: int

    @field_serializer('*')
    defserialize(self, v):
        if not isinstance(v, int):
            raise PydanticSerializationUnexpectedValue(f'Expected type `int`, got {type(v)} with value {v}')
        return v

point = BasicPoint(x=1, y=2)
# some sort of mutation
point.x = 'a'

print(point.model_dump())
'''
UserWarning: Pydantic serializer warnings:
PydanticSerializationUnexpectedValue(Expected type `int`, got <class 'str'> with value a)
return self.__pydantic_serializer__.to_python(
{'x': 'a', 'y': 2}
'''

```

This is often used internally in `pydantic-core` when unexpected types are encountered during serialization, but it can also be used by users in custom serializers, as seen above.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`message` |  |  The message associated with the unexpected value. |  _required_  
##  Url [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url)
```
Url(url: )

```

Bases: `SupportsAllComparisons`
A URL type, internal logic uses the 
##  MultiHostUrl [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl)
```
MultiHostUrl(url: )

```

Bases: `SupportsAllComparisons`
A URL type with support for multiple hosts, as used by some databases for DSNs, e.g. `https://foo.com,bar.com/path`.
Internal URL logic uses the 
##  MultiHostHost [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostHost)
Bases: 
A host part of a multi-host URL.
###  username `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostHost.username)
```
username: | None

```

The username part of this host, or `None`.
###  password `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostHost.password)
```
password: | None

```

The password part of this host, or `None`.
###  host `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostHost.host)
```
host: | None

```

The host part of this host, or `None`.
###  port `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostHost.port)
```
port: | None

```

The port part of this host, or `None`.
##  ArgsKwargs [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ArgsKwargs)
```
ArgsKwargs(
    args: [, ...],
    kwargs: [, ] | None = None,
)

```

A construct used to store arguments and keyword arguments for a function call.
This data structure is generally used to store information for core schemas associated with functions (like in an arguments schema). This data structure is also currently used for some validation against dataclasses.
Example
```
frompydantic.dataclassesimport dataclass
frompydanticimport model_validator


@dataclass
classModel:
    a: int
    b: int

    @model_validator(mode="before")
    @classmethod
    defno_op_validator(cls, values):
        print(values)
        return values

Model(1, b=2)
#> ArgsKwargs((1,), {"b": 2})

Model(1, 2)
#> ArgsKwargs((1, 2), {})

Model(a=1, b=2)
#> ArgsKwargs((), {"a": 1, "b": 2})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`args` |  |  The arguments (inherently ordered) for a function call. |  _required_  
`kwargs` |  |  The keyword arguments for a function call |  `None`  
###  args `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ArgsKwargs.args)
```
args: [, ...]

```

The arguments (inherently ordered) for a function call.
###  kwargs `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ArgsKwargs.kwargs)
```
kwargs: [, ] | None

```

The keyword arguments for a function call.
##  Some [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some)
Bases: `_T]`
Similar to Rust's 
Generally used in a union with `None` to different between "some value which could be None" and no value.
###  value `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Some.value)
```
value: _T

```

Returns the value wrapped by `Some`.
##  TzInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo)
```
TzInfo(seconds: = 0.0)

```

Bases: 
An `pydantic-core` implementation of the abstract 
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`seconds` |  |  The offset from UTC in seconds. Defaults to 0.0 (UTC). |  `0.0`  
###  tzname [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.tzname)
```
tzname(dt: | None) -> | None

```

Return the time zone name corresponding to the _dt_ , as a string.
For more info, see 
###  utcoffset [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.utcoffset)
```
utcoffset(dt: | None) -> | None

```

Return offset of local time from UTC, as a 
More info can be found at 
###  dst [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.dst)
```
dst(dt: | None) -> | None

```

Return the daylight saving time (DST) adjustment, as a `None` if DST information isn’t known.
More info can be found at
###  fromutc [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.fromutc)
```
fromutc(dt: ) -> 
```

Adjust the date and time data associated datetime object _dt_ , returning an equivalent datetime in self’s local time.
More info can be found at 
##  ErrorTypeInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo)
Bases: 
Gives information about errors.
###  type `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.type)
```
type: ErrorType

```

The type of error that occurred, this should be a "slug" identifier that changes rarely or never.
###  message_template_python `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.message_template_python)
```
message_template_python: 
```

String template to render a human readable error message from using context, when the input is Python.
###  example_message_python `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.example_message_python)
```
example_message_python: 
```

Example of a human readable error message, when the input is Python.
###  message_template_json `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.message_template_json)
```
message_template_json: []

```

String template to render a human readable error message from using context, when the input is JSON data.
###  example_message_json `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.example_message_json)
```
example_message_json: []

```

Example of a human readable error message, when the input is JSON data.
###  example_context `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorTypeInfo.example_context)
```
example_context: [, ] | None

```

Example of context values.
##  to_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.to_json)
```
to_json(
    value: ,
    *,
    indent: | None = None,
    ensure_ascii: = False,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias: = True,
    exclude_none: = False,
    round_trip: = False,
    timedelta_mode: ["iso8601", "float"] = "iso8601",
    temporal_mode: [
        "iso8601", "seconds", "milliseconds"
    ] = "iso8601",
    bytes_mode: ["utf8", "base64", "hex"] = "utf8",
    inf_nan_mode: [
        "null", "constants", "strings"
    ] = "constants",
    serialize_unknown: = False,
    fallback: [[], ] | None = None,
    serialize_as_any: = False,
    context: | None = None
) -> 
```

Serialize a Python object to JSON including transforming and filtering data.
This is effectively a standalone version of [`SchemaSerializer.to_json`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_json).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The Python object to serialize. |  _required_  
`indent` |  |  If `None`, the JSON will be compact, otherwise it will be pretty-printed with the indent provided. |  `None`  
`ensure_ascii` |  |  If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |  `False`  
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`  
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`  
`by_alias` |  |  Whether to use the alias names of fields. |  `True`  
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`  
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`  
`timedelta_mode` |  |  How to serialize `timedelta` objects, either `'iso8601'` or `'float'`. |  `'iso8601'`  
`temporal_mode` |  |  How to serialize datetime-like objects (`datetime`, `date`, `time`), either `'iso8601'`, `'seconds'`, or `'milliseconds'`. `iso8601` returns an ISO 8601 string; `seconds` returns the Unix timestamp in seconds as a float; `milliseconds` returns the Unix timestamp in milliseconds as a float. |  `'iso8601'`  
`bytes_mode` |  |  How to serialize `bytes` objects, either `'utf8'`, `'base64'`, or `'hex'`. |  `'utf8'`  
`inf_nan_mode` |  |  How to serialize `Infinity`, `-Infinity` and `NaN` values, either `'null'`, `'constants'`, or `'strings'`. |  `'constants'`  
`serialize_unknown` |  |  Attempt to serialize unknown types, `str(value)` will be used, if that fails `"<Unserializable {value_type} object>"` will be used. |  `False`  
`fallback` |  |  A function to call when an unknown value is encountered, if `None` a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`  
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`  
`context` |  |  The context to use for serialization, this is passed to functional serializers as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context). |  `None`  
Raises:
Type | Description  
---|---  
`PydanticSerializationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)` |  If serialization fails and no `fallback` function is provided.  
Returns:
Type | Description  
---|---  
|  JSON bytes.  
##  from_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.from_json)
```
from_json(
    data: | | ,
    *,
    allow_inf_nan: = True,
    cache_strings: (
        | ["all", "keys", "none"]
    ) = True,
    allow_partial: (
        | ["off", "on", "trailing-strings"]
    ) = False
) -> 
```

Deserialize JSON data to a Python object.
This is effectively a faster version of `json.loads()`, with some extra functionality.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`data` |  |  The JSON data to deserialize. |  _required_  
`allow_inf_nan` |  |  Whether to allow `Infinity`, `-Infinity` and `NaN` values as `json.loads()` does by default. |  `True`  
`cache_strings` |  |  Whether to cache strings to avoid constructing new Python objects, this should have a significant impact on performance while increasing memory usage slightly, `all/True` means cache all strings, `keys` means cache only dict keys, `none/False` means no caching. |  `True`  
`allow_partial` |  |  Whether to allow partial deserialization, if `True` JSON data is returned if the end of the input is reached before the full object is deserialized, e.g. `["aa", "bb", "c` would return `['aa', 'bb']`. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`  
Raises:
Type | Description  
---|---  
|  If deserialization fails.  
Returns:
Type | Description  
---|---  
|  The deserialized Python object.  
##  to_jsonable_python [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.to_jsonable_python)
```
to_jsonable_python(
    value: ,
    *,
    include: _IncEx | None = None,
    exclude: _IncEx | None = None,
    by_alias: = True,
    exclude_none: = False,
    round_trip: = False,
    timedelta_mode: ["iso8601", "float"] = "iso8601",
    temporal_mode: [
        "iso8601", "seconds", "milliseconds"
    ] = "iso8601",
    bytes_mode: ["utf8", "base64", "hex"] = "utf8",
    inf_nan_mode: [
        "null", "constants", "strings"
    ] = "constants",
    serialize_unknown: = False,
    fallback: [[], ] | None = None,
    serialize_as_any: = False,
    context: | None = None
) -> 
```

Serialize/marshal a Python object to a JSON-serializable Python object including transforming and filtering data.
This is effectively a standalone version of [`SchemaSerializer.to_python(mode='json')`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer.to_python).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The Python object to serialize. |  _required_  
`include` |  `_IncEx | None` |  A set of fields to include, if `None` all fields are included. |  `None`  
`exclude` |  `_IncEx | None` |  A set of fields to exclude, if `None` no fields are excluded. |  `None`  
`by_alias` |  |  Whether to use the alias names of fields. |  `True`  
`exclude_none` |  |  Whether to exclude fields that have a value of `None`. |  `False`  
`round_trip` |  |  Whether to enable serialization and validation round-trip support. |  `False`  
`timedelta_mode` |  |  How to serialize `timedelta` objects, either `'iso8601'` or `'float'`. |  `'iso8601'`  
`temporal_mode` |  |  How to serialize datetime-like objects (`datetime`, `date`, `time`), either `'iso8601'`, `'seconds'`, or `'milliseconds'`. `iso8601` returns an ISO 8601 string; `seconds` returns the Unix timestamp in seconds as a float; `milliseconds` returns the Unix timestamp in milliseconds as a float. |  `'iso8601'`  
`bytes_mode` |  |  How to serialize `bytes` objects, either `'utf8'`, `'base64'`, or `'hex'`. |  `'utf8'`  
`inf_nan_mode` |  |  How to serialize `Infinity`, `-Infinity` and `NaN` values, either `'null'`, `'constants'`, or `'strings'`. |  `'constants'`  
`serialize_unknown` |  |  Attempt to serialize unknown types, `str(value)` will be used, if that fails `"<Unserializable {value_type} object>"` will be used. |  `False`  
`fallback` |  |  A function to call when an unknown value is encountered, if `None` a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |  `None`  
`serialize_as_any` |  |  Whether to serialize fields with duck-typing serialization behavior. |  `False`  
`context` |  |  The context to use for serialization, this is passed to functional serializers as [`info.context`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context). |  `None`  
Raises:
Type | Description  
---|---  
`PydanticSerializationError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError)` |  If serialization fails and no `fallback` function is provided.  
Returns:
Type | Description  
---|---  
|  The serialized Python object.  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
