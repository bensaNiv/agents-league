---
# Smart Librarian Export (v2.0)
- Page Number: 48
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/dataclasses
- Page Title: Pydantic Dataclasses - Pydantic Validation
- Semantic Filename: pydantic_dataclasses_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 22,837 characters
---

# Pydantic Dataclasses - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Pydantic Dataclasses
Provide an enhanced dataclass that performs validation.
##  dataclass [¶](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.dataclass)
```
dataclass(
    *,
    init: [False] = False,
    repr: = True,
    eq: = True,
    order: = False,
    unsafe_hash: = False,
    frozen: = False,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | [] | None = None,
    validate_on_init: | None = None,
    kw_only: = ...,
    slots: = ...
) -> [[[_T]], [PydanticDataclass]]

```

```
dataclass(
    _cls: [_T],
    *,
    init: [False] = False,
    repr: = True,
    eq: = True,
    order: = False,
    unsafe_hash: = False,
    frozen: | None = None,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | [] | None = None,
    validate_on_init: | None = None,
    kw_only: = ...,
    slots: = ...
) -> [PydanticDataclass]

```

```
dataclass(
    *,
    init: [False] = False,
    repr: = True,
    eq: = True,
    order: = False,
    unsafe_hash: = False,
    frozen: | None = None,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | [] | None = None,
    validate_on_init: | None = None
) -> [[[_T]], [PydanticDataclass]]

```

```
dataclass(
    _cls: [_T],
    *,
    init: [False] = False,
    repr: = True,
    eq: = True,
    order: = False,
    unsafe_hash: = False,
    frozen: | None = None,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | [] | None = None,
    validate_on_init: | None = None
) -> [PydanticDataclass]

```

```
dataclass(
    _cls: [_T] | None = None,
    *,
    init: [False] = False,
    repr: = True,
    eq: = True,
    order: = False,
    unsafe_hash: = False,
    frozen: | None = None,
    config: ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | [] | None = None,
    validate_on_init: | None = None,
    kw_only: = False,
    slots: = False
) -> (
    [[[_T]], [PydanticDataclass]]
    | [PydanticDataclass]
)

```

