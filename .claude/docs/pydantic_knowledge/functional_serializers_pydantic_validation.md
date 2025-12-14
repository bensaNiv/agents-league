---
# Smart Librarian Export (v2.0)
- Page Number: 45
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/functional_serializers
- Page Title: Functional Serializers - Pydantic Validation
- Semantic Filename: functional_serializers_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 20,903 characters
---

# Functional Serializers - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Functional Serializers
This module contains related classes and functions for serialization.
##  FieldPlainSerializer `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.FieldPlainSerializer)
```
FieldPlainSerializer: = (
    "core_schema.SerializerFunction | _Partial"
)

```

A field serializer method or function in `plain` mode.
##  FieldWrapSerializer `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.FieldWrapSerializer)
```
FieldWrapSerializer: = (
    "core_schema.WrapSerializerFunction | _Partial"
)

```

A field serializer method or function in `wrap` mode.
##  FieldSerializer `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.FieldSerializer)
```
FieldSerializer: = (
    "FieldPlainSerializer | FieldWrapSerializer"
)

```

A field serializer method or function.
##  ModelPlainSerializerWithInfo `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.ModelPlainSerializerWithInfo)
```
ModelPlainSerializerWithInfo: = [
    [, SerializationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo)[]], ]

```

A model serializer method with the `info` argument, in `plain` mode.
##  ModelPlainSerializerWithoutInfo `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.ModelPlainSerializerWithoutInfo)
```
ModelPlainSerializerWithoutInfo: = [
    [], ]

```

A model serializer method without the `info` argument, in `plain` mode.
##  ModelPlainSerializer `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.ModelPlainSerializer)
```
ModelPlainSerializer: = (
    "ModelPlainSerializerWithInfo | ModelPlainSerializerWithoutInfo"
)

```

A model serializer method in `plain` mode.
##  ModelWrapSerializerWithInfo `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.ModelWrapSerializerWithInfo)
```
ModelWrapSerializerWithInfo: = [
    [
        ,
        SerializerFunctionWrapHandler,
        SerializationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo)[],
    ],
    ,
]

```

A model serializer method with the `info` argument, in `wrap` mode.
##  ModelWrapSerializerWithoutInfo `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.ModelWrapSerializerWithoutInfo)
```
ModelWrapSerializerWithoutInfo: = [
    [, SerializerFunctionWrapHandler], ]

```

A model serializer method without the `info` argument, in `wrap` mode.
##  ModelWrapSerializer `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.ModelWrapSerializer)
```
ModelWrapSerializer: = (
    "ModelWrapSerializerWithInfo | ModelWrapSerializerWithoutInfo"
)

```

A model serializer method in `wrap` mode.
##  PlainSerializer `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.PlainSerializer)
```
PlainSerializer(
    func: SerializerFunction,
    return_type: = PydanticUndefined,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always",
)

```

Plain serializers use a function to modify the output of serialization.
This is particularly helpful when you want to customize the serialization for annotated types. Consider an input of `list`, which will be serialized into a space-delimited string.
```
fromtypingimport Annotated

frompydanticimport BaseModel, PlainSerializer

CustomStr = Annotated[
    list, PlainSerializer(lambda x: ' '.join(x), return_type=str)
]

classStudentModel(BaseModel):
    courses: CustomStr

student = StudentModel(courses=['Math', 'Chemistry', 'English'])
print(student.model_dump())
#> {'courses': 'Math Chemistry English'}

```

Attributes:
Name | Type | Description  
---|---|---  
`func` |  `SerializerFunction` |  The serializer function.  
`return_type` |  |  The return type for the function. If omitted it will be inferred from the type annotation.  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Determines when this serializer should be used. Accepts a string with values `'always'`, `'unless-none'`, `'json'`, and `'json-unless-none'`. Defaults to 'always'.  
##  WrapSerializer `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.WrapSerializer)
```
WrapSerializer(
    func: WrapSerializerFunction,
    return_type: = PydanticUndefined,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always",
)

```

