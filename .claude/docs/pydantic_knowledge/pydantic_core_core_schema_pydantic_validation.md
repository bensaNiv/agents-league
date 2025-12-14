---
# Smart Librarian Export (v2.0)
- Page Number: 50
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/pydantic_core_schema
- Page Title: pydantic_core.core_schema - Pydantic Validation
- Semantic Filename: pydantic_core_core_schema_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 244,363 characters
---

# pydantic_core.core_schema - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# pydantic_core.core_schema
This module contains definitions to build schemas which `pydantic_core` can validate and serialize.
##  WhenUsed `module-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)
```
WhenUsed = [
    "always", "unless-none", "json", "json-unless-none"
]

```

Values have the following meanings:
  * `'always'` means always use
  * `'unless-none'` means use unless the value is `None`
  * `'json'` means use when serializing to JSON
  * `'json-unless-none'` means use when serializing to JSON and the value is not `None`


##  CoreConfig [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig)
Bases: 
Base class for schema configuration options.
Attributes:
Name | Type | Description  
---|---|---  
`title` |  |  The name of the configuration.  
`strict` |  |  Whether the configuration should strictly adhere to specified rules.  
`extra_fields_behavior` |  `ExtraBehavior` |  The behavior for handling extra fields.  
`typed_dict_total` |  |  Whether the TypedDict should be considered total. Default is `True`.  
`from_attributes` |  |  Whether to use attributes for models, dataclasses, and tagged union keys.  
`loc_by_alias` |  |  Whether to use the used alias (or first alias for "field required" errors) instead of `field_names` to construct error `loc`s. Default is `True`.  
`revalidate_instances` |  |  Whether instances of models and dataclasses should re-validate. Default is 'never'.  
`validate_default` |  |  Whether to validate default values during validation. Default is `False`.  
`str_max_length` |  |  The maximum length for string fields.  
`str_min_length` |  |  The minimum length for string fields.  
`str_strip_whitespace` |  |  Whether to strip whitespace from string fields.  
`str_to_lower` |  |  Whether to convert string fields to lowercase.  
`str_to_upper` |  |  Whether to convert string fields to uppercase.  
`allow_inf_nan` |  |  Whether to allow infinity and NaN values for float fields. Default is `True`.  
`ser_json_timedelta` |  |  The serialization option for `timedelta` values. Default is 'iso8601'. Note that if ser_json_temporal is set, then this param will be ignored.  
`ser_json_temporal` |  |  The serialization option for datetime like values. Default is 'iso8601'. The types this covers are datetime, date, time and timedelta. If this is set, it will take precedence over ser_json_timedelta  
`ser_json_bytes` |  |  The serialization option for `bytes` values. Default is 'utf8'.  
`ser_json_inf_nan` |  |  The serialization option for infinity and NaN values in float fields. Default is 'null'.  
`val_json_bytes` |  |  The validation option for `bytes` values, complementing ser_json_bytes. Default is 'utf8'.  
`hide_input_in_errors` |  |  Whether to hide input data from `ValidationError` representation.  
`validation_error_cause` |  |  Whether to add user-python excs to the **cause** of a ValidationError. Requires exceptiongroup backport pre Python 3.11.  
`coerce_numbers_to_str` |  |  Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).  
`regex_engine` |  |  The regex engine to use for regex pattern validation. Default is 'rust-regex'. See `StringSchema`.  
`cache_strings` |  |  Whether to cache strings. Default is `True`, `True` or `'all'` is required to cache strings during general validation since validators don't know if they're in a key or a value.  
`validate_by_alias` |  |  Whether to use the field's alias when validating against the provided input data. Default is `True`.  
`validate_by_name` |  |  Whether to use the field's name when validating against the provided input data. Default is `False`. Replacement for `populate_by_name`.  
`serialize_by_alias` |  |  Whether to serialize by alias. Default is `False`, expected to change to `True` in V3.  
`url_preserve_empty_path` |  |  Whether to preserve empty URL paths when validating values for a URL type. Defaults to `False`.  
##  SerializationInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo)
Bases: `ContextT]`
Extra data used during serialization.
###  include `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.include)
```
include: IncExCall

```

The `include` argument set during serialization.
###  exclude `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.exclude)
```
exclude: IncExCall

```

The `exclude` argument set during serialization.
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.context)
```
context: ContextT

```

The current serialization context.
###  mode `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.mode)
```
mode: ['python', 'json'] | 
```

The serialization mode set during serialization.
###  by_alias `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.by_alias)
```
by_alias: 
```

The `by_alias` argument set during serialization.
###  exclude_unset `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.exclude_unset)
```
exclude_unset: 
```

The `exclude_unset` argument set during serialization.
###  exclude_defaults `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.exclude_defaults)
```
exclude_defaults: 
```

The `exclude_defaults` argument set during serialization.
###  exclude_none `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.exclude_none)
```
exclude_none: 
```

The `exclude_none` argument set during serialization.
###  exclude_computed_fields `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.exclude_computed_fields)
```
exclude_computed_fields: 
```

The `exclude_computed_fields` argument set during serialization.
###  serialize_as_any `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.serialize_as_any)
```
serialize_as_any: 
```

The `serialize_as_any` argument set during serialization.
###  round_trip `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo.round_trip)
```
round_trip: 
```

The `round_trip` argument set during serialization.
##  FieldSerializationInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.FieldSerializationInfo)
Bases: `SerializationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo)[ContextT]`, 
Extra data used during field serialization.
###  field_name `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.FieldSerializationInfo.field_name)
```
field_name: 
```

The name of the current field being serialized.
##  ValidationInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)
Bases: `ContextT]`
Extra data used during validation.
###  context `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.context)
```
context: ContextT

```

The current validation context.
###  config `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.config)
```
config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None

```

The CoreConfig that applies to this validation.
###  mode `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.mode)
```
mode: ['python', 'json']

```

The type of input data we are currently validating.
###  data `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.data)
```
data: [, ]

```

The data being validated for this model.
###  field_name `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo.field_name)
```
field_name: | None

```

The name of the current field being validated if this validator is attached to a model field.
##  simple_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.simple_ser_schema)
```
simple_ser_schema(
    type: ExpectedSerializationTypes,
) -> SimpleSerSchema

```

Returns a schema for serialization with a custom type.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`type` |  `ExpectedSerializationTypes` |  The type to use for serialization |  _required_  
Source code in `pydantic_core/core_schema.py`
```
267
268
269
270
271
272
273
274
```
| ```
defsimple_ser_schema(type: ExpectedSerializationTypes) -> SimpleSerSchema:
"""
    Returns a schema for serialization with a custom type.

    Args:
        type: The type to use for serialization
    """
    return SimpleSerSchema(type=type)

```
  
---|---  
##  plain_serializer_function_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.plain_serializer_function_ser_schema)
```
plain_serializer_function_ser_schema(
    function: SerializerFunction,
    *,
    is_field_serializer: | None = None,
    info_arg: | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always"
) -> PlainSerializerFunctionSerSchema

```

Returns a schema for serialization with a function, can be either a "general" or "field" function.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `SerializerFunction` |  The function to use for serialization |  _required_  
`is_field_serializer` |  |  Whether the serializer is for a field, e.g. takes `model` as the first argument, and `info` includes `field_name` |  `None`  
`info_arg` |  |  Whether the function takes an `info` argument |  `None`  
`return_schema` |  `CoreSchema | None` |  Schema to use for serializing return value |  `None`  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  When the function should be called |  `'always'`  
Source code in `pydantic_core/core_schema.py`
```
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
```
| ```
defplain_serializer_function_ser_schema(
    function: SerializerFunction,
    *,
    is_field_serializer: bool | None = None,
    info_arg: bool | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed = 'always',
) -> PlainSerializerFunctionSerSchema:
"""
    Returns a schema for serialization with a function, can be either a "general" or "field" function.

    Args:
        function: The function to use for serialization
        is_field_serializer: Whether the serializer is for a field, e.g. takes `model` as the first argument,
            and `info` includes `field_name`
        info_arg: Whether the function takes an `info` argument
        return_schema: Schema to use for serializing return value
        when_used: When the function should be called
    """
    if when_used == 'always':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        when_used = None  # type: ignore
    return _dict_not_none(
        type='function-plain',
        function=function,
        is_field_serializer=is_field_serializer,
        info_arg=info_arg,
        return_schema=return_schema,
        when_used=when_used,
    )

```
  
---|---  
##  wrap_serializer_function_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.wrap_serializer_function_ser_schema)
```
wrap_serializer_function_ser_schema(
    function: WrapSerializerFunction,
    *,
    is_field_serializer: | None = None,
    info_arg: | None = None,
    schema: CoreSchema | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always"
) -> WrapSerializerFunctionSerSchema

```

Returns a schema for serialization with a wrap function, can be either a "general" or "field" function.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `WrapSerializerFunction` |  The function to use for serialization |  _required_  
`is_field_serializer` |  |  Whether the serializer is for a field, e.g. takes `model` as the first argument, and `info` includes `field_name` |  `None`  
`info_arg` |  |  Whether the function takes an `info` argument |  `None`  
`schema` |  `CoreSchema | None` |  The schema to use for the inner serialization |  `None`  
`return_schema` |  `CoreSchema | None` |  Schema to use for serializing return value |  `None`  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  When the function should be called |  `'always'`  
Source code in `pydantic_core/core_schema.py`
```
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
```
| ```
defwrap_serializer_function_ser_schema(
    function: WrapSerializerFunction,
    *,
    is_field_serializer: bool | None = None,
    info_arg: bool | None = None,
    schema: CoreSchema | None = None,
    return_schema: CoreSchema | None = None,
    when_used: WhenUsed = 'always',
) -> WrapSerializerFunctionSerSchema:
"""
    Returns a schema for serialization with a wrap function, can be either a "general" or "field" function.

    Args:
        function: The function to use for serialization
        is_field_serializer: Whether the serializer is for a field, e.g. takes `model` as the first argument,
            and `info` includes `field_name`
        info_arg: Whether the function takes an `info` argument
        schema: The schema to use for the inner serialization
        return_schema: Schema to use for serializing return value
        when_used: When the function should be called
    """
    if when_used == 'always':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        when_used = None  # type: ignore
    return _dict_not_none(
        type='function-wrap',
        function=function,
        is_field_serializer=is_field_serializer,
        info_arg=info_arg,
        schema=schema,
        return_schema=return_schema,
        when_used=when_used,
    )

```
  
---|---  
##  format_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.format_ser_schema)
```
format_ser_schema(
    formatting_string: ,
    *,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "json-unless-none"
) -> FormatSerSchema

```

Returns a schema for serialization using python's `format` method.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`formatting_string` |  |  String defining the format to use |  _required_  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Same meaning as for [general_function_plain_ser_schema], but with a different default |  `'json-unless-none'`  
Source code in `pydantic_core/core_schema.py`
```
415
416
417
418
419
420
421
422
423
424
425
426
```
| ```
defformat_ser_schema(formatting_string: str, *, when_used: WhenUsed = 'json-unless-none') -> FormatSerSchema:
"""
    Returns a schema for serialization using python's `format` method.

    Args:
        formatting_string: String defining the format to use
        when_used: Same meaning as for [general_function_plain_ser_schema], but with a different default
    """
    if when_used == 'json-unless-none':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        when_used = None  # type: ignore
    return _dict_not_none(type='format', formatting_string=formatting_string, when_used=when_used)

```
  
---|---  
##  to_string_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.to_string_ser_schema)
```
to_string_ser_schema(
    *, when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "json-unless-none"
) -> ToStringSerSchema

```

Returns a schema for serialization using python's `str()` / `__str__` method.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Same meaning as for [general_function_plain_ser_schema], but with a different default |  `'json-unless-none'`  
Source code in `pydantic_core/core_schema.py`
```
434
435
436
437
438
439
440
441
442
443
444
445
```
| ```
defto_string_ser_schema(*, when_used: WhenUsed = 'json-unless-none') -> ToStringSerSchema:
"""
    Returns a schema for serialization using python's `str()` / `__str__` method.

    Args:
        when_used: Same meaning as for [general_function_plain_ser_schema], but with a different default
    """
    s = dict(type='to-string')
    if when_used != 'json-unless-none':
        # just to avoid extra elements in schema, and to use the actual default defined in rust
        s['when_used'] = when_used
    return s  # type: ignore

```
  
---|---  
##  model_ser_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_ser_schema)
```
model_ser_schema(
    cls: [], schema: CoreSchema
) -> ModelSerSchema

```

Returns a schema for serialization using a model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  |  The expected class type, used to generate warnings if the wrong type is passed |  _required_  
`schema` |  `CoreSchema` |  Internal schema to use to serialize the model dict |  _required_  
Source code in `pydantic_core/core_schema.py`
```
454
455
456
457
458
459
460
461
462
```
| ```
defmodel_ser_schema(cls: type[Any], schema: CoreSchema) -> ModelSerSchema:
"""
    Returns a schema for serialization using a model.

    Args:
        cls: The expected class type, used to generate warnings if the wrong type is passed
        schema: Internal schema to use to serialize the model dict
    """
    return ModelSerSchema(type='model', cls=cls, schema=schema)

```
  
---|---  
##  invalid_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.invalid_schema)
```
invalid_schema(
    ref: | None = None,
    metadata: [, ] | None = None,
) -> InvalidSchema

```

Returns an invalid schema, used to indicate that a schema is invalid.
```
Returns a schema that matches any value, e.g.:

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
Source code in `pydantic_core/core_schema.py`
```
484
485
486
487
488
489
490
491
492
493
494
495
```
| ```
definvalid_schema(ref: str | None = None, metadata: dict[str, Any] | None = None) -> InvalidSchema:
"""
    Returns an invalid schema, used to indicate that a schema is invalid.

        Returns a schema that matches any value, e.g.:

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """

    return _dict_not_none(type='invalid', ref=ref, metadata=metadata)

```
  
---|---  
##  computed_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.computed_field)
```
computed_field(
    property_name: ,
    return_schema: CoreSchema,
    *,
    alias: | None = None,
    metadata: [, ] | None = None
) -> ComputedField

```

ComputedFields are properties of a model or dataclass that are included in serialization.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`property_name` |  |  The name of the property on the model or dataclass |  _required_  
`return_schema` |  `CoreSchema` |  The schema used for the type returned by the computed field |  _required_  
`alias` |  |  The name to use in the serialized output |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
Source code in `pydantic_core/core_schema.py`
```
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
```
| ```
defcomputed_field(
    property_name: str, return_schema: CoreSchema, *, alias: str | None = None, metadata: dict[str, Any] | None = None
) -> ComputedField:
"""
    ComputedFields are properties of a model or dataclass that are included in serialization.

    Args:
        property_name: The name of the property on the model or dataclass
        return_schema: The schema used for the type returned by the computed field
        alias: The name to use in the serialized output
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """
    return _dict_not_none(
        type='computed-field', property_name=property_name, return_schema=return_schema, alias=alias, metadata=metadata
    )

```
  
---|---  
##  any_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.any_schema)
```
any_schema(
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> AnySchema

```

Returns a schema that matches any value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.any_schema()
v = SchemaValidator(schema)
assert v.validate_python(1) == 1

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
```
| ```
defany_schema(
    *, ref: str | None = None, metadata: dict[str, Any] | None = None, serialization: SerSchema | None = None
) -> AnySchema:
"""
    Returns a schema that matches any value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.any_schema()
    v = SchemaValidator(schema)
    assert v.validate_python(1) == 1
```

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='any', ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  none_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.none_schema)
```
none_schema(
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> NoneSchema

```

Returns a schema that matches a None value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.none_schema()
v = SchemaValidator(schema)
assert v.validate_python(None) is None

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
```
| ```
defnone_schema(
    *, ref: str | None = None, metadata: dict[str, Any] | None = None, serialization: SerSchema | None = None
) -> NoneSchema:
"""
    Returns a schema that matches a None value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.none_schema()
    v = SchemaValidator(schema)
    assert v.validate_python(None) is None
```

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='none', ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  bool_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.bool_schema)
```
bool_schema(
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
) -> BoolSchema

```

Returns a schema that matches a bool value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.bool_schema()
v = SchemaValidator(schema)
assert v.validate_python('True') is True

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether the value should be a bool or a value that can be converted to a bool |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
```
| ```
defbool_schema(
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BoolSchema:
"""
    Returns a schema that matches a bool value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.bool_schema()
    v = SchemaValidator(schema)
    assert v.validate_python('True') is True
```

    Args:
        strict: Whether the value should be a bool or a value that can be converted to a bool
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='bool', strict=strict, ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  int_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.int_schema)
```
int_schema(
    *,
    multiple_of: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> IntSchema

```

Returns a schema that matches a int value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.int_schema(multiple_of=2, le=6, ge=2)
v = SchemaValidator(schema)
assert v.validate_python('4') == 4

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`multiple_of` |  |  The value must be a multiple of this number |  `None`  
`le` |  |  The value must be less than or equal to this number |  `None`  
`ge` |  |  The value must be greater than or equal to this number |  `None`  
`lt` |  |  The value must be strictly less than this number |  `None`  
`gt` |  |  The value must be strictly greater than this number |  `None`  
`strict` |  |  Whether the value should be a int or a value that can be converted to a int |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
```
| ```
defint_schema(
    *,
    multiple_of: int | None = None,
    le: int | None = None,
    ge: int | None = None,
    lt: int | None = None,
    gt: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> IntSchema:
"""
    Returns a schema that matches a int value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.int_schema(multiple_of=2, le=6, ge=2)
    v = SchemaValidator(schema)
    assert v.validate_python('4') == 4
```

    Args:
        multiple_of: The value must be a multiple of this number
        le: The value must be less than or equal to this number
        ge: The value must be greater than or equal to this number
        lt: The value must be strictly less than this number
        gt: The value must be strictly greater than this number
        strict: Whether the value should be a int or a value that can be converted to a int
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='int',
        multiple_of=multiple_of,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  float_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.float_schema)
