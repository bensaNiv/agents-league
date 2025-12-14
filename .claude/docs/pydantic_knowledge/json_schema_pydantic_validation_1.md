---
# Smart Librarian Export (v2.0)
- Page Number: 51
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/json_schema
- Page Title: JSON Schema - Pydantic Validation
- Semantic Filename: json_schema_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 174,142 characters
---

# JSON Schema - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# JSON Schema
Usage Documentation
[JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
The `json_schema` module contains classes and functions to allow the way 
In general you shouldn't need to use this module directly; instead, you can use [`BaseModel.model_json_schema`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema) and [`TypeAdapter.json_schema`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.json_schema).
##  CoreSchemaOrFieldType `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.CoreSchemaOrFieldType)
```
CoreSchemaOrFieldType = [
    CoreSchemaType, CoreSchemaFieldType
]

```

A type alias for defined schema types that represents a union of `core_schema.CoreSchemaType` and `core_schema.CoreSchemaFieldType`.
##  JsonSchemaValue `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)
```
JsonSchemaValue = [, ]

```

A type alias for a JSON schema value. This is a dictionary of string keys to arbitrary JSON values.
##  JsonSchemaMode `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)
```
JsonSchemaMode = ['validation', 'serialization']

```

A type alias that represents the mode of a JSON schema; either 'validation' or 'serialization'.
For some types, the inputs to validation differ from the outputs of serialization. For example, computed fields will only be present when serializing, and should not be provided when validating. This flag provides a way to indicate whether you want the JSON schema required for validation inputs, or that will be matched by serialization outputs.
##  JsonSchemaWarningKind `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind)
```
JsonSchemaWarningKind = [
    "skipped-choice",
    "non-serializable-default",
    "skipped-discriminator",
]

```

A type alias representing the kinds of warnings that can be emitted during JSON schema generation.
See [`GenerateJsonSchema.render_warning_message`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.render_warning_message) for more details.
##  NoDefault `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.NoDefault)
```
NoDefault = ()

```

A sentinel value used to indicate that no default value should be used when generating a JSON Schema for a core schema with a default value.
##  DEFAULT_REF_TEMPLATE `module-attribute` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)
```
DEFAULT_REF_TEMPLATE = '#/$defs/{model}'

```

The default format string used to generate reference names.
##  PydanticJsonSchemaWarning [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.PydanticJsonSchemaWarning)
Bases: 
This class is used to emit warnings produced during JSON schema generation. See the [`GenerateJsonSchema.emit_warning`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.emit_warning) and [`GenerateJsonSchema.render_warning_message`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.render_warning_message) methods for more details; these can be overridden to control warning behavior.
##  GenerateJsonSchema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
```
GenerateJsonSchema(
    by_alias: = True,
    ref_template: = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
)

```

Usage Documentation
[Customizing the JSON Schema Generation Process](https://docs.pydantic.dev/latest/concepts/json_schema/#customizing-the-json-schema-generation-process)
A class for generating JSON schemas.
This class generates JSON schemas based on configured parameters. The default schema dialect is `by_alias` to configure how fields with multiple names are handled and `ref_template` to format reference names.
Attributes:
Name | Type | Description  
---|---|---  
`schema_dialect` |  |  The JSON schema dialect used to generate the schema. See   
`ignored_warning_kinds` |  `JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind)]` |  Warnings to ignore when generating the schema. `self.render_warning_message` will do nothing if its argument `kind` is in `ignored_warning_kinds`; this value can be modified on subclasses to easily control which warnings are emitted.  
`by_alias` |  |  Whether to use field aliases when generating the schema.  
`ref_template` |  |  The format string used when generating reference names.  
`core_to_json_refs` |  `CoreModeRef, JsonRef]` |  A mapping of core refs to JSON refs.  
`core_to_defs_refs` |  `CoreModeRef, DefsRef]` |  A mapping of core refs to definition refs.  
`defs_to_core_refs` |  `DefsRef, CoreModeRef]` |  A mapping of definition refs to core refs.  
`json_to_defs_refs` |  `JsonRef, DefsRef]` |  A mapping of JSON refs to definition refs.  
`definitions` |  `DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  Definitions in the schema.  
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`by_alias` |  |  Whether to use field aliases in the generated schemas. |  `True`  
`ref_template` |  |  The format string to use when generating reference names. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)`  
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the 
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`  
Raises:
Type | Description  
---|---  
`JsonSchemaError` |  If the instance of the class is inadvertently reused after generating a schema.  
Source code in `pydantic/json_schema.py`
```
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
```
| ```
def__init__(
    self,
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
) -> None:
    self.by_alias = by_alias
    self.ref_template = ref_template
    self.union_format: Literal['any_of', 'primitive_type_array'] = union_format

    self.core_to_json_refs: dict[CoreModeRef, JsonRef] = {}
    self.core_to_defs_refs: dict[CoreModeRef, DefsRef] = {}
    self.defs_to_core_refs: dict[DefsRef, CoreModeRef] = {}
    self.json_to_defs_refs: dict[JsonRef, DefsRef] = {}

    self.definitions: dict[DefsRef, JsonSchemaValue] = {}
    self._config_wrapper_stack = _config.ConfigWrapperStack(_config.ConfigWrapper({}))

    self._mode: JsonSchemaMode = 'validation'

    # The following includes a mapping of a fully-unique defs ref choice to a list of preferred
    # alternatives, which are generally simpler, such as only including the class name.
    # At the end of schema generation, we use these to produce a JSON schema with more human-readable
    # definitions, which would also work better in a generated OpenAPI client, etc.
    self._prioritized_defsref_choices: dict[DefsRef, list[DefsRef]] = {}
    self._collision_counter: dict[str, int] = defaultdict(int)
    self._collision_index: dict[str, int] = {}

    self._schema_type_to_method = self.build_schema_type_to_method()

    # When we encounter definitions we need to try to build them immediately
    # so that they are available schemas that reference them
    # But it's possible that CoreSchema was never going to be used
    # (e.g. because the CoreSchema that references short circuits is JSON schema generation without needing
    #  the reference) so instead of failing altogether if we can't build a definition we
    # store the error raised and re-throw it if we end up needing that def
    self._core_defs_invalid_for_json_schema: dict[DefsRef, PydanticInvalidForJsonSchema] = {}

    # This changes to True after generating a schema, to prevent issues caused by accidental reuse
    # of a single instance of a schema generator
    self._used = False

```
  
---|---  
###  ValidationsMapping [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.ValidationsMapping)
This class just contains mappings from core_schema attribute names to the corresponding JSON schema attribute names. While I suspect it is unlikely to be necessary, you can in principle override this class in a subclass of GenerateJsonSchema (by inheriting from GenerateJsonSchema.ValidationsMapping) to change these mappings.
###  build_schema_type_to_method [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.build_schema_type_to_method)
```
build_schema_type_to_method() -> [
    CoreSchemaOrFieldType[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.CoreSchemaOrFieldType),
    [[CoreSchemaOrField], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)],
]

```

Builds a dictionary mapping fields to methods for generating JSON schemas.
Returns:
Type | Description  
---|---  
`CoreSchemaOrFieldType[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.CoreSchemaOrFieldType), CoreSchemaOrField], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]]` |  A dictionary containing the mapping of `CoreSchemaOrFieldType` to a handler method.  
Raises:
Type | Description  
---|---  
|  If no method has been defined for generating a JSON schema for a given pydantic core schema type.  
Source code in `pydantic/json_schema.py`
```
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
342
343
```
| ```
defbuild_schema_type_to_method(
    self,
) -> dict[CoreSchemaOrFieldType, Callable[[CoreSchemaOrField], JsonSchemaValue]]:
"""Builds a dictionary mapping fields to methods for generating JSON schemas.

    Returns:
        A dictionary containing the mapping of `CoreSchemaOrFieldType` to a handler method.

    Raises:
        TypeError: If no method has been defined for generating a JSON schema for a given pydantic core schema type.
    """
    mapping: dict[CoreSchemaOrFieldType, Callable[[CoreSchemaOrField], JsonSchemaValue]] = {}
    core_schema_types: list[CoreSchemaOrFieldType] = list(get_literal_values(CoreSchemaOrFieldType))
    for key in core_schema_types:
        method_name = f'{key.replace("-","_")}_schema'
        try:
            mapping[key] = getattr(self, method_name)
        except AttributeError as e:  # pragma: no cover
            if os.getenv('PYDANTIC_PRIVATE_ALLOW_UNHANDLED_SCHEMA_TYPES'):
                continue
            raise TypeError(
                f'No method for generating JsonSchema for core_schema.type={key!r} '
                f'(expected: {type(self).__name__}.{method_name})'
            ) frome
    return mapping

```
  
---|---  
###  generate_definitions [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate_definitions)
```
generate_definitions(
    inputs: [
        [JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode), CoreSchema]
    ]
) -> [
    [
        [JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)],
        JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
    ],
    [DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)],
]

```

Generates JSON schema definitions from a list of core schemas, pairing the generated definitions with a mapping that links the input keys to the definition references.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`inputs` |  `JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode), CoreSchema]]` |  A sequence of tuples, where:
  * The first element is a JSON schema key type.
  * The second element is the JSON mode: either 'validation' or 'serialization'.
  * The third element is a core schema.

|  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)], DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]]` |  A tuple where:
  * The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.)
  * The second element is a dictionary whose keys are definition references for the JSON schemas from the first returned element, and whose values are the actual JSON schema definitions.

  
Raises:
Type | Description  
---|---  
`PydanticUserError[](https://docs.pydantic.dev/latest/api/errors/#pydantic.errors.PydanticUserError)` |  Raised if the JSON schema generator has already been used to generate a JSON schema.  
Source code in `pydantic/json_schema.py`
```
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
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
```
| ```
defgenerate_definitions(
    self, inputs: Sequence[tuple[JsonSchemaKeyT, JsonSchemaMode, core_schema.CoreSchema]]
) -> tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], dict[DefsRef, JsonSchemaValue]]:
"""Generates JSON schema definitions from a list of core schemas, pairing the generated definitions with a
    mapping that links the input keys to the definition references.

    Args:
        inputs: A sequence of tuples, where:

            - The first element is a JSON schema key type.
            - The second element is the JSON mode: either 'validation' or 'serialization'.
            - The third element is a core schema.

    Returns:
        A tuple where:

            - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and
                whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have
                JsonRef references to definitions that are defined in the second returned element.)
            - The second element is a dictionary whose keys are definition references for the JSON schemas
                from the first returned element, and whose values are the actual JSON schema definitions.

    Raises:
        PydanticUserError: Raised if the JSON schema generator has already been used to generate a JSON schema.
    """
    if self._used:
        raise PydanticUserError(
            'This JSON schema generator has already been used to generate a JSON schema. '
            f'You must create a new instance of {type(self).__name__} to generate a new JSON schema.',
            code='json-schema-already-used',
        )

    for _, mode, schema in inputs:
        self._mode = mode
        self.generate_inner(schema)

    definitions_remapping = self._build_definitions_remapping()

    json_schemas_map: dict[tuple[JsonSchemaKeyT, JsonSchemaMode], DefsRef] = {}
    for key, mode, schema in inputs:
        self._mode = mode
        json_schema = self.generate_inner(schema)
        json_schemas_map[(key, mode)] = definitions_remapping.remap_json_schema(json_schema)

    json_schema = {'$defs': self.definitions}
    json_schema = definitions_remapping.remap_json_schema(json_schema)
    self._used = True
    return json_schemas_map, self.sort(json_schema['$defs'])  # type: ignore

```
  