Wrap serializers receive the raw inputs along with a handler function that applies the standard serialization logic, and can modify the resulting value before returning it as the final output of serialization.
For example, here's a scenario in which a wrap serializer transforms timezones to UTC **and** utilizes the existing `datetime` serialization logic.
```
fromdatetimeimport datetime, timezone
fromtypingimport Annotated, Any

frompydanticimport BaseModel, WrapSerializer

classEventDatetime(BaseModel):
    start: datetime
    end: datetime

defconvert_to_utc(value: Any, handler, info) -> dict[str, datetime]:
    # Note that `handler` can actually help serialize the `value` for
    # further custom serialization in case it's a subclass.
    partial_result = handler(value, info)
    if info.mode == 'json':
        return {
            k: datetime.fromisoformat(v).astimezone(timezone.utc)
            for k, v in partial_result.items()
        }
    return {k: v.astimezone(timezone.utc) for k, v in partial_result.items()}

UTCEventDatetime = Annotated[EventDatetime, WrapSerializer(convert_to_utc)]

classEventModel(BaseModel):
    event_datetime: UTCEventDatetime

dt = EventDatetime(
    start='2024-01-01T07:00:00-08:00', end='2024-01-03T20:00:00+06:00'
)
event = EventModel(event_datetime=dt)
print(event.model_dump())
'''
{
    'event_datetime': {
        'start': datetime.datetime(
            2024, 1, 1, 15, 0, tzinfo=datetime.timezone.utc
        ),
        'end': datetime.datetime(
            2024, 1, 3, 14, 0, tzinfo=datetime.timezone.utc
        ),
    }
}
'''

print(event.model_dump_json())
'''
{"event_datetime":{"start":"2024-01-01T15:00:00Z","end":"2024-01-03T14:00:00Z"}}
'''

```

Attributes:
Name | Type | Description  
---|---|---  
`func` |  `WrapSerializerFunction` |  The serializer function to be wrapped.  
`return_type` |  |  The return type for the function. If omitted it will be inferred from the type annotation.  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Determines when this serializer should be used. Accepts a string with values `'always'`, `'unless-none'`, `'json'`, and `'json-unless-none'`. Defaults to 'always'.  
##  SerializeAsAny `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.SerializeAsAny)
```
SerializeAsAny()

```