```
float_schema(
    *,
    allow_inf_nan: | None = None,
    multiple_of: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> FloatSchema

```

Returns a schema that matches a float value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.float_schema(le=0.8, ge=0.2)
v = SchemaValidator(schema)
assert v.validate_python('0.5') == 0.5

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`allow_inf_nan` |  |  Whether to allow inf and nan values |  `None`  
`multiple_of` |  |  The value must be a multiple of this number |  `None`  
`le` |  |  The value must be less than or equal to this number |  `None`  
`ge` |  |  The value must be greater than or equal to this number |  `None`  
`lt` |  |  The value must be strictly less than this number |  `None`  
`gt` |  |  The value must be strictly greater than this number |  `None`  
`strict` |  |  Whether the value should be a float or a value that can be converted to a float |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
```
| ```
deffloat_schema(
    *,
    allow_inf_nan: bool | None = None,
    multiple_of: float | None = None,
    le: float | None = None,
    ge: float | None = None,
    lt: float | None = None,
    gt: float | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> FloatSchema:
"""
    Returns a schema that matches a float value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.float_schema(le=0.8, ge=0.2)
    v = SchemaValidator(schema)
    assert v.validate_python('0.5') == 0.5
```

    Args:
        allow_inf_nan: Whether to allow inf and nan values
        multiple_of: The value must be a multiple of this number
        le: The value must be less than or equal to this number
        ge: The value must be greater than or equal to this number
        lt: The value must be strictly less than this number
        gt: The value must be strictly greater than this number
        strict: Whether the value should be a float or a value that can be converted to a float
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='float',
        allow_inf_nan=allow_inf_nan,
        multiple_of=multiple_of,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  decimal_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.decimal_schema)
```
decimal_schema(
    *,
    allow_inf_nan: | None = None,
    multiple_of: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    max_digits: | None = None,
    decimal_places: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DecimalSchema

```

Returns a schema that matches a decimal value, e.g.:
```
fromdecimalimport Decimal
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.decimal_schema(le=0.8, ge=0.2)
v = SchemaValidator(schema)
assert v.validate_python('0.5') == Decimal('0.5')

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`allow_inf_nan` |  |  Whether to allow inf and nan values |  `None`  
`multiple_of` |  |  The value must be a multiple of this number |  `None`  
`le` |  |  The value must be less than or equal to this number |  `None`  
`ge` |  |  The value must be greater than or equal to this number |  `None`  
`lt` |  |  The value must be strictly less than this number |  `None`  
`gt` |  |  The value must be strictly greater than this number |  `None`  
`max_digits` |  |  The maximum number of decimal digits allowed |  `None`  
`decimal_places` |  |  The maximum number of decimal places allowed |  `None`  
`strict` |  |  Whether the value should be a float or a value that can be converted to a float |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
```
| ```
defdecimal_schema(
    *,
    allow_inf_nan: bool | None = None,
    multiple_of: Decimal | None = None,
    le: Decimal | None = None,
    ge: Decimal | None = None,
    lt: Decimal | None = None,
    gt: Decimal | None = None,
    max_digits: int | None = None,
    decimal_places: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DecimalSchema:
"""
    Returns a schema that matches a decimal value, e.g.:

```py
    from decimal import Decimal
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.decimal_schema(le=0.8, ge=0.2)
    v = SchemaValidator(schema)
    assert v.validate_python('0.5') == Decimal('0.5')
```

    Args:
        allow_inf_nan: Whether to allow inf and nan values
        multiple_of: The value must be a multiple of this number
        le: The value must be less than or equal to this number
        ge: The value must be greater than or equal to this number
        lt: The value must be strictly less than this number
        gt: The value must be strictly greater than this number
        max_digits: The maximum number of decimal digits allowed
        decimal_places: The maximum number of decimal places allowed
        strict: Whether the value should be a float or a value that can be converted to a float
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='decimal',
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        max_digits=max_digits,
        decimal_places=decimal_places,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  complex_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.complex_schema)
```
complex_schema(
    *,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ComplexSchema

```