---|---  
###  generate [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate)
```
generate(
    schema: CoreSchema, mode: JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode) = "validation"
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema for a specified schema in a specified mode.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchema` |  A Pydantic model. |  _required_  
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)` |  The mode in which to generate the schema. Defaults to 'validation'. |  `'validation'`  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  A JSON schema representing the specified schema.  
Raises:
Type | Description  
---|---  
`PydanticUserError[](https://docs.pydantic.dev/latest/api/errors/#pydantic.errors.PydanticUserError)` |  If the JSON schema generator has already been used to generate a JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
407
408
409
410
411
412
413
414
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
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
```
| ```
defgenerate(self, schema: CoreSchema, mode: JsonSchemaMode = 'validation') -> JsonSchemaValue:
"""Generates a JSON schema for a specified schema in a specified mode.

    Args:
        schema: A Pydantic model.
        mode: The mode in which to generate the schema. Defaults to 'validation'.

    Returns:
        A JSON schema representing the specified schema.

    Raises:
        PydanticUserError: If the JSON schema generator has already been used to generate a JSON schema.
    """
    self._mode = mode
    if self._used:
        raise PydanticUserError(
            'This JSON schema generator has already been used to generate a JSON schema. '
            f'You must create a new instance of {type(self).__name__} to generate a new JSON schema.',
            code='json-schema-already-used',
        )

    json_schema: JsonSchemaValue = self.generate_inner(schema)
    json_ref_counts = self.get_json_ref_counts(json_schema)

    ref = cast(JsonRef, json_schema.get('$ref'))
    while ref is not None:  # may need to unpack multiple levels
        ref_json_schema = self.get_schema_from_definitions(ref)
        if json_ref_counts[ref] == 1 and ref_json_schema is not None and len(json_schema) == 1:
            # "Unpack" the ref since this is the only reference and there are no sibling keys
            json_schema = ref_json_schema.copy()  # copy to prevent recursive dict reference
            json_ref_counts[ref] -= 1
            ref = cast(JsonRef, json_schema.get('$ref'))
        ref = None

    self._garbage_collect_definitions(json_schema)
    definitions_remapping = self._build_definitions_remapping()

    if self.definitions:
        json_schema['$defs'] = self.definitions

    json_schema = definitions_remapping.remap_json_schema(json_schema)

    # For now, we will not set the $schema key. However, if desired, this can be easily added by overriding
    # this method and adding the following line after a call to super().generate(schema):
    # json_schema['$schema'] = self.schema_dialect

    self._used = True
    return self.sort(json_schema)

```
  
---|---  
###  generate_inner [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate_inner)
```
generate_inner(
    schema: CoreSchemaOrField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema for a given core schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchemaOrField` |  The given core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
TODO: the nested function definitions here seem like bad practice, I'd like to unpack these in a future PR. It'd be great if we could shorten the call stack a bit for JSON schema generation, and I think there's potential for that here.
Source code in `pydantic/json_schema.py`
```
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
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
496
497
498
499
500
501
502
503
504
505
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
521
522
523
524
525
526
527
528
529
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
550
551
552
553
554
555
556
557
558
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
579
580
581
```
| ```
defgenerate_inner(self, schema: CoreSchemaOrField) -> JsonSchemaValue:  # noqa: C901
"""Generates a JSON schema for a given core schema.

    Args:
        schema: The given core schema.

    Returns:
        The generated JSON schema.

    TODO: the nested function definitions here seem like bad practice, I'd like to unpack these
    in a future PR. It'd be great if we could shorten the call stack a bit for JSON schema generation,
    and I think there's potential for that here.
    """
    # If a schema with the same CoreRef has been handled, just return a reference to it
    # Note that this assumes that it will _never_ be the case that the same CoreRef is used
    # on types that should have different JSON schemas
    if 'ref' in schema:
        core_ref = CoreRef(schema['ref'])  # type: ignore[typeddict-item]
        core_mode_ref = (core_ref, self.mode)
        if core_mode_ref in self.core_to_defs_refs and self.core_to_defs_refs[core_mode_ref] in self.definitions:
            return {'$ref': self.core_to_json_refs[core_mode_ref]}

    defpopulate_defs(core_schema: CoreSchema, json_schema: JsonSchemaValue) -> JsonSchemaValue:
        if 'ref' in core_schema:
            core_ref = CoreRef(core_schema['ref'])  # type: ignore[typeddict-item]
            defs_ref, ref_json_schema = self.get_cache_defs_ref_schema(core_ref)
            json_ref = JsonRef(ref_json_schema['$ref'])
            # Replace the schema if it's not a reference to itself
            # What we want to avoid is having the def be just a ref to itself
            # which is what would happen if we blindly assigned any
            if json_schema.get('$ref', None) != json_ref:
                self.definitions[defs_ref] = json_schema
                self._core_defs_invalid_for_json_schema.pop(defs_ref, None)
            json_schema = ref_json_schema
        return json_schema

    defhandler_func(schema_or_field: CoreSchemaOrField) -> JsonSchemaValue:
"""Generate a JSON schema based on the input schema.

        Args:
            schema_or_field: The core schema to generate a JSON schema from.

        Returns:
            The generated JSON schema.

        Raises:
            TypeError: If an unexpected schema type is encountered.
        """
        # Generate the core-schema-type-specific bits of the schema generation:
        json_schema: JsonSchemaValue | None = None
        if self.mode == 'serialization' and 'serialization' in schema_or_field:
            # In this case, we skip the JSON Schema generation of the schema
            # and use the `'serialization'` schema instead (canonical example:
            # `Annotated[int, PlainSerializer(str)]`).
            ser_schema = schema_or_field['serialization']  # type: ignore
            json_schema = self.ser_schema(ser_schema)

            # It might be that the 'serialization'` is skipped depending on `when_used`.
            # This is only relevant for `nullable` schemas though, so we special case here.
            if (
                json_schema is not None
                and ser_schema.get('when_used') in ('unless-none', 'json-unless-none')
                and schema_or_field['type'] == 'nullable'
            ):
                json_schema = self.get_union_of_schemas([{'type': 'null'}, json_schema])
        if json_schema is None:
            if _core_utils.is_core_schema(schema_or_field) or _core_utils.is_core_schema_field(schema_or_field):
                generate_for_schema_type = self._schema_type_to_method[schema_or_field['type']]
                json_schema = generate_for_schema_type(schema_or_field)
            else:
                raise TypeError(f'Unexpected schema type: schema={schema_or_field}')
        return json_schema

    current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, handler_func)

    metadata = cast(_core_metadata.CoreMetadata, schema.get('metadata', {}))

    # TODO: I dislike that we have to wrap these basic dict updates in callables, is there any way around this?

    if js_updates := metadata.get('pydantic_js_updates'):

        defjs_updates_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
        ) -> JsonSchemaValue:
            json_schema = {**current_handler(schema_or_field), **js_updates}
            return json_schema

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, js_updates_handler_func)

    if js_extra := metadata.get('pydantic_js_extra'):

        defjs_extra_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
        ) -> JsonSchemaValue:
            json_schema = current_handler(schema_or_field)
            if isinstance(js_extra, dict):
                json_schema.update(to_jsonable_python(js_extra))
            elif callable(js_extra):
                # similar to typing issue in _update_class_schema when we're working with callable js extra
                js_extra(json_schema)  # type: ignore
            return json_schema

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, js_extra_handler_func)

    for js_modify_function in metadata.get('pydantic_js_functions', ()):

        defnew_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
            js_modify_function: GetJsonSchemaFunction = js_modify_function,
        ) -> JsonSchemaValue:
            json_schema = js_modify_function(schema_or_field, current_handler)
            if _core_utils.is_core_schema(schema_or_field):
                json_schema = populate_defs(schema_or_field, json_schema)
            original_schema = current_handler.resolve_ref_schema(json_schema)
            ref = json_schema.pop('$ref', None)
            if ref and json_schema:
                original_schema.update(json_schema)
            return original_schema

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, new_handler_func)

    for js_modify_function in metadata.get('pydantic_js_annotation_functions', ()):

        defnew_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
            js_modify_function: GetJsonSchemaFunction = js_modify_function,
        ) -> JsonSchemaValue:
            return js_modify_function(schema_or_field, current_handler)

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, new_handler_func)

    json_schema = current_handler(schema)
    if _core_utils.is_core_schema(schema):
        json_schema = populate_defs(schema, json_schema)
    return json_schema