Annotation used to mark a type as having duck-typing serialization behavior.
See [usage documentation](https://docs.pydantic.dev/latest/concepts/serialization/#serializing-with-duck-typing) for more details.
##  field_serializer [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.field_serializer)
```
field_serializer(
    field: ,
    /,
    *fields: ,
    mode: ["wrap"],
    return_type: = ...,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = ...,
    check_fields: | None = ...,
) -> [
    [_FieldWrapSerializerT], _FieldWrapSerializerT
]

```

```
field_serializer(
    field: ,
    /,
    *fields: ,
    mode: ["plain"] = ...,
    return_type: = ...,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = ...,
    check_fields: | None = ...,
) -> [
    [_FieldPlainSerializerT], _FieldPlainSerializerT
]

```

```
field_serializer(
    *fields: ,
    mode: ["plain", "wrap"] = "plain",
    return_type: = PydanticUndefined,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always",
    check_fields: | None = None
) -> (
    [[_FieldWrapSerializerT], _FieldWrapSerializerT]
    | [
        [_FieldPlainSerializerT], _FieldPlainSerializerT
    ]
)

```

Decorator that enables custom field serialization.
In the below example, a field of type `set` is used to mitigate duplication. A `field_serializer` is used to serialize the data as a sorted list.
```
frompydanticimport BaseModel, field_serializer

classStudentModel(BaseModel):
    name: str = 'Jane'
    courses: set[str]

    @field_serializer('courses', when_used='json')
    defserialize_courses_in_order(self, courses: set[str]):
        return sorted(courses)

student = StudentModel(courses={'Math', 'Chemistry', 'English'})
print(student.model_dump_json())
#> {"name":"Jane","courses":["Chemistry","English","Math"]}

```

See [the usage documentation](https://docs.pydantic.dev/latest/concepts/serialization/#serializers) for more information.
Four signatures are supported:
  * `(self, value: Any, info: FieldSerializationInfo)`
  * `(self, value: Any, nxt: SerializerFunctionWrapHandler, info: FieldSerializationInfo)`
  * `(value: Any, info: SerializationInfo)`
  * `(value: Any, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`


Parameters:
Name | Type | Description | Default  
---|---|---|---  
`fields` |  |  Which field(s) the method should be called on. |  `()`  
`mode` |  |  The serialization mode.
  * `plain` means the function will be called instead of the default serialization logic,
  * `wrap` means the function will be called with an argument to optionally call the default serialization logic.

|  `'plain'`  
`return_type` |  |  Optional return type for the function, if omitted it will be inferred from the type annotation. |  `PydanticUndefined`  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Determines the serializer will be used for serialization. |  `'always'`  
`check_fields` |  |  Whether to check that the fields actually exist on the model. |  `None`  
Returns:
Type | Description  
---|---  
`_FieldWrapSerializerT], _FieldWrapSerializerT] | _FieldPlainSerializerT], _FieldPlainSerializerT]` |  The decorator function.  
Source code in `pydantic/functional_serializers.py`
```
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
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
```
| ```
deffield_serializer(
    *fields: str,
    mode: Literal['plain', 'wrap'] = 'plain',
    # TODO PEP 747 (grep for 'return_type' on the whole code base):
    return_type: Any = PydanticUndefined,
    when_used: WhenUsed = 'always',
    check_fields: bool | None = None,
) -> (
    Callable[[_FieldWrapSerializerT], _FieldWrapSerializerT]
    | Callable[[_FieldPlainSerializerT], _FieldPlainSerializerT]
):
"""Decorator that enables custom field serialization.

    In the below example, a field of type `set` is used to mitigate duplication. A `field_serializer` is used to serialize the data as a sorted list.

```python
    from pydantic import BaseModel, field_serializer

    class StudentModel(BaseModel):
        name: str = 'Jane'
        courses: set[str]

        @field_serializer('courses', when_used='json')
        def serialize_courses_in_order(self, courses: set[str]):
            return sorted(courses)

    student = StudentModel(courses={'Math', 'Chemistry', 'English'})
    print(student.model_dump_json())
    #> {"name":"Jane","courses":["Chemistry","English","Math"]}
```

    See [the usage documentation](../concepts/serialization.md#serializers) for more information.

    Four signatures are supported:

    - `(self, value: Any, info: FieldSerializationInfo)`
    - `(self, value: Any, nxt: SerializerFunctionWrapHandler, info: FieldSerializationInfo)`
    - `(value: Any, info: SerializationInfo)`
    - `(value: Any, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

    Args:
        fields: Which field(s) the method should be called on.
        mode: The serialization mode.

            - `plain` means the function will be called instead of the default serialization logic,
            - `wrap` means the function will be called with an argument to optionally call the
               default serialization logic.
        return_type: Optional return type for the function, if omitted it will be inferred from the type annotation.
        when_used: Determines the serializer will be used for serialization.
        check_fields: Whether to check that the fields actually exist on the model.

    Returns:
        The decorator function.
    """

    defdec(f: FieldSerializer) -> _decorators.PydanticDescriptorProxy[Any]:
        dec_info = _decorators.FieldSerializerDecoratorInfo(
            fields=fields,
            mode=mode,
            return_type=return_type,
            when_used=when_used,
            check_fields=check_fields,
        )
        return _decorators.PydanticDescriptorProxy(f, dec_info)  # pyright: ignore[reportArgumentType]

    return dec  # pyright: ignore[reportReturnType]

```
  
---|---  
##  model_serializer [¶](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.model_serializer)
```
model_serializer(
    f: _ModelPlainSerializerT,
) -> _ModelPlainSerializerT

```

```
model_serializer(
    *,
    mode: ["wrap"],
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always",
    return_type: = ...
) -> [
    [_ModelWrapSerializerT], _ModelWrapSerializerT
]

```

```
model_serializer(
    *,
    mode: ["plain"] = ...,
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always",
    return_type: = ...
) -> [
    [_ModelPlainSerializerT], _ModelPlainSerializerT
]

```

```
model_serializer(
    f: (
        _ModelPlainSerializerT
        | _ModelWrapSerializerT
        | None
    ) = None,
    /,
    *,
    mode: ["plain", "wrap"] = "plain",
    when_used: WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed) = "always",
    return_type: = PydanticUndefined,
) -> (
    _ModelPlainSerializerT
    | [
        [_ModelWrapSerializerT], _ModelWrapSerializerT
    ]
    | [
        [_ModelPlainSerializerT], _ModelPlainSerializerT
    ]
)

```

Decorator that enables custom model serialization.
This is useful when a model need to be serialized in a customized manner, allowing for flexibility beyond just specific fields.
An example would be to serialize temperature to the same temperature scale, such as degrees Celsius.
```
fromtypingimport Literal

frompydanticimport BaseModel, model_serializer

classTemperatureModel(BaseModel):
    unit: Literal['C', 'F']
    value: int

    @model_serializer()
    defserialize_model(self):
        if self.unit == 'F':
            return {'unit': 'C', 'value': int((self.value - 32) / 1.8)}
        return {'unit': self.unit, 'value': self.value}

temperature = TemperatureModel(unit='F', value=212)
print(temperature.model_dump())
#> {'unit': 'C', 'value': 100}

```

Two signatures are supported for `mode='plain'`, which is the default:
  * `(self)`
  * `(self, info: SerializationInfo)`


And two other signatures for `mode='wrap'`:
  * `(self, nxt: SerializerFunctionWrapHandler)`
  * `(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`
See [the usage documentation](https://docs.pydantic.dev/latest/concepts/serialization/#serializers) for more information.


Parameters:
Name | Type | Description | Default  
---|---|---|---  
`f` |  `_ModelPlainSerializerT | _ModelWrapSerializerT | None` |  The function to be decorated. |  `None`  
`mode` |  |  The serialization mode.
  * `'plain'` means the function will be called instead of the default serialization logic
  * `'wrap'` means the function will be called with an argument to optionally call the default serialization logic.

|  `'plain'`  
`when_used` |  `WhenUsed[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)` |  Determines when this serializer should be used. |  `'always'`  
`return_type` |  |  The return type for the function. If omitted it will be inferred from the type annotation. |  `PydanticUndefined`  
Returns:
Type | Description  
---|---  
`_ModelPlainSerializerT | _ModelWrapSerializerT], _ModelWrapSerializerT] | _ModelPlainSerializerT], _ModelPlainSerializerT]` |  The decorator function.  
Source code in `pydantic/functional_serializers.py`
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
```
| ```
defmodel_serializer(
    f: _ModelPlainSerializerT | _ModelWrapSerializerT | None = None,
    /,
    *,
    mode: Literal['plain', 'wrap'] = 'plain',
    when_used: WhenUsed = 'always',
    return_type: Any = PydanticUndefined,
) -> (
    _ModelPlainSerializerT
    | Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT]
    | Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]
):
"""Decorator that enables custom model serialization.

    This is useful when a model need to be serialized in a customized manner, allowing for flexibility beyond just specific fields.

    An example would be to serialize temperature to the same temperature scale, such as degrees Celsius.

```python
    from typing import Literal

    from pydantic import BaseModel, model_serializer

    class TemperatureModel(BaseModel):
        unit: Literal['C', 'F']
        value: int

        @model_serializer()
        def serialize_model(self):
            if self.unit == 'F':
                return {'unit': 'C', 'value': int((self.value - 32) / 1.8)}
            return {'unit': self.unit, 'value': self.value}

    temperature = TemperatureModel(unit='F', value=212)
    print(temperature.model_dump())
    #> {'unit': 'C', 'value': 100}
```

    Two signatures are supported for `mode='plain'`, which is the default:

    - `(self)`
    - `(self, info: SerializationInfo)`

    And two other signatures for `mode='wrap'`:

    - `(self, nxt: SerializerFunctionWrapHandler)`
    - `(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

        See [the usage documentation](../concepts/serialization.md#serializers) for more information.

    Args:
        f: The function to be decorated.
        mode: The serialization mode.

            - `'plain'` means the function will be called instead of the default serialization logic
            - `'wrap'` means the function will be called with an argument to optionally call the default
                serialization logic.
        when_used: Determines when this serializer should be used.
        return_type: The return type for the function. If omitted it will be inferred from the type annotation.

    Returns:
        The decorator function.
    """

    defdec(f: ModelSerializer) -> _decorators.PydanticDescriptorProxy[Any]:
        dec_info = _decorators.ModelSerializerDecoratorInfo(mode=mode, return_type=return_type, when_used=when_used)
        return _decorators.PydanticDescriptorProxy(f, dec_info)

    if f is None:
        return dec  # pyright: ignore[reportReturnType]
    else:
        return dec(f)  # pyright: ignore[reportReturnType]

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