Usage Documentation
[`dataclasses`](https://docs.pydantic.dev/latest/concepts/dataclasses/)
A decorator used to create a Pydantic-enhanced dataclass, similar to the standard Python `dataclass`, but with added validation.
This function should be used similarly to `dataclasses.dataclass`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`_cls` |  `_T] | None` |  The target `dataclass`. |  `None`  
`init` |  |  Included for signature compatibility with `dataclasses.dataclass`, and is passed through to `dataclasses.dataclass` when appropriate. If specified, must be set to `False`, as pydantic inserts its own `__init__` function. |  `False`  
`repr` |  |  A boolean indicating whether to include the field in the `__repr__` output. |  `True`  
`eq` |  |  Determines if a `__eq__` method should be generated for the class. |  `True`  
`order` |  |  Determines if comparison magic methods should be generated, such as `__lt__`, but not `__eq__`. |  `False`  
`unsafe_hash` |  |  Determines if a `__hash__` method should be included in the class, as in `dataclasses.dataclass`. |  `False`  
`frozen` |  |  Determines if the generated class should be a 'frozen' `dataclass`, which does not allow its attributes to be modified after it has been initialized. If not set, the value from the provided `config` argument will be used (and will default to `False` otherwise). |  `None`  
`config` |  `ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) | ` |  The Pydantic config to use for the `dataclass`. |  `None`  
`validate_on_init` |  |  A deprecated parameter included for backwards compatibility; in V2, all Pydantic dataclasses are validated on init. |  `None`  
`kw_only` |  |  Determines if `__init__` method parameters must be specified by keyword only. Defaults to `False`. |  `False`  
`slots` |  |  Determines if the generated class should be a 'slots' `dataclass`, which does not allow the addition of new attributes after instantiation. |  `False`  
Returns:
Type | Description  
---|---  
`_T]], PydanticDataclass]] | PydanticDataclass]` |  A decorator that accepts a class as its argument and returns a Pydantic `dataclass`.  
Raises:
Type | Description  
---|---  
|  Raised if `init` is not `False` or `validate_on_init` is `False`.  
Source code in `pydantic/dataclasses.py`
```
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
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
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
307
308
309
310
311
312
313
```
| ```
@dataclass_transform(field_specifiers=(dataclasses.field, Field, PrivateAttr))
defdataclass(
    _cls: type[_T] | None = None,
    *,
    init: Literal[False] = False,
    repr: bool = True,
    eq: bool = True,
    order: bool = False,
    unsafe_hash: bool = False,
    frozen: bool | None = None,
    config: ConfigDict | type[object] | None = None,
    validate_on_init: bool | None = None,
    kw_only: bool = False,
    slots: bool = False,
) -> Callable[[type[_T]], type[PydanticDataclass]] | type[PydanticDataclass]:
"""!!! abstract "Usage Documentation"
        [`dataclasses`](../concepts/dataclasses.md)

    A decorator used to create a Pydantic-enhanced dataclass, similar to the standard Python `dataclass`,
    but with added validation.

    This function should be used similarly to `dataclasses.dataclass`.

    Args:
        _cls: The target `dataclass`.
        init: Included for signature compatibility with `dataclasses.dataclass`, and is passed through to
            `dataclasses.dataclass` when appropriate. If specified, must be set to `False`, as pydantic inserts its
            own  `__init__` function.
        repr: A boolean indicating whether to include the field in the `__repr__` output.
        eq: Determines if a `__eq__` method should be generated for the class.
        order: Determines if comparison magic methods should be generated, such as `__lt__`, but not `__eq__`.
        unsafe_hash: Determines if a `__hash__` method should be included in the class, as in `dataclasses.dataclass`.
        frozen: Determines if the generated class should be a 'frozen' `dataclass`, which does not allow its
            attributes to be modified after it has been initialized. If not set, the value from the provided `config` argument will be used (and will default to `False` otherwise).
        config: The Pydantic config to use for the `dataclass`.
        validate_on_init: A deprecated parameter included for backwards compatibility; in V2, all Pydantic dataclasses
            are validated on init.
        kw_only: Determines if `__init__` method parameters must be specified by keyword only. Defaults to `False`.
        slots: Determines if the generated class should be a 'slots' `dataclass`, which does not allow the addition of
            new attributes after instantiation.

    Returns:
        A decorator that accepts a class as its argument and returns a Pydantic `dataclass`.

    Raises:
        AssertionError: Raised if `init` is not `False` or `validate_on_init` is `False`.
    """
    assert init is False, 'pydantic.dataclasses.dataclass only supports init=False'
    assert validate_on_init is not False, 'validate_on_init=False is no longer supported'

    if sys.version_info >= (3, 10):
        kwargs = {'kw_only': kw_only, 'slots': slots}
    else:
        kwargs = {}

    defcreate_dataclass(cls: type[Any]) -> type[PydanticDataclass]:
"""Create a Pydantic dataclass from a regular dataclass.

        Args:
            cls: The class to create the Pydantic dataclass from.

        Returns:
            A Pydantic dataclass.
        """
        from._internal._utilsimport is_model_class

        if is_model_class(cls):
            raise PydanticUserError(
                f'Cannot create a Pydantic dataclass from {cls.__name__} as it is already a Pydantic model',
                code='dataclass-on-model',
            )

        original_cls = cls

        # we warn on conflicting config specifications, but only if the class doesn't have a dataclass base
        # because a dataclass base might provide a __pydantic_config__ attribute that we don't want to warn about
        has_dataclass_base = any(dataclasses.is_dataclass(base) for base in cls.__bases__)
        if not has_dataclass_base and config is not None and hasattr(cls, '__pydantic_config__'):
            warn(
                f'`config` is set via both the `dataclass` decorator and `__pydantic_config__` for dataclass {cls.__name__}. '
                f'The `config` specification from `dataclass` decorator will take priority.',
                category=UserWarning,
                stacklevel=2,
            )

        # if config is not explicitly provided, try to read it from the type
        config_dict = config if config is not None else getattr(cls, '__pydantic_config__', None)
        config_wrapper = _config.ConfigWrapper(config_dict)
        decorators = _decorators.DecoratorInfos.build(cls)
        decorators.update_from_config(config_wrapper)

        # Keep track of the original __doc__ so that we can restore it after applying the dataclasses decorator
        # Otherwise, classes with no __doc__ will have their signature added into the JSON schema description,
        # since dataclasses.dataclass will set this as the __doc__
        original_doc = cls.__doc__

        if _pydantic_dataclasses.is_stdlib_dataclass(cls):
            # Vanilla dataclasses include a default docstring (representing the class signature),
            # which we don't want to preserve.
            original_doc = None

            # We don't want to add validation to the existing std lib dataclass, so we will subclass it
            #   If the class is generic, we need to make sure the subclass also inherits from Generic
            #   with all the same parameters.
            bases = (cls,)
            if issubclass(cls, Generic):
                generic_base = Generic[cls.__parameters__]  # type: ignore
                bases = bases + (generic_base,)
            cls = types.new_class(cls.__name__, bases)

        # Respect frozen setting from dataclass constructor and fallback to config setting if not provided
        if frozen is not None:
            frozen_ = frozen
            if config_wrapper.frozen:
                # It's not recommended to define both, as the setting from the dataclass decorator will take priority.
                warn(
                    f'`frozen` is set via both the `dataclass` decorator and `config` for dataclass {cls.__name__!r}.'
                    'This is not recommended. The `frozen` specification on `dataclass` will take priority.',
                    category=UserWarning,
                    stacklevel=2,
                )
        else:
            frozen_ = config_wrapper.frozen or False

        # Make Pydantic's `Field()` function compatible with stdlib dataclasses. As we'll decorate
        # `cls` with the stdlib `@dataclass` decorator first, there are two attributes, `kw_only` and
        # `repr` that need to be understood *during* the stdlib creation. We do so in two steps:

        # 1. On the decorated class, wrap `Field()` assignment with `dataclass.field()`, with the
        # two attributes set (done in `as_dataclass_field()`)
        cls_anns = _typing_extra.safe_get_annotations(cls)
        for field_name in cls_anns:
            # We should look for assignments in `__dict__` instead, but for now we follow
            # the same behavior as stdlib dataclasses (see https://github.com/python/cpython/issues/88609)
            field_value = getattr(cls, field_name, None)
            if isinstance(field_value, FieldInfo):
                setattr(cls, field_name, _pydantic_dataclasses.as_dataclass_field(field_value))

        # 2. For bases of `cls` that are stdlib dataclasses, we temporarily patch their fields
        # (see the docstring of the context manager):
        with _pydantic_dataclasses.patch_base_fields(cls):
            cls = dataclasses.dataclass(  # pyright: ignore[reportCallIssue]
                cls,
                # the value of init here doesn't affect anything except that it makes it easier to generate a signature
                init=True,
                repr=repr,
                eq=eq,
                order=order,
                unsafe_hash=unsafe_hash,
                frozen=frozen_,
                **kwargs,
            )

        if config_wrapper.validate_assignment:
            original_setattr = cls.__setattr__

            @functools.wraps(cls.__setattr__)
            defvalidated_setattr(instance: PydanticDataclass, name: str, value: Any, /) -> None:
                if frozen_:
                    return original_setattr(instance, name, value)  # pyright: ignore[reportCallIssue]
                inst_cls = type(instance)
                attr = getattr(inst_cls, name, None)

                if isinstance(attr, property):
                    attr.__set__(instance, value)
                elif isinstance(attr, functools.cached_property):
                    instance.__dict__.__setitem__(name, value)
                else:
                    inst_cls.__pydantic_validator__.validate_assignment(instance, name, value)

            cls.__setattr__ = validated_setattr.__get__(None, cls)  # type: ignore

            if slots and not hasattr(cls, '__setstate__'):
                # If slots is set, `pickle` (relied on by `copy.copy()`) will use
                # `__setattr__()` to reconstruct the dataclass. However, the custom
                # `__setattr__()` set above relies on `validate_assignment()`, which
                # in turn expects all the field values to be already present on the
                # instance, resulting in attribute errors.
                # As such, we make use of `object.__setattr__()` instead.
                # Note that we do so only if `__setstate__()` isn't already set (this is the
                # case if on top of `slots`, `frozen` is used).

                # Taken from `dataclasses._dataclass_get/setstate()`:
                def_dataclass_getstate(self: Any) -> list[Any]:
                    return [getattr(self, f.name) for f in dataclasses.fields(self)]

                def_dataclass_setstate(self: Any, state: list[Any]) -> None:
                    for field, value in zip(dataclasses.fields(self), state):
                        object.__setattr__(self, field.name, value)

                cls.__getstate__ = _dataclass_getstate  # pyright: ignore[reportAttributeAccessIssue]
                cls.__setstate__ = _dataclass_setstate  # pyright: ignore[reportAttributeAccessIssue]

        # This is an undocumented attribute to distinguish stdlib/Pydantic dataclasses.
        # It should be set as early as possible:
        cls.__is_pydantic_dataclass__ = True
        cls.__pydantic_decorators__ = decorators  # type: ignore
        cls.__doc__ = original_doc
        # Can be non-existent for dynamically created classes:
        firstlineno = getattr(original_cls, '__firstlineno__', None)
        cls.__module__ = original_cls.__module__
        if sys.version_info >= (3, 13) and firstlineno is not None:
            # As per https://docs.python.org/3/reference/datamodel.html#type.__firstlineno__:
            # Setting the `__module__` attribute removes the `__firstlineno__` item from the type’s dictionary.
            original_cls.__firstlineno__ = firstlineno
            cls.__firstlineno__ = firstlineno
        cls.__qualname__ = original_cls.__qualname__
        cls.__pydantic_fields_complete__ = classmethod(_pydantic_fields_complete)
        cls.__pydantic_complete__ = False  # `complete_dataclass` will set it to `True` if successful.
        # TODO `parent_namespace` is currently None, but we could do the same thing as Pydantic models:
        # fetch the parent ns using `parent_frame_namespace` (if the dataclass was defined in a function),
        # and possibly cache it (see the `__pydantic_parent_namespace__` logic for models).
        _pydantic_dataclasses.complete_dataclass(cls, config_wrapper, raise_errors=False)
        return cls

    return create_dataclass if _cls is None else create_dataclass(_cls)

```
  
---|---  
##  rebuild_dataclass [¶](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.rebuild_dataclass)
```
rebuild_dataclass(
    cls: [PydanticDataclass],
    *,
    force: = False,
    raise_errors: = True,
    _parent_namespace_depth: = 2,
    _types_namespace: MappingNamespace | None = None
) -> | None

```

Try to rebuild the pydantic-core schema for the dataclass.
This may be necessary when one of the annotations is a ForwardRef which could not be resolved during the initial attempt to build the schema, and automatic rebuilding fails.
This is analogous to `BaseModel.model_rebuild`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`cls` |  `PydanticDataclass]` |  The class to rebuild the pydantic-core schema for. |  _required_  
`force` |  |  Whether to force the rebuilding of the schema, defaults to `False`. |  `False`  
`raise_errors` |  |  Whether to raise errors, defaults to `True`. |  `True`  
`_parent_namespace_depth` |  |  The depth level of the parent namespace, defaults to 2. |  `2`  
`_types_namespace` |  `MappingNamespace | None` |  The types namespace, defaults to `None`. |  `None`  
Returns:
Type | Description  
---|---  
|  Returns `None` if the schema is already "complete" and rebuilding was not required.  
|  If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.  
Source code in `pydantic/dataclasses.py`
```
340
341
342
343
344
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
```
| ```
defrebuild_dataclass(
    cls: type[PydanticDataclass],
    *,
    force: bool = False,
    raise_errors: bool = True,
    _parent_namespace_depth: int = 2,
    _types_namespace: MappingNamespace | None = None,
) -> bool | None:
"""Try to rebuild the pydantic-core schema for the dataclass.

    This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
    the initial attempt to build the schema, and automatic rebuilding fails.

    This is analogous to `BaseModel.model_rebuild`.

    Args:
        cls: The class to rebuild the pydantic-core schema for.
        force: Whether to force the rebuilding of the schema, defaults to `False`.
        raise_errors: Whether to raise errors, defaults to `True`.
        _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
        _types_namespace: The types namespace, defaults to `None`.

    Returns:
        Returns `None` if the schema is already "complete" and rebuilding was not required.
        If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
    """
    if not force and cls.__pydantic_complete__:
        return None

    for attr in ('__pydantic_core_schema__', '__pydantic_validator__', '__pydantic_serializer__'):
        if attr in cls.__dict__ and not isinstance(getattr(cls, attr), _mock_val_ser.MockValSer):
            # Deleting the validator/serializer is necessary as otherwise they can get reused in
            # pydantic-core. Same applies for the core schema that can be reused in schema generation.
            delattr(cls, attr)

    cls.__pydantic_complete__ = False

    if _types_namespace is not None:
        rebuild_ns = _types_namespace
    elif _parent_namespace_depth > 0:
        rebuild_ns = _typing_extra.parent_frame_namespace(parent_depth=_parent_namespace_depth, force=True) or {}
    else:
        rebuild_ns = {}

    ns_resolver = _namespace_utils.NsResolver(
        parent_namespace=rebuild_ns,
    )

    return _pydantic_dataclasses.complete_dataclass(
        cls,
        _config.ConfigWrapper(cls.__pydantic_config__, check=False),
        raise_errors=raise_errors,
        ns_resolver=ns_resolver,
        # We could provide a different config instead (with `'defer_build'` set to `True`)
        # of this explicit `_force_build` argument, but because config can come from the
        # decorator parameter or the `__pydantic_config__` attribute, `complete_dataclass`
        # will overwrite `__pydantic_config__` with the provided config above:
        _force_build=True,
    )

```
  
---|---  
##  is_pydantic_dataclass [¶](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.is_pydantic_dataclass)
```
is_pydantic_dataclass(
    class_: [],
) -> [[PydanticDataclass]]

```

Whether a class is a pydantic dataclass.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`class_` |  |  The class. |  _required_  
Returns:
Type | Description  
---|---  
`PydanticDataclass]]` |  `True` if the class is a pydantic dataclass, `False` otherwise.  
Source code in `pydantic/dataclasses.py`
```
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
```
| ```
defis_pydantic_dataclass(class_: type[Any], /) -> TypeGuard[type[PydanticDataclass]]:
"""Whether a class is a pydantic dataclass.

    Args:
        class_: The class.

    Returns:
        `True` if the class is a pydantic dataclass, `False` otherwise.
    """
    try:
        return '__is_pydantic_dataclass__' in class_.__dict__ and dataclasses.is_dataclass(class_)
    except AttributeError:
        return False

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