```
  
---|---  
###  sort [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.sort)
```
sort(
    value: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue), parent_key: | None = None
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Override this method to customize the sorting of the JSON schema (e.g., don't sort at all, sort all keys unconditionally, etc.)
By default, alphabetically sort the keys in the JSON schema, skipping the 'properties' and 'default' keys to preserve field definition order. This sort is recursive, so it will sort all nested dictionaries as well.
Source code in `pydantic/json_schema.py`
```
583
584
585
586
587
588
589
590
591
592
593
594
595
```
| ```
defsort(self, value: JsonSchemaValue, parent_key: str | None = None) -> JsonSchemaValue:
"""Override this method to customize the sorting of the JSON schema (e.g., don't sort at all, sort all keys unconditionally, etc.)

    By default, alphabetically sort the keys in the JSON schema, skipping the 'properties' and 'default' keys to preserve field definition order.
    This sort is recursive, so it will sort all nested dictionaries as well.
    """
    sorted_dict: dict[str, JsonSchemaValue] = {}
    keys = value.keys()
    if parent_key not in ('properties', 'default'):
        keys = sorted(keys)
    for key in keys:
        sorted_dict[key] = self._sort_recursive(value[key], parent_key=key)
    return sorted_dict

```
  
---|---  
###  invalid_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.invalid_schema)
```
invalid_schema(schema: InvalidSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Placeholder - should never be called.
Source code in `pydantic/json_schema.py`
```
615
616
617
618
```
| ```
definvalid_schema(self, schema: core_schema.InvalidSchema) -> JsonSchemaValue:
"""Placeholder - should never be called."""

    raise RuntimeError('Cannot generate schema for invalid_schema. This is a bug! Please report it.')

```
  
---|---  
###  any_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.any_schema)
```
any_schema(schema: AnySchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches any value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `AnySchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
620
621
622
623
624
625
626
627
628
629
```
| ```
defany_schema(self, schema: core_schema.AnySchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches any value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {}

```
  
---|---  
###  none_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.none_schema)
```
none_schema(schema: NoneSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches `None`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `NoneSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defnone_schema(self, schema: core_schema.NoneSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches `None`.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'null'}

```
  
---|---  
###  bool_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.bool_schema)
```
bool_schema(schema: BoolSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a bool value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `BoolSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defbool_schema(self, schema: core_schema.BoolSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a bool value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'boolean'}

```
  
---|---  
###  int_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.int_schema)
```
int_schema(schema: IntSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches an int value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `IntSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defint_schema(self, schema: core_schema.IntSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches an int value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: dict[str, Any] = {'type': 'integer'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.numeric)
    json_schema = {k: v for k, v in json_schema.items() if v not in {math.inf, -math.inf}}
    return json_schema

```
  
---|---  
###  float_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.float_schema)
```
float_schema(schema: FloatSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a float value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `FloatSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
667
668
669
670
671
672
673
674
675
676
677
678
679
```
| ```
deffloat_schema(self, schema: core_schema.FloatSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a float value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: dict[str, Any] = {'type': 'number'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.numeric)
    json_schema = {k: v for k, v in json_schema.items() if v not in {math.inf, -math.inf}}
    return json_schema

```
  
---|---  
###  decimal_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.decimal_schema)
```
decimal_schema(schema: DecimalSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a decimal value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DecimalSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
681
682
683
684
685
686
687
688
689
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
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
```
| ```
defdecimal_schema(self, schema: core_schema.DecimalSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a decimal value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """

    defget_decimal_pattern(schema: core_schema.DecimalSchema) -> str:
        max_digits = schema.get('max_digits')
        decimal_places = schema.get('decimal_places')

        pattern = (
            r'^(?!^[-+.]*$)[+-]?0*'  # check it is not empty string and not one or sequence of ".+-" characters.
        )

        # Case 1: Both max_digits and decimal_places are set
        if max_digits is not None and decimal_places is not None:
            integer_places = max(0, max_digits - decimal_places)
            pattern += (
                rf'(?:'
                rf'\d{{0,{integer_places}}}'
                rf'|'
                rf'(?=[\d.]{{1,{max_digits+1}}}0*$)'
                rf'\d{{0,{integer_places}}}\.\d{{0,{decimal_places}}}0*$'
                rf')'
            )

        # Case 2: Only max_digits is set
        elif max_digits is not None and decimal_places is None:
            pattern += (
                rf'(?:'
                rf'\d{{0,{max_digits}}}'
                rf'|'
                rf'(?=[\d.]{{1,{max_digits+1}}}0*$)'
                rf'\d*\.\d*0*$'
                rf')'
            )

        # Case 3: Only decimal_places is set
        elif max_digits is None and decimal_places is not None:
            pattern += rf'\d*\.?\d{{0,{decimal_places}}}0*$'

        # Case 4: Both are None (no restrictions)
        else:
            pattern += r'\d*\.?\d*$'  # look for arbitrary integer or decimal

        return pattern

    json_schema = self.str_schema(core_schema.str_schema(pattern=get_decimal_pattern(schema)))
    if self.mode == 'validation':
        multiple_of = schema.get('multiple_of')
        le = schema.get('le')
        ge = schema.get('ge')
        lt = schema.get('lt')
        gt = schema.get('gt')
        json_schema = {
            'anyOf': [
                self.float_schema(
                    core_schema.float_schema(
                        allow_inf_nan=schema.get('allow_inf_nan'),
                        multiple_of=None if multiple_of is None else float(multiple_of),
                        le=None if le is None else float(le),
                        ge=None if ge is None else float(ge),
                        lt=None if lt is None else float(lt),
                        gt=None if gt is None else float(gt),
                    )
                ),
                json_schema,
            ],
        }
    return json_schema

```
  
---|---  
###  str_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.str_schema)
```
str_schema(schema: StringSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a string value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `StringSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
756
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
```
| ```
defstr_schema(self, schema: core_schema.StringSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a string value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = {'type': 'string'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.string)
    if isinstance(json_schema.get('pattern'), Pattern):
        # TODO: should we add regex flags to the pattern?
        json_schema['pattern'] = json_schema.get('pattern').pattern  # type: ignore
    return json_schema

```
  
---|---  
###  bytes_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.bytes_schema)
```
bytes_schema(schema: BytesSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a bytes value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `BytesSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defbytes_schema(self, schema: core_schema.BytesSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a bytes value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = {'type': 'string', 'format': 'base64url' if self._config.ser_json_bytes == 'base64' else 'binary'}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.bytes)
    return json_schema

```
  
---|---  
###  date_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.date_schema)
```
date_schema(schema: DateSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a date value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DateSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defdate_schema(self, schema: core_schema.DateSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a date value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'date'}

```
  
---|---  
###  time_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.time_schema)
```
time_schema(schema: TimeSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a time value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `TimeSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deftime_schema(self, schema: core_schema.TimeSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a time value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'time'}

```
  
---|---  
###  datetime_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.datetime_schema)
```
datetime_schema(schema: DatetimeSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a datetime value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DatetimeSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
807
808
809
810
811
812
813
814
815
816
```
| ```
defdatetime_schema(self, schema: core_schema.DatetimeSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a datetime value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'date-time'}

```
  
---|---  
###  timedelta_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.timedelta_schema)
```
timedelta_schema(
    schema: TimedeltaSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a timedelta value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `TimedeltaSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
818
819
820
821
822
823
824
825
826
827
828
829
```
| ```
deftimedelta_schema(self, schema: core_schema.TimedeltaSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a timedelta value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self._config.ser_json_timedelta == 'float':
        return {'type': 'number'}
    return {'type': 'string', 'format': 'duration'}

```
  
---|---  
###  literal_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.literal_schema)
```
literal_schema(schema: LiteralSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a literal value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `LiteralSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
855
856
857
858
859
860
861
```
| ```
defliteral_schema(self, schema: core_schema.LiteralSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a literal value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    expected = [to_jsonable_python(v.value if isinstance(v, Enum) else v) for v in schema['expected']]

    result: dict[str, Any] = {}
    if len(expected) == 1:
        result['const'] = expected[0]
    else:
        result['enum'] = expected

    types = {type(e) for e in expected}
    if types == {str}:
        result['type'] = 'string'
    elif types == {int}:
        result['type'] = 'integer'
    elif types == {float}:
        result['type'] = 'number'
    elif types == {bool}:
        result['type'] = 'boolean'
    elif types == {list}:
        result['type'] = 'array'
    elif types == {type(None)}:
        result['type'] = 'null'
    return result

```
  
---|---  
###  missing_sentinel_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.missing_sentinel_schema)
```
missing_sentinel_schema(
    schema: MissingSentinelSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches the `MISSING` sentinel value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `MissingSentinelSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
863
864
865
866
867
868
869
870
871
872
```
| ```
defmissing_sentinel_schema(self, schema: core_schema.MissingSentinelSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches the `MISSING` sentinel value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    raise PydanticOmit

```
  
---|---  
###  enum_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.enum_schema)
```
enum_schema(schema: EnumSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches an Enum value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `EnumSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defenum_schema(self, schema: core_schema.EnumSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches an Enum value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    enum_type = schema['cls']
    description = None if not enum_type.__doc__ else inspect.cleandoc(enum_type.__doc__)
    if (
        description == 'An enumeration.'
    ):  # This is the default value provided by enum.EnumMeta.__new__; don't use it
        description = None
    result: dict[str, Any] = {'title': enum_type.__name__, 'description': description}
    result = {k: v for k, v in result.items() if v is not None}

    expected = [to_jsonable_python(v.value) for v in schema['members']]

    result['enum'] = expected

    types = {type(e) for e in expected}
    if isinstance(enum_type, str) or types == {str}:
        result['type'] = 'string'
    elif isinstance(enum_type, int) or types == {int}:
        result['type'] = 'integer'
    elif isinstance(enum_type, float) or types == {float}:
        result['type'] = 'number'
    elif types == {bool}:
        result['type'] = 'boolean'
    elif types == {list}:
        result['type'] = 'array'

    return result

```
  
---|---  
###  is_instance_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.is_instance_schema)
```
is_instance_schema(
    schema: IsInstanceSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Handles JSON schema generation for a core schema that checks if a value is an instance of a class.
Unless overridden in a subclass, this raises an error.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `IsInstanceSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defis_instance_schema(self, schema: core_schema.IsInstanceSchema) -> JsonSchemaValue:
"""Handles JSON schema generation for a core schema that checks if a value is an instance of a class.

    Unless overridden in a subclass, this raises an error.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.handle_invalid_for_json_schema(schema, f'core_schema.IsInstanceSchema ({schema["cls"]})')

```
  
---|---  
###  is_subclass_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.is_subclass_schema)
```
is_subclass_schema(
    schema: IsSubclassSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Handles JSON schema generation for a core schema that checks if a value is a subclass of a class.
For backwards compatibility with v1, this does not raise an error, but can be overridden to change this.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `IsSubclassSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
933
934
935
```
| ```
defis_subclass_schema(self, schema: core_schema.IsSubclassSchema) -> JsonSchemaValue:
"""Handles JSON schema generation for a core schema that checks if a value is a subclass of a class.

    For backwards compatibility with v1, this does not raise an error, but can be overridden to change this.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # Note: This is for compatibility with V1; you can override if you want different behavior.
    return {}

```
  
---|---  
###  callable_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.callable_schema)
```
callable_schema(schema: CallableSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a callable value.
Unless overridden in a subclass, this raises an error.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CallableSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
937
938
939
940
941
942
943
944
945
946
947
948
```
| ```
defcallable_schema(self, schema: core_schema.CallableSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a callable value.

    Unless overridden in a subclass, this raises an error.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.handle_invalid_for_json_schema(schema, 'core_schema.CallableSchema')

```
  
---|---  
###  list_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.list_schema)
```
list_schema(schema: ListSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Returns a schema that matches a list schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ListSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deflist_schema(self, schema: core_schema.ListSchema) -> JsonSchemaValue:
"""Returns a schema that matches a list schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    items_schema = {} if 'items_schema' not in schema else self.generate_inner(schema['items_schema'])
    json_schema = {'type': 'array', 'items': items_schema}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.array)
    return json_schema

```
  
---|---  
###  tuple_positional_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tuple_positional_schema)
```
tuple_positional_schema(
    schema: TupleSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Replaced by `tuple_schema`.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
@deprecated('`tuple_positional_schema` is deprecated. Use `tuple_schema` instead.', category=None)
@final
deftuple_positional_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue:
"""Replaced by `tuple_schema`."""
    warnings.warn(
        '`tuple_positional_schema` is deprecated. Use `tuple_schema` instead.',
        PydanticDeprecatedSince26,
        stacklevel=2,
    )
    return self.tuple_schema(schema)

```
  
---|---  
###  tuple_variable_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tuple_variable_schema)
```
tuple_variable_schema(
    schema: TupleSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Replaced by `tuple_schema`.
Source code in `pydantic/json_schema.py`
```
975
976
977
978
979
980
981
982
983
984
```
| ```
@deprecated('`tuple_variable_schema` is deprecated. Use `tuple_schema` instead.', category=None)
@final
deftuple_variable_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue:
"""Replaced by `tuple_schema`."""
    warnings.warn(
        '`tuple_variable_schema` is deprecated. Use `tuple_schema` instead.',
        PydanticDeprecatedSince26,
        stacklevel=2,
    )
    return self.tuple_schema(schema)

```
  
---|---  
###  tuple_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tuple_schema)
```
tuple_schema(schema: TupleSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a tuple schema e.g. `tuple[int, str, bool]` or `tuple[int, ...]`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `TupleSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
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
```
| ```
deftuple_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a tuple schema e.g. `tuple[int,
    str, bool]` or `tuple[int, ...]`.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: JsonSchemaValue = {'type': 'array'}
    if 'variadic_item_index' in schema:
        variadic_item_index = schema['variadic_item_index']
        if variadic_item_index > 0:
            json_schema['minItems'] = variadic_item_index
            json_schema['prefixItems'] = [
                self.generate_inner(item) for item in schema['items_schema'][:variadic_item_index]
            ]
        if variadic_item_index + 1 == len(schema['items_schema']):
            # if the variadic item is the last item, then represent it faithfully
            json_schema['items'] = self.generate_inner(schema['items_schema'][variadic_item_index])
        else:
            # otherwise, 'items' represents the schema for the variadic
            # item plus the suffix, so just allow anything for simplicity
            # for now
            json_schema['items'] = True
    else:
        prefixItems = [self.generate_inner(item) for item in schema['items_schema']]
        if prefixItems:
            json_schema['prefixItems'] = prefixItems
        json_schema['minItems'] = len(prefixItems)
        json_schema['maxItems'] = len(prefixItems)
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.array)
    return json_schema

```
  
---|---  
###  set_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.set_schema)
```
set_schema(schema: SetSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a set schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `SetSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defset_schema(self, schema: core_schema.SetSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a set schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self._common_set_schema(schema)

```
  
---|---  
###  frozenset_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.frozenset_schema)
```
frozenset_schema(
    schema: FrozenSetSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a frozenset schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `FrozenSetSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deffrozenset_schema(self, schema: core_schema.FrozenSetSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a frozenset schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self._common_set_schema(schema)

```
  
---|---  
###  generator_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generator_schema)
```
generator_schema(
    schema: GeneratorSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Returns a JSON schema that represents the provided GeneratorSchema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `GeneratorSchema` |  The schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
```
| ```
defgenerator_schema(self, schema: core_schema.GeneratorSchema) -> JsonSchemaValue:
"""Returns a JSON schema that represents the provided GeneratorSchema.

    Args:
        schema: The schema.

    Returns:
        The generated JSON schema.
    """
    items_schema = {} if 'items_schema' not in schema else self.generate_inner(schema['items_schema'])
    json_schema = {'type': 'array', 'items': items_schema}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.array)
    return json_schema

```
  
---|---  
###  dict_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dict_schema)
```
dict_schema(schema: DictSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a dict schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DictSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1063
1064
1065
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
```
| ```
defdict_schema(self, schema: core_schema.DictSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a dict schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema: JsonSchemaValue = {'type': 'object'}

    keys_schema = self.generate_inner(schema['keys_schema']).copy() if 'keys_schema' in schema else {}
    if '$ref' not in keys_schema:
        keys_pattern = keys_schema.pop('pattern', None)
        # Don't give a title to patternProperties/propertyNames:
        keys_schema.pop('title', None)
    else:
        # Here, we assume that if the keys schema is a definition reference,
        # it can't be a simple string core schema (and thus no pattern can exist).
        # However, this is only in practice (in theory, a definition reference core
        # schema could be generated for a simple string schema).
        # Note that we avoid calling `self.resolve_ref_schema`, as it might not exist yet.
        keys_pattern = None

    values_schema = self.generate_inner(schema['values_schema']).copy() if 'values_schema' in schema else {}
    # don't give a title to additionalProperties:
    values_schema.pop('title', None)

    if values_schema or keys_pattern is not None:
        if keys_pattern is None:
            json_schema['additionalProperties'] = values_schema
        else:
            json_schema['patternProperties'] = {keys_pattern: values_schema}
    else:  # for `dict[str, Any]`, we allow any key and any value, since `str` is the default key type
        json_schema['additionalProperties'] = True

    if (
        # The len check indicates that constraints are probably present:
        (keys_schema.get('type') == 'string' and len(keys_schema) > 1)
        # If this is a definition reference schema, it most likely has constraints:
        or '$ref' in keys_schema
    ):
        keys_schema.pop('type', None)
        json_schema['propertyNames'] = keys_schema

    self.update_with_validations(json_schema, schema, self.ValidationsMapping.object)
    return json_schema

```
  
---|---  
###  function_before_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_before_schema)
```
function_before_schema(
    schema: BeforeValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-before schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `BeforeValidatorFunctionSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
```
| ```
deffunction_before_schema(self, schema: core_schema.BeforeValidatorFunctionSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a function-before schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self.mode == 'validation' and (input_schema := schema.get('json_schema_input_schema')):
        return self.generate_inner(input_schema)

    return self.generate_inner(schema['schema'])

```
  
---|---  
###  function_after_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_after_schema)
```
function_after_schema(
    schema: AfterValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-after schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `AfterValidatorFunctionSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
```
| ```
deffunction_after_schema(self, schema: core_schema.AfterValidatorFunctionSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a function-after schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```
  
---|---  
###  function_plain_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_plain_schema)
```
function_plain_schema(
    schema: PlainValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-plain schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `PlainValidatorFunctionSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
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
```
| ```
deffunction_plain_schema(self, schema: core_schema.PlainValidatorFunctionSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a function-plain schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self.mode == 'validation' and (input_schema := schema.get('json_schema_input_schema')):
        return self.generate_inner(input_schema)

    return self.handle_invalid_for_json_schema(
        schema, f'core_schema.PlainValidatorFunctionSchema ({schema["function"]})'
    )

```
  
---|---  
###  function_wrap_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.function_wrap_schema)
```
function_wrap_schema(
    schema: WrapValidatorFunctionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a function-wrap schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `WrapValidatorFunctionSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deffunction_wrap_schema(self, schema: core_schema.WrapValidatorFunctionSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a function-wrap schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    if self.mode == 'validation' and (input_schema := schema.get('json_schema_input_schema')):
        return self.generate_inner(input_schema)

    return self.generate_inner(schema['schema'])

```
  
---|---  
###  default_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.default_schema)
```
default_schema(
    schema: WithDefaultSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema with a default value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `WithDefaultSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
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
```
| ```
defdefault_schema(self, schema: core_schema.WithDefaultSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema with a default value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = self.generate_inner(schema['schema'])

    default = self.get_default_value(schema)
    if default is NoDefault or default is MISSING:
        return json_schema

    # we reflect the application of custom plain, no-info serializers to defaults for
    # JSON Schemas viewed in serialization mode:
    # TODO: improvements along with https://github.com/pydantic/pydantic/issues/8208
    if self.mode == 'serialization':
        # `_get_ser_schema_for_default_value()` is used to unpack potentially nested validator schemas:
        ser_schema = _get_ser_schema_for_default_value(schema['schema'])
        if (
            ser_schema is not None
            and (ser_func := ser_schema.get('function'))
            and not (default is None and ser_schema.get('when_used') in ('unless-none', 'json-unless-none'))
        ):
            try:
                default = ser_func(default)  # type: ignore
            except Exception:
                # It might be that the provided default needs to be validated (read: parsed) first
                # (assuming `validate_default` is enabled). However, we can't perform
                # such validation during JSON Schema generation so we don't support
                # this pattern for now.
                # (One example is when using `foo: ByteSize = '1MB'`, which validates and
                # serializes as an int. In this case, `ser_func` is `int` and `int('1MB')` fails).
                self.emit_warning(
                    'non-serializable-default',
                    f'Unable to serialize value {default!r} with the plain serializer; excluding default from JSON schema',
                )
                return json_schema

    try:
        encoded_default = self.encode_default(default)
    except pydantic_core.PydanticSerializationError:
        self.emit_warning(
            'non-serializable-default',
            f'Default value {default} is not JSON serializable; excluding default from JSON schema',
        )
        # Return the inner schema, as though there was no default
        return json_schema

    json_schema['default'] = encoded_default
    return json_schema

```
  
---|---  
###  get_default_value [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_default_value)
```
get_default_value(schema: WithDefaultSchema) -> 
```

Get the default value to be used when generating a JSON Schema for a core schema with a default.
The default implementation is to use the statically defined default value. This method can be overridden if you want to make use of the default factory.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `WithDefaultSchema` |  The `'with-default'` core schema. |  _required_  
Returns:
Type | Description  
---|---  
|  The default value to use, or [`NoDefault`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.NoDefault) if no default value is available.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defget_default_value(self, schema: core_schema.WithDefaultSchema) -> Any:
"""Get the default value to be used when generating a JSON Schema for a core schema with a default.

    The default implementation is to use the statically defined default value. This method can be overridden
    if you want to make use of the default factory.

    Args:
        schema: The `'with-default'` core schema.

    Returns:
        The default value to use, or [`NoDefault`][pydantic.json_schema.NoDefault] if no default
            value is available.
    """
    return schema.get('default', NoDefault)

```
  
---|---  
###  nullable_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.nullable_schema)
```
nullable_schema(schema: NullableSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows null values.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `NullableSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defnullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that allows null values.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    null_schema = {'type': 'null'}
    inner_json_schema = self.generate_inner(schema['schema'])

    if inner_json_schema == null_schema:
        return null_schema
    else:
        return self.get_union_of_schemas([inner_json_schema, null_schema])

```
  
---|---  
###  union_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.union_schema)
```
union_schema(schema: UnionSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching any of the given schemas.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `UnionSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
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
```
| ```
defunion_schema(self, schema: core_schema.UnionSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that allows values matching any of the given schemas.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    generated: list[JsonSchemaValue] = []

    choices = schema['choices']
    for choice in choices:
        # choice will be a tuple if an explicit label was provided
        choice_schema = choice[0] if isinstance(choice, tuple) else choice
        try:
            generated.append(self.generate_inner(choice_schema))
        except PydanticOmit:
            continue
        except PydanticInvalidForJsonSchema as exc:
            self.emit_warning('skipped-choice', exc.message)
    if len(generated) == 1:
        return generated[0]
    return self.get_union_of_schemas(generated)

```
  
---|---  
###  get_union_of_schemas [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_union_of_schemas)
```
get_union_of_schemas(
    schemas: [JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)],
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Returns the JSON Schema representation for the union of the provided JSON Schemas.
The result depends on the configured `'union_format'`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schemas` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  The list of JSON Schemas to be included in the union. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The JSON Schema representing the union of schemas.  
Source code in `pydantic/json_schema.py`
```
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
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
```
| ```
defget_union_of_schemas(self, schemas: list[JsonSchemaValue]) -> JsonSchemaValue:
"""Returns the JSON Schema representation for the union of the provided JSON Schemas.

    The result depends on the configured `'union_format'`.

    Args:
        schemas: The list of JSON Schemas to be included in the union.

    Returns:
        The JSON Schema representing the union of schemas.
    """
    if self.union_format == 'primitive_type_array':
        types: list[str] = []
        for schema in schemas:
            schema_types: list[str] | str | None = schema.get('type')
            if schema_types is None:
                # No type, meaning it can be a ref or an empty schema.
                break
            if not isinstance(schema_types, list):
                schema_types = [schema_types]
            if not all(t in _PRIMITIVE_JSON_SCHEMA_TYPES for t in schema_types):
                break
            if len(schema) != 1:
                # We only want to include types that don't have any constraints. For instance,
                # if `schemas = [{'type': 'string', 'maxLength': 3}, {'type': 'string', 'minLength': 5}]`,
                # we don't want to produce `{'type': 'string', 'maxLength': 3, 'minLength': 5}`.
                # Same if we have some metadata (e.g. `title`) on a specific union member, we want to preserve it.
                break

            types.extend(schema_types)
        else:
            # If we got there, all the schemas where valid to be used with the `'primitive_type_array` format
            return {'type': list(dict.fromkeys(types))}

    return self.get_flattened_anyof(schemas)

```
  
---|---  
###  tagged_union_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.tagged_union_schema)
```
tagged_union_schema(
    schema: TaggedUnionSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching any of the given schemas, where the schemas are tagged with a discriminator field that indicates which schema should be used to validate the value.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `TaggedUnionSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deftagged_union_schema(self, schema: core_schema.TaggedUnionSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that allows values matching any of the given schemas, where
    the schemas are tagged with a discriminator field that indicates which schema should be used to validate
    the value.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    generated: dict[str, JsonSchemaValue] = {}
    for k, v in schema['choices'].items():
        if isinstance(k, Enum):
            k = k.value
        try:
            # Use str(k) since keys must be strings for json; while not technically correct,
            # it's the closest that can be represented in valid JSON
            generated[str(k)] = self.generate_inner(v).copy()
        except PydanticOmit:
            continue
        except PydanticInvalidForJsonSchema as exc:
            self.emit_warning('skipped-choice', exc.message)

    one_of_choices = _deduplicate_schemas(generated.values())
    json_schema: JsonSchemaValue = {'oneOf': one_of_choices}

    # This reflects the v1 behavior; TODO: we should make it possible to exclude OpenAPI stuff from the JSON schema
    openapi_discriminator = self._extract_discriminator(schema, one_of_choices)
    if openapi_discriminator is not None:
        json_schema['discriminator'] = {
            'propertyName': openapi_discriminator,
            'mapping': {k: v.get('$ref', v) for k, v in generated.items()},
        }

    return json_schema

```
  
---|---  
###  chain_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.chain_schema)
```
chain_schema(schema: ChainSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a core_schema.ChainSchema.
When generating a schema for validation, we return the validation JSON schema for the first step in the chain. For serialization, we return the serialization JSON schema for the last step in the chain.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ChainSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defchain_schema(self, schema: core_schema.ChainSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a core_schema.ChainSchema.

    When generating a schema for validation, we return the validation JSON schema for the first step in the chain.
    For serialization, we return the serialization JSON schema for the last step in the chain.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    step_index = 0 if self.mode == 'validation' else -1  # use first step for validation, last for serialization
    return self.generate_inner(schema['steps'][step_index])

```
  
---|---  
###  lax_or_strict_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.lax_or_strict_schema)
```
lax_or_strict_schema(
    schema: LaxOrStrictSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching either the lax schema or the strict schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `LaxOrStrictSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
1420
1421
1422
1423
1424
1425
1426
1427
```
| ```
deflax_or_strict_schema(self, schema: core_schema.LaxOrStrictSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that allows values matching either the lax schema or the
    strict schema.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # TODO: Need to read the default value off of model config or whatever
    use_strict = schema.get('strict', False)  # TODO: replace this default False
    # If your JSON schema fails to generate it is probably
    # because one of the following two branches failed.
    if use_strict:
        return self.generate_inner(schema['strict_schema'])
    else:
        return self.generate_inner(schema['lax_schema'])

```
  
---|---  
###  json_or_python_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.json_or_python_schema)
```
json_or_python_schema(
    schema: JsonOrPythonSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that allows values matching either the JSON schema or the Python schema.
The JSON schema is used instead of the Python schema. If you want to use the Python schema, you should override this method.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `JsonOrPythonSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1429
1430
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
```
| ```
defjson_or_python_schema(self, schema: core_schema.JsonOrPythonSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that allows values matching either the JSON schema or the
    Python schema.

    The JSON schema is used instead of the Python schema. If you want to use the Python schema, you should override
    this method.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['json_schema'])

```
  
---|---  
###  typed_dict_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.typed_dict_schema)
```
typed_dict_schema(
    schema: TypedDictSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a typed dict.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `TypedDictSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
1466
1467
1468
1469
1470
1471
1472
1473
1474
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
```
| ```
deftyped_dict_schema(self, schema: core_schema.TypedDictSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a typed dict.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    total = schema.get('total', True)
    named_required_fields: list[tuple[str, bool, CoreSchemaField]] = [
        (name, self.field_is_required(field, total), field)
        for name, field in schema['fields'].items()
        if self.field_is_present(field)
    ]
    if self.mode == 'serialization':
        named_required_fields.extend(self._name_required_computed_fields(schema.get('computed_fields', [])))
    cls = schema.get('cls')
    config = _get_typed_dict_config(cls)
    with self._config_wrapper_stack.push(config):
        json_schema = self._named_required_fields_schema(named_required_fields)

    # There's some duplication between `extra_behavior` and
    # the config's `extra`/core config's `extra_fields_behavior`.
    # However, it is common to manually create TypedDictSchemas,
    # where you don't necessarily have a class.
    # At runtime, `extra_behavior` takes priority over the config
    # for validation, so follow the same for the JSON Schema:
    if schema.get('extra_behavior') == 'forbid':
        json_schema['additionalProperties'] = False
    elif schema.get('extra_behavior') == 'allow':
        if 'extras_schema' in schema and schema['extras_schema'] != {'type': 'any'}:
            json_schema['additionalProperties'] = self.generate_inner(schema['extras_schema'])
        else:
            json_schema['additionalProperties'] = True

    if cls is not None:
        # `_update_class_schema()` will not override
        # `additionalProperties` if already present:
        self._update_class_schema(json_schema, cls, config)
    elif 'additionalProperties' not in json_schema:
        extra = schema.get('config', {}).get('extra_fields_behavior')
        if extra == 'forbid':
            json_schema['additionalProperties'] = False
        elif extra == 'allow':
            json_schema['additionalProperties'] = True

    return json_schema

```
  
---|---  
###  typed_dict_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.typed_dict_field_schema)
```
typed_dict_field_schema(
    schema: TypedDictField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a typed dict field.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `TypedDictField` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deftyped_dict_field_schema(self, schema: core_schema.TypedDictField) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a typed dict field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```
  
---|---  
###  dataclass_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dataclass_field_schema)
```
dataclass_field_schema(
    schema: DataclassField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a dataclass field.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DataclassField` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defdataclass_field_schema(self, schema: core_schema.DataclassField) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a dataclass field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```
  
---|---  
###  model_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.model_field_schema)
```
model_field_schema(schema: ModelField) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a model field.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ModelField` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defmodel_field_schema(self, schema: core_schema.ModelField) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a model field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```
  
---|---  
###  computed_field_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.computed_field_schema)
```
computed_field_schema(
    schema: ComputedField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a computed field.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ComputedField` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
```
| ```
defcomputed_field_schema(self, schema: core_schema.ComputedField) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a computed field.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['return_schema'])

```
  
---|---  
###  model_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.model_schema)
```
model_schema(schema: ModelSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ModelSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1589
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
```
| ```
defmodel_schema(self, schema: core_schema.ModelSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a model.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # We do not use schema['model'].model_json_schema() here
    # because it could lead to inconsistent refs handling, etc.
    cls = cast('type[BaseModel]', schema['cls'])
    config = cls.model_config

    with self._config_wrapper_stack.push(config):
        json_schema = self.generate_inner(schema['schema'])

    self._update_class_schema(json_schema, cls, config)

    return json_schema

```
  
---|---  
###  resolve_ref_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.resolve_ref_schema)
```
resolve_ref_schema(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Resolve a JsonSchemaValue to the non-ref schema if it is a $ref schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The schema to resolve. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The resolved schema.  
Raises:
Type | Description  
---|---  
|  If the schema reference can't be found in definitions.  
Source code in `pydantic/json_schema.py`
```
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
```
| ```
defresolve_ref_schema(self, json_schema: JsonSchemaValue) -> JsonSchemaValue:
"""Resolve a JsonSchemaValue to the non-ref schema if it is a $ref schema.

    Args:
        json_schema: The schema to resolve.

    Returns:
        The resolved schema.

    Raises:
        RuntimeError: If the schema reference can't be found in definitions.
    """
    while '$ref' in json_schema:
        ref = json_schema['$ref']
        schema_to_update = self.get_schema_from_definitions(JsonRef(ref))
        if schema_to_update is None:
            raise RuntimeError(f'Cannot update undefined schema for $ref={ref}')
        json_schema = schema_to_update
    return json_schema

```
  
---|---  
###  model_fields_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.model_fields_schema)
```
model_fields_schema(
    schema: ModelFieldsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a model's fields.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ModelFieldsSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defmodel_fields_schema(self, schema: core_schema.ModelFieldsSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a model's fields.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    named_required_fields: list[tuple[str, bool, CoreSchemaField]] = [
        (name, self.field_is_required(field, total=True), field)
        for name, field in schema['fields'].items()
        if self.field_is_present(field)
    ]
    if self.mode == 'serialization':
        named_required_fields.extend(self._name_required_computed_fields(schema.get('computed_fields', [])))
    json_schema = self._named_required_fields_schema(named_required_fields)
    extras_schema = schema.get('extras_schema', None)
    if extras_schema is not None:
        schema_to_update = self.resolve_ref_schema(json_schema)
        schema_to_update['additionalProperties'] = self.generate_inner(extras_schema)
    return json_schema

```
  
---|---  
###  field_is_present [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.field_is_present)
```
field_is_present(field: CoreSchemaField) -> 
```

Whether the field should be included in the generated JSON schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`field` |  `CoreSchemaField` |  The schema for the field itself. |  _required_  
Returns:
Type | Description  
---|---  
|  `True` if the field should be included in the generated JSON schema, `False` otherwise.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
deffield_is_present(self, field: CoreSchemaField) -> bool:
"""Whether the field should be included in the generated JSON schema.

    Args:
        field: The schema for the field itself.

    Returns:
        `True` if the field should be included in the generated JSON schema, `False` otherwise.
    """
    if self.mode == 'serialization':
        # If you still want to include the field in the generated JSON schema,
        # override this method and return True
        return not field.get('serialization_exclude')
    elif self.mode == 'validation':
        return True
    else:
        assert_never(self.mode)

```
  
---|---  
###  field_is_required [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.field_is_required)
```
field_is_required(
    field: ModelField | DataclassField | TypedDictField,
    total: ,
) -> 
```

Whether the field should be marked as required in the generated JSON schema. (Note that this is irrelevant if the field is not present in the JSON schema.).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`field` |  `ModelField | DataclassField | TypedDictField` |  The schema for the field itself. |  _required_  
`total` |  |  Only applies to `TypedDictField`s. Indicates if the `TypedDict` this field belongs to is total, in which case any fields that don't explicitly specify `required=False` are required. |  _required_  
Returns:
Type | Description  
---|---  
|  `True` if the field should be marked as required in the generated JSON schema, `False` otherwise.  
Source code in `pydantic/json_schema.py`
```
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
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
```
| ```
deffield_is_required(
    self,
    field: core_schema.ModelField | core_schema.DataclassField | core_schema.TypedDictField,
    total: bool,
) -> bool:
"""Whether the field should be marked as required in the generated JSON schema.
    (Note that this is irrelevant if the field is not present in the JSON schema.).

    Args:
        field: The schema for the field itself.
        total: Only applies to `TypedDictField`s.
            Indicates if the `TypedDict` this field belongs to is total, in which case any fields that don't
            explicitly specify `required=False` are required.

    Returns:
        `True` if the field should be marked as required in the generated JSON schema, `False` otherwise.
    """
    if field['type'] == 'typed-dict-field':
        required = field.get('required', total)
    else:
        required = field['schema']['type'] != 'default'

    if self.mode == 'serialization':
        has_exclude_if = field.get('serialization_exclude_if') is not None
        if self._config.json_schema_serialization_defaults_required:
            return not has_exclude_if
        else:
            return required and not has_exclude_if
    else:
        return required

```
  
---|---  
###  dataclass_args_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dataclass_args_schema)
```
dataclass_args_schema(
    schema: DataclassArgsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a dataclass's constructor arguments.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DataclassArgsSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defdataclass_args_schema(self, schema: core_schema.DataclassArgsSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a dataclass's constructor arguments.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    named_required_fields: list[tuple[str, bool, CoreSchemaField]] = [
        (field['name'], self.field_is_required(field, total=True), field)
        for field in schema['fields']
        if self.field_is_present(field)
    ]
    if self.mode == 'serialization':
        named_required_fields.extend(self._name_required_computed_fields(schema.get('computed_fields', [])))
    return self._named_required_fields_schema(named_required_fields)

```
  
---|---  
###  dataclass_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dataclass_schema)
```
dataclass_schema(
    schema: DataclassSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a dataclass.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DataclassSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
```
| ```
defdataclass_schema(self, schema: core_schema.DataclassSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a dataclass.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    from._internal._dataclassesimport is_stdlib_dataclass

    cls = schema['cls']
    config: ConfigDict = getattr(cls, '__pydantic_config__', cast('ConfigDict', {}))

    with self._config_wrapper_stack.push(config):
        json_schema = self.generate_inner(schema['schema']).copy()

    self._update_class_schema(json_schema, cls, config)

    # Dataclass-specific handling of description
    if is_stdlib_dataclass(cls):
        # vanilla dataclass; don't use cls.__doc__ as it will contain the class signature by default
        description = None
    else:
        description = None if cls.__doc__ is None else inspect.cleandoc(cls.__doc__)
    if description:
        json_schema['description'] = description

    return json_schema

```
  
---|---  
###  arguments_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.arguments_schema)
```
arguments_schema(
    schema: ArgumentsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's arguments.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ArgumentsSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defarguments_schema(self, schema: core_schema.ArgumentsSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a function's arguments.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    prefer_positional = schema.get('metadata', {}).get('pydantic_js_prefer_positional_arguments')

    arguments = schema['arguments_schema']
    kw_only_arguments = [a for a in arguments if a.get('mode') == 'keyword_only']
    kw_or_p_arguments = [a for a in arguments if a.get('mode') in {'positional_or_keyword', None}]
    p_only_arguments = [a for a in arguments if a.get('mode') == 'positional_only']
    var_args_schema = schema.get('var_args_schema')
    var_kwargs_schema = schema.get('var_kwargs_schema')

    if prefer_positional:
        positional_possible = not kw_only_arguments and not var_kwargs_schema
        if positional_possible:
            return self.p_arguments_schema(p_only_arguments + kw_or_p_arguments, var_args_schema)

    keyword_possible = not p_only_arguments and not var_args_schema
    if keyword_possible:
        return self.kw_arguments_schema(kw_or_p_arguments + kw_only_arguments, var_kwargs_schema)

    if not prefer_positional:
        positional_possible = not kw_only_arguments and not var_kwargs_schema
        if positional_possible:
            return self.p_arguments_schema(p_only_arguments + kw_or_p_arguments, var_args_schema)

    raise PydanticInvalidForJsonSchema(
        'Unable to generate JSON schema for arguments validator with positional-only and keyword-only arguments'
    )

```
  
---|---  
###  kw_arguments_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.kw_arguments_schema)
```
kw_arguments_schema(
    arguments: [ArgumentsParameter],
    var_kwargs_schema: CoreSchema | None,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's keyword arguments.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`arguments` |  `ArgumentsParameter]` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
1868
1869
1870
1871
1872
1873
1874
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
```
| ```
defkw_arguments_schema(
    self, arguments: list[core_schema.ArgumentsParameter], var_kwargs_schema: CoreSchema | None
) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a function's keyword arguments.

    Args:
        arguments: The core schema.

    Returns:
        The generated JSON schema.
    """
    properties: dict[str, JsonSchemaValue] = {}
    required: list[str] = []
    for argument in arguments:
        name = self.get_argument_name(argument)
        argument_schema = self.generate_inner(argument['schema']).copy()
        if 'title' not in argument_schema and self.field_title_should_be_set(argument['schema']):
            argument_schema['title'] = self.get_title_from_name(name)
        properties[name] = argument_schema

        if argument['schema']['type'] != 'default':
            # This assumes that if the argument has a default value,
            # the inner schema must be of type WithDefaultSchema.
            # I believe this is true, but I am not 100% sure
            required.append(name)

    json_schema: JsonSchemaValue = {'type': 'object', 'properties': properties}
    if required:
        json_schema['required'] = required

    if var_kwargs_schema:
        additional_properties_schema = self.generate_inner(var_kwargs_schema)
        if additional_properties_schema:
            json_schema['additionalProperties'] = additional_properties_schema
    else:
        json_schema['additionalProperties'] = False
    return json_schema

```
  
---|---  
###  p_arguments_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.p_arguments_schema)
```
p_arguments_schema(
    arguments: [ArgumentsParameter],
    var_args_schema: CoreSchema | None,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's positional arguments.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`arguments` |  `ArgumentsParameter]` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
```
| ```
defp_arguments_schema(
    self, arguments: list[core_schema.ArgumentsParameter], var_args_schema: CoreSchema | None
) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a function's positional arguments.

    Args:
        arguments: The core schema.

    Returns:
        The generated JSON schema.
    """
    prefix_items: list[JsonSchemaValue] = []
    min_items = 0

    for argument in arguments:
        name = self.get_argument_name(argument)

        argument_schema = self.generate_inner(argument['schema']).copy()
        if 'title' not in argument_schema and self.field_title_should_be_set(argument['schema']):
            argument_schema['title'] = self.get_title_from_name(name)
        prefix_items.append(argument_schema)

        if argument['schema']['type'] != 'default':
            # This assumes that if the argument has a default value,
            # the inner schema must be of type WithDefaultSchema.
            # I believe this is true, but I am not 100% sure
            min_items += 1

    json_schema: JsonSchemaValue = {'type': 'array'}
    if prefix_items:
        json_schema['prefixItems'] = prefix_items
    if min_items:
        json_schema['minItems'] = min_items

    if var_args_schema:
        items_schema = self.generate_inner(var_args_schema)
        if items_schema:
            json_schema['items'] = items_schema
    else:
        json_schema['maxItems'] = len(prefix_items)

    return json_schema

```
  
---|---  
###  get_argument_name [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_argument_name)
```
get_argument_name(
    argument: ArgumentsParameter | ArgumentsV3Parameter,
) -> 
```

Retrieves the name of an argument.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`argument` |  `ArgumentsParameter | ArgumentsV3Parameter` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
|  The name of the argument.  
Source code in `pydantic/json_schema.py`
```
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
```
| ```
defget_argument_name(self, argument: core_schema.ArgumentsParameter | core_schema.ArgumentsV3Parameter) -> str:
"""Retrieves the name of an argument.

    Args:
        argument: The core schema.

    Returns:
        The name of the argument.
    """
    name = argument['name']
    if self.by_alias:
        alias = argument.get('alias')
        if isinstance(alias, str):
            name = alias
        else:
            pass  # might want to do something else?
    return name

```
  
---|---  
###  arguments_v3_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.arguments_v3_schema)
```
arguments_v3_schema(
    schema: ArgumentsV3Schema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's arguments.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ArgumentsV3Schema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defarguments_v3_schema(self, schema: core_schema.ArgumentsV3Schema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a function's arguments.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    arguments = schema['arguments_schema']
    properties: dict[str, JsonSchemaValue] = {}
    required: list[str] = []
    for argument in arguments:
        mode = argument.get('mode', 'positional_or_keyword')
        name = self.get_argument_name(argument)
        argument_schema = self.generate_inner(argument['schema']).copy()
        if mode == 'var_args':
            argument_schema = {'type': 'array', 'items': argument_schema}
        elif mode == 'var_kwargs_uniform':
            argument_schema = {'type': 'object', 'additionalProperties': argument_schema}

        argument_schema.setdefault('title', self.get_title_from_name(name))
        properties[name] = argument_schema

        if (
            (mode == 'var_kwargs_unpacked_typed_dict' and 'required' in argument_schema)
            or mode not in {'var_args', 'var_kwargs_uniform', 'var_kwargs_unpacked_typed_dict'}
            and argument['schema']['type'] != 'default'
        ):
            # This assumes that if the argument has a default value,
            # the inner schema must be of type WithDefaultSchema.
            # I believe this is true, but I am not 100% sure
            required.append(name)

    json_schema: JsonSchemaValue = {'type': 'object', 'properties': properties}
    if required:
        json_schema['required'] = required
    return json_schema

```
  
---|---  
###  call_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.call_schema)
```
call_schema(schema: CallSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function call.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CallSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
```
| ```
defcall_schema(self, schema: core_schema.CallSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a function call.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['arguments_schema'])

```
  
---|---  
###  custom_error_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.custom_error_schema)
```
custom_error_schema(
    schema: CustomErrorSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a custom error.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CustomErrorSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
```
| ```
defcustom_error_schema(self, schema: core_schema.CustomErrorSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a custom error.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```
  
---|---  
###  json_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.json_schema)
```
json_schema(schema: JsonSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a JSON object.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `JsonSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
2017
2018
2019
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029
2030
2031
2032
```
| ```
defjson_schema(self, schema: core_schema.JsonSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a JSON object.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    content_core_schema = schema.get('schema') or core_schema.any_schema()
    content_json_schema = self.generate_inner(content_core_schema)
    if self.mode == 'validation':
        return {'type': 'string', 'contentMediaType': 'application/json', 'contentSchema': content_json_schema}
    else:
        # self.mode == 'serialization'
        return content_json_schema

```
  
---|---  
###  url_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.url_schema)
```
url_schema(schema: UrlSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a URL.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `UrlSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
2034
2035
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
```
| ```
defurl_schema(self, schema: core_schema.UrlSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a URL.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = {'type': 'string', 'format': 'uri', 'minLength': 1}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.string)
    return json_schema

```
  
---|---  
###  multi_host_url_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.multi_host_url_schema)
```
multi_host_url_schema(
    schema: MultiHostUrlSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a URL that can be used with multiple hosts.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `MultiHostUrlSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defmulti_host_url_schema(self, schema: core_schema.MultiHostUrlSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a URL that can be used with multiple hosts.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # Note: 'multi-host-uri' is a custom/pydantic-specific format, not part of the JSON Schema spec
    json_schema = {'type': 'string', 'format': 'multi-host-uri', 'minLength': 1}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.string)
    return json_schema

```
  
---|---  
###  uuid_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.uuid_schema)
```
uuid_schema(schema: UuidSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a UUID.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `UuidSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defuuid_schema(self, schema: core_schema.UuidSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a UUID.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'uuid'}

```
  
---|---  
###  definitions_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.definitions_schema)
```
definitions_schema(
    schema: DefinitionsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a JSON object with definitions.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DefinitionsSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
2072
2073
2074
2075
2076
2077
2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
```
| ```
defdefinitions_schema(self, schema: core_schema.DefinitionsSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that defines a JSON object with definitions.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    for definition in schema['definitions']:
        try:
            self.generate_inner(definition)
        except PydanticInvalidForJsonSchema as e:  # noqa: PERF203
            core_ref: CoreRef = CoreRef(definition['ref'])  # type: ignore
            self._core_defs_invalid_for_json_schema[self.get_defs_ref((core_ref, self.mode))] = e
            continue
    return self.generate_inner(schema['schema'])

```
  
---|---  
###  definition_ref_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.definition_ref_schema)
```
definition_ref_schema(
    schema: DefinitionReferenceSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that references a definition.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `DefinitionReferenceSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defdefinition_ref_schema(self, schema: core_schema.DefinitionReferenceSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a schema that references a definition.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    core_ref = CoreRef(schema['schema_ref'])
    _, ref_json_schema = self.get_cache_defs_ref_schema(core_ref)
    return ref_json_schema

```
  
---|---  
###  ser_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.ser_schema)
```
ser_schema(
    schema: (
        SerSchema | IncExSeqSerSchema | IncExDictSerSchema
    ),
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue) | None

```

Generates a JSON schema that matches a schema that defines a serialized object.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `SerSchema | IncExSeqSerSchema | IncExDictSerSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue) | None` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defser_schema(
    self, schema: core_schema.SerSchema | core_schema.IncExSeqSerSchema | core_schema.IncExDictSerSchema
) -> JsonSchemaValue | None:
"""Generates a JSON schema that matches a schema that defines a serialized object.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    schema_type = schema['type']
    if schema_type == 'function-plain' or schema_type == 'function-wrap':
        # PlainSerializerFunctionSerSchema or WrapSerializerFunctionSerSchema
        return_schema = schema.get('return_schema')
        if return_schema is not None:
            return self.generate_inner(return_schema)
    elif schema_type == 'format' or schema_type == 'to-string':
        # FormatSerSchema or ToStringSerSchema
        return self.str_schema(core_schema.str_schema())
    elif schema['type'] == 'model':
        # ModelSerSchema
        return self.generate_inner(schema['schema'])
    return None

```
  
---|---  
###  complex_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.complex_schema)
```
complex_schema(schema: ComplexSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a complex number.
JSON has no standard way to represent complex numbers. Complex number is not a numeric type. Here we represent complex number as strings following the rule defined by Python. For instance, '1+2j' is an accepted complex string. Details can be found in 
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `ComplexSchema` |  The core schema. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.  
Source code in `pydantic/json_schema.py`
```
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
2138
2139
2140
2141
2142
```
| ```
defcomplex_schema(self, schema: core_schema.ComplexSchema) -> JsonSchemaValue:
"""Generates a JSON schema that matches a complex number.

    JSON has no standard way to represent complex numbers. Complex number is not a numeric
    type. Here we represent complex number as strings following the rule defined by Python.
    For instance, '1+2j' is an accepted complex string. Details can be found in
    [Python's `complex` documentation][complex].

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string'}

```
  
---|---  
###  get_title_from_name [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_title_from_name)
```
get_title_from_name(name: ) -> 
```

Retrieves a title from a name.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`name` |  |  The name to retrieve a title from. |  _required_  
Returns:
Type | Description  
---|---  
|  The title.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defget_title_from_name(self, name: str) -> str:
"""Retrieves a title from a name.

    Args:
        name: The name to retrieve a title from.

    Returns:
        The title.
    """
    return name.title().replace('_', ' ').strip()

```
  
---|---  
###  field_title_should_be_set [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.field_title_should_be_set)
```
field_title_should_be_set(
    schema: CoreSchemaOrField,
) -> 
```

Returns true if a field with the given schema should have a title set based on the field name.
Intuitively, we want this to return true for schemas that wouldn't otherwise provide their own title (e.g., int, float, str), and false for those that would (e.g., BaseModel subclasses).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`schema` |  `CoreSchemaOrField` |  The schema to check. |  _required_  
Returns:
Type | Description  
---|---  
|  `True` if the field should have a title set, `False` otherwise.  
Source code in `pydantic/json_schema.py`
```
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
2186
2187
2188
2189
2190
```
| ```
deffield_title_should_be_set(self, schema: CoreSchemaOrField) -> bool:
"""Returns true if a field with the given schema should have a title set based on the field name.

    Intuitively, we want this to return true for schemas that wouldn't otherwise provide their own title
    (e.g., int, float, str), and false for those that would (e.g., BaseModel subclasses).

    Args:
        schema: The schema to check.

    Returns:
        `True` if the field should have a title set, `False` otherwise.
    """
    if _core_utils.is_core_schema_field(schema):
        if schema['type'] == 'computed-field':
            field_schema = schema['return_schema']
        else:
            field_schema = schema['schema']
        return self.field_title_should_be_set(field_schema)

    elif _core_utils.is_core_schema(schema):
        if schema.get('ref'):  # things with refs, such as models and enums, should not have titles set
            return False
        if schema['type'] in {'default', 'nullable', 'definitions'}:
            return self.field_title_should_be_set(schema['schema'])  # type: ignore[typeddict-item]
        if _core_utils.is_function_with_inner_schema(schema):
            return self.field_title_should_be_set(schema['schema'])
        if schema['type'] == 'definition-ref':
            # Referenced schemas should not have titles set for the same reason
            # schemas with refs should not
            return False
        return True  # anything else should have title set

    else:
        raise PydanticInvalidForJsonSchema(f'Unexpected schema type: schema={schema}')  # pragma: no cover

```
  
---|---  
###  normalize_name [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.normalize_name)
```
normalize_name(name: ) -> 
```

Normalizes a name to be used as a key in a dictionary.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`name` |  |  The name to normalize. |  _required_  
Returns:
Type | Description  
---|---  
|  The normalized name.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defnormalize_name(self, name: str) -> str:
"""Normalizes a name to be used as a key in a dictionary.

    Args:
        name: The name to normalize.

    Returns:
        The normalized name.
    """
    return re.sub(r'[^a-zA-Z0-9.\-_]', '_', name).replace('.', '__')

```
  
---|---  
###  get_defs_ref [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_defs_ref)
```
get_defs_ref(core_mode_ref: CoreModeRef) -> DefsRef

```

Override this method to change the way that definitions keys are generated from a core reference.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`core_mode_ref` |  `CoreModeRef` |  The core reference. |  _required_  
Returns:
Type | Description  
---|---  
`DefsRef` |  The definitions key.  
Source code in `pydantic/json_schema.py`
```
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
2241
2242
2243
2244
2245
2246
2247
2248
2249
```
| ```
defget_defs_ref(self, core_mode_ref: CoreModeRef) -> DefsRef:
"""Override this method to change the way that definitions keys are generated from a core reference.

    Args:
        core_mode_ref: The core reference.

    Returns:
        The definitions key.
    """
    # Split the core ref into "components"; generic origins and arguments are each separate components
    core_ref, mode = core_mode_ref
    components = re.split(r'([\][,])', core_ref)
    # Remove IDs from each component
    components = [x.rsplit(':', 1)[0] for x in components]
    core_ref_no_id = ''.join(components)
    # Remove everything before the last period from each "component"
    components = [re.sub(r'(?:[^.[\]]+\.)+((?:[^.[\]]+))', r'\1', x) for x in components]
    short_ref = ''.join(components)

    mode_title = _MODE_TITLE_MAPPING[mode]

    # It is important that the generated defs_ref values be such that at least one choice will not
    # be generated for any other core_ref. Currently, this should be the case because we include
    # the id of the source type in the core_ref
    name = DefsRef(self.normalize_name(short_ref))
    name_mode = DefsRef(self.normalize_name(short_ref) + f'-{mode_title}')
    module_qualname = DefsRef(self.normalize_name(core_ref_no_id))
    module_qualname_mode = DefsRef(f'{module_qualname}-{mode_title}')
    module_qualname_id = DefsRef(self.normalize_name(core_ref))
    occurrence_index = self._collision_index.get(module_qualname_id)
    if occurrence_index is None:
        self._collision_counter[module_qualname] += 1
        occurrence_index = self._collision_index[module_qualname_id] = self._collision_counter[module_qualname]

    module_qualname_occurrence = DefsRef(f'{module_qualname}__{occurrence_index}')
    module_qualname_occurrence_mode = DefsRef(f'{module_qualname_mode}__{occurrence_index}')

    self._prioritized_defsref_choices[module_qualname_occurrence_mode] = [
        name,
        name_mode,
        module_qualname,
        module_qualname_mode,
        module_qualname_occurrence,
        module_qualname_occurrence_mode,
    ]

    return module_qualname_occurrence_mode

```
  
---|---  
###  get_cache_defs_ref_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_cache_defs_ref_schema)
```
get_cache_defs_ref_schema(
    core_ref: CoreRef,
) -> [DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]

```

This method wraps the get_defs_ref method with some cache-lookup/population logic, and returns both the produced defs_ref and the JSON schema that will refer to the right definition.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`core_ref` |  `CoreRef` |  The core reference to get the definitions reference for. |  _required_  
Returns:
Type | Description  
---|---  
`DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  A tuple of the definitions reference and the JSON schema that will refer to it.  
Source code in `pydantic/json_schema.py`
```
2251
2252
2253
2254
2255
2256
2257
2258
2259
2260
2261
2262
2263
2264
2265
2266
2267
2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
```
| ```
defget_cache_defs_ref_schema(self, core_ref: CoreRef) -> tuple[DefsRef, JsonSchemaValue]:
"""This method wraps the get_defs_ref method with some cache-lookup/population logic,
    and returns both the produced defs_ref and the JSON schema that will refer to the right definition.

    Args:
        core_ref: The core reference to get the definitions reference for.

    Returns:
        A tuple of the definitions reference and the JSON schema that will refer to it.
    """
    core_mode_ref = (core_ref, self.mode)
    maybe_defs_ref = self.core_to_defs_refs.get(core_mode_ref)
    if maybe_defs_ref is not None:
        json_ref = self.core_to_json_refs[core_mode_ref]
        return maybe_defs_ref, {'$ref': json_ref}

    defs_ref = self.get_defs_ref(core_mode_ref)

    # populate the ref translation mappings
    self.core_to_defs_refs[core_mode_ref] = defs_ref
    self.defs_to_core_refs[defs_ref] = core_mode_ref

    json_ref = JsonRef(self.ref_template.format(model=defs_ref))
    self.core_to_json_refs[core_mode_ref] = json_ref
    self.json_to_defs_refs[json_ref] = defs_ref
    ref_json_schema = {'$ref': json_ref}
    return defs_ref, ref_json_schema

```
  
---|---  
###  handle_ref_overrides [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.handle_ref_overrides)
```
handle_ref_overrides(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Remove any sibling keys that are redundant with the referenced schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The schema to remove redundant sibling keys from. |  _required_  
Returns:
Type | Description  
---|---  
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The schema with redundant sibling keys removed.  
Source code in `pydantic/json_schema.py`
```
2279
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
```
| ```
defhandle_ref_overrides(self, json_schema: JsonSchemaValue) -> JsonSchemaValue:
"""Remove any sibling keys that are redundant with the referenced schema.

    Args:
        json_schema: The schema to remove redundant sibling keys from.

    Returns:
        The schema with redundant sibling keys removed.
    """
    if '$ref' in json_schema:
        # prevent modifications to the input; this copy may be safe to drop if there is significant overhead
        json_schema = json_schema.copy()

        referenced_json_schema = self.get_schema_from_definitions(JsonRef(json_schema['$ref']))
        if referenced_json_schema is None:
            # This can happen when building schemas for models with not-yet-defined references.
            # It may be a good idea to do a recursive pass at the end of the generation to remove
            # any redundant override keys.
            return json_schema
        for k, v in list(json_schema.items()):
            if k == '$ref':
                continue
            if k in referenced_json_schema and referenced_json_schema[k] == v:
                del json_schema[k]  # redundant key

    return json_schema

```
  
---|---  
###  encode_default [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.encode_default)
```
encode_default(dft: ) -> 
```

Encode a default value to a JSON-serializable value.
This is used to encode default values for fields in the generated JSON schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`dft` |  |  The default value to encode. |  _required_  
Returns:
Type | Description  
---|---  
|  The encoded default value.  
Source code in `pydantic/json_schema.py`
```
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
2327
2328
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
```
| ```
defencode_default(self, dft: Any) -> Any:
"""Encode a default value to a JSON-serializable value.

    This is used to encode default values for fields in the generated JSON schema.

    Args:
        dft: The default value to encode.

    Returns:
        The encoded default value.
    """
    from.type_adapterimport TypeAdapter, _type_has_config

    config = self._config
    try:
        default = (
            dft
            if _type_has_config(type(dft))
            else TypeAdapter(type(dft), config=config.config_dict).dump_python(
                dft, by_alias=self.by_alias, mode='json'
            )
        )
    except PydanticSchemaGenerationError:
        raise pydantic_core.PydanticSerializationError(f'Unable to encode default value {dft}')

    return pydantic_core.to_jsonable_python(
        default, timedelta_mode=config.ser_json_timedelta, bytes_mode=config.ser_json_bytes, by_alias=self.by_alias
    )

```
  
---|---  
###  update_with_validations [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.update_with_validations)
```
update_with_validations(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
    core_schema: CoreSchema,
    mapping: [, ],
) -> None

```

Update the json_schema with the corresponding validations specified in the core_schema, using the provided mapping to translate keys in core_schema to the appropriate keys for a JSON schema.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The JSON schema to update. |  _required_  
`core_schema` |  `CoreSchema` |  The core schema to get the validations from. |  _required_  
`mapping` |  |  A mapping from core_schema attribute names to the corresponding JSON schema attribute names. |  _required_  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defupdate_with_validations(
    self, json_schema: JsonSchemaValue, core_schema: CoreSchema, mapping: dict[str, str]
) -> None:
"""Update the json_schema with the corresponding validations specified in the core_schema,
    using the provided mapping to translate keys in core_schema to the appropriate keys for a JSON schema.

    Args:
        json_schema: The JSON schema to update.
        core_schema: The core schema to get the validations from.
        mapping: A mapping from core_schema attribute names to the corresponding JSON schema attribute names.
    """
    for core_key, json_schema_key in mapping.items():
        if core_key in core_schema:
            json_schema[json_schema_key] = core_schema[core_key]

```
  
---|---  
###  get_json_ref_counts [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_json_ref_counts)
```
get_json_ref_counts(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
) -> [JsonRef, ]

```

Get all values corresponding to the key '$ref' anywhere in the json_schema.
Source code in `pydantic/json_schema.py`
```
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
2435
2436
2437
2438
2439
```
| ```
defget_json_ref_counts(self, json_schema: JsonSchemaValue) -> dict[JsonRef, int]:
"""Get all values corresponding to the key '$ref' anywhere in the json_schema."""
    json_refs: dict[JsonRef, int] = Counter()

    def_add_json_refs(schema: Any) -> None:
        if isinstance(schema, dict):
            if '$ref' in schema:
                json_ref = JsonRef(schema['$ref'])
                if not isinstance(json_ref, str):
                    return  # in this case, '$ref' might have been the name of a property
                already_visited = json_ref in json_refs
                json_refs[json_ref] += 1
                if already_visited:
                    return  # prevent recursion on a definition that was already visited
                try:
                    defs_ref = self.json_to_defs_refs[json_ref]
                    if defs_ref in self._core_defs_invalid_for_json_schema:
                        raise self._core_defs_invalid_for_json_schema[defs_ref]
                    _add_json_refs(self.definitions[defs_ref])
                except KeyError:
                    if not json_ref.startswith(('http://', 'https://')):
                        raise

            for k, v in schema.items():
                if k == 'examples' and isinstance(v, list):
                    # Skip examples that may contain arbitrary values and references
                    # (see the comment in `_get_all_json_refs` for more details).
                    continue
                _add_json_refs(v)
        elif isinstance(schema, list):
            for v in schema:
                _add_json_refs(v)

    _add_json_refs(json_schema)
    return json_refs

```
  
---|---  
###  emit_warning [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.emit_warning)
```
emit_warning(
    kind: JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind), detail: ) -> None

```

This method simply emits PydanticJsonSchemaWarnings based on handling in the `warning_message` method.
Source code in `pydantic/json_schema.py`
```
2444
2445
2446
2447
2448
```
| ```
defemit_warning(self, kind: JsonSchemaWarningKind, detail: str) -> None:
"""This method simply emits PydanticJsonSchemaWarnings based on handling in the `warning_message` method."""
    message = self.render_warning_message(kind, detail)
    if message is not None:
        warnings.warn(message, PydanticJsonSchemaWarning)

```
  
---|---  
###  render_warning_message [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.render_warning_message)
```
render_warning_message(
    kind: JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind), detail: ) -> | None

```

This method is responsible for ignoring warnings as desired, and for formatting the warning messages.
You can override the value of `ignored_warning_kinds` in a subclass of GenerateJsonSchema to modify what warnings are generated. If you want more control, you can override this method; just return None in situations where you don't want warnings to be emitted.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`kind` |  `JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind)` |  The kind of warning to render. It can be one of the following:
  * 'skipped-choice': A choice field was skipped because it had no valid choices.
  * 'non-serializable-default': A default value was skipped because it was not JSON-serializable.

|  _required_  
`detail` |  |  A string with additional details about the warning. |  _required_  
Returns:
Type | Description  
---|---  
|  The formatted warning message, or `None` if no warning should be emitted.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defrender_warning_message(self, kind: JsonSchemaWarningKind, detail: str) -> str | None:
"""This method is responsible for ignoring warnings as desired, and for formatting the warning messages.

    You can override the value of `ignored_warning_kinds` in a subclass of GenerateJsonSchema
    to modify what warnings are generated. If you want more control, you can override this method;
    just return None in situations where you don't want warnings to be emitted.

    Args:
        kind: The kind of warning to render. It can be one of the following:

            - 'skipped-choice': A choice field was skipped because it had no valid choices.
            - 'non-serializable-default': A default value was skipped because it was not JSON-serializable.
        detail: A string with additional details about the warning.

    Returns:
        The formatted warning message, or `None` if no warning should be emitted.
    """
    if kind in self.ignored_warning_kinds:
        return None
    return f'{detail} [{kind}]'

```
  
---|---  
##  WithJsonSchema `dataclass` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.WithJsonSchema)
```
WithJsonSchema(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue) | None,
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

Usage Documentation
[`WithJsonSchema` Annotation](https://docs.pydantic.dev/latest/concepts/json_schema/#withjsonschema-annotation)
Add this as an annotation on a field to override the (base) JSON schema that would be generated for that field. This provides a way to set a JSON schema for types that would otherwise raise errors when producing a JSON schema, such as Callable, or types that have an is-instance core schema, without needing to go so far as creating a custom subclass of pydantic.json_schema.GenerateJsonSchema. Note that any _modifications_ to the schema that would normally be made (such as setting the title for model fields) will still be performed.
If `mode` is set this will only apply to that schema generation mode, allowing you to set different json schemas for validation and serialization.
##  Examples [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.Examples)
```
Examples(
    examples: [, ],
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

```
Examples(
    examples: [],
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

```
Examples(
    examples: [, ] | [],
    mode: (
        ["validation", "serialization"] | None
    ) = None,
)

```

Add examples to a JSON schema.
If the JSON Schema already contains examples, the provided examples will be appended.
If `mode` is set this will only apply to that schema generation mode, allowing you to add different examples for validation and serialization.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def__init__(
    self, examples: dict[str, Any] | list[Any], mode: Literal['validation', 'serialization'] | None = None
) -> None:
    if isinstance(examples, dict):
        warnings.warn(
            'Using a dict for `examples` is deprecated, use a list instead.',
            PydanticDeprecatedSince29,
            stacklevel=2,
        )
    self.examples = examples
    self.mode = mode

```
  
---|---  
##  SkipJsonSchema `dataclass` [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.SkipJsonSchema)
```
SkipJsonSchema()

```

Usage Documentation
[`SkipJsonSchema` Annotation](https://docs.pydantic.dev/latest/concepts/json_schema/#skipjsonschema-annotation)
Add this as an annotation on a field to skip generating a JSON schema for that field.
Example
```
frompprintimport pprint
fromtypingimport Union

frompydanticimport BaseModel
frompydantic.json_schemaimport SkipJsonSchema

classModel(BaseModel):
    a: Union[int, None] = None  [](https://docs.pydantic.dev/latest/api/json_schema/#__code_180_annotation_1)
    b: Union[int, SkipJsonSchema[None]] = None  [](https://docs.pydantic.dev/latest/api/json_schema/#__code_180_annotation_2)
    c: SkipJsonSchema[Union[int, None]] = None  [](https://docs.pydantic.dev/latest/api/json_schema/#__code_180_annotation_3)

pprint(Model.model_json_schema())
'''
{
    'properties': {
        'a': {
            'anyOf': [
                {'type': 'integer'},
                {'type': 'null'}
            ],
            'default': None,
            'title': 'A'
        },
        'b': {
            'default': None,
            'title': 'B',
            'type': 'integer'
        }
    },
    'title': 'Model',
    'type': 'object'
}
'''

```

##  model_json_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.model_json_schema)
```
model_json_schema(
    cls: [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | [PydanticDataclass],
    by_alias: = True,
    ref_template: = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema),
    mode: JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode) = "validation",
) -> [, ]

```

Utility function to generate a JSON Schema for a model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | PydanticDataclass]` |  The model class to generate a JSON Schema for. |  _required_  
`by_alias` |  |  If `True` (the default), fields will be serialized according to their alias. If `False`, fields will be serialized according to their attribute name. |  `True`  
`ref_template` |  |  The template to use for generating JSON Schema references. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)`  
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the 
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`  
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)]` |  The class to use for generating the JSON Schema. |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)`  
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)` |  The mode to use for generating the JSON Schema. It can be one of the following:
  * 'validation': Generate a JSON Schema for validating data.
  * 'serialization': Generate a JSON Schema for serializing data.

|  `'validation'`  
Returns:
Type | Description  
---|---  
|  The generated JSON Schema.  
Source code in `pydantic/json_schema.py`
```
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
```
| ```
defmodel_json_schema(
    cls: type[BaseModel] | type[PydanticDataclass],
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
    mode: JsonSchemaMode = 'validation',
) -> dict[str, Any]:
"""Utility function to generate a JSON Schema for a model.

    Args:
        cls: The model class to generate a JSON Schema for.
        by_alias: If `True` (the default), fields will be serialized according to their alias.
            If `False`, fields will be serialized according to their attribute name.
        ref_template: The template to use for generating JSON Schema references.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
              keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
              keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
              type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
              `any_of`.
        schema_generator: The class to use for generating the JSON Schema.
        mode: The mode to use for generating the JSON Schema. It can be one of the following:

            - 'validation': Generate a JSON Schema for validating data.
            - 'serialization': Generate a JSON Schema for serializing data.

    Returns:
        The generated JSON Schema.
    """
    from.mainimport BaseModel

    schema_generator_instance = schema_generator(
        by_alias=by_alias, ref_template=ref_template, union_format=union_format
    )

    if isinstance(cls.__pydantic_core_schema__, _mock_val_ser.MockCoreSchema):
        cls.__pydantic_core_schema__.rebuild()

    if cls is BaseModel:
        raise AttributeError('model_json_schema() must be called on a subclass of BaseModel, not BaseModel itself.')

    assert not isinstance(cls.__pydantic_core_schema__, _mock_val_ser.MockCoreSchema), 'this is a bug! please report it'
    return schema_generator_instance.generate(cls.__pydantic_core_schema__, mode=mode)

```
  
---|---  
##  models_json_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.models_json_schema)
```
models_json_schema(
    models: [
        [
            [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | [PydanticDataclass],
            JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode),
        ]
    ],
    *,
    by_alias: = True,
    title: | None = None,
    description: | None = None,
    ref_template: = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
    schema_generator: [
        GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
    ] = GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
) -> [
    [
        [
            [BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | [PydanticDataclass],
            JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode),
        ],
        JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
    ],
    JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
]

```

Utility function to generate a JSON Schema for multiple models.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`models` |  `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | PydanticDataclass], JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)]]` |  A sequence of tuples of the form (model, mode). |  _required_  
`by_alias` |  |  Whether field aliases should be used as keys in the generated JSON Schema. |  `True`  
`title` |  |  The title of the generated JSON Schema. |  `None`  
`description` |  |  The description of the generated JSON Schema. |  `None`  
`ref_template` |  |  The reference template to use for generating JSON Schema references. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)`  
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the 
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`  
`schema_generator` |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)]` |  The schema generator to use for generating the JSON Schema. |  `GenerateJsonSchema[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)`  
Returns:
Type | Description  
---|---  
`BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)] | PydanticDataclass], JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  A tuple where: - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.) - The second element is a JSON schema containing all definitions referenced in the first returned element, along with the optional title and description keys.  
Source code in `pydantic/json_schema.py`
```
2551
2552
2553
2554
2555
2556
2557
2558
2559
2560
2561
2562
2563
2564
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
2594
2595
2596
2597
2598
2599
2600
2601
2602
2603
2604
2605
```
| ```
defmodels_json_schema(
    models: Sequence[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode]],
    *,
    by_alias: bool = True,
    title: str | None = None,
    description: str | None = None,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
) -> tuple[dict[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]:
"""Utility function to generate a JSON Schema for multiple models.

    Args:
        models: A sequence of tuples of the form (model, mode).
        by_alias: Whether field aliases should be used as keys in the generated JSON Schema.
        title: The title of the generated JSON Schema.
        description: The description of the generated JSON Schema.
        ref_template: The reference template to use for generating JSON Schema references.
        union_format: The format to use when combining schemas from unions together. Can be one of:

            - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf)
              keyword to combine schemas (the default).
            - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type)
              keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive
              type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to
              `any_of`.
        schema_generator: The schema generator to use for generating the JSON Schema.

    Returns:
        A tuple where:
            - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and
                whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have
                JsonRef references to definitions that are defined in the second returned element.)
            - The second element is a JSON schema containing all definitions referenced in the first returned
                    element, along with the optional title and description keys.
    """
    for cls, _ in models:
        if isinstance(cls.__pydantic_core_schema__, _mock_val_ser.MockCoreSchema):
            cls.__pydantic_core_schema__.rebuild()

    instance = schema_generator(by_alias=by_alias, ref_template=ref_template, union_format=union_format)
    inputs: list[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode, CoreSchema]] = [
        (m, mode, m.__pydantic_core_schema__) for m, mode in models
    ]
    json_schemas_map, definitions = instance.generate_definitions(inputs)

    json_schema: dict[str, Any] = {}
    if definitions:
        json_schema['$defs'] = definitions
    if title:
        json_schema['title'] = title
    if description:
        json_schema['description'] = description

    return json_schemas_map, json_schema

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
