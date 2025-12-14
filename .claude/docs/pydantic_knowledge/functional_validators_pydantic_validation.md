---
# Smart Librarian Export (v2.0)
- Page Number: 49
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/functional_validators
- Page Title: Functional Validators - Pydantic Validation
- Semantic Filename: functional_validators_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 24,291 characters
---

# Functional Validators - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Functional Validators
This module contains related classes and functions for validation.
##  ModelAfterValidatorWithoutInfo `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelAfterValidatorWithoutInfo)
```
ModelAfterValidatorWithoutInfo = [
    [_ModelType], _ModelType
]

```

A `@model_validator` decorated function signature. This is used when `mode='after'` and the function does not have info argument.
##  ModelAfterValidator `module-attribute` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelAfterValidator)
```
ModelAfterValidator = [
    [_ModelType, ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)[]], _ModelType
]

```

A `@model_validator` decorated function signature. This is used when `mode='after'`.
##  AfterValidator `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.AfterValidator)
```
AfterValidator(
    func: (
        NoInfoValidatorFunction | WithInfoValidatorFunction
    ),
)

```

Usage Documentation
[field _after_ validators](https://docs.pydantic.dev/latest/concepts/validators/#field-after-validator)
A metadata class that indicates that a validation should be applied **after** the inner validation logic.
Attributes:
Name | Type | Description  
---|---|---  
`func` |  `NoInfoValidatorFunction | WithInfoValidatorFunction` |  The validator function.  
Example
```
fromtypingimport Annotated

frompydanticimport AfterValidator, BaseModel, ValidationError

MyInt = Annotated[int, AfterValidator(lambda v: v + 1)]

classModel(BaseModel):
    a: MyInt

print(Model(a=1).a)
#> 2

try:
    Model(a='a')
except ValidationError as e:
    print(e.json(indent=2))
'''
    [
      {
        "type": "int_parsing",
        "loc": [
          "a"
        ],
        "msg": "Input should be a valid integer, unable to parse string as an integer",
        "input": "a",
        "url": "https://errors.pydantic.dev/2/v/int_parsing"
      }
    ]
    '''

```

##  BeforeValidator `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.BeforeValidator)
```
BeforeValidator(
    func: (
        NoInfoValidatorFunction | WithInfoValidatorFunction
    ),
    json_schema_input_type: = PydanticUndefined,
)

```

Usage Documentation
[field _before_ validators](https://docs.pydantic.dev/latest/concepts/validators/#field-before-validator)
A metadata class that indicates that a validation should be applied **before** the inner validation logic.
Attributes:
Name | Type | Description  
---|---|---  
`func` |  `NoInfoValidatorFunction | WithInfoValidatorFunction` |  The validator function.  
`json_schema_input_type` |  |  The input type used to generate the appropriate JSON Schema (in validation mode). The actual input type is `Any`.  
Example
```
fromtypingimport Annotated

frompydanticimport BaseModel, BeforeValidator

MyInt = Annotated[int, BeforeValidator(lambda v: v + 1)]

classModel(BaseModel):
    a: MyInt

print(Model(a=1).a)
#> 2

try:
    Model(a='a')
except TypeError as e:
    print(e)
    #> can only concatenate str (not "int") to str

```

##  PlainValidator `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.PlainValidator)
```
PlainValidator(
    func: (
        NoInfoValidatorFunction | WithInfoValidatorFunction
    ),
    json_schema_input_type: = ,
)

```

Usage Documentation
[field _plain_ validators](https://docs.pydantic.dev/latest/concepts/validators/#field-plain-validator)
A metadata class that indicates that a validation should be applied **instead** of the inner validation logic.
Note
Before v2.9, `PlainValidator` wasn't always compatible with JSON Schema generation for `mode='validation'`. You can now use the `json_schema_input_type` argument to specify the input type of the function to be used in the JSON schema when `mode='validation'` (the default). See the example below for more details.
Attributes:
Name | Type | Description  
---|---|---  
`func` |  `NoInfoValidatorFunction | WithInfoValidatorFunction` |  The validator function.  
`json_schema_input_type` |  |  The input type used to generate the appropriate JSON Schema (in validation mode). The actual input type is `Any`.  
Example
```
fromtypingimport Annotated, Union

frompydanticimport BaseModel, PlainValidator

defvalidate(v: object) -> int:
    if not isinstance(v, (int, str)):
        raise ValueError(f'Expected int or str, go {type(v)}')

    return int(v) + 1

MyInt = Annotated[
    int,
    PlainValidator(validate, json_schema_input_type=Union[str, int]),  [](https://docs.pydantic.dev/latest/api/functional_validators/#__code_7_annotation_1)
]

classModel(BaseModel):
    a: MyInt

print(Model(a='1').a)
#> 2

print(Model(a=1).a)
#> 2

```

##  WrapValidator `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.WrapValidator)
```
WrapValidator(
    func: (
        NoInfoWrapValidatorFunction
        | WithInfoWrapValidatorFunction
    ),
    json_schema_input_type: = PydanticUndefined,
)

```

Usage Documentation
[field _wrap_ validators](https://docs.pydantic.dev/latest/concepts/validators/#field-wrap-validator)
A metadata class that indicates that a validation should be applied **around** the inner validation logic.
Attributes:
Name | Type | Description  
---|---|---  
`func` |  `NoInfoWrapValidatorFunction | WithInfoWrapValidatorFunction` |  The validator function.  
`json_schema_input_type` |  |  The input type used to generate the appropriate JSON Schema (in validation mode). The actual input type is `Any`.  
```
fromdatetimeimport datetime
fromtypingimport Annotated

frompydanticimport BaseModel, ValidationError, WrapValidator

defvalidate_timestamp(v, handler):
    if v == 'now':
        # we don't want to bother with further validation, just return the new value
        return datetime.now()
    try:
        return handler(v)
    except ValidationError:
        # validation failed, in this case we want to return a default value
        return datetime(2000, 1, 1)

MyTimestamp = Annotated[datetime, WrapValidator(validate_timestamp)]

classModel(BaseModel):
    a: MyTimestamp

print(Model(a='now').a)
#> 2032-01-02 03:04:05.000006
print(Model(a='invalid').a)
#> 2000-01-01 00:00:00

```

##  ModelWrapValidatorHandler [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelWrapValidatorHandler)
Bases: `ValidatorFunctionWrapHandler`, `_ModelTypeCo]`
`@model_validator` decorated function handler argument type. This is used when `mode='wrap'`.
##  ModelWrapValidatorWithoutInfo [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelWrapValidatorWithoutInfo)
Bases: `_ModelType]`
A `@model_validator` decorated function signature. This is used when `mode='wrap'` and the function does not have info argument.
##  ModelWrapValidator [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelWrapValidator)
Bases: `_ModelType]`
A `@model_validator` decorated function signature. This is used when `mode='wrap'`.
##  FreeModelBeforeValidatorWithoutInfo [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.FreeModelBeforeValidatorWithoutInfo)
Bases: 
A `@model_validator` decorated function signature. This is used when `mode='before'` and the function does not have info argument.
##  ModelBeforeValidatorWithoutInfo [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelBeforeValidatorWithoutInfo)
Bases: 
A `@model_validator` decorated function signature. This is used when `mode='before'` and the function does not have info argument.
##  FreeModelBeforeValidator [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.FreeModelBeforeValidator)
Bases: 
A `@model_validator` decorated function signature. This is used when `mode='before'`.
##  ModelBeforeValidator [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelBeforeValidator)
Bases: 
A `@model_validator` decorated function signature. This is used when `mode='before'`.
##  InstanceOf `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.InstanceOf)
```
InstanceOf()

```

Generic type for annotating a type that is an instance of a given class.
Example
```
frompydanticimport BaseModel, InstanceOf

classFoo:
    ...

classBar(BaseModel):
    foo: InstanceOf[Foo]

Bar(foo=Foo())
try:
    Bar(foo=42)
except ValidationError as e:
    print(e)
"""
    [
    │   {
    │   │   'type': 'is_instance_of',
    │   │   'loc': ('foo',),
    │   │   'msg': 'Input should be an instance of Foo',
    │   │   'input': 42,
    │   │   'ctx': {'class': 'Foo'},
    │   │   'url': 'https://errors.pydantic.dev/0.38.0/v/is_instance_of'
    │   }
    ]
    """

```

##  SkipValidation `dataclass` [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.SkipValidation)
```
SkipValidation()

```

If this is applied as an annotation (e.g., via `x: Annotated[int, SkipValidation]`), validation will be skipped. You can also use `SkipValidation[int]` as a shorthand for `Annotated[int, SkipValidation]`.
This can be useful if you want to use a type annotation for documentation/IDE/type-checking purposes, and know that it is safe to skip validation for one or more of the fields.
Because this converts the validation schema to `any_schema`, subsequent annotation-applied transformations may not have the expected effects. Therefore, when used, this annotation should generally be the final annotation applied to a type.
##  ValidateAs [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ValidateAs)
```
ValidateAs(
    from_type: [_FromTypeT],
    /,
    instantiation_hook: [[_FromTypeT], ],
)

```

A helper class to validate a custom type from a type that is natively supported by Pydantic.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`from_type` |  `_FromTypeT]` |  The type natively supported by Pydantic to use to perform validation. |  _required_  
`instantiation_hook` |  `_FromTypeT], ` |  A callable taking the validated type as an argument, and returning the populated custom type. |  _required_  
Example
```
fromtypingimport Annotated

frompydanticimport BaseModel, TypeAdapter, ValidateAs

classMyCls:
    def__init__(self, a: int) -> None:
        self.a = a

    def__repr__(self) -> str:
        return f"MyCls(a={self.a})"

classModel(BaseModel):
    a: int


ta = TypeAdapter(
    Annotated[MyCls, ValidateAs(Model, lambda v: MyCls(a=v.a))]
)

print(ta.validate_python({'a': 1}))
#> MyCls(a=1)

```

Source code in `pydantic/functional_validators.py`
```
884
885
886
```
| ```
def__init__(self, from_type: type[_FromTypeT], /, instantiation_hook: Callable[[_FromTypeT], Any]) -> None:
    self.from_type = from_type
    self.instantiation_hook = instantiation_hook

```
  
---|---  
##  field_validator [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.field_validator)
```
field_validator(
    field: ,
    /,
    *fields: ,
    mode: ["wrap"],
    check_fields: | None = ...,
    json_schema_input_type: = ...,
) -> [[_V2WrapValidatorType], _V2WrapValidatorType]

```

```
field_validator(
    field: ,
    /,
    *fields: ,
    mode: ["before", "plain"],
    check_fields: | None = ...,
    json_schema_input_type: = ...,
) -> [
    [_V2BeforeAfterOrPlainValidatorType],
    _V2BeforeAfterOrPlainValidatorType,
]

```

```
field_validator(
    field: ,
    /,
    *fields: ,
    mode: ["after"] = ...,
    check_fields: | None = ...,
) -> [
    [_V2BeforeAfterOrPlainValidatorType],
    _V2BeforeAfterOrPlainValidatorType,
]

```

```
field_validator(
    field: ,
    /,
    *fields: ,
    mode: FieldValidatorModes = "after",
    check_fields: | None = None,
    json_schema_input_type: = PydanticUndefined,
) -> [[], ]

```

Usage Documentation
[field validators](https://docs.pydantic.dev/latest/concepts/validators/#field-validators)
Decorate methods on the class indicating that they should be used to validate fields.
Example usage: 
```
fromtypingimport Any

frompydanticimport (
    BaseModel,
    ValidationError,
    field_validator,
)

classModel(BaseModel):
    a: str

    @field_validator('a')
    @classmethod
    defensure_foobar(cls, v: Any):
        if 'foobar' not in v:
            raise ValueError('"foobar" not found in a')
        return v

print(repr(Model(a='this is foobar good')))
#> Model(a='this is foobar good')

try:
    Model(a='snap')
except ValidationError as exc_info:
    print(exc_info)
'''
    1 validation error for Model
    a
      Value error, "foobar" not found in a [type=value_error, input_value='snap', input_type=str]
    '''

```

For more in depth examples, see [Field Validators](https://docs.pydantic.dev/latest/concepts/validators/#field-validators).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`field` |  |  The first field the `field_validator` should be called on; this is separate from `fields` to ensure an error is raised if you don't pass at least one. |  _required_  
`*fields` |  |  Additional field(s) the `field_validator` should be called on. |  `()`  
`mode` |  `FieldValidatorModes` |  Specifies whether to validate the fields before or after validation. |  `'after'`  
`check_fields` |  |  Whether to check that the fields actually exist on the model. |  `None`  
`json_schema_input_type` |  |  The input type of the function. This is only used to generate the appropriate JSON Schema (in validation mode) and can only specified when `mode` is either `'before'`, `'plain'` or `'wrap'`. |  `PydanticUndefined`  
Returns:
Type | Description  
---|---  
|  A decorator that can be used to decorate a function to be used as a field_validator.  
Raises:
Type | Description  
---|---  
`PydanticUserError[](https://docs.pydantic.dev/latest/api/errors/#pydantic.errors.PydanticUserError)` | 
  * If `@field_validator` is used bare (with no fields).
  * If the args passed to `@field_validator` as fields are not strings.
  * If `@field_validator` applied to instance methods.

  
Source code in `pydantic/functional_validators.py`
```
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
442
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
```
| ```
deffield_validator(
    field: str,
    /,
    *fields: str,
    mode: FieldValidatorModes = 'after',
    check_fields: bool | None = None,
    json_schema_input_type: Any = PydanticUndefined,
) -> Callable[[Any], Any]:
"""!!! abstract "Usage Documentation"
        [field validators](../concepts/validators.md#field-validators)

    Decorate methods on the class indicating that they should be used to validate fields.

    Example usage:
```python
    from typing import Any

    from pydantic import (
        BaseModel,
        ValidationError,
        field_validator,
    )

    class Model(BaseModel):
        a: str

        @field_validator('a')
        @classmethod
        def ensure_foobar(cls, v: Any):
            if 'foobar' not in v:
                raise ValueError('"foobar" not found in a')
            return v

    print(repr(Model(a='this is foobar good')))
    #> Model(a='this is foobar good')

    try:
        Model(a='snap')
    except ValidationError as exc_info:
        print(exc_info)
        '''
        1 validation error for Model
        a
          Value error, "foobar" not found in a [type=value_error, input_value='snap', input_type=str]
        '''
```

    For more in depth examples, see [Field Validators](../concepts/validators.md#field-validators).

    Args:
        field: The first field the `field_validator` should be called on; this is separate
            from `fields` to ensure an error is raised if you don't pass at least one.
        *fields: Additional field(s) the `field_validator` should be called on.
        mode: Specifies whether to validate the fields before or after validation.
        check_fields: Whether to check that the fields actually exist on the model.
        json_schema_input_type: The input type of the function. This is only used to generate
            the appropriate JSON Schema (in validation mode) and can only specified
            when `mode` is either `'before'`, `'plain'` or `'wrap'`.

    Returns:
        A decorator that can be used to decorate a function to be used as a field_validator.

    Raises:
        PydanticUserError:
            - If `@field_validator` is used bare (with no fields).
            - If the args passed to `@field_validator` as fields are not strings.
            - If `@field_validator` applied to instance methods.
    """
    if isinstance(field, FunctionType):
        raise PydanticUserError(
            '`@field_validator` should be used with fields and keyword arguments, not bare. '
            "E.g. usage should be `@validator('<field_name>', ...)`",
            code='validator-no-fields',
        )

    if mode not in ('before', 'plain', 'wrap') and json_schema_input_type is not PydanticUndefined:
        raise PydanticUserError(
            f"`json_schema_input_type` can't be used when mode is set to {mode!r}",
            code='validator-input-type',
        )

    if json_schema_input_type is PydanticUndefined and mode == 'plain':
        json_schema_input_type = Any

    fields = field, *fields
    if not all(isinstance(field, str) for field in fields):
        raise PydanticUserError(
            '`@field_validator` fields should be passed as separate string args. '
            "E.g. usage should be `@validator('<field_name_1>', '<field_name_2>', ...)`",
            code='validator-invalid-fields',
        )

    defdec(
        f: Callable[..., Any] | staticmethod[Any, Any] | classmethod[Any, Any, Any],
    ) -> _decorators.PydanticDescriptorProxy[Any]:
        if _decorators.is_instance_method_from_sig(f):
            raise PydanticUserError(
                '`@field_validator` cannot be applied to instance methods', code='validator-instance-method'
            )

        # auto apply the @classmethod decorator
        f = _decorators.ensure_classmethod_based_on_signature(f)

        dec_info = _decorators.FieldValidatorDecoratorInfo(
            fields=fields, mode=mode, check_fields=check_fields, json_schema_input_type=json_schema_input_type
        )
        return _decorators.PydanticDescriptorProxy(f, dec_info)

    return dec

```
  
---|---  
##  model_validator [¶](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.model_validator)
```
model_validator(*, mode: ["wrap"]) -> [
    [_AnyModelWrapValidator[_ModelType]],
    PydanticDescriptorProxy[ModelValidatorDecoratorInfo],
]

```

```
model_validator(*, mode: ["before"]) -> [
    [_AnyModelBeforeValidator],
    PydanticDescriptorProxy[ModelValidatorDecoratorInfo],
]

```

```
model_validator(*, mode: ["after"]) -> [
    [_AnyModelAfterValidator[_ModelType]],
    PydanticDescriptorProxy[ModelValidatorDecoratorInfo],
]

```

```
model_validator(
    *, mode: ["wrap", "before", "after"]
) -> 
```

Usage Documentation
[Model Validators](https://docs.pydantic.dev/latest/concepts/validators/#model-validators)
Decorate model methods for validation purposes.
Example usage: 
```
fromtyping_extensionsimport Self

frompydanticimport BaseModel, ValidationError, model_validator

classSquare(BaseModel):
    width: float
    height: float

    @model_validator(mode='after')
    defverify_square(self) -> Self:
        if self.width != self.height:
            raise ValueError('width and height do not match')
        return self

s = Square(width=1, height=1)
print(repr(s))
#> Square(width=1.0, height=1.0)

try:
    Square(width=1, height=2)
except ValidationError as e:
    print(e)
'''
    1 validation error for Square
      Value error, width and height do not match [type=value_error, input_value={'width': 1, 'height': 2}, input_type=dict]
    '''

```

For more in depth examples, see [Model Validators](https://docs.pydantic.dev/latest/concepts/validators/#model-validators).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`mode` |  |  A required string literal that specifies the validation mode. It can be one of the following: 'wrap', 'before', or 'after'. |  _required_  
Returns:
Type | Description  
---|---  
|  A decorator that can be used to decorate a function to be used as a model validator.  
Source code in `pydantic/functional_validators.py`
```
672
673
674
675
676
677
678
679
680
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
```
| ```
defmodel_validator(
    *,
    mode: Literal['wrap', 'before', 'after'],
) -> Any:
"""!!! abstract "Usage Documentation"
        [Model Validators](../concepts/validators.md#model-validators)

    Decorate model methods for validation purposes.

    Example usage:
```python
    from typing_extensions import Self

    from pydantic import BaseModel, ValidationError, model_validator

    class Square(BaseModel):
        width: float
        height: float

        @model_validator(mode='after')
        def verify_square(self) -> Self:
            if self.width != self.height:
                raise ValueError('width and height do not match')
            return self

    s = Square(width=1, height=1)
    print(repr(s))
    #> Square(width=1.0, height=1.0)

    try:
        Square(width=1, height=2)
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Square
          Value error, width and height do not match [type=value_error, input_value={'width': 1, 'height': 2}, input_type=dict]
        '''
```

    For more in depth examples, see [Model Validators](../concepts/validators.md#model-validators).

    Args:
        mode: A required string literal that specifies the validation mode.
            It can be one of the following: 'wrap', 'before', or 'after'.

    Returns:
        A decorator that can be used to decorate a function to be used as a model validator.
    """

    defdec(f: Any) -> _decorators.PydanticDescriptorProxy[Any]:
        # auto apply the @classmethod decorator. NOTE: in V3, do not apply the conversion for 'after' validators:
        f = _decorators.ensure_classmethod_based_on_signature(f)
        if mode == 'after' and isinstance(f, classmethod):
            warnings.warn(
                category=PydanticDeprecatedSince212,
                message=(
                    "Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. "
                    f'See the documentation at https://docs.pydantic.dev/{version_short()}/concepts/validators/#model-after-validator.'
                ),
                stacklevel=2,
            )

        dec_info = _decorators.ModelValidatorDecoratorInfo(mode=mode)
        return _decorators.PydanticDescriptorProxy(f, dec_info)

    return dec

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