Returns a schema that matches a complex value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.complex_schema()
v = SchemaValidator(schema)
assert v.validate_python('1+2j') == complex(1, 2)
assert v.validate_python(complex(1, 2)) == complex(1, 2)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether the value should be a complex object instance or a value that can be converted to a complex object |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
```
| ```
defcomplex_schema(
    *,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ComplexSchema:
"""
    Returns a schema that matches a complex value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.complex_schema()
    v = SchemaValidator(schema)
    assert v.validate_python('1+2j') == complex(1, 2)
    assert v.validate_python(complex(1, 2)) == complex(1, 2)
```

    Args:
        strict: Whether the value should be a complex object instance or a value that can be converted to a complex object
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='complex',
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  str_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.str_schema)
```
str_schema(
    *,
    pattern: | [] | None = None,
    max_length: | None = None,
    min_length: | None = None,
    strip_whitespace: | None = None,
    to_lower: | None = None,
    to_upper: | None = None,
    regex_engine: (
        ["rust-regex", "python-re"] | None
    ) = None,
    strict: | None = None,
    coerce_numbers_to_str: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> StringSchema

```

Returns a schema that matches a string value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.str_schema(max_length=10, min_length=2)
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`pattern` |  |  A regex pattern that the value must match |  `None`  
`max_length` |  |  The value must be at most this length |  `None`  
`min_length` |  |  The value must be at least this length |  `None`  
`strip_whitespace` |  |  Whether to strip whitespace from the value |  `None`  
`to_lower` |  |  Whether to convert the value to lowercase |  `None`  
`to_upper` |  |  Whether to convert the value to uppercase |  `None`  
`regex_engine` |  |  The regex engine to use for pattern validation. Default is 'rust-regex'. - `rust-regex` uses the `python-re` use the  |  `None`  
`strict` |  |  Whether the value should be a string or a value that can be converted to a string |  `None`  
`coerce_numbers_to_str` |  |  Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode). |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
```
| ```
defstr_schema(
    *,
    pattern: str | Pattern[str] | None = None,
    max_length: int | None = None,
    min_length: int | None = None,
    strip_whitespace: bool | None = None,
    to_lower: bool | None = None,
    to_upper: bool | None = None,
    regex_engine: Literal['rust-regex', 'python-re'] | None = None,
    strict: bool | None = None,
    coerce_numbers_to_str: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> StringSchema:
"""
    Returns a schema that matches a string value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.str_schema(max_length=10, min_length=2)
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello'
```

    Args:
        pattern: A regex pattern that the value must match
        max_length: The value must be at most this length
        min_length: The value must be at least this length
        strip_whitespace: Whether to strip whitespace from the value
        to_lower: Whether to convert the value to lowercase
        to_upper: Whether to convert the value to uppercase
        regex_engine: The regex engine to use for pattern validation. Default is 'rust-regex'.
            - `rust-regex` uses the [`regex`](https://docs.rs/regex) Rust
              crate, which is non-backtracking and therefore more DDoS
              resistant, but does not support all regex features.
            - `python-re` use the [`re`](https://docs.python.org/3/library/re.html) module,
              which supports all regex features, but may be slower.
        strict: Whether the value should be a string or a value that can be converted to a string
        coerce_numbers_to_str: Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='str',
        pattern=pattern,
        max_length=max_length,
        min_length=min_length,
        strip_whitespace=strip_whitespace,
        to_lower=to_lower,
        to_upper=to_upper,
        regex_engine=regex_engine,
        strict=strict,
        coerce_numbers_to_str=coerce_numbers_to_str,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  bytes_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.bytes_schema)
```
bytes_schema(
    *,
    max_length: | None = None,
    min_length: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> BytesSchema

```

Returns a schema that matches a bytes value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.bytes_schema(max_length=10, min_length=2)
v = SchemaValidator(schema)
assert v.validate_python(b'hello') == b'hello'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`max_length` |  |  The value must be at most this length |  `None`  
`min_length` |  |  The value must be at least this length |  `None`  
`strict` |  |  Whether the value should be a bytes or a value that can be converted to a bytes |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
```
| ```
defbytes_schema(
    *,
    max_length: int | None = None,
    min_length: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BytesSchema:
"""
    Returns a schema that matches a bytes value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.bytes_schema(max_length=10, min_length=2)
    v = SchemaValidator(schema)
    assert v.validate_python(b'hello') == b'hello'
```

    Args:
        max_length: The value must be at most this length
        min_length: The value must be at least this length
        strict: Whether the value should be a bytes or a value that can be converted to a bytes
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='bytes',
        max_length=max_length,
        min_length=min_length,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  date_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.date_schema)
```
date_schema(
    *,
    strict: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    now_op: ["past", "future"] | None = None,
    now_utc_offset: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DateSchema

```

Returns a schema that matches a date value, e.g.:
```
fromdatetimeimport date
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.date_schema(le=date(2020, 1, 1), ge=date(2019, 1, 1))
v = SchemaValidator(schema)
assert v.validate_python(date(2019, 6, 1)) == date(2019, 6, 1)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether the value should be a date or a value that can be converted to a date |  `None`  
`le` |  |  The value must be less than or equal to this date |  `None`  
`ge` |  |  The value must be greater than or equal to this date |  `None`  
`lt` |  |  The value must be strictly less than this date |  `None`  
`gt` |  |  The value must be strictly greater than this date |  `None`  
`now_op` |  |  The value must be in the past or future relative to the current date |  `None`  
`now_utc_offset` |  |  The value must be in the past or future relative to the current date with this utc offset |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
```
| ```
defdate_schema(
    *,
    strict: bool | None = None,
    le: date | None = None,
    ge: date | None = None,
    lt: date | None = None,
    gt: date | None = None,
    now_op: Literal['past', 'future'] | None = None,
    now_utc_offset: int | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DateSchema:
"""
    Returns a schema that matches a date value, e.g.:

```py
    from datetime import date
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.date_schema(le=date(2020, 1, 1), ge=date(2019, 1, 1))
    v = SchemaValidator(schema)
    assert v.validate_python(date(2019, 6, 1)) == date(2019, 6, 1)
```

    Args:
        strict: Whether the value should be a date or a value that can be converted to a date
        le: The value must be less than or equal to this date
        ge: The value must be greater than or equal to this date
        lt: The value must be strictly less than this date
        gt: The value must be strictly greater than this date
        now_op: The value must be in the past or future relative to the current date
        now_utc_offset: The value must be in the past or future relative to the current date with this utc offset
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='date',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        now_op=now_op,
        now_utc_offset=now_utc_offset,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  time_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.time_schema)
```
time_schema(
    *,
    strict: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    tz_constraint: (
        ["aware", "naive"] | | None
    ) = None,
    microseconds_precision: [
        "truncate", "error"
    ] = "truncate",
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> TimeSchema

```

Returns a schema that matches a time value, e.g.:
```
fromdatetimeimport time
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.time_schema(le=time(12, 0, 0), ge=time(6, 0, 0))
v = SchemaValidator(schema)
assert v.validate_python(time(9, 0, 0)) == time(9, 0, 0)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether the value should be a time or a value that can be converted to a time |  `None`  
`le` |  |  The value must be less than or equal to this time |  `None`  
`ge` |  |  The value must be greater than or equal to this time |  `None`  
`lt` |  |  The value must be strictly less than this time |  `None`  
`gt` |  |  The value must be strictly greater than this time |  `None`  
`tz_constraint` |  |  The value must be timezone aware or naive, or an int to indicate required tz offset |  `None`  
`microseconds_precision` |  |  The behavior when seconds have more than 6 digits or microseconds is too large |  `'truncate'`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
```
| ```
deftime_schema(
    *,
    strict: bool | None = None,
    le: time | None = None,
    ge: time | None = None,
    lt: time | None = None,
    gt: time | None = None,
    tz_constraint: Literal['aware', 'naive'] | int | None = None,
    microseconds_precision: Literal['truncate', 'error'] = 'truncate',
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> TimeSchema:
"""
    Returns a schema that matches a time value, e.g.:

```py
    from datetime import time
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.time_schema(le=time(12, 0, 0), ge=time(6, 0, 0))
    v = SchemaValidator(schema)
    assert v.validate_python(time(9, 0, 0)) == time(9, 0, 0)
```

    Args:
        strict: Whether the value should be a time or a value that can be converted to a time
        le: The value must be less than or equal to this time
        ge: The value must be greater than or equal to this time
        lt: The value must be strictly less than this time
        gt: The value must be strictly greater than this time
        tz_constraint: The value must be timezone aware or naive, or an int to indicate required tz offset
        microseconds_precision: The behavior when seconds have more than 6 digits or microseconds is too large
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='time',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        tz_constraint=tz_constraint,
        microseconds_precision=microseconds_precision,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  datetime_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.datetime_schema)
```
datetime_schema(
    *,
    strict: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    now_op: ["past", "future"] | None = None,
    tz_constraint: (
        ["aware", "naive"] | | None
    ) = None,
    now_utc_offset: | None = None,
    microseconds_precision: [
        "truncate", "error"
    ] = "truncate",
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DatetimeSchema

```

Returns a schema that matches a datetime value, e.g.:
```
fromdatetimeimport datetime
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.datetime_schema()
v = SchemaValidator(schema)
now = datetime.now()
assert v.validate_python(str(now)) == now

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether the value should be a datetime or a value that can be converted to a datetime |  `None`  
`le` |  |  The value must be less than or equal to this datetime |  `None`  
`ge` |  |  The value must be greater than or equal to this datetime |  `None`  
`lt` |  |  The value must be strictly less than this datetime |  `None`  
`gt` |  |  The value must be strictly greater than this datetime |  `None`  
`now_op` |  |  The value must be in the past or future relative to the current datetime |  `None`  
`tz_constraint` |  |  The value must be timezone aware or naive, or an int to indicate required tz offset TODO: use of a tzinfo where offset changes based on the datetime is not yet supported |  `None`  
`now_utc_offset` |  |  The value must be in the past or future relative to the current datetime with this utc offset |  `None`  
`microseconds_precision` |  |  The behavior when seconds have more than 6 digits or microseconds is too large |  `'truncate'`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
```
| ```
defdatetime_schema(
    *,
    strict: bool | None = None,
    le: datetime | None = None,
    ge: datetime | None = None,
    lt: datetime | None = None,
    gt: datetime | None = None,
    now_op: Literal['past', 'future'] | None = None,
    tz_constraint: Literal['aware', 'naive'] | int | None = None,
    now_utc_offset: int | None = None,
    microseconds_precision: Literal['truncate', 'error'] = 'truncate',
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DatetimeSchema:
"""
    Returns a schema that matches a datetime value, e.g.:

```py
    from datetime import datetime
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.datetime_schema()
    v = SchemaValidator(schema)
    now = datetime.now()
    assert v.validate_python(str(now)) == now
```

    Args:
        strict: Whether the value should be a datetime or a value that can be converted to a datetime
        le: The value must be less than or equal to this datetime
        ge: The value must be greater than or equal to this datetime
        lt: The value must be strictly less than this datetime
        gt: The value must be strictly greater than this datetime
        now_op: The value must be in the past or future relative to the current datetime
        tz_constraint: The value must be timezone aware or naive, or an int to indicate required tz offset
            TODO: use of a tzinfo where offset changes based on the datetime is not yet supported
        now_utc_offset: The value must be in the past or future relative to the current datetime with this utc offset
        microseconds_precision: The behavior when seconds have more than 6 digits or microseconds is too large
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='datetime',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        now_op=now_op,
        tz_constraint=tz_constraint,
        now_utc_offset=now_utc_offset,
        microseconds_precision=microseconds_precision,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  timedelta_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.timedelta_schema)
```
timedelta_schema(
    *,
    strict: | None = None,
    le: | None = None,
    ge: | None = None,
    lt: | None = None,
    gt: | None = None,
    microseconds_precision: [
        "truncate", "error"
    ] = "truncate",
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> TimedeltaSchema

```

Returns a schema that matches a timedelta value, e.g.:
```
fromdatetimeimport timedelta
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.timedelta_schema(le=timedelta(days=1), ge=timedelta(days=0))
v = SchemaValidator(schema)
assert v.validate_python(timedelta(hours=12)) == timedelta(hours=12)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether the value should be a timedelta or a value that can be converted to a timedelta |  `None`  
`le` |  |  The value must be less than or equal to this timedelta |  `None`  
`ge` |  |  The value must be greater than or equal to this timedelta |  `None`  
`lt` |  |  The value must be strictly less than this timedelta |  `None`  
`gt` |  |  The value must be strictly greater than this timedelta |  `None`  
`microseconds_precision` |  |  The behavior when seconds have more than 6 digits or microseconds is too large |  `'truncate'`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
```
| ```
deftimedelta_schema(
    *,
    strict: bool | None = None,
    le: timedelta | None = None,
    ge: timedelta | None = None,
    lt: timedelta | None = None,
    gt: timedelta | None = None,
    microseconds_precision: Literal['truncate', 'error'] = 'truncate',
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> TimedeltaSchema:
"""
    Returns a schema that matches a timedelta value, e.g.:

```py
    from datetime import timedelta
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.timedelta_schema(le=timedelta(days=1), ge=timedelta(days=0))
    v = SchemaValidator(schema)
    assert v.validate_python(timedelta(hours=12)) == timedelta(hours=12)
```

    Args:
        strict: Whether the value should be a timedelta or a value that can be converted to a timedelta
        le: The value must be less than or equal to this timedelta
        ge: The value must be greater than or equal to this timedelta
        lt: The value must be strictly less than this timedelta
        gt: The value must be strictly greater than this timedelta
        microseconds_precision: The behavior when seconds have more than 6 digits or microseconds is too large
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='timedelta',
        strict=strict,
        le=le,
        ge=ge,
        lt=lt,
        gt=gt,
        microseconds_precision=microseconds_precision,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  literal_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.literal_schema)
```
literal_schema(
    expected: [],
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> LiteralSchema

```

Returns a schema that matches a literal value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.literal_schema(['hello', 'world'])
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`expected` |  |  The value must be one of these values |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
```
| ```
defliteral_schema(
    expected: list[Any],
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> LiteralSchema:
"""
    Returns a schema that matches a literal value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.literal_schema(['hello', 'world'])
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello'
```

    Args:
        expected: The value must be one of these values
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='literal', expected=expected, ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  enum_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.enum_schema)
```
enum_schema(
    cls: ,
    members: [],
    *,
    sub_type: ["str", "int", "float"] | None = None,
    missing: [[], ] | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> EnumSchema

```

Returns a schema that matches an enum value, e.g.:
```
fromenumimport Enum
frompydantic_coreimport SchemaValidator, core_schema

classColor(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

schema = core_schema.enum_schema(Color, list(Color.__members__.values()))
v = SchemaValidator(schema)
assert v.validate_python(2) is Color.GREEN

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  |  The enum class |  _required_  
`members` |  |  The members of the enum, generally `list(MyEnum.__members__.values())` |  _required_  
`sub_type` |  |  The type of the enum, either 'str' or 'int' or None for plain enums |  `None`  
`missing` |  |  A function to use when the value is not found in the enum, from `_missing_` |  `None`  
`strict` |  |  Whether to use strict mode, defaults to False |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
```
| ```
defenum_schema(
    cls: Any,
    members: list[Any],
    *,
    sub_type: Literal['str', 'int', 'float'] | None = None,
    missing: Callable[[Any], Any] | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> EnumSchema:
"""
    Returns a schema that matches an enum value, e.g.:

```py
    from enum import Enum
    from pydantic_core import SchemaValidator, core_schema

    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    schema = core_schema.enum_schema(Color, list(Color.__members__.values()))
    v = SchemaValidator(schema)
    assert v.validate_python(2) is Color.GREEN
```

    Args:
        cls: The enum class
        members: The members of the enum, generally `list(MyEnum.__members__.values())`
        sub_type: The type of the enum, either 'str' or 'int' or None for plain enums
        missing: A function to use when the value is not found in the enum, from `_missing_`
        strict: Whether to use strict mode, defaults to False
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='enum',
        cls=cls,
        members=members,
        sub_type=sub_type,
        missing=missing,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  missing_sentinel_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.missing_sentinel_schema)
```
missing_sentinel_schema(
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
) -> MissingSentinelSchema

```

Returns a schema for the `MISSING` sentinel.
Source code in `pydantic_core/core_schema.py`
```
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
```
| ```
defmissing_sentinel_schema(
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> MissingSentinelSchema:
"""Returns a schema for the `MISSING` sentinel."""

    return _dict_not_none(
        type='missing-sentinel',
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  is_instance_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.is_instance_schema)
```
is_instance_schema(
    cls: ,
    *,
    cls_repr: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> IsInstanceSchema

```

Returns a schema that checks if a value is an instance of a class, equivalent to python's `isinstance` method, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

classA:
    pass

schema = core_schema.is_instance_schema(cls=A)
v = SchemaValidator(schema)
v.validate_python(A())

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  |  The value must be an instance of this class |  _required_  
`cls_repr` |  |  If provided this string is used in the validator name instead of `repr(cls)` |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
```
| ```
defis_instance_schema(
    cls: Any,
    *,
    cls_repr: str | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> IsInstanceSchema:
"""
    Returns a schema that checks if a value is an instance of a class, equivalent to python's `isinstance` method, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    class A:
        pass

    schema = core_schema.is_instance_schema(cls=A)
    v = SchemaValidator(schema)
    v.validate_python(A())
```

    Args:
        cls: The value must be an instance of this class
        cls_repr: If provided this string is used in the validator name instead of `repr(cls)`
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='is-instance', cls=cls, cls_repr=cls_repr, ref=ref, metadata=metadata, serialization=serialization
    )

```
  
---|---  
##  is_subclass_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.is_subclass_schema)
```
is_subclass_schema(
    cls: [],
    *,
    cls_repr: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> IsInstanceSchema

```

Returns a schema that checks if a value is a subtype of a class, equivalent to python's `issubclass` method, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

classA:
    pass

classB(A):
    pass

schema = core_schema.is_subclass_schema(cls=A)
v = SchemaValidator(schema)
v.validate_python(B)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  |  The value must be a subclass of this class |  _required_  
`cls_repr` |  |  If provided this string is used in the validator name instead of `repr(cls)` |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
```
| ```
defis_subclass_schema(
    cls: type[Any],
    *,
    cls_repr: str | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> IsInstanceSchema:
"""
    Returns a schema that checks if a value is a subtype of a class, equivalent to python's `issubclass` method, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    class A:
        pass

    class B(A):
        pass

    schema = core_schema.is_subclass_schema(cls=A)
    v = SchemaValidator(schema)
    v.validate_python(B)
```

    Args:
        cls: The value must be a subclass of this class
        cls_repr: If provided this string is used in the validator name instead of `repr(cls)`
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='is-subclass', cls=cls, cls_repr=cls_repr, ref=ref, metadata=metadata, serialization=serialization
    )

```
  
---|---  
##  callable_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.callable_schema)
```
callable_schema(
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> CallableSchema

```

Returns a schema that checks if a value is callable, equivalent to python's `callable` method, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.callable_schema()
v = SchemaValidator(schema)
v.validate_python(min)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
```
| ```
defcallable_schema(
    *, ref: str | None = None, metadata: dict[str, Any] | None = None, serialization: SerSchema | None = None
) -> CallableSchema:
"""
    Returns a schema that checks if a value is callable, equivalent to python's `callable` method, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.callable_schema()
    v = SchemaValidator(schema)
    v.validate_python(min)
```

    Args:
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='callable', ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  list_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.list_schema)
```
list_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: | None = None,
    max_length: | None = None,
    fail_fast: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> ListSchema

```

Returns a schema that matches a list value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.list_schema(core_schema.int_schema(), min_length=0, max_length=10)
v = SchemaValidator(schema)
assert v.validate_python(['4']) == [4]

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema | None` |  The value must be a list of items that match this schema |  `None`  
`min_length` |  |  The value must be a list with at least this many items |  `None`  
`max_length` |  |  The value must be a list with at most this many items |  `None`  
`fail_fast` |  |  Stop validation on the first error |  `None`  
`strict` |  |  The value must be a list with exactly this many items |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
```
| ```
deflist_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> ListSchema:
"""
    Returns a schema that matches a list value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.list_schema(core_schema.int_schema(), min_length=0, max_length=10)
    v = SchemaValidator(schema)
    assert v.validate_python(['4']) == [4]
```

    Args:
        items_schema: The value must be a list of items that match this schema
        min_length: The value must be a list with at least this many items
        max_length: The value must be a list with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a list with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='list',
        items_schema=items_schema,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  tuple_positional_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tuple_positional_schema)
```
tuple_positional_schema(
    items_schema: [CoreSchema],
    *,
    extras_schema: CoreSchema | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> TupleSchema

```

Returns a schema that matches a tuple of schemas, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.tuple_positional_schema(
    [core_schema.int_schema(), core_schema.str_schema()]
)
v = SchemaValidator(schema)
assert v.validate_python((1, 'hello')) == (1, 'hello')

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema]` |  The value must be a tuple with items that match these schemas |  _required_  
`extras_schema` |  `CoreSchema | None` |  The value must be a tuple with items that match this schema This was inspired by JSON schema's `prefixItems` and `items` fields. In python's `typing.Tuple`, you can't specify a type for "extra" items -- they must all be the same type if the length is variable. So this field won't be set from a `typing.Tuple` annotation on a pydantic model. |  `None`  
`strict` |  |  The value must be a tuple with exactly this many items |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
```
| ```
deftuple_positional_schema(
    items_schema: list[CoreSchema],
    *,
    extras_schema: CoreSchema | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> TupleSchema:
"""
    Returns a schema that matches a tuple of schemas, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.tuple_positional_schema(
        [core_schema.int_schema(), core_schema.str_schema()]
    )
    v = SchemaValidator(schema)
    assert v.validate_python((1, 'hello')) == (1, 'hello')
```

    Args:
        items_schema: The value must be a tuple with items that match these schemas
        extras_schema: The value must be a tuple with items that match this schema
            This was inspired by JSON schema's `prefixItems` and `items` fields.
            In python's `typing.Tuple`, you can't specify a type for "extra" items -- they must all be the same type
            if the length is variable. So this field won't be set from a `typing.Tuple` annotation on a pydantic model.
        strict: The value must be a tuple with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if extras_schema is not None:
        variadic_item_index = len(items_schema)
        items_schema = items_schema + [extras_schema]
    else:
        variadic_item_index = None
    return tuple_schema(
        items_schema=items_schema,
        variadic_item_index=variadic_item_index,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  tuple_variable_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tuple_variable_schema)
```
tuple_variable_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: | None = None,
    max_length: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> TupleSchema

```

Returns a schema that matches a tuple of a given schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.tuple_variable_schema(
    items_schema=core_schema.int_schema(), min_length=0, max_length=10
)
v = SchemaValidator(schema)
assert v.validate_python(('1', 2, 3)) == (1, 2, 3)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema | None` |  The value must be a tuple with items that match this schema |  `None`  
`min_length` |  |  The value must be a tuple with at least this many items |  `None`  
`max_length` |  |  The value must be a tuple with at most this many items |  `None`  
`strict` |  |  The value must be a tuple with exactly this many items |  `None`  
`ref` |  |  Optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
```
| ```
deftuple_variable_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> TupleSchema:
"""
    Returns a schema that matches a tuple of a given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.tuple_variable_schema(
        items_schema=core_schema.int_schema(), min_length=0, max_length=10
    )
    v = SchemaValidator(schema)
    assert v.validate_python(('1', 2, 3)) == (1, 2, 3)
```

    Args:
        items_schema: The value must be a tuple with items that match this schema
        min_length: The value must be a tuple with at least this many items
        max_length: The value must be a tuple with at most this many items
        strict: The value must be a tuple with exactly this many items
        ref: Optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return tuple_schema(
        items_schema=[items_schema or any_schema()],
        variadic_item_index=0,
        min_length=min_length,
        max_length=max_length,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  tuple_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tuple_schema)
```
tuple_schema(
    items_schema: [CoreSchema],
    *,
    variadic_item_index: | None = None,
    min_length: | None = None,
    max_length: | None = None,
    fail_fast: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> TupleSchema

```

Returns a schema that matches a tuple of schemas, with an optional variadic item, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.tuple_schema(
    [core_schema.int_schema(), core_schema.str_schema(), core_schema.float_schema()],
    variadic_item_index=1,
)
v = SchemaValidator(schema)
assert v.validate_python((1, 'hello', 'world', 1.5)) == (1, 'hello', 'world', 1.5)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema]` |  The value must be a tuple with items that match these schemas |  _required_  
`variadic_item_index` |  |  The index of the schema in `items_schema` to be treated as variadic (following PEP 646) |  `None`  
`min_length` |  |  The value must be a tuple with at least this many items |  `None`  
`max_length` |  |  The value must be a tuple with at most this many items |  `None`  
`fail_fast` |  |  Stop validation on the first error |  `None`  
`strict` |  |  The value must be a tuple with exactly this many items |  `None`  
`ref` |  |  Optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
```
| ```
deftuple_schema(
    items_schema: list[CoreSchema],
    *,
    variadic_item_index: int | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> TupleSchema:
"""
    Returns a schema that matches a tuple of schemas, with an optional variadic item, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.tuple_schema(
        [core_schema.int_schema(), core_schema.str_schema(), core_schema.float_schema()],
        variadic_item_index=1,
    )
    v = SchemaValidator(schema)
    assert v.validate_python((1, 'hello', 'world', 1.5)) == (1, 'hello', 'world', 1.5)
```

    Args:
        items_schema: The value must be a tuple with items that match these schemas
        variadic_item_index: The index of the schema in `items_schema` to be treated as variadic (following PEP 646)
        min_length: The value must be a tuple with at least this many items
        max_length: The value must be a tuple with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a tuple with exactly this many items
        ref: Optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='tuple',
        items_schema=items_schema,
        variadic_item_index=variadic_item_index,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  set_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.set_schema)
```
set_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: | None = None,
    max_length: | None = None,
    fail_fast: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> SetSchema

```

Returns a schema that matches a set of a given schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.set_schema(
    items_schema=core_schema.int_schema(), min_length=0, max_length=10
)
v = SchemaValidator(schema)
assert v.validate_python({1, '2', 3}) == {1, 2, 3}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema | None` |  The value must be a set with items that match this schema |  `None`  
`min_length` |  |  The value must be a set with at least this many items |  `None`  
`max_length` |  |  The value must be a set with at most this many items |  `None`  
`fail_fast` |  |  Stop validation on the first error |  `None`  
`strict` |  |  The value must be a set with exactly this many items |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
```
| ```
defset_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> SetSchema:
"""
    Returns a schema that matches a set of a given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.set_schema(
        items_schema=core_schema.int_schema(), min_length=0, max_length=10
    )
    v = SchemaValidator(schema)
    assert v.validate_python({1, '2', 3}) == {1, 2, 3}
```

    Args:
        items_schema: The value must be a set with items that match this schema
        min_length: The value must be a set with at least this many items
        max_length: The value must be a set with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a set with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='set',
        items_schema=items_schema,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  frozenset_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.frozenset_schema)
```
frozenset_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: | None = None,
    max_length: | None = None,
    fail_fast: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> FrozenSetSchema

```

Returns a schema that matches a frozenset of a given schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.frozenset_schema(
    items_schema=core_schema.int_schema(), min_length=0, max_length=10
)
v = SchemaValidator(schema)
assert v.validate_python(frozenset(range(3))) == frozenset({0, 1, 2})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema | None` |  The value must be a frozenset with items that match this schema |  `None`  
`min_length` |  |  The value must be a frozenset with at least this many items |  `None`  
`max_length` |  |  The value must be a frozenset with at most this many items |  `None`  
`fail_fast` |  |  Stop validation on the first error |  `None`  
`strict` |  |  The value must be a frozenset with exactly this many items |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
```
| ```
deffrozenset_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> FrozenSetSchema:
"""
    Returns a schema that matches a frozenset of a given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.frozenset_schema(
        items_schema=core_schema.int_schema(), min_length=0, max_length=10
    )
    v = SchemaValidator(schema)
    assert v.validate_python(frozenset(range(3))) == frozenset({0, 1, 2})
```

    Args:
        items_schema: The value must be a frozenset with items that match this schema
        min_length: The value must be a frozenset with at least this many items
        max_length: The value must be a frozenset with at most this many items
        fail_fast: Stop validation on the first error
        strict: The value must be a frozenset with exactly this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='frozenset',
        items_schema=items_schema,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  generator_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.generator_schema)
```
generator_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: | None = None,
    max_length: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None
) -> GeneratorSchema

```

Returns a schema that matches a generator value, e.g.:
```
fromtypingimport Iterator
frompydantic_coreimport SchemaValidator, core_schema

defgen() -> Iterator[int]:
    yield 1

schema = core_schema.generator_schema(items_schema=core_schema.int_schema())
v = SchemaValidator(schema)
v.validate_python(gen())

```

Unlike other types, validated generators do not raise ValidationErrors eagerly, but instead will raise a ValidationError when a violating value is actually read from the generator. This is to ensure that "validated" generators retain the benefit of lazy evaluation.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`items_schema` |  `CoreSchema | None` |  The value must be a generator with items that match this schema |  `None`  
`min_length` |  |  The value must be a generator that yields at least this many items |  `None`  
`max_length` |  |  The value must be a generator that yields at most this many items |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `IncExSeqOrElseSerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
```
| ```
defgenerator_schema(
    items_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: IncExSeqOrElseSerSchema | None = None,
) -> GeneratorSchema:
"""
    Returns a schema that matches a generator value, e.g.:

```py
    from typing import Iterator
    from pydantic_core import SchemaValidator, core_schema

    def gen() -> Iterator[int]:
        yield 1

    schema = core_schema.generator_schema(items_schema=core_schema.int_schema())
    v = SchemaValidator(schema)
    v.validate_python(gen())
```

    Unlike other types, validated generators do not raise ValidationErrors eagerly,
    but instead will raise a ValidationError when a violating value is actually read from the generator.
    This is to ensure that "validated" generators retain the benefit of lazy evaluation.

    Args:
        items_schema: The value must be a generator with items that match this schema
        min_length: The value must be a generator that yields at least this many items
        max_length: The value must be a generator that yields at most this many items
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='generator',
        items_schema=items_schema,
        min_length=min_length,
        max_length=max_length,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  dict_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dict_schema)
```
dict_schema(
    keys_schema: CoreSchema | None = None,
    values_schema: CoreSchema | None = None,
    *,
    min_length: | None = None,
    max_length: | None = None,
    fail_fast: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> DictSchema

```

Returns a schema that matches a dict value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.dict_schema(
    keys_schema=core_schema.str_schema(), values_schema=core_schema.int_schema()
)
v = SchemaValidator(schema)
assert v.validate_python({'a': '1', 'b': 2}) == {'a': 1, 'b': 2}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`keys_schema` |  `CoreSchema | None` |  The value must be a dict with keys that match this schema |  `None`  
`values_schema` |  `CoreSchema | None` |  The value must be a dict with values that match this schema |  `None`  
`min_length` |  |  The value must be a dict with at least this many items |  `None`  
`max_length` |  |  The value must be a dict with at most this many items |  `None`  
`fail_fast` |  |  Stop validation on the first error |  `None`  
`strict` |  |  Whether the keys and values should be validated with strict mode |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
```
| ```
defdict_schema(
    keys_schema: CoreSchema | None = None,
    values_schema: CoreSchema | None = None,
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    fail_fast: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DictSchema:
"""
    Returns a schema that matches a dict value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.dict_schema(
        keys_schema=core_schema.str_schema(), values_schema=core_schema.int_schema()
    )
    v = SchemaValidator(schema)
    assert v.validate_python({'a': '1', 'b': 2}) == {'a': 1, 'b': 2}
```

    Args:
        keys_schema: The value must be a dict with keys that match this schema
        values_schema: The value must be a dict with values that match this schema
        min_length: The value must be a dict with at least this many items
        max_length: The value must be a dict with at most this many items
        fail_fast: Stop validation on the first error
        strict: Whether the keys and values should be validated with strict mode
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='dict',
        keys_schema=keys_schema,
        values_schema=values_schema,
        min_length=min_length,
        max_length=max_length,
        fail_fast=fail_fast,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  no_info_before_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_before_validator_function)
```
no_info_before_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> BeforeValidatorFunctionSchema

```

Returns a schema that calls a validator function before validating, no `info` argument is provided, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: bytes) -> str:
    return v.decode() + 'world'

func_schema = core_schema.no_info_before_validator_function(
    function=fn, schema=core_schema.str_schema()
)
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `NoInfoValidatorFunction` |  The validator function to call |  _required_  
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
2076
2077
2078
2079
```
| ```
defno_info_before_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BeforeValidatorFunctionSchema:
"""
    Returns a schema that calls a validator function before validating, no `info` argument is provided, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: bytes) -> str:
        return v.decode() + 'world'

    func_schema = core_schema.no_info_before_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call
        schema: The schema to validate the output of the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-before',
        function={'type': 'no-info', 'function': function},
        schema=schema,
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  with_info_before_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_before_validator_function)
```
with_info_before_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: | None = None,
    ref: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> BeforeValidatorFunctionSchema

```

Returns a schema that calls a validator function before validation, the function is called with an `info` argument, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: bytes, info: core_schema.ValidationInfo) -> str:
    assert info.data is not None
    assert info.field_name is not None
    return v.decode() + 'world'

func_schema = core_schema.with_info_before_validator_function(
    function=fn, schema=core_schema.str_schema()
)
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `WithInfoValidatorFunction` |  The validator function to call |  _required_  
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`  
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
2112
2113
2114
2115
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
```
| ```
defwith_info_before_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: str | None = None,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> BeforeValidatorFunctionSchema:
"""
    Returns a schema that calls a validator function before validation, the function is called with
    an `info` argument, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: bytes, info: core_schema.ValidationInfo) -> str:
        assert info.data is not None
        assert info.field_name is not None
        return v.decode() + 'world'

    func_schema = core_schema.with_info_before_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call
        field_name: The name of the field this validator is applied to, if any (deprecated)
        schema: The schema to validate the output of the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_before_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-before',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        schema=schema,
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  no_info_after_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_after_validator_function)
```
no_info_after_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> AfterValidatorFunctionSchema

```

Returns a schema that calls a validator function after validating, no `info` argument is provided, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: str) -> str:
    return v + 'world'

func_schema = core_schema.no_info_after_validator_function(fn, core_schema.str_schema())
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `NoInfoValidatorFunction` |  The validator function to call after the schema is validated |  _required_  
`schema` |  `CoreSchema` |  The schema to validate before the validator function |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
2183
2184
2185
```
| ```
defno_info_after_validator_function(
    function: NoInfoValidatorFunction,
    schema: CoreSchema,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> AfterValidatorFunctionSchema:
"""
    Returns a schema that calls a validator function after validating, no `info` argument is provided, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str) -> str:
        return v + 'world'

    func_schema = core_schema.no_info_after_validator_function(fn, core_schema.str_schema())
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call after the schema is validated
        schema: The schema to validate before the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-after',
        function={'type': 'no-info', 'function': function},
        schema=schema,
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  with_info_after_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_after_validator_function)
```
with_info_after_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> AfterValidatorFunctionSchema

```

Returns a schema that calls a validator function after validation, the function is called with an `info` argument, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: str, info: core_schema.ValidationInfo) -> str:
    assert info.data is not None
    assert info.field_name is not None
    return v + 'world'

func_schema = core_schema.with_info_after_validator_function(
    function=fn, schema=core_schema.str_schema()
)
schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

v = SchemaValidator(schema)
assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `WithInfoValidatorFunction` |  The validator function to call after the schema is validated |  _required_  
`schema` |  `CoreSchema` |  The schema to validate before the validator function |  _required_  
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2188
2189
2190
2191
2192
2193
2194
2195
2196
2197
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
2216
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
```
| ```
defwith_info_after_validator_function(
    function: WithInfoValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: str | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> AfterValidatorFunctionSchema:
"""
    Returns a schema that calls a validator function after validation, the function is called with
    an `info` argument, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert info.data is not None
        assert info.field_name is not None
        return v + 'world'

    func_schema = core_schema.with_info_after_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    schema = core_schema.typed_dict_schema({'a': core_schema.typed_dict_field(func_schema)})

    v = SchemaValidator(schema)
    assert v.validate_python({'a': b'hello '}) == {'a': 'hello world'}
```

    Args:
        function: The validator function to call after the schema is validated
        schema: The schema to validate before the validator function
        field_name: The name of the field this validator is applied to, if any (deprecated)
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_after_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-after',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        schema=schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  no_info_wrap_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_wrap_validator_function)
```
no_info_wrap_validator_function(
    function: NoInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    ref: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> WrapValidatorFunctionSchema

```

Returns a schema which calls a function with a `validator` callable argument which can optionally be used to call inner validation with the function logic, this is much like the "onion" implementation of middleware in many popular web frameworks, no `info` argument is passed, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(
    v: str,
    validator: core_schema.ValidatorFunctionWrapHandler,
) -> str:
    return validator(input_value=v) + 'world'

schema = core_schema.no_info_wrap_validator_function(
    function=fn, schema=core_schema.str_schema()
)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `NoInfoWrapValidatorFunction` |  The validator function to call |  _required_  
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
2311
2312
2313
2314
2315
2316
2317
2318
2319
2320
2321
2322
2323
2324
2325
2326
```
| ```
defno_info_wrap_validator_function(
    function: NoInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> WrapValidatorFunctionSchema:
"""
    Returns a schema which calls a function with a `validator` callable argument which can
    optionally be used to call inner validation with the function logic, this is much like the
    "onion" implementation of middleware in many popular web frameworks, no `info` argument is passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(
        v: str,
        validator: core_schema.ValidatorFunctionWrapHandler,
    ) -> str:
        return validator(input_value=v) + 'world'

    schema = core_schema.no_info_wrap_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        schema: The schema to validate the output of the validator function
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-wrap',
        function={'type': 'no-info', 'function': function},
        schema=schema,
        json_schema_input_schema=json_schema_input_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  with_info_wrap_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_wrap_validator_function)
```
with_info_wrap_validator_function(
    function: WithInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> WrapValidatorFunctionSchema

```

Returns a schema which calls a function with a `validator` callable argument which can optionally be used to call inner validation with the function logic, this is much like the "onion" implementation of middleware in many popular web frameworks, an `info` argument is also passed, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(
    v: str,
    validator: core_schema.ValidatorFunctionWrapHandler,
    info: core_schema.ValidationInfo,
) -> str:
    return validator(input_value=v) + 'world'

schema = core_schema.with_info_wrap_validator_function(
    function=fn, schema=core_schema.str_schema()
)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `WithInfoWrapValidatorFunction` |  The validator function to call |  _required_  
`schema` |  `CoreSchema` |  The schema to validate the output of the validator function |  _required_  
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2329
2330
2331
2332
2333
2334
2335
2336
2337
2338
2339
2340
2341
2342
2343
2344
2345
2346
2347
2348
2349
2350
2351
2352
2353
2354
2355
2356
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
2368
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
2380
2381
2382
2383
2384
2385
```
| ```
defwith_info_wrap_validator_function(
    function: WithInfoWrapValidatorFunction,
    schema: CoreSchema,
    *,
    field_name: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> WrapValidatorFunctionSchema:
"""
    Returns a schema which calls a function with a `validator` callable argument which can
    optionally be used to call inner validation with the function logic, this is much like the
    "onion" implementation of middleware in many popular web frameworks, an `info` argument is also passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(
        v: str,
        validator: core_schema.ValidatorFunctionWrapHandler,
        info: core_schema.ValidationInfo,
    ) -> str:
        return validator(input_value=v) + 'world'

    schema = core_schema.with_info_wrap_validator_function(
        function=fn, schema=core_schema.str_schema()
    )
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        schema: The schema to validate the output of the validator function
        field_name: The name of the field this validator is applied to, if any (deprecated)
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_wrap_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-wrap',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        schema=schema,
        json_schema_input_schema=json_schema_input_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  no_info_plain_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.no_info_plain_validator_function)
```
no_info_plain_validator_function(
    function: NoInfoValidatorFunction,
    *,
    ref: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> PlainValidatorFunctionSchema

```

Returns a schema that uses the provided function for validation, no `info` argument is passed, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: str) -> str:
    assert 'hello' in v
    return v + 'world'

schema = core_schema.no_info_plain_validator_function(function=fn)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `NoInfoValidatorFunction` |  The validator function to call |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2397
2398
2399
2400
2401
2402
2403
2404
2405
2406
2407
2408
2409
2410
2411
2412
2413
2414
2415
2416
2417
2418
2419
2420
2421
2422
2423
2424
2425
2426
2427
2428
2429
2430
2431
2432
2433
2434
```
| ```
defno_info_plain_validator_function(
    function: NoInfoValidatorFunction,
    *,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> PlainValidatorFunctionSchema:
"""
    Returns a schema that uses the provided function for validation, no `info` argument is passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str) -> str:
        assert 'hello' in v
        return v + 'world'

    schema = core_schema.no_info_plain_validator_function(function=fn)
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='function-plain',
        function={'type': 'no-info', 'function': function},
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  with_info_plain_validator_function [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_info_plain_validator_function)
```
with_info_plain_validator_function(
    function: WithInfoValidatorFunction,
    *,
    field_name: | None = None,
    ref: | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> PlainValidatorFunctionSchema

```

Returns a schema that uses the provided function for validation, an `info` argument is passed, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: str, info: core_schema.ValidationInfo) -> str:
    assert 'hello' in v
    return v + 'world'

schema = core_schema.with_info_plain_validator_function(function=fn)
v = SchemaValidator(schema)
assert v.validate_python('hello ') == 'hello world'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `WithInfoValidatorFunction` |  The validator function to call |  _required_  
`field_name` |  |  The name of the field this validator is applied to, if any (deprecated) |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`json_schema_input_schema` |  `CoreSchema | None` |  The core schema to be used to generate the corresponding JSON Schema input type |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
2448
2449
2450
2451
2452
2453
2454
2455
2456
2457
2458
2459
2460
2461
2462
2463
2464
2465
2466
2467
2468
2469
2470
2471
2472
2473
2474
2475
2476
2477
2478
2479
2480
2481
2482
2483
```
| ```
defwith_info_plain_validator_function(
    function: WithInfoValidatorFunction,
    *,
    field_name: str | None = None,
    ref: str | None = None,
    json_schema_input_schema: CoreSchema | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> PlainValidatorFunctionSchema:
"""
    Returns a schema that uses the provided function for validation, an `info` argument is passed, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert 'hello' in v
        return v + 'world'

    schema = core_schema.with_info_plain_validator_function(function=fn)
    v = SchemaValidator(schema)
    assert v.validate_python('hello ') == 'hello world'
```

    Args:
        function: The validator function to call
        field_name: The name of the field this validator is applied to, if any (deprecated)
        ref: optional unique identifier of the schema, used to reference the schema in other places
        json_schema_input_schema: The core schema to be used to generate the corresponding JSON Schema input type
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    if field_name is not None:
        warnings.warn(
            'The `field_name` argument on `with_info_plain_validator_function` is deprecated, it will be passed to the function through `ValidationState` instead.',
            DeprecationWarning,
            stacklevel=2,
        )

    return _dict_not_none(
        type='function-plain',
        function=_dict_not_none(type='with-info', function=function, field_name=field_name),
        ref=ref,
        json_schema_input_schema=json_schema_input_schema,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  with_default_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.with_default_schema)
```
with_default_schema(
    schema: CoreSchema,
    *,
    default: = PydanticUndefined,
    default_factory: [
        [[], ],
        [[[, ]], ],
        None,
    ] = None,
    default_factory_takes_data: | None = None,
    on_error: (
        ["raise", "omit", "default"] | None
    ) = None,
    validate_default: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> WithDefaultSchema

```

Returns a schema that adds a default value to the given schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.with_default_schema(core_schema.str_schema(), default='hello')
wrapper_schema = core_schema.typed_dict_schema(
    {'a': core_schema.typed_dict_field(schema)}
)
v = SchemaValidator(wrapper_schema)
assert v.validate_python({}) == v.validate_python({'a': 'hello'})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The schema to add a default value to |  _required_  
`default` |  |  The default value to use |  `PydanticUndefined`  
`default_factory` |  |  A callable that returns the default value to use |  `None`  
`default_factory_takes_data` |  |  Whether the default factory takes a validated data argument |  `None`  
`on_error` |  |  What to do if the schema validation fails. One of 'raise', 'omit', 'default' |  `None`  
`validate_default` |  |  Whether the default value should be validated |  `None`  
`strict` |  |  Whether the underlying schema should be validated with strict mode |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2500
2501
2502
2503
2504
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
2516
2517
2518
2519
2520
2521
2522
2523
2524
2525
2526
2527
2528
2529
2530
2531
2532
2533
2534
2535
2536
2537
2538
2539
2540
2541
2542
2543
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
```
| ```
defwith_default_schema(
    schema: CoreSchema,
    *,
    default: Any = PydanticUndefined,
    default_factory: Union[Callable[[], Any], Callable[[dict[str, Any]], Any], None] = None,
    default_factory_takes_data: bool | None = None,
    on_error: Literal['raise', 'omit', 'default'] | None = None,
    validate_default: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> WithDefaultSchema:
"""
    Returns a schema that adds a default value to the given schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.with_default_schema(core_schema.str_schema(), default='hello')
    wrapper_schema = core_schema.typed_dict_schema(
        {'a': core_schema.typed_dict_field(schema)}
    )
    v = SchemaValidator(wrapper_schema)
    assert v.validate_python({}) == v.validate_python({'a': 'hello'})
```

    Args:
        schema: The schema to add a default value to
        default: The default value to use
        default_factory: A callable that returns the default value to use
        default_factory_takes_data: Whether the default factory takes a validated data argument
        on_error: What to do if the schema validation fails. One of 'raise', 'omit', 'default'
        validate_default: Whether the default value should be validated
        strict: Whether the underlying schema should be validated with strict mode
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    s = _dict_not_none(
        type='default',
        schema=schema,
        default_factory=default_factory,
        default_factory_takes_data=default_factory_takes_data,
        on_error=on_error,
        validate_default=validate_default,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )
    if default is not PydanticUndefined:
        s['default'] = default
    return s

```
  
---|---  
##  nullable_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.nullable_schema)
```
nullable_schema(
    schema: CoreSchema,
    *,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> NullableSchema

```

Returns a schema that matches a nullable value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.nullable_schema(core_schema.str_schema())
v = SchemaValidator(schema)
assert v.validate_python(None) is None

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The schema to wrap |  _required_  
`strict` |  |  Whether the underlying schema should be validated with strict mode |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2565
2566
2567
2568
2569
2570
2571
2572
2573
2574
2575
2576
2577
2578
2579
2580
2581
2582
2583
2584
2585
2586
2587
2588
2589
2590
2591
2592
2593
```
| ```
defnullable_schema(
    schema: CoreSchema,
    *,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> NullableSchema:
"""
    Returns a schema that matches a nullable value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.nullable_schema(core_schema.str_schema())
    v = SchemaValidator(schema)
    assert v.validate_python(None) is None
```

    Args:
        schema: The schema to wrap
        strict: Whether the underlying schema should be validated with strict mode
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='nullable', schema=schema, strict=strict, ref=ref, metadata=metadata, serialization=serialization
    )

```
  
---|---  
##  union_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.union_schema)
```
union_schema(
    choices: [CoreSchema | [CoreSchema, ]],
    *,
    auto_collapse: | None = None,
    custom_error_type: | None = None,
    custom_error_message: | None = None,
    custom_error_context: (
        [, | ] | None
    ) = None,
    mode: ["smart", "left_to_right"] | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> UnionSchema

```

Returns a schema that matches a union value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.union_schema([core_schema.str_schema(), core_schema.int_schema()])
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello'
assert v.validate_python(1) == 1

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`choices` |  `CoreSchema | CoreSchema, ` |  The schemas to match. If a tuple, the second item is used as the label for the case. |  _required_  
`auto_collapse` |  |  whether to automatically collapse unions with one element to the inner validator, default true |  `None`  
`custom_error_type` |  |  The custom error type to use if the validation fails |  `None`  
`custom_error_message` |  |  The custom error message to use if the validation fails |  `None`  
`custom_error_context` |  |  The custom error context to use if the validation fails |  `None`  
`mode` |  |  How to select which choice to return * `smart` (default) will try to return the choice which is the closest match to the input value * `left_to_right` will return the first choice in `choices` which succeeds validation |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2611
2612
2613
2614
2615
2616
2617
2618
2619
2620
2621
2622
2623
2624
2625
2626
2627
2628
2629
2630
2631
2632
2633
2634
2635
2636
2637
2638
2639
2640
2641
2642
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
2653
2654
2655
2656
2657
2658
2659
```
| ```
defunion_schema(
    choices: list[CoreSchema | tuple[CoreSchema, str]],
    *,
    auto_collapse: bool | None = None,
    custom_error_type: str | None = None,
    custom_error_message: str | None = None,
    custom_error_context: dict[str, str | int] | None = None,
    mode: Literal['smart', 'left_to_right'] | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> UnionSchema:
"""
    Returns a schema that matches a union value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.union_schema([core_schema.str_schema(), core_schema.int_schema()])
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello'
    assert v.validate_python(1) == 1
```

    Args:
        choices: The schemas to match. If a tuple, the second item is used as the label for the case.
        auto_collapse: whether to automatically collapse unions with one element to the inner validator, default true
        custom_error_type: The custom error type to use if the validation fails
        custom_error_message: The custom error message to use if the validation fails
        custom_error_context: The custom error context to use if the validation fails
        mode: How to select which choice to return
            * `smart` (default) will try to return the choice which is the closest match to the input value
            * `left_to_right` will return the first choice in `choices` which succeeds validation
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='union',
        choices=choices,
        auto_collapse=auto_collapse,
        custom_error_type=custom_error_type,
        custom_error_message=custom_error_message,
        custom_error_context=custom_error_context,
        mode=mode,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  tagged_union_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.tagged_union_schema)
```
tagged_union_schema(
    choices: [, CoreSchema],
    discriminator: (
        | [| ]
        | [[| ]]
        | [[], ]
    ),
    *,
    custom_error_type: | None = None,
    custom_error_message: | None = None,
    custom_error_context: (
        [, | | ] | None
    ) = None,
    strict: | None = None,
    from_attributes: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> TaggedUnionSchema

```

Returns a schema that matches a tagged union value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

apple_schema = core_schema.typed_dict_schema(
    {
        'foo': core_schema.typed_dict_field(core_schema.str_schema()),
        'bar': core_schema.typed_dict_field(core_schema.int_schema()),
    }
)
banana_schema = core_schema.typed_dict_schema(
    {
        'foo': core_schema.typed_dict_field(core_schema.str_schema()),
        'spam': core_schema.typed_dict_field(
            core_schema.list_schema(items_schema=core_schema.int_schema())
        ),
    }
)
schema = core_schema.tagged_union_schema(
    choices={
        'apple': apple_schema,
        'banana': banana_schema,
    },
    discriminator='foo',
)
v = SchemaValidator(schema)
assert v.validate_python({'foo': 'apple', 'bar': '123'}) == {'foo': 'apple', 'bar': 123}
assert v.validate_python({'foo': 'banana', 'spam': [1, 2, 3]}) == {
    'foo': 'banana',
    'spam': [1, 2, 3],
}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`choices` |  `CoreSchema]` |  The schemas to match When retrieving a schema from `choices` using the discriminator value, if the value is a str, it should be fed back into the `choices` map until a schema is obtained (This approach is to prevent multiple ownership of a single schema in Rust) |  _required_  
`discriminator` |  |  The discriminator to use to determine the schema to use * If `discriminator` is a str, it is the name of the attribute to use as the discriminator * If `discriminator` is a list of int/str, it should be used as a "path" to access the discriminator * If `discriminator` is a list of lists, each inner list is a path, and the first path that exists is used * If `discriminator` is a callable, it should return the discriminator when called on the value to validate; the callable can return `None` to indicate that there is no matching discriminator present on the input |  _required_  
`custom_error_type` |  |  The custom error type to use if the validation fails |  `None`  
`custom_error_message` |  |  The custom error message to use if the validation fails |  `None`  
`custom_error_context` |  |  The custom error context to use if the validation fails |  `None`  
`strict` |  |  Whether the underlying schemas should be validated with strict mode |  `None`  
`from_attributes` |  |  Whether to use the attributes of the object to retrieve the discriminator value |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2676
2677
2678
2679
2680
2681
2682
2683
2684
2685
2686
2687
2688
2689
2690
2691
2692
2693
2694
2695
2696
2697
2698
2699
2700
2701
2702
2703
2704
2705
2706
2707
2708
2709
2710
2711
2712
2713
2714
2715
2716
2717
2718
2719
2720
2721
2722
2723
2724
2725
2726
2727
2728
2729
2730
2731
2732
2733
2734
2735
2736
2737
2738
2739
2740
2741
2742
2743
2744
2745
2746
2747
2748
2749
2750
2751
2752
2753
2754
2755
2756
```
| ```
deftagged_union_schema(
    choices: dict[Any, CoreSchema],
    discriminator: str | list[str | int] | list[list[str | int]] | Callable[[Any], Any],
    *,
    custom_error_type: str | None = None,
    custom_error_message: str | None = None,
    custom_error_context: dict[str, int | str | float] | None = None,
    strict: bool | None = None,
    from_attributes: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> TaggedUnionSchema:
"""
    Returns a schema that matches a tagged union value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    apple_schema = core_schema.typed_dict_schema(
        {
            'foo': core_schema.typed_dict_field(core_schema.str_schema()),
            'bar': core_schema.typed_dict_field(core_schema.int_schema()),
        }
    )
    banana_schema = core_schema.typed_dict_schema(
        {
            'foo': core_schema.typed_dict_field(core_schema.str_schema()),
            'spam': core_schema.typed_dict_field(
                core_schema.list_schema(items_schema=core_schema.int_schema())
            ),
        }
    )
    schema = core_schema.tagged_union_schema(
        choices={
            'apple': apple_schema,
            'banana': banana_schema,
        },
        discriminator='foo',
    )
    v = SchemaValidator(schema)
    assert v.validate_python({'foo': 'apple', 'bar': '123'}) == {'foo': 'apple', 'bar': 123}
    assert v.validate_python({'foo': 'banana', 'spam': [1, 2, 3]}) == {
        'foo': 'banana',
        'spam': [1, 2, 3],
    }
```

    Args:
        choices: The schemas to match
            When retrieving a schema from `choices` using the discriminator value, if the value is a str,
            it should be fed back into the `choices` map until a schema is obtained
            (This approach is to prevent multiple ownership of a single schema in Rust)
        discriminator: The discriminator to use to determine the schema to use
            * If `discriminator` is a str, it is the name of the attribute to use as the discriminator
            * If `discriminator` is a list of int/str, it should be used as a "path" to access the discriminator
            * If `discriminator` is a list of lists, each inner list is a path, and the first path that exists is used
            * If `discriminator` is a callable, it should return the discriminator when called on the value to validate;
              the callable can return `None` to indicate that there is no matching discriminator present on the input
        custom_error_type: The custom error type to use if the validation fails
        custom_error_message: The custom error message to use if the validation fails
        custom_error_context: The custom error context to use if the validation fails
        strict: Whether the underlying schemas should be validated with strict mode
        from_attributes: Whether to use the attributes of the object to retrieve the discriminator value
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='tagged-union',
        choices=choices,
        discriminator=discriminator,
        custom_error_type=custom_error_type,
        custom_error_message=custom_error_message,
        custom_error_context=custom_error_context,
        strict=strict,
        from_attributes=from_attributes,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  chain_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.chain_schema)
```
chain_schema(
    steps: [CoreSchema],
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ChainSchema

```

Returns a schema that chains the provided validation schemas, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: str, info: core_schema.ValidationInfo) -> str:
    assert 'hello' in v
    return v + ' world'

fn_schema = core_schema.with_info_plain_validator_function(function=fn)
schema = core_schema.chain_schema(
    [fn_schema, fn_schema, fn_schema, core_schema.str_schema()]
)
v = SchemaValidator(schema)
assert v.validate_python('hello') == 'hello world world world'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`steps` |  `CoreSchema]` |  The schemas to chain |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2767
2768
2769
2770
2771
2772
2773
2774
2775
2776
2777
2778
2779
2780
2781
2782
2783
2784
2785
2786
2787
2788
2789
2790
2791
2792
2793
2794
2795
2796
2797
2798
```
| ```
defchain_schema(
    steps: list[CoreSchema],
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ChainSchema:
"""
    Returns a schema that chains the provided validation schemas, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert 'hello' in v
        return v + ' world'

    fn_schema = core_schema.with_info_plain_validator_function(function=fn)
    schema = core_schema.chain_schema(
        [fn_schema, fn_schema, fn_schema, core_schema.str_schema()]
    )
    v = SchemaValidator(schema)
    assert v.validate_python('hello') == 'hello world world world'
```

    Args:
        steps: The schemas to chain
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='chain', steps=steps, ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  lax_or_strict_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.lax_or_strict_schema)
```
lax_or_strict_schema(
    lax_schema: CoreSchema,
    strict_schema: CoreSchema,
    *,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> LaxOrStrictSchema

```

Returns a schema that uses the lax or strict schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

deffn(v: str, info: core_schema.ValidationInfo) -> str:
    assert 'hello' in v
    return v + ' world'

lax_schema = core_schema.int_schema(strict=False)
strict_schema = core_schema.int_schema(strict=True)

schema = core_schema.lax_or_strict_schema(
    lax_schema=lax_schema, strict_schema=strict_schema, strict=True
)
v = SchemaValidator(schema)
assert v.validate_python(123) == 123

schema = core_schema.lax_or_strict_schema(
    lax_schema=lax_schema, strict_schema=strict_schema, strict=False
)
v = SchemaValidator(schema)
assert v.validate_python('123') == 123

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`lax_schema` |  `CoreSchema` |  The lax schema to use |  _required_  
`strict_schema` |  `CoreSchema` |  The strict schema to use |  _required_  
`strict` |  |  Whether the strict schema should be used |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2811
2812
2813
2814
2815
2816
2817
2818
2819
2820
2821
2822
2823
2824
2825
2826
2827
2828
2829
2830
2831
2832
2833
2834
2835
2836
2837
2838
2839
2840
2841
2842
2843
2844
2845
2846
2847
2848
2849
2850
2851
2852
2853
2854
2855
2856
2857
2858
2859
2860
2861
2862
```
| ```
deflax_or_strict_schema(
    lax_schema: CoreSchema,
    strict_schema: CoreSchema,
    *,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> LaxOrStrictSchema:
"""
    Returns a schema that uses the lax or strict schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    def fn(v: str, info: core_schema.ValidationInfo) -> str:
        assert 'hello' in v
        return v + ' world'

    lax_schema = core_schema.int_schema(strict=False)
    strict_schema = core_schema.int_schema(strict=True)

    schema = core_schema.lax_or_strict_schema(
        lax_schema=lax_schema, strict_schema=strict_schema, strict=True
    )
    v = SchemaValidator(schema)
    assert v.validate_python(123) == 123

    schema = core_schema.lax_or_strict_schema(
        lax_schema=lax_schema, strict_schema=strict_schema, strict=False
    )
    v = SchemaValidator(schema)
    assert v.validate_python('123') == 123
```

    Args:
        lax_schema: The lax schema to use
        strict_schema: The strict schema to use
        strict: Whether the strict schema should be used
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='lax-or-strict',
        lax_schema=lax_schema,
        strict_schema=strict_schema,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  json_or_python_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.json_or_python_schema)
```
json_or_python_schema(
    json_schema: CoreSchema,
    python_schema: CoreSchema,
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> JsonOrPythonSchema

```

Returns a schema that uses the Json or Python schema depending on the input:
```
frompydantic_coreimport SchemaValidator, ValidationError, core_schema

v = SchemaValidator(
    core_schema.json_or_python_schema(
        json_schema=core_schema.int_schema(),
        python_schema=core_schema.int_schema(strict=True),
    )
)

assert v.validate_json('"123"') == 123

try:
    v.validate_python('123')
except ValidationError:
    pass
else:
    raise AssertionError('Validation should have failed')

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`json_schema` |  `CoreSchema` |  The schema to use for Json inputs |  _required_  
`python_schema` |  `CoreSchema` |  The schema to use for Python inputs |  _required_  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2874
2875
2876
2877
2878
2879
2880
2881
2882
2883
2884
2885
2886
2887
2888
2889
2890
2891
2892
2893
2894
2895
2896
2897
2898
2899
2900
2901
2902
2903
2904
2905
2906
2907
2908
2909
2910
2911
2912
2913
2914
2915
2916
2917
2918
2919
```
| ```
defjson_or_python_schema(
    json_schema: CoreSchema,
    python_schema: CoreSchema,
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> JsonOrPythonSchema:
"""
    Returns a schema that uses the Json or Python schema depending on the input:

```py
    from pydantic_core import SchemaValidator, ValidationError, core_schema

    v = SchemaValidator(
        core_schema.json_or_python_schema(
            json_schema=core_schema.int_schema(),
            python_schema=core_schema.int_schema(strict=True),
        )
    )

    assert v.validate_json('"123"') == 123

    try:
        v.validate_python('123')
    except ValidationError:
        pass
    else:
        raise AssertionError('Validation should have failed')
```

    Args:
        json_schema: The schema to use for Json inputs
        python_schema: The schema to use for Python inputs
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='json-or-python',
        json_schema=json_schema,
        python_schema=python_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  typed_dict_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_field)
```
typed_dict_field(
    schema: CoreSchema,
    *,
    required: | None = None,
    validation_alias: (
        | [| ] | [[| ]] | None
    ) = None,
    serialization_alias: | None = None,
    serialization_exclude: | None = None,
    metadata: [, ] | None = None,
    serialization_exclude_if: (
        [[], ] | None
    ) = None
) -> TypedDictField

```

Returns a schema that matches a typed dict field, e.g.:
```
frompydantic_coreimport core_schema

field = core_schema.typed_dict_field(schema=core_schema.int_schema(), required=True)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The schema to use for the field |  _required_  
`required` |  |  Whether the field is required, otherwise uses the value from `total` on the typed dict |  `None`  
`validation_alias` |  |  The alias(es) to use to find the field in the validation data |  `None`  
`serialization_alias` |  |  The alias to use as a key when serializing |  `None`  
`serialization_exclude` |  |  Whether to exclude the field when serializing |  `None`  
`serialization_exclude_if` |  |  A callable that determines whether to exclude the field when serializing based on its value. |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2933
2934
2935
2936
2937
2938
2939
2940
2941
2942
2943
2944
2945
2946
2947
2948
2949
2950
2951
2952
2953
2954
2955
2956
2957
2958
2959
2960
2961
2962
2963
2964
2965
2966
2967
2968
2969
2970
```
| ```
deftyped_dict_field(
    schema: CoreSchema,
    *,
    required: bool | None = None,
    validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
    serialization_alias: str | None = None,
    serialization_exclude: bool | None = None,
    metadata: dict[str, Any] | None = None,
    serialization_exclude_if: Callable[[Any], bool] | None = None,
) -> TypedDictField:
"""
    Returns a schema that matches a typed dict field, e.g.:

```py
    from pydantic_core import core_schema

    field = core_schema.typed_dict_field(schema=core_schema.int_schema(), required=True)
```

    Args:
        schema: The schema to use for the field
        required: Whether the field is required, otherwise uses the value from `total` on the typed dict
        validation_alias: The alias(es) to use to find the field in the validation data
        serialization_alias: The alias to use as a key when serializing
        serialization_exclude: Whether to exclude the field when serializing
        serialization_exclude_if: A callable that determines whether to exclude the field when serializing based on its value.
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """
    return _dict_not_none(
        type='typed-dict-field',
        schema=schema,
        required=required,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        serialization_exclude=serialization_exclude,
        serialization_exclude_if=serialization_exclude_if,
        metadata=metadata,
    )

```
  
---|---  
##  typed_dict_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_schema)
```
typed_dict_schema(
    fields: [, TypedDictField],
    *,
    cls: [] | None = None,
    cls_name: | None = None,
    computed_fields: [ComputedField] | None = None,
    strict: | None = None,
    extras_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    total: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
    config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
) -> TypedDictSchema

```

Returns a schema that matches a typed dict, e.g.:
```
fromtyping_extensionsimport TypedDict

frompydantic_coreimport SchemaValidator, core_schema

classMyTypedDict(TypedDict):
    a: str

wrapper_schema = core_schema.typed_dict_schema(
    {'a': core_schema.typed_dict_field(core_schema.str_schema())}, cls=MyTypedDict
)
v = SchemaValidator(wrapper_schema)
assert v.validate_python({'a': 'hello'}) == {'a': 'hello'}

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`fields` |  `TypedDictField]` |  The fields to use for the typed dict |  _required_  
`cls` |  |  The class to use for the typed dict |  `None`  
`cls_name` |  |  The name to use in error locations. Falls back to `cls.__name__`, or the validator name if no class is provided. |  `None`  
`computed_fields` |  `ComputedField] | None` |  Computed fields to use when serializing the model, only applies when directly inside a model |  `None`  
`strict` |  |  Whether the typed dict is strict |  `None`  
`extras_schema` |  `CoreSchema | None` |  The extra validator to use for the typed dict |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`extra_behavior` |  `ExtraBehavior | None` |  The extra behavior to use for the typed dict |  `None`  
`total` |  |  Whether the typed dict is total, otherwise uses `typed_dict_total` from config |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
2990
2991
2992
2993
2994
2995
2996
2997
2998
2999
3000
3001
3002
3003
3004
3005
3006
3007
3008
3009
3010
3011
3012
3013
3014
3015
3016
3017
3018
3019
3020
3021
3022
3023
3024
3025
3026
3027
3028
3029
3030
3031
3032
3033
3034
3035
3036
3037
3038
3039
3040
3041
3042
3043
3044
3045
3046
3047
3048
3049
3050
3051
```
| ```
deftyped_dict_schema(
    fields: dict[str, TypedDictField],
    *,
    cls: type[Any] | None = None,
    cls_name: str | None = None,
    computed_fields: list[ComputedField] | None = None,
    strict: bool | None = None,
    extras_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    total: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
    config: CoreConfig | None = None,
) -> TypedDictSchema:
"""
    Returns a schema that matches a typed dict, e.g.:

```py
    from typing_extensions import TypedDict

    from pydantic_core import SchemaValidator, core_schema

    class MyTypedDict(TypedDict):
        a: str

    wrapper_schema = core_schema.typed_dict_schema(
        {'a': core_schema.typed_dict_field(core_schema.str_schema())}, cls=MyTypedDict
    )
    v = SchemaValidator(wrapper_schema)
    assert v.validate_python({'a': 'hello'}) == {'a': 'hello'}
```

    Args:
        fields: The fields to use for the typed dict
        cls: The class to use for the typed dict
        cls_name: The name to use in error locations. Falls back to `cls.__name__`, or the validator name if no class
            is provided.
        computed_fields: Computed fields to use when serializing the model, only applies when directly inside a model
        strict: Whether the typed dict is strict
        extras_schema: The extra validator to use for the typed dict
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        extra_behavior: The extra behavior to use for the typed dict
        total: Whether the typed dict is total, otherwise uses `typed_dict_total` from config
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='typed-dict',
        fields=fields,
        cls=cls,
        cls_name=cls_name,
        computed_fields=computed_fields,
        strict=strict,
        extras_schema=extras_schema,
        extra_behavior=extra_behavior,
        total=total,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
        config=config,
    )

```
  
---|---  
##  model_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_field)
```
model_field(
    schema: CoreSchema,
    *,
    validation_alias: (
        | [| ] | [[| ]] | None
    ) = None,
    serialization_alias: | None = None,
    serialization_exclude: | None = None,
    serialization_exclude_if: (
        [[], ] | None
    ) = None,
    frozen: | None = None,
    metadata: [, ] | None = None
) -> ModelField

```

Returns a schema for a model field, e.g.:
```
frompydantic_coreimport core_schema

field = core_schema.model_field(schema=core_schema.int_schema())

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The schema to use for the field |  _required_  
`validation_alias` |  |  The alias(es) to use to find the field in the validation data |  `None`  
`serialization_alias` |  |  The alias to use as a key when serializing |  `None`  
`serialization_exclude` |  |  Whether to exclude the field when serializing |  `None`  
`serialization_exclude_if` |  |  A Callable that determines whether to exclude a field during serialization based on its value. |  `None`  
`frozen` |  |  Whether the field is frozen |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3065
3066
3067
3068
3069
3070
3071
3072
3073
3074
3075
3076
3077
3078
3079
3080
3081
3082
3083
3084
3085
3086
3087
3088
3089
3090
3091
3092
3093
3094
3095
3096
3097
3098
3099
3100
3101
3102
```
| ```
defmodel_field(
    schema: CoreSchema,
    *,
    validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
    serialization_alias: str | None = None,
    serialization_exclude: bool | None = None,
    serialization_exclude_if: Callable[[Any], bool] | None = None,
    frozen: bool | None = None,
    metadata: dict[str, Any] | None = None,
) -> ModelField:
"""
    Returns a schema for a model field, e.g.:

```py
    from pydantic_core import core_schema

    field = core_schema.model_field(schema=core_schema.int_schema())
```

    Args:
        schema: The schema to use for the field
        validation_alias: The alias(es) to use to find the field in the validation data
        serialization_alias: The alias to use as a key when serializing
        serialization_exclude: Whether to exclude the field when serializing
        serialization_exclude_if: A Callable that determines whether to exclude a field during serialization based on its value.
        frozen: Whether the field is frozen
        metadata: Any other information you want to include with the schema, not used by pydantic-core
    """
    return _dict_not_none(
        type='model-field',
        schema=schema,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        serialization_exclude=serialization_exclude,
        serialization_exclude_if=serialization_exclude_if,
        frozen=frozen,
        metadata=metadata,
    )

```
  
---|---  
##  model_fields_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_fields_schema)
```
model_fields_schema(
    fields: [, ModelField],
    *,
    model_name: | None = None,
    computed_fields: [ComputedField] | None = None,
    strict: | None = None,
    extras_schema: CoreSchema | None = None,
    extras_keys_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    from_attributes: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ModelFieldsSchema

```

Returns a schema that matches the fields of a Pydantic model, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

wrapper_schema = core_schema.model_fields_schema(
    {'a': core_schema.model_field(core_schema.str_schema())}
)
v = SchemaValidator(wrapper_schema)
print(v.validate_python({'a': 'hello'}))
#> ({'a': 'hello'}, None, {'a'})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`fields` |  `ModelField]` |  The fields of the model |  _required_  
`model_name` |  |  The name of the model, used for error messages, defaults to "Model" |  `None`  
`computed_fields` |  `ComputedField] | None` |  Computed fields to use when serializing the model, only applies when directly inside a model |  `None`  
`strict` |  |  Whether the model is strict |  `None`  
`extras_schema` |  `CoreSchema | None` |  The schema to use when validating extra input data |  `None`  
`extras_keys_schema` |  `CoreSchema | None` |  The schema to use when validating the keys of extra input data |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`extra_behavior` |  `ExtraBehavior | None` |  The extra behavior to use for the model fields |  `None`  
`from_attributes` |  |  Whether the model fields should be populated from attributes |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3120
3121
3122
3123
3124
3125
3126
3127
3128
3129
3130
3131
3132
3133
3134
3135
3136
3137
3138
3139
3140
3141
3142
3143
3144
3145
3146
3147
3148
3149
3150
3151
3152
3153
3154
3155
3156
3157
3158
3159
3160
3161
3162
3163
3164
3165
3166
3167
3168
3169
3170
3171
3172
3173
3174
```
| ```
defmodel_fields_schema(
    fields: dict[str, ModelField],
    *,
    model_name: str | None = None,
    computed_fields: list[ComputedField] | None = None,
    strict: bool | None = None,
    extras_schema: CoreSchema | None = None,
    extras_keys_schema: CoreSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
    from_attributes: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ModelFieldsSchema:
"""
    Returns a schema that matches the fields of a Pydantic model, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    wrapper_schema = core_schema.model_fields_schema(
        {'a': core_schema.model_field(core_schema.str_schema())}
    )
    v = SchemaValidator(wrapper_schema)
    print(v.validate_python({'a': 'hello'}))
    #> ({'a': 'hello'}, None, {'a'})
```

    Args:
        fields: The fields of the model
        model_name: The name of the model, used for error messages, defaults to "Model"
        computed_fields: Computed fields to use when serializing the model, only applies when directly inside a model
        strict: Whether the model is strict
        extras_schema: The schema to use when validating extra input data
        extras_keys_schema: The schema to use when validating the keys of extra input data
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        extra_behavior: The extra behavior to use for the model fields
        from_attributes: Whether the model fields should be populated from attributes
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='model-fields',
        fields=fields,
        model_name=model_name,
        computed_fields=computed_fields,
        strict=strict,
        extras_schema=extras_schema,
        extras_keys_schema=extras_keys_schema,
        extra_behavior=extra_behavior,
        from_attributes=from_attributes,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  model_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.model_schema)
```
model_schema(
    cls: [],
    schema: CoreSchema,
    *,
    generic_origin: [] | None = None,
    custom_init: | None = None,
    root_model: | None = None,
    post_init: | None = None,
    revalidate_instances: (
        ["always", "never", "subclass-instances"]
        | None
    ) = None,
    strict: | None = None,
    frozen: | None = None,
    extra_behavior: ExtraBehavior | None = None,
    config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ModelSchema

```

A model schema generally contains a typed-dict schema. It will run the typed dict validator, then create a new class and set the dict and fields set returned from the typed dict validator to `__dict__` and `__pydantic_fields_set__` respectively.
Example:
```
frompydantic_coreimport CoreConfig, SchemaValidator, core_schema

classMyModel:
    __slots__ = (
        '__dict__',
        '__pydantic_fields_set__',
        '__pydantic_extra__',
        '__pydantic_private__',
    )

schema = core_schema.model_schema(
    cls=MyModel,
    config=CoreConfig(str_max_length=5),
    schema=core_schema.model_fields_schema(
        fields={'a': core_schema.model_field(core_schema.str_schema())},
    ),
)
v = SchemaValidator(schema)
assert v.isinstance_python({'a': 'hello'}) is True
assert v.isinstance_python({'a': 'too long'}) is False

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  |  The class to use for the model |  _required_  
`schema` |  `CoreSchema` |  The schema to use for the model |  _required_  
`generic_origin` |  |  The origin type used for this model, if it's a parametrized generic. Ex, if this model schema represents `SomeModel[int]`, generic_origin is `SomeModel` |  `None`  
`custom_init` |  |  Whether the model has a custom init method |  `None`  
`root_model` |  |  Whether the model is a `RootModel` |  `None`  
`post_init` |  |  The call after init to use for the model |  `None`  
`revalidate_instances` |  |  whether instances of models and dataclasses (including subclass instances) should re-validate defaults to config.revalidate_instances, else 'never' |  `None`  
`strict` |  |  Whether the model is strict |  `None`  
`frozen` |  |  Whether the model is frozen |  `None`  
`extra_behavior` |  `ExtraBehavior | None` |  The extra behavior to use for the model, used in serialization |  `None`  
`config` |  `CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None` |  The config to use for the model |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3195
3196
3197
3198
3199
3200
3201
3202
3203
3204
3205
3206
3207
3208
3209
3210
3211
3212
3213
3214
3215
3216
3217
3218
3219
3220
3221
3222
3223
3224
3225
3226
3227
3228
3229
3230
3231
3232
3233
3234
3235
3236
3237
3238
3239
3240
3241
3242
3243
3244
3245
3246
3247
3248
3249
3250
3251
3252
3253
3254
3255
3256
3257
3258
3259
3260
3261
3262
3263
3264
3265
3266
3267
3268
3269
3270
3271
3272
3273
3274
3275
3276
3277
```
| ```
defmodel_schema(
    cls: type[Any],
    schema: CoreSchema,
    *,
    generic_origin: type[Any] | None = None,
    custom_init: bool | None = None,
    root_model: bool | None = None,
    post_init: str | None = None,
    revalidate_instances: Literal['always', 'never', 'subclass-instances'] | None = None,
    strict: bool | None = None,
    frozen: bool | None = None,
    extra_behavior: ExtraBehavior | None = None,
    config: CoreConfig | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ModelSchema:
"""
    A model schema generally contains a typed-dict schema.
    It will run the typed dict validator, then create a new class
    and set the dict and fields set returned from the typed dict validator
    to `__dict__` and `__pydantic_fields_set__` respectively.

    Example:

```py
    from pydantic_core import CoreConfig, SchemaValidator, core_schema

    class MyModel:
        __slots__ = (
            '__dict__',
            '__pydantic_fields_set__',
            '__pydantic_extra__',
            '__pydantic_private__',
        )

    schema = core_schema.model_schema(
        cls=MyModel,
        config=CoreConfig(str_max_length=5),
        schema=core_schema.model_fields_schema(
            fields={'a': core_schema.model_field(core_schema.str_schema())},
        ),
    )
    v = SchemaValidator(schema)
    assert v.isinstance_python({'a': 'hello'}) is True
    assert v.isinstance_python({'a': 'too long'}) is False
```

    Args:
        cls: The class to use for the model
        schema: The schema to use for the model
        generic_origin: The origin type used for this model, if it's a parametrized generic. Ex,
            if this model schema represents `SomeModel[int]`, generic_origin is `SomeModel`
        custom_init: Whether the model has a custom init method
        root_model: Whether the model is a `RootModel`
        post_init: The call after init to use for the model
        revalidate_instances: whether instances of models and dataclasses (including subclass instances)
            should re-validate defaults to config.revalidate_instances, else 'never'
        strict: Whether the model is strict
        frozen: Whether the model is frozen
        extra_behavior: The extra behavior to use for the model, used in serialization
        config: The config to use for the model
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='model',
        cls=cls,
        generic_origin=generic_origin,
        schema=schema,
        custom_init=custom_init,
        root_model=root_model,
        post_init=post_init,
        revalidate_instances=revalidate_instances,
        strict=strict,
        frozen=frozen,
        extra_behavior=extra_behavior,
        config=config,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  dataclass_field [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dataclass_field)
```
dataclass_field(
    name: ,
    schema: CoreSchema,
    *,
    kw_only: | None = None,
    init: | None = None,
    init_only: | None = None,
    validation_alias: (
        | [| ] | [[| ]] | None
    ) = None,
    serialization_alias: | None = None,
    serialization_exclude: | None = None,
    metadata: [, ] | None = None,
    serialization_exclude_if: (
        [[], ] | None
    ) = None,
    frozen: | None = None
) -> DataclassField

```

Returns a schema for a dataclass field, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

field = core_schema.dataclass_field(
    name='a', schema=core_schema.str_schema(), kw_only=False
)
schema = core_schema.dataclass_args_schema('Foobar', [field])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hello'}) == ({'a': 'hello'}, None)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`name` |  |  The name to use for the argument parameter |  _required_  
`schema` |  `CoreSchema` |  The schema to use for the argument parameter |  _required_  
`kw_only` |  |  Whether the field can be set with a positional argument as well as a keyword argument |  `None`  
`init` |  |  Whether the field should be validated during initialization |  `None`  
`init_only` |  |  Whether the field should be omitted from `__dict__` and passed to `__post_init__` |  `None`  
`validation_alias` |  |  The alias(es) to use to find the field in the validation data |  `None`  
`serialization_alias` |  |  The alias to use as a key when serializing |  `None`  
`serialization_exclude` |  |  Whether to exclude the field when serializing |  `None`  
`serialization_exclude_if` |  |  A callable that determines whether to exclude the field when serializing based on its value. |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`frozen` |  |  Whether the field is frozen |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3295
3296
3297
3298
3299
3300
3301
3302
3303
3304
3305
3306
3307
3308
3309
3310
3311
3312
3313
3314
3315
3316
3317
3318
3319
3320
3321
3322
3323
3324
3325
3326
3327
3328
3329
3330
3331
3332
3333
3334
3335
3336
3337
3338
3339
3340
3341
3342
3343
3344
3345
3346
3347
3348
3349
```
| ```
defdataclass_field(
    name: str,
    schema: CoreSchema,
    *,
    kw_only: bool | None = None,
    init: bool | None = None,
    init_only: bool | None = None,
    validation_alias: str | list[str | int] | list[list[str | int]] | None = None,
    serialization_alias: str | None = None,
    serialization_exclude: bool | None = None,
    metadata: dict[str, Any] | None = None,
    serialization_exclude_if: Callable[[Any], bool] | None = None,
    frozen: bool | None = None,
) -> DataclassField:
"""
    Returns a schema for a dataclass field, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    field = core_schema.dataclass_field(
        name='a', schema=core_schema.str_schema(), kw_only=False
    )
    schema = core_schema.dataclass_args_schema('Foobar', [field])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hello'}) == ({'a': 'hello'}, None)
```

    Args:
        name: The name to use for the argument parameter
        schema: The schema to use for the argument parameter
        kw_only: Whether the field can be set with a positional argument as well as a keyword argument
        init: Whether the field should be validated during initialization
        init_only: Whether the field should be omitted  from `__dict__` and passed to `__post_init__`
        validation_alias: The alias(es) to use to find the field in the validation data
        serialization_alias: The alias to use as a key when serializing
        serialization_exclude: Whether to exclude the field when serializing
        serialization_exclude_if: A callable that determines whether to exclude the field when serializing based on its value.
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        frozen: Whether the field is frozen
    """
    return _dict_not_none(
        type='dataclass-field',
        name=name,
        schema=schema,
        kw_only=kw_only,
        init=init,
        init_only=init_only,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        serialization_exclude=serialization_exclude,
        serialization_exclude_if=serialization_exclude_if,
        metadata=metadata,
        frozen=frozen,
    )

```
  
---|---  
##  dataclass_args_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dataclass_args_schema)
```
dataclass_args_schema(
    dataclass_name: ,
    fields: [DataclassField],
    *,
    computed_fields: [ComputedField] | None = None,
    collect_init_only: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
    extra_behavior: ExtraBehavior | None = None
) -> DataclassArgsSchema

```

Returns a schema for validating dataclass arguments, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

field_a = core_schema.dataclass_field(
    name='a', schema=core_schema.str_schema(), kw_only=False
)
field_b = core_schema.dataclass_field(
    name='b', schema=core_schema.bool_schema(), kw_only=False
)
schema = core_schema.dataclass_args_schema('Foobar', [field_a, field_b])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hello', 'b': True}) == ({'a': 'hello', 'b': True}, None)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`dataclass_name` |  |  The name of the dataclass being validated |  _required_  
`fields` |  `DataclassField]` |  The fields to use for the dataclass |  _required_  
`computed_fields` |  `ComputedField] | None` |  Computed fields to use when serializing the dataclass |  `None`  
`collect_init_only` |  |  Whether to collect init only fields into a dict to pass to `__post_init__` |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
`extra_behavior` |  `ExtraBehavior | None` |  How to handle extra fields |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3364
3365
3366
3367
3368
3369
3370
3371
3372
3373
3374
3375
3376
3377
3378
3379
3380
3381
3382
3383
3384
3385
3386
3387
3388
3389
3390
3391
3392
3393
3394
3395
3396
3397
3398
3399
3400
3401
3402
3403
3404
3405
3406
3407
3408
3409
3410
3411
3412
```
| ```
defdataclass_args_schema(
    dataclass_name: str,
    fields: list[DataclassField],
    *,
    computed_fields: list[ComputedField] | None = None,
    collect_init_only: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
    extra_behavior: ExtraBehavior | None = None,
) -> DataclassArgsSchema:
"""
    Returns a schema for validating dataclass arguments, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    field_a = core_schema.dataclass_field(
        name='a', schema=core_schema.str_schema(), kw_only=False
    )
    field_b = core_schema.dataclass_field(
        name='b', schema=core_schema.bool_schema(), kw_only=False
    )
    schema = core_schema.dataclass_args_schema('Foobar', [field_a, field_b])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hello', 'b': True}) == ({'a': 'hello', 'b': True}, None)
```

    Args:
        dataclass_name: The name of the dataclass being validated
        fields: The fields to use for the dataclass
        computed_fields: Computed fields to use when serializing the dataclass
        collect_init_only: Whether to collect init only fields into a dict to pass to `__post_init__`
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
        extra_behavior: How to handle extra fields
    """
    return _dict_not_none(
        type='dataclass-args',
        dataclass_name=dataclass_name,
        fields=fields,
        computed_fields=computed_fields,
        collect_init_only=collect_init_only,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
        extra_behavior=extra_behavior,
    )

```
  
---|---  
##  dataclass_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.dataclass_schema)
```
dataclass_schema(
    cls: [],
    schema: CoreSchema,
    fields: [],
    *,
    generic_origin: [] | None = None,
    cls_name: | None = None,
    post_init: | None = None,
    revalidate_instances: (
        ["always", "never", "subclass-instances"]
        | None
    ) = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
    frozen: | None = None,
    slots: | None = None,
    config: CoreConfig[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig) | None = None
) -> DataclassSchema

```

Returns a schema for a dataclass. As with `ModelSchema`, this schema can only be used as a field within another schema, not as the root type.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  |  The dataclass type, used to perform subclass checks |  _required_  
`schema` |  `CoreSchema` |  The schema to use for the dataclass fields |  _required_  
`fields` |  |  Fields of the dataclass, this is used in serialization and in validation during re-validation and while validating assignment |  _required_  
`generic_origin` |  |  The origin type used for this dataclass, if it's a parametrized generic. Ex, if this model schema represents `SomeDataclass[int]`, generic_origin is `SomeDataclass` |  `None`  
`cls_name` |  |  The name to use in error locs, etc; this is useful for generics (default: `cls.__name__`) |  `None`  
`post_init` |  |  Whether to call `__post_init__` after validation |  `None`  
`revalidate_instances` |  |  whether instances of models and dataclasses (including subclass instances) should re-validate defaults to config.revalidate_instances, else 'never' |  `None`  
`strict` |  |  Whether to require an exact instance of `cls` |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
`frozen` |  |  Whether the dataclass is frozen |  `None`  
`slots` |  |  Whether `slots=True` on the dataclass, means each field is assigned independently, rather than simply setting `__dict__`, default false |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3433
3434
3435
3436
3437
3438
3439
3440
3441
3442
3443
3444
3445
3446
3447
3448
3449
3450
3451
3452
3453
3454
3455
3456
3457
3458
3459
3460
3461
3462
3463
3464
3465
3466
3467
3468
3469
3470
3471
3472
3473
3474
3475
3476
3477
3478
3479
3480
3481
3482
3483
3484
3485
3486
3487
3488
3489
```
| ```
defdataclass_schema(
    cls: type[Any],
    schema: CoreSchema,
    fields: list[str],
    *,
    generic_origin: type[Any] | None = None,
    cls_name: str | None = None,
    post_init: bool | None = None,
    revalidate_instances: Literal['always', 'never', 'subclass-instances'] | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
    frozen: bool | None = None,
    slots: bool | None = None,
    config: CoreConfig | None = None,
) -> DataclassSchema:
"""
    Returns a schema for a dataclass. As with `ModelSchema`, this schema can only be used as a field within
    another schema, not as the root type.

    Args:
        cls: The dataclass type, used to perform subclass checks
        schema: The schema to use for the dataclass fields
        fields: Fields of the dataclass, this is used in serialization and in validation during re-validation
            and while validating assignment
        generic_origin: The origin type used for this dataclass, if it's a parametrized generic. Ex,
            if this model schema represents `SomeDataclass[int]`, generic_origin is `SomeDataclass`
        cls_name: The name to use in error locs, etc; this is useful for generics (default: `cls.__name__`)
        post_init: Whether to call `__post_init__` after validation
        revalidate_instances: whether instances of models and dataclasses (including subclass instances)
            should re-validate defaults to config.revalidate_instances, else 'never'
        strict: Whether to require an exact instance of `cls`
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
        frozen: Whether the dataclass is frozen
        slots: Whether `slots=True` on the dataclass, means each field is assigned independently, rather than
            simply setting `__dict__`, default false
    """
    return _dict_not_none(
        type='dataclass',
        cls=cls,
        generic_origin=generic_origin,
        fields=fields,
        cls_name=cls_name,
        schema=schema,
        post_init=post_init,
        revalidate_instances=revalidate_instances,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
        frozen=frozen,
        slots=slots,
        config=config,
    )

```
  
---|---  
##  arguments_parameter [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_parameter)
```
arguments_parameter(
    name: ,
    schema: CoreSchema,
    *,
    mode: (
        [
            "positional_only",
            "positional_or_keyword",
            "keyword_only",
        ]
        | None
    ) = None,
    alias: (
        | [| ] | [[| ]] | None
    ) = None
) -> ArgumentsParameter

```

Returns a schema that matches an argument parameter, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

param = core_schema.arguments_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
schema = core_schema.arguments_schema([param])
v = SchemaValidator(schema)
assert v.validate_python(('hello',)) == (('hello',), {})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`name` |  |  The name to use for the argument parameter |  _required_  
`schema` |  `CoreSchema` |  The schema to use for the argument parameter |  _required_  
`mode` |  |  The mode to use for the argument parameter |  `None`  
`alias` |  |  The alias to use for the argument parameter |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3499
3500
3501
3502
3503
3504
3505
3506
3507
3508
3509
3510
3511
3512
3513
3514
3515
3516
3517
3518
3519
3520
3521
3522
3523
3524
3525
3526
```
| ```
defarguments_parameter(
    name: str,
    schema: CoreSchema,
    *,
    mode: Literal['positional_only', 'positional_or_keyword', 'keyword_only'] | None = None,
    alias: str | list[str | int] | list[list[str | int]] | None = None,
) -> ArgumentsParameter:
"""
    Returns a schema that matches an argument parameter, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param = core_schema.arguments_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    schema = core_schema.arguments_schema([param])
    v = SchemaValidator(schema)
    assert v.validate_python(('hello',)) == (('hello',), {})
```

    Args:
        name: The name to use for the argument parameter
        schema: The schema to use for the argument parameter
        mode: The mode to use for the argument parameter
        alias: The alias to use for the argument parameter
    """
    return _dict_not_none(name=name, schema=schema, mode=mode, alias=alias)

```
  
---|---  
##  arguments_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_schema)
```
arguments_schema(
    arguments: [ArgumentsParameter],
    *,
    validate_by_name: | None = None,
    validate_by_alias: | None = None,
    var_args_schema: CoreSchema | None = None,
    var_kwargs_mode: VarKwargsMode | None = None,
    var_kwargs_schema: CoreSchema | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ArgumentsSchema

```

Returns a schema that matches an arguments schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

param_a = core_schema.arguments_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
param_b = core_schema.arguments_parameter(
    name='b', schema=core_schema.bool_schema(), mode='positional_only'
)
schema = core_schema.arguments_schema([param_a, param_b])
v = SchemaValidator(schema)
assert v.validate_python(('hello', True)) == (('hello', True), {})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`arguments` |  `ArgumentsParameter]` |  The arguments to use for the arguments schema |  _required_  
`validate_by_name` |  |  Whether to populate by the parameter names, defaults to `False`. |  `None`  
`validate_by_alias` |  |  Whether to populate by the parameter aliases, defaults to `True`. |  `None`  
`var_args_schema` |  `CoreSchema | None` |  The variable args schema to use for the arguments schema |  `None`  
`var_kwargs_mode` |  `VarKwargsMode | None` |  The validation mode to use for variadic keyword arguments. If `'uniform'`, every value of the keyword arguments will be validated against the `var_kwargs_schema` schema. If `'unpacked-typed-dict'`, the `var_kwargs_schema` argument must be a [`typed_dict_schema`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_schema) |  `None`  
`var_kwargs_schema` |  `CoreSchema | None` |  The variable kwargs schema to use for the arguments schema |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3545
3546
3547
3548
3549
3550
3551
3552
3553
3554
3555
3556
3557
3558
3559
3560
3561
3562
3563
3564
3565
3566
3567
3568
3569
3570
3571
3572
3573
3574
3575
3576
3577
3578
3579
3580
3581
3582
3583
3584
3585
3586
3587
3588
3589
3590
3591
3592
3593
3594
3595
3596
3597
3598
```
| ```
defarguments_schema(
    arguments: list[ArgumentsParameter],
    *,
    validate_by_name: bool | None = None,
    validate_by_alias: bool | None = None,
    var_args_schema: CoreSchema | None = None,
    var_kwargs_mode: VarKwargsMode | None = None,
    var_kwargs_schema: CoreSchema | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ArgumentsSchema:
"""
    Returns a schema that matches an arguments schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param_a = core_schema.arguments_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    param_b = core_schema.arguments_parameter(
        name='b', schema=core_schema.bool_schema(), mode='positional_only'
    )
    schema = core_schema.arguments_schema([param_a, param_b])
    v = SchemaValidator(schema)
    assert v.validate_python(('hello', True)) == (('hello', True), {})
```

    Args:
        arguments: The arguments to use for the arguments schema
        validate_by_name: Whether to populate by the parameter names, defaults to `False`.
        validate_by_alias: Whether to populate by the parameter aliases, defaults to `True`.
        var_args_schema: The variable args schema to use for the arguments schema
        var_kwargs_mode: The validation mode to use for variadic keyword arguments. If `'uniform'`, every value of the
            keyword arguments will be validated against the `var_kwargs_schema` schema. If `'unpacked-typed-dict'`,
            the `var_kwargs_schema` argument must be a [`typed_dict_schema`][pydantic_core.core_schema.typed_dict_schema]
        var_kwargs_schema: The variable kwargs schema to use for the arguments schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='arguments',
        arguments_schema=arguments,
        validate_by_name=validate_by_name,
        validate_by_alias=validate_by_alias,
        var_args_schema=var_args_schema,
        var_kwargs_mode=var_kwargs_mode,
        var_kwargs_schema=var_kwargs_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  arguments_v3_parameter [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_v3_parameter)
```
arguments_v3_parameter(
    name: ,
    schema: CoreSchema,
    *,
    mode: (
        [
            "positional_only",
            "positional_or_keyword",
            "keyword_only",
            "var_args",
            "var_kwargs_uniform",
            "var_kwargs_unpacked_typed_dict",
        ]
        | None
    ) = None,
    alias: (
        | [| ] | [[| ]] | None
    ) = None
) -> ArgumentsV3Parameter

```

Returns a schema that matches an argument parameter, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

param = core_schema.arguments_v3_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
schema = core_schema.arguments_v3_schema([param])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hello'}) == (('hello',), {})

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`name` |  |  The name to use for the argument parameter |  _required_  
`schema` |  `CoreSchema` |  The schema to use for the argument parameter |  _required_  
`mode` |  |  The mode to use for the argument parameter |  `None`  
`alias` |  |  The alias to use for the argument parameter |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3615
3616
3617
3618
3619
3620
3621
3622
3623
3624
3625
3626
3627
3628
3629
3630
3631
3632
3633
3634
3635
3636
3637
3638
3639
3640
3641
3642
3643
3644
3645
3646
3647
3648
3649
3650
```
| ```
defarguments_v3_parameter(
    name: str,
    schema: CoreSchema,
    *,
    mode: Literal[
        'positional_only',
        'positional_or_keyword',
        'keyword_only',
        'var_args',
        'var_kwargs_uniform',
        'var_kwargs_unpacked_typed_dict',
    ]
    | None = None,
    alias: str | list[str | int] | list[list[str | int]] | None = None,
) -> ArgumentsV3Parameter:
"""
    Returns a schema that matches an argument parameter, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param = core_schema.arguments_v3_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    schema = core_schema.arguments_v3_schema([param])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hello'}) == (('hello',), {})
```

    Args:
        name: The name to use for the argument parameter
        schema: The schema to use for the argument parameter
        mode: The mode to use for the argument parameter
        alias: The alias to use for the argument parameter
    """
    return _dict_not_none(name=name, schema=schema, mode=mode, alias=alias)

```
  
---|---  
##  arguments_v3_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.arguments_v3_schema)
```
arguments_v3_schema(
    arguments: [ArgumentsV3Parameter],
    *,
    validate_by_name: | None = None,
    validate_by_alias: | None = None,
    extra_behavior: (
        ["forbid", "ignore"] | None
    ) = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> ArgumentsV3Schema

```

Returns a schema that matches an arguments schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

param_a = core_schema.arguments_v3_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
param_b = core_schema.arguments_v3_parameter(
    name='kwargs', schema=core_schema.bool_schema(), mode='var_kwargs_uniform'
)
schema = core_schema.arguments_v3_schema([param_a, param_b])
v = SchemaValidator(schema)
assert v.validate_python({'a': 'hi', 'kwargs': {'b': True}}) == (('hi',), {'b': True})

```

This schema is currently not used by other Pydantic components. In V3, it will most likely become the default arguments schema for the `'call'` schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`arguments` |  `ArgumentsV3Parameter]` |  The arguments to use for the arguments schema. |  _required_  
`validate_by_name` |  |  Whether to populate by the parameter names, defaults to `False`. |  `None`  
`validate_by_alias` |  |  Whether to populate by the parameter aliases, defaults to `True`. |  `None`  
`extra_behavior` |  |  The extra behavior to use. |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places. |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core. |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema. |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3664
3665
3666
3667
3668
3669
3670
3671
3672
3673
3674
3675
3676
3677
3678
3679
3680
3681
3682
3683
3684
3685
3686
3687
3688
3689
3690
3691
3692
3693
3694
3695
3696
3697
3698
3699
3700
3701
3702
3703
3704
3705
3706
3707
3708
3709
3710
3711
3712
```
| ```
defarguments_v3_schema(
    arguments: list[ArgumentsV3Parameter],
    *,
    validate_by_name: bool | None = None,
    validate_by_alias: bool | None = None,
    extra_behavior: Literal['forbid', 'ignore'] | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> ArgumentsV3Schema:
"""
    Returns a schema that matches an arguments schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param_a = core_schema.arguments_v3_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    param_b = core_schema.arguments_v3_parameter(
        name='kwargs', schema=core_schema.bool_schema(), mode='var_kwargs_uniform'
    )
    schema = core_schema.arguments_v3_schema([param_a, param_b])
    v = SchemaValidator(schema)
    assert v.validate_python({'a': 'hi', 'kwargs': {'b': True}}) == (('hi',), {'b': True})
```

    This schema is currently not used by other Pydantic components. In V3, it will most likely
    become the default arguments schema for the `'call'` schema.

    Args:
        arguments: The arguments to use for the arguments schema.
        validate_by_name: Whether to populate by the parameter names, defaults to `False`.
        validate_by_alias: Whether to populate by the parameter aliases, defaults to `True`.
        extra_behavior: The extra behavior to use.
        ref: optional unique identifier of the schema, used to reference the schema in other places.
        metadata: Any other information you want to include with the schema, not used by pydantic-core.
        serialization: Custom serialization schema.
    """
    return _dict_not_none(
        type='arguments-v3',
        arguments_schema=arguments,
        validate_by_name=validate_by_name,
        validate_by_alias=validate_by_alias,
        extra_behavior=extra_behavior,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  call_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.call_schema)
```
call_schema(
    arguments: CoreSchema,
    function: [..., ],
    *,
    function_name: | None = None,
    return_schema: CoreSchema | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> CallSchema

```

Returns a schema that matches an arguments schema, then calls a function, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

param_a = core_schema.arguments_parameter(
    name='a', schema=core_schema.str_schema(), mode='positional_only'
)
param_b = core_schema.arguments_parameter(
    name='b', schema=core_schema.bool_schema(), mode='positional_only'
)
args_schema = core_schema.arguments_schema([param_a, param_b])

schema = core_schema.call_schema(
    arguments=args_schema,
    function=lambda a, b: a + str(not b),
    return_schema=core_schema.str_schema(),
)
v = SchemaValidator(schema)
assert v.validate_python((('hello', True))) == 'helloFalse'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`arguments` |  `CoreSchema` |  The arguments to use for the arguments schema |  _required_  
`function` |  |  The function to use for the call schema |  _required_  
`function_name` |  |  The function name to use for the call schema, if not provided `function.__name__` is used |  `None`  
`return_schema` |  `CoreSchema | None` |  The return schema to use for the call schema |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3726
3727
3728
3729
3730
3731
3732
3733
3734
3735
3736
3737
3738
3739
3740
3741
3742
3743
3744
3745
3746
3747
3748
3749
3750
3751
3752
3753
3754
3755
3756
3757
3758
3759
3760
3761
3762
3763
3764
3765
3766
3767
3768
3769
3770
3771
3772
3773
3774
3775
3776
3777
```
| ```
defcall_schema(
    arguments: CoreSchema,
    function: Callable[..., Any],
    *,
    function_name: str | None = None,
    return_schema: CoreSchema | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> CallSchema:
"""
    Returns a schema that matches an arguments schema, then calls a function, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    param_a = core_schema.arguments_parameter(
        name='a', schema=core_schema.str_schema(), mode='positional_only'
    )
    param_b = core_schema.arguments_parameter(
        name='b', schema=core_schema.bool_schema(), mode='positional_only'
    )
    args_schema = core_schema.arguments_schema([param_a, param_b])

    schema = core_schema.call_schema(
        arguments=args_schema,
        function=lambda a, b: a + str(not b),
        return_schema=core_schema.str_schema(),
    )
    v = SchemaValidator(schema)
    assert v.validate_python((('hello', True))) == 'helloFalse'
```

    Args:
        arguments: The arguments to use for the arguments schema
        function: The function to use for the call schema
        function_name: The function name to use for the call schema, if not provided `function.__name__` is used
        return_schema: The return schema to use for the call schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='call',
        arguments_schema=arguments,
        function=function,
        function_name=function_name,
        return_schema=return_schema,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  custom_error_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.custom_error_schema)
```
custom_error_schema(
    schema: CoreSchema,
    custom_error_type: ,
    *,
    custom_error_message: | None = None,
    custom_error_context: [, ] | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> CustomErrorSchema

```

Returns a schema that matches a custom error value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.custom_error_schema(
    schema=core_schema.int_schema(),
    custom_error_type='MyError',
    custom_error_message='Error msg',
)
v = SchemaValidator(schema)
v.validate_python(1)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The schema to use for the custom error schema |  _required_  
`custom_error_type` |  |  The custom error type to use for the custom error schema |  _required_  
`custom_error_message` |  |  The custom error message to use for the custom error schema |  `None`  
`custom_error_context` |  |  The custom error context to use for the custom error schema |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3791
3792
3793
3794
3795
3796
3797
3798
3799
3800
3801
3802
3803
3804
3805
3806
3807
3808
3809
3810
3811
3812
3813
3814
3815
3816
3817
3818
3819
3820
3821
3822
3823
3824
3825
3826
3827
3828
3829
3830
3831
3832
3833
3834
```
| ```
defcustom_error_schema(
    schema: CoreSchema,
    custom_error_type: str,
    *,
    custom_error_message: str | None = None,
    custom_error_context: dict[str, Any] | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> CustomErrorSchema:
"""
    Returns a schema that matches a custom error value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.custom_error_schema(
        schema=core_schema.int_schema(),
        custom_error_type='MyError',
        custom_error_message='Error msg',
    )
    v = SchemaValidator(schema)
    v.validate_python(1)
```

    Args:
        schema: The schema to use for the custom error schema
        custom_error_type: The custom error type to use for the custom error schema
        custom_error_message: The custom error message to use for the custom error schema
        custom_error_context: The custom error context to use for the custom error schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='custom-error',
        schema=schema,
        custom_error_type=custom_error_type,
        custom_error_message=custom_error_message,
        custom_error_context=custom_error_context,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  json_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.json_schema)
```
json_schema(
    schema: CoreSchema | None = None,
    *,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> JsonSchema

```

Returns a schema that matches a JSON value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

dict_schema = core_schema.model_fields_schema(
    {
        'field_a': core_schema.model_field(core_schema.str_schema()),
        'field_b': core_schema.model_field(core_schema.bool_schema()),
    },
)

classMyModel:
    __slots__ = (
        '__dict__',
        '__pydantic_fields_set__',
        '__pydantic_extra__',
        '__pydantic_private__',
    )
    field_a: str
    field_b: bool

json_schema = core_schema.json_schema(schema=dict_schema)
schema = core_schema.model_schema(cls=MyModel, schema=json_schema)
v = SchemaValidator(schema)
m = v.validate_python('{"field_a": "hello", "field_b": true}')
assert isinstance(m, MyModel)

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema | None` |  The schema to use for the JSON schema |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3845
3846
3847
3848
3849
3850
3851
3852
3853
3854
3855
3856
3857
3858
3859
3860
3861
3862
3863
3864
3865
3866
3867
3868
3869
3870
3871
3872
3873
3874
3875
3876
3877
3878
3879
3880
3881
3882
3883
3884
3885
3886
3887
3888
```
| ```
defjson_schema(
    schema: CoreSchema | None = None,
    *,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> JsonSchema:
"""
    Returns a schema that matches a JSON value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    dict_schema = core_schema.model_fields_schema(
        {
            'field_a': core_schema.model_field(core_schema.str_schema()),
            'field_b': core_schema.model_field(core_schema.bool_schema()),
        },
    )

    class MyModel:
        __slots__ = (
            '__dict__',
            '__pydantic_fields_set__',
            '__pydantic_extra__',
            '__pydantic_private__',
        )
        field_a: str
        field_b: bool

    json_schema = core_schema.json_schema(schema=dict_schema)
    schema = core_schema.model_schema(cls=MyModel, schema=json_schema)
    v = SchemaValidator(schema)
    m = v.validate_python('{"field_a": "hello", "field_b": true}')
    assert isinstance(m, MyModel)
```

    Args:
        schema: The schema to use for the JSON schema
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(type='json', schema=schema, ref=ref, metadata=metadata, serialization=serialization)

```
  
---|---  
##  url_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.url_schema)
```
url_schema(
    *,
    max_length: | None = None,
    allowed_schemes: [] | None = None,
    host_required: | None = None,
    default_host: | None = None,
    default_port: | None = None,
    default_path: | None = None,
    preserve_empty_path: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> UrlSchema

```

Returns a schema that matches a URL value, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.url_schema()
v = SchemaValidator(schema)
print(v.validate_python('https://example.com'))
#> https://example.com/

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`max_length` |  |  The maximum length of the URL |  `None`  
`allowed_schemes` |  |  The allowed URL schemes |  `None`  
`host_required` |  |  Whether the URL must have a host |  `None`  
`default_host` |  |  The default host to use if the URL does not have a host |  `None`  
`default_port` |  |  The default port to use if the URL does not have a port |  `None`  
`default_path` |  |  The default path to use if the URL does not have a path |  `None`  
`preserve_empty_path` |  |  Whether to preserve an empty path or convert it to '/', default False |  `None`  
`strict` |  |  Whether to use strict URL parsing |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3905
3906
3907
3908
3909
3910
3911
3912
3913
3914
3915
3916
3917
3918
3919
3920
3921
3922
3923
3924
3925
3926
3927
3928
3929
3930
3931
3932
3933
3934
3935
3936
3937
3938
3939
3940
3941
3942
3943
3944
3945
3946
3947
3948
3949
3950
3951
3952
3953
3954
3955
3956
3957
```
| ```
defurl_schema(
    *,
    max_length: int | None = None,
    allowed_schemes: list[str] | None = None,
    host_required: bool | None = None,
    default_host: str | None = None,
    default_port: int | None = None,
    default_path: str | None = None,
    preserve_empty_path: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> UrlSchema:
"""
    Returns a schema that matches a URL value, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.url_schema()
    v = SchemaValidator(schema)
    print(v.validate_python('https://example.com'))
    #> https://example.com/
```

    Args:
        max_length: The maximum length of the URL
        allowed_schemes: The allowed URL schemes
        host_required: Whether the URL must have a host
        default_host: The default host to use if the URL does not have a host
        default_port: The default port to use if the URL does not have a port
        default_path: The default path to use if the URL does not have a path
        preserve_empty_path: Whether to preserve an empty path or convert it to '/', default False
        strict: Whether to use strict URL parsing
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='url',
        max_length=max_length,
        allowed_schemes=allowed_schemes,
        host_required=host_required,
        default_host=default_host,
        default_port=default_port,
        default_path=default_path,
        preserve_empty_path=preserve_empty_path,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  multi_host_url_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.multi_host_url_schema)
```
multi_host_url_schema(
    *,
    max_length: | None = None,
    allowed_schemes: [] | None = None,
    host_required: | None = None,
    default_host: | None = None,
    default_port: | None = None,
    default_path: | None = None,
    preserve_empty_path: | None = None,
    strict: | None = None,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None
) -> MultiHostUrlSchema

```

Returns a schema that matches a URL value with possibly multiple hosts, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.multi_host_url_schema()
v = SchemaValidator(schema)
print(v.validate_python('redis://localhost,0.0.0.0,127.0.0.1'))
#> redis://localhost,0.0.0.0,127.0.0.1

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`max_length` |  |  The maximum length of the URL |  `None`  
`allowed_schemes` |  |  The allowed URL schemes |  `None`  
`host_required` |  |  Whether the URL must have a host |  `None`  
`default_host` |  |  The default host to use if the URL does not have a host |  `None`  
`default_port` |  |  The default port to use if the URL does not have a port |  `None`  
`default_path` |  |  The default path to use if the URL does not have a path |  `None`  
`preserve_empty_path` |  |  Whether to preserve an empty path or convert it to '/', default False |  `None`  
`strict` |  |  Whether to use strict URL parsing |  `None`  
`ref` |  |  optional unique identifier of the schema, used to reference the schema in other places |  `None`  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
3974
3975
3976
3977
3978
3979
3980
3981
3982
3983
3984
3985
3986
3987
3988
3989
3990
3991
3992
3993
3994
3995
3996
3997
3998
3999
4000
4001
4002
4003
4004
4005
4006
4007
4008
4009
4010
4011
4012
4013
4014
4015
4016
4017
4018
4019
4020
4021
4022
4023
4024
4025
4026
```
| ```
defmulti_host_url_schema(
    *,
    max_length: int | None = None,
    allowed_schemes: list[str] | None = None,
    host_required: bool | None = None,
    default_host: str | None = None,
    default_port: int | None = None,
    default_path: str | None = None,
    preserve_empty_path: bool | None = None,
    strict: bool | None = None,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> MultiHostUrlSchema:
"""
    Returns a schema that matches a URL value with possibly multiple hosts, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.multi_host_url_schema()
    v = SchemaValidator(schema)
    print(v.validate_python('redis://localhost,0.0.0.0,127.0.0.1'))
    #> redis://localhost,0.0.0.0,127.0.0.1
```

    Args:
        max_length: The maximum length of the URL
        allowed_schemes: The allowed URL schemes
        host_required: Whether the URL must have a host
        default_host: The default host to use if the URL does not have a host
        default_port: The default port to use if the URL does not have a port
        default_path: The default path to use if the URL does not have a path
        preserve_empty_path: Whether to preserve an empty path or convert it to '/', default False
        strict: Whether to use strict URL parsing
        ref: optional unique identifier of the schema, used to reference the schema in other places
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='multi-host-url',
        max_length=max_length,
        allowed_schemes=allowed_schemes,
        host_required=host_required,
        default_host=default_host,
        default_port=default_port,
        default_path=default_path,
        preserve_empty_path=preserve_empty_path,
        strict=strict,
        ref=ref,
        metadata=metadata,
        serialization=serialization,
    )

```
  
---|---  
##  definitions_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.definitions_schema)
```
definitions_schema(
    schema: CoreSchema, definitions: [CoreSchema]
) -> DefinitionsSchema

```

Build a schema that contains both an inner schema and a list of definitions which can be used within the inner schema.
```
frompydantic_coreimport SchemaValidator, core_schema

schema = core_schema.definitions_schema(
    core_schema.list_schema(core_schema.definition_reference_schema('foobar')),
    [core_schema.int_schema(ref='foobar')],
)
v = SchemaValidator(schema)
assert v.validate_python([1, 2, '3']) == [1, 2, 3]

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  The inner schema |  _required_  
`definitions` |  `CoreSchema]` |  List of definitions which can be referenced within inner schema |  _required_  
Source code in `pydantic_core/core_schema.py`
```
4037
4038
4039
4040
4041
4042
4043
4044
4045
4046
4047
4048
4049
4050
4051
4052
4053
4054
4055
4056
4057
```
| ```
defdefinitions_schema(schema: CoreSchema, definitions: list[CoreSchema]) -> DefinitionsSchema:
"""
    Build a schema that contains both an inner schema and a list of definitions which can be used
    within the inner schema.

```py
    from pydantic_core import SchemaValidator, core_schema

    schema = core_schema.definitions_schema(
        core_schema.list_schema(core_schema.definition_reference_schema('foobar')),
        [core_schema.int_schema(ref='foobar')],
    )
    v = SchemaValidator(schema)
    assert v.validate_python([1, 2, '3']) == [1, 2, 3]
```

    Args:
        schema: The inner schema
        definitions: List of definitions which can be referenced within inner schema
    """
    return DefinitionsSchema(type='definitions', schema=schema, definitions=definitions)

```
  
---|---  
##  definition_reference_schema [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.definition_reference_schema)
```
definition_reference_schema(
    schema_ref: ,
    ref: | None = None,
    metadata: [, ] | None = None,
    serialization: SerSchema | None = None,
) -> DefinitionReferenceSchema

```

Returns a schema that points to a schema stored in "definitions", this is useful for nested recursive models and also when you want to define validators separately from the main schema, e.g.:
```
frompydantic_coreimport SchemaValidator, core_schema

schema_definition = core_schema.definition_reference_schema('list-schema')
schema = core_schema.definitions_schema(
    schema=schema_definition,
    definitions=[
        core_schema.list_schema(items_schema=schema_definition, ref='list-schema'),
    ],
)
v = SchemaValidator(schema)
assert v.validate_python([()]) == [[]]

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema_ref` |  |  The schema ref to use for the definition reference schema |  _required_  
`metadata` |  |  Any other information you want to include with the schema, not used by pydantic-core |  `None`  
`serialization` |  `SerSchema | None` |  Custom serialization schema |  `None`  
Source code in `pydantic_core/core_schema.py`
```
4068
4069
4070
4071
4072
4073
4074
4075
4076
4077
4078
4079
4080
4081
4082
4083
4084
4085
4086
4087
4088
4089
4090
4091
4092
4093
4094
4095
4096
4097
4098
4099
```
| ```
defdefinition_reference_schema(
    schema_ref: str,
    ref: str | None = None,
    metadata: dict[str, Any] | None = None,
    serialization: SerSchema | None = None,
) -> DefinitionReferenceSchema:
"""
    Returns a schema that points to a schema stored in "definitions", this is useful for nested recursive
    models and also when you want to define validators separately from the main schema, e.g.:

```py
    from pydantic_core import SchemaValidator, core_schema

    schema_definition = core_schema.definition_reference_schema('list-schema')
    schema = core_schema.definitions_schema(
        schema=schema_definition,
        definitions=[
            core_schema.list_schema(items_schema=schema_definition, ref='list-schema'),
        ],
    )
    v = SchemaValidator(schema)
    assert v.validate_python([()]) == [[]]
```

    Args:
        schema_ref: The schema ref to use for the definition reference schema
        metadata: Any other information you want to include with the schema, not used by pydantic-core
        serialization: Custom serialization schema
    """
    return _dict_not_none(
        type='definition-ref', schema_ref=schema_ref, ref=ref, metadata=metadata, serialization=serialization
    )

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
