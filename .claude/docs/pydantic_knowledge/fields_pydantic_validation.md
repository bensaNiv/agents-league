---
# Smart Librarian Export (v2.0)
- Page Number: 38
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/fields
- Page Title: Fields - Pydantic Validation
- Semantic Filename: fields_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 28,051 characters
---

# Fields - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/fields/#the-annotated-pattern)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Fields
API Documentation
[`pydantic.fields.Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field)  

In this section, we will go through the available mechanisms to customize Pydantic model fields: [default values](https://docs.pydantic.dev/latest/concepts/fields/#default-values), [JSON Schema metadata](https://docs.pydantic.dev/latest/concepts/fields/#customizing-json-schema), [constraints](https://docs.pydantic.dev/latest/concepts/fields/#field-constraints), etc.
To do so, the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function is used a lot, and behaves the same way as the standard library 
```
frompydanticimport BaseModel, Field


classModel(BaseModel):
    name: str = Field(frozen=True)

```

Note
Even though `name` is assigned a value, it is still required and has no default value. If you want to emphasize on the fact that a value must be provided, you can use the 
```
classModel(BaseModel):
    name: str = Field(..., frozen=True)

```

However, its usage is discouraged as it doesn't play well with static type checkers.
## The annotated pattern[¶](https://docs.pydantic.dev/latest/concepts/fields/#the-annotated-pattern)
To apply constraints or attach [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) functions to a model field, Pydantic also supports the 
```
fromtypingimport Annotated

frompydanticimport BaseModel, Field, WithJsonSchema


classModel(BaseModel):
    name: Annotated[str, Field(strict=True), WithJsonSchema({'extra': 'data'})]

```

As far as static type checkers are concerned, `name` is still typed as `str`, but Pydantic leverages the available metadata to add validation logic, type constraints, etc.
Using this pattern has some advantages:
  * Using the `f: <type> = Field(...)` form can be confusing and might trick users into thinking `f` has a default value, while in reality it is still required.
  * You can provide an arbitrary amount of metadata elements for a field. As shown in the example above, the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function only supports a limited set of constraints/metadata, and you may have to use different Pydantic utilities such as [`WithJsonSchema`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.WithJsonSchema) in some cases.
  * Types can be made reusable (see the documentation on [custom types](https://docs.pydantic.dev/latest/concepts/types/#using-the-annotated-pattern) using this pattern).


However, note that certain arguments to the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function (namely, `default`, `default_factory`, and `alias`) are taken into account by static type checkers to synthesize a correct `__init__()` method. The annotated pattern is _not_ understood by them, so you should use the normal assignment form instead.
Tip
The annotated pattern can also be used to add metadata to specific parts of the type. For instance, [validation constraints](https://docs.pydantic.dev/latest/concepts/fields/#field-constraints) can be added this way:
```
fromtypingimport Annotated

frompydanticimport BaseModel, Field


classModel(BaseModel):
    int_list: list[Annotated[int, Field(gt=0)]]
    # Valid: [1, 3]
    # Invalid: [-1, 2]

```

Be careful not mixing _field_ and _type_ metadata:
```
classModel(BaseModel):
    field_bad: Annotated[int, Field(deprecated=True)] | None = None  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_4_annotation_1)
    field_ok: Annotated[int | None, Field(deprecated=True)] = None  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_4_annotation_2)

```

## Inspecting model fields[¶](https://docs.pydantic.dev/latest/concepts/fields/#inspecting-model-fields)
The fields of a model can be inspected using the [`model_fields`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields) class attribute (or the `__pydantic_fields__` attribute for [Pydantic dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/)). It is a mapping of field names to their definition (represented as [`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) instances).
```
fromtypingimport Annotated

frompydanticimport BaseModel, Field, WithJsonSchema


classModel(BaseModel):
    a: Annotated[
        int, Field(gt=1), WithJsonSchema({'extra': 'data'}), Field(alias='b')
    ] = 1


field_info = Model.model_fields['a']
print(field_info.annotation)
#> <class 'int'>
print(field_info.alias)
#> b
print(field_info.metadata)
#> [Gt(gt=1), WithJsonSchema(json_schema={'extra': 'data'}, mode=None)]

```

## Default values[¶](https://docs.pydantic.dev/latest/concepts/fields/#default-values)
Default values for fields can be provided using the normal assignment syntax or by providing a value to the `default` argument:
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    # Both fields aren't required:
    name: str = 'John Doe'
    age: int = Field(default=20)

```

Warning
[In Pydantic V1](https://docs.pydantic.dev/latest/migration/#required-optional-and-nullable-fields), a type annotated as `None` even if no default was explicitly specified. This is no longer the case in Pydantic V2.
You can also pass a callable to the `default_factory` argument that will be called to generate a default value:
```
fromuuidimport uuid4

frompydanticimport BaseModel, Field


classUser(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)

```

[](https://docs.pydantic.dev/latest/concepts/fields/)
The default factory can also take a single required argument, in which case the already validated data will be passed as a dictionary.
```
frompydanticimport BaseModel, EmailStr, Field


classUser(BaseModel):
    email: EmailStr
    username: str = Field(default_factory=lambda data: data['email'])


user = User(email='user@example.com')
print(user.username)
#> user@example.com

```

The `data` argument will _only_ contain the already validated data, based on the [order of model fields](https://docs.pydantic.dev/latest/concepts/models/#field-ordering) (the above example would fail if `username` were to be defined before `email`).
## Validate default values[¶](https://docs.pydantic.dev/latest/concepts/fields/#validate-default-values)
By default, Pydantic will _not_ validate default values. The `validate_default` field parameter (or the [`validate_default`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.validate_default) configuration value) can be used to enable this behavior:
```
frompydanticimport BaseModel, Field, ValidationError


classUser(BaseModel):
    age: int = Field(default='twelve', validate_default=True)


try:
    user = User()
except ValidationError as e:
    print(e)
"""
    1 validation error for User
    age
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twelve', input_type=str]
    """

```

### Mutable default values[¶](https://docs.pydantic.dev/latest/concepts/fields/#mutable-default-values)
A common source of bugs in Python is to use a mutable object as a default value for a function or method argument, as the same instance ends up being reused in each call.
The 
While the same thing can be done in Pydantic, it is not required. In the event that the default value is not hashable, Pydantic will create a deep copy of the default value when creating each instance of the model:
```
frompydanticimport BaseModel


classModel(BaseModel):
    item_counts: list[dict[str, int]] = [{}]


m1 = Model()
m1.item_counts[0]['a'] = 1
print(m1.item_counts)
#> [{'a': 1}]

m2 = Model()
print(m2.item_counts)
#> [{}]

```

## Field aliases[¶](https://docs.pydantic.dev/latest/concepts/fields/#field-aliases)
Tip
Read more about aliases in the [dedicated section](https://docs.pydantic.dev/latest/concepts/alias/).
For validation and serialization, you can define an alias for a field.
There are three ways to define an alias:
  * `Field(alias='foo')`
  * `Field(validation_alias='foo')`
  * `Field(serialization_alias='foo')`


The `alias` parameter is used for both validation _and_ serialization. If you want to use _different_ aliases for validation and serialization respectively, you can use the `validation_alias` and `serialization_alias` parameters, which will apply only in their respective use cases.
Here is an example of using the `alias` parameter:
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str = Field(alias='username')


user = User(username='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_11_annotation_1)
print(user)
#> name='johndoe'
print(user.model_dump(by_alias=True))  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_11_annotation_2)
#> {'username': 'johndoe'}

```

If you want to use an alias _only_ for validation, you can use the `validation_alias` parameter:
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str = Field(validation_alias='username')


user = User(username='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_12_annotation_1)
print(user)
#> name='johndoe'
print(user.model_dump(by_alias=True))  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_12_annotation_2)
#> {'name': 'johndoe'}

```

If you only want to define an alias for _serialization_ , you can use the `serialization_alias` parameter:
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str = Field(serialization_alias='username')


user = User(name='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_13_annotation_1)
print(user)
#> name='johndoe'
print(user.model_dump(by_alias=True))  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_13_annotation_2)
#> {'username': 'johndoe'}

```

Alias precedence and priority
In case you use `alias` together with `validation_alias` or `serialization_alias` at the same time, the `validation_alias` will have priority over `alias` for validation, and `serialization_alias` will have priority over `alias` for serialization.
If you provide a value for the [`alias_generator`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.alias_generator) model setting, you can control the order of precedence for field alias and generated aliases via the `alias_priority` field parameter. You can read more about alias precedence [here](https://docs.pydantic.dev/latest/concepts/alias/#alias-precedence).
Static type checking/IDE support
If you provide a value for the `alias` field parameter, static type checkers will use this alias instead of the actual field name to synthesize the `__init__` method:
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str = Field(alias='username')


user = User(username='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_14_annotation_1)

```

This means that when using the [`validate_by_name`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.validate_by_name) model setting (which allows both the field name and alias to be used during model validation), type checkers will error when the actual field name is used:
```
frompydanticimport BaseModel, ConfigDict, Field


classUser(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    name: str = Field(alias='username')


user = User(name='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_15_annotation_1)

```

If you still want type checkers to use the field name and not the alias, the [annotated pattern](https://docs.pydantic.dev/latest/concepts/fields/#the-annotated-pattern) can be used (which is only understood by Pydantic):
```
fromtypingimport Annotated

frompydanticimport BaseModel, ConfigDict, Field


classUser(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    name: Annotated[str, Field(alias='username')]


user = User(name='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_16_annotation_1)
user = User(username='johndoe')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_16_annotation_2)

```

### Validation Alias
Even though Pydantic treats `alias` and `validation_alias` the same when creating model instances, type checkers only understand the `alias` field parameter. As a workaround, you can instead specify both an `alias` and `serialization_alias` (identical to the field name), as the `serialization_alias` will override the `alias` during serialization:
```
frompydanticimport BaseModel, Field


classMyModel(BaseModel):
    my_field: int = Field(validation_alias='myValidationAlias')

```

with:
```
frompydanticimport BaseModel, Field


classMyModel(BaseModel):
    my_field: int = Field(
        alias='myValidationAlias',
        serialization_alias='my_field',
    )


m = MyModel(myValidationAlias=1)
print(m.model_dump(by_alias=True))
#> {'my_field': 1}

```

[](https://docs.pydantic.dev/latest/concepts/fields/)
[](https://docs.pydantic.dev/latest/concepts/fields/)
[](https://docs.pydantic.dev/latest/concepts/fields/)
## Field constraints[¶](https://docs.pydantic.dev/latest/concepts/fields/#field-constraints)
The [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function can also be used to add constraints to specific types:
```
fromdecimalimport Decimal

frompydanticimport BaseModel, Field


classModel(BaseModel):
    positive: int = Field(gt=0)
    short_str: str = Field(max_length=3)
    precise_decimal: Decimal = Field(max_digits=5, decimal_places=2)

```

The available constraints for each type (and the way they affect the JSON Schema) are described in the [standard library types](https://docs.pydantic.dev/latest/api/standard_library_types/) documentation.
[](https://docs.pydantic.dev/latest/concepts/fields/)
## Strict fields[¶](https://docs.pydantic.dev/latest/concepts/fields/#strict-fields)
The `strict` parameter of the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function specifies whether the field should be validated in [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/).
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str = Field(strict=True)
    age: int = Field(strict=False)  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_20_annotation_1)


user = User(name='John', age='42')  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_20_annotation_2)
print(user)
#> name='John' age=42

```

The [standard library types](https://docs.pydantic.dev/latest/api/standard_library_types/) documentation describes the strict behavior for each type.
[](https://docs.pydantic.dev/latest/concepts/fields/)
## Dataclass fields[¶](https://docs.pydantic.dev/latest/concepts/fields/#dataclass-fields)
Some parameters of the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function can be used on [dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/):
  * `init`: Whether the field should be included in the synthesized `__init__()` method of the dataclass.
  * `init_var`: Whether the field should be 
  * `kw_only`: Whether the field should be a keyword-only argument in the constructor of the dataclass.


Here is an example:
```
frompydanticimport BaseModel, Field
frompydantic.dataclassesimport dataclass


@dataclass
classFoo:
    bar: str
    baz: str = Field(init_var=True)
    qux: str = Field(kw_only=True)


classModel(BaseModel):
    foo: Foo


model = Model(foo=Foo('bar', baz='baz', qux='qux'))
print(model.model_dump())  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_21_annotation_1)
#> {'foo': {'bar': 'bar', 'qux': 'qux'}}

```

## Field Representation[¶](https://docs.pydantic.dev/latest/concepts/fields/#field-representation)
The parameter `repr` can be used to control whether the field should be included in the string representation of the model.
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str = Field(repr=True)  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_22_annotation_1)
    age: int = Field(repr=False)


user = User(name='John', age=42)
print(user)
#> name='John'

```

## Discriminator[¶](https://docs.pydantic.dev/latest/concepts/fields/#discriminator)
The parameter `discriminator` can be used to control the field that will be used to discriminate between different models in a union. It takes either the name of a field or a `Discriminator` instance. The `Discriminator` approach can be useful when the discriminator fields aren't the same for all the models in the `Union`.
The following example shows how to use `discriminator` with a field name:
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/fields/#__tabbed_1_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/fields/#__tabbed_1_2)
```
fromtypingimport Literal, Union

frompydanticimport BaseModel, Field


classCat(BaseModel):
    pet_type: Literal['cat']
    age: int


classDog(BaseModel):
    pet_type: Literal['dog']
    age: int


classModel(BaseModel):
    pet: Union[Cat, Dog] = Field(discriminator='pet_type')


print(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}}))  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_23_annotation_1)
#> pet=Cat(pet_type='cat', age=12)

```

```
fromtypingimport Literal

frompydanticimport BaseModel, Field


classCat(BaseModel):
    pet_type: Literal['cat']
    age: int


classDog(BaseModel):
    pet_type: Literal['dog']
    age: int


classModel(BaseModel):
    pet: Cat | Dog = Field(discriminator='pet_type')


print(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}}))  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_24_annotation_1)
#> pet=Cat(pet_type='cat', age=12)

```

  1. See more about [Validating data](https://docs.pydantic.dev/latest/concepts/models/#validating-data) in the [Models](https://docs.pydantic.dev/latest/concepts/models/) page.


The following example shows how to use the `discriminator` keyword argument with a `Discriminator` instance:
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/fields/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/fields/#__tabbed_2_2)
```
fromtypingimport Annotated, Literal, Union

frompydanticimport BaseModel, Discriminator, Field, Tag


classCat(BaseModel):
    pet_type: Literal['cat']
    age: int


classDog(BaseModel):
    pet_kind: Literal['dog']
    age: int


defpet_discriminator(v):
    if isinstance(v, dict):
        return v.get('pet_type', v.get('pet_kind'))
    return getattr(v, 'pet_type', getattr(v, 'pet_kind', None))


classModel(BaseModel):
    pet: Union[Annotated[Cat, Tag('cat')], Annotated[Dog, Tag('dog')]] = Field(
        discriminator=Discriminator(pet_discriminator)
    )


print(repr(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}})))
#> Model(pet=Cat(pet_type='cat', age=12))

print(repr(Model.model_validate({'pet': {'pet_kind': 'dog', 'age': 12}})))
#> Model(pet=Dog(pet_kind='dog', age=12))

```

```
fromtypingimport Annotated, Literal

frompydanticimport BaseModel, Discriminator, Field, Tag


classCat(BaseModel):
    pet_type: Literal['cat']
    age: int


classDog(BaseModel):
    pet_kind: Literal['dog']
    age: int


defpet_discriminator(v):
    if isinstance(v, dict):
        return v.get('pet_type', v.get('pet_kind'))
    return getattr(v, 'pet_type', getattr(v, 'pet_kind', None))


classModel(BaseModel):
    pet: Annotated[Cat, Tag('cat')] | Annotated[Dog, Tag('dog')] = Field(
        discriminator=Discriminator(pet_discriminator)
    )


print(repr(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}})))
#> Model(pet=Cat(pet_type='cat', age=12))

print(repr(Model.model_validate({'pet': {'pet_kind': 'dog', 'age': 12}})))
#> Model(pet=Dog(pet_kind='dog', age=12))

```

You can also take advantage of `Annotated` to define your discriminated unions. See the [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) docs for more details.
## Immutability[¶](https://docs.pydantic.dev/latest/concepts/fields/#immutability)
The parameter `frozen` is used to emulate the frozen dataclass behaviour. It is used to prevent the field from being assigned a new value after the model is created (immutability).
See the 
```
frompydanticimport BaseModel, Field, ValidationError


classUser(BaseModel):
    name: str = Field(frozen=True)
    age: int


user = User(name='John', age=42)

try:
    user.name = 'Jane'  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_27_annotation_1)
except ValidationError as e:
    print(e)
"""
    1 validation error for User
    name
      Field is frozen [type=frozen_field, input_value='Jane', input_type=str]
    """

```

[](https://docs.pydantic.dev/latest/concepts/fields/)
## Excluding fields[¶](https://docs.pydantic.dev/latest/concepts/fields/#excluding-fields)
The `exclude` and `exclude_if` parameters can be used to control which fields should be excluded from the model when exporting the model.
See the following example:
```
frompydanticimport BaseModel, Field


classUser(BaseModel):
    name: str
    age: int = Field(exclude=True)


user = User(name='John', age=42)
print(user.model_dump())  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_28_annotation_1)
#> {'name': 'John'}

```

See the dedicated [serialization section](https://docs.pydantic.dev/latest/concepts/serialization/#field-inclusion-and-exclusion) for more details.
## Deprecated fields[¶](https://docs.pydantic.dev/latest/concepts/fields/#deprecated-fields)
The `deprecated` parameter can be used to mark a field as being deprecated. Doing so will result in:
  * a runtime deprecation warning emitted when accessing the field.
  * The 


This parameter accepts different types, described below.
###  `deprecated` as a string[¶](https://docs.pydantic.dev/latest/concepts/fields/#deprecated-as-a-string)
The value will be used as the deprecation message.
```
fromtypingimport Annotated

frompydanticimport BaseModel, Field


classModel(BaseModel):
    deprecated_field: Annotated[int, Field(deprecated='This is deprecated')]


print(Model.model_json_schema()['properties']['deprecated_field'])
#> {'deprecated': True, 'title': 'Deprecated Field', 'type': 'integer'}

```

###  `deprecated` via the `@warnings.deprecated` decorator[¶](https://docs.pydantic.dev/latest/concepts/fields/#deprecated-via-the-warningsdeprecated-decorator)
The 
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/fields/#__tabbed_3_1)[Python 3.13 and above](https://docs.pydantic.dev/latest/concepts/fields/#__tabbed_3_2)
```
fromtypingimport Annotated

fromtyping_extensionsimport deprecated

frompydanticimport BaseModel, Field


classModel(BaseModel):
    deprecated_field: Annotated[int, deprecated('This is deprecated')]

    # Or explicitly using `Field`:
    alt_form: Annotated[int, Field(deprecated=deprecated('This is deprecated'))]

```

```
fromtypingimport Annotated
fromwarningsimport deprecated

frompydanticimport BaseModel, Field


classModel(BaseModel):
    deprecated_field: Annotated[int, deprecated('This is deprecated')]

    # Or explicitly using `Field`:
    alt_form: Annotated[int, Field(deprecated=deprecated('This is deprecated'))]

```

Support for `category` and `stacklevel`
The current implementation of this feature does not take into account the `category` and `stacklevel` arguments to the `deprecated` decorator. This might land in a future version of Pydantic.
###  `deprecated` as a boolean[¶](https://docs.pydantic.dev/latest/concepts/fields/#deprecated-as-a-boolean)
```
fromtypingimport Annotated

frompydanticimport BaseModel, Field


classModel(BaseModel):
    deprecated_field: Annotated[int, Field(deprecated=True)]


print(Model.model_json_schema()['properties']['deprecated_field'])
#> {'deprecated': True, 'title': 'Deprecated Field', 'type': 'integer'}

```

Accessing a deprecated field in validators
When accessing a deprecated field inside a validator, the deprecation warning will be emitted. You can use 
```
importwarnings

fromtyping_extensionsimport Self

frompydanticimport BaseModel, Field, model_validator


classModel(BaseModel):
    deprecated_field: int = Field(deprecated='This is deprecated')

    @model_validator(mode='after')
    defvalidate_model(self) -> Self:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            self.deprecated_field = self.deprecated_field * 2

```

## Customizing JSON Schema[¶](https://docs.pydantic.dev/latest/concepts/fields/#customizing-json-schema)
Some field parameters are used exclusively to customize the generated JSON schema. The parameters in question are:
  * `title`
  * `description`
  * `examples`
  * `json_schema_extra`


Read more about JSON schema customization / modification with fields in the [Customizing JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/#field-level-customization) section of the JSON schema docs.
## The `computed_field` decorator[¶](https://docs.pydantic.dev/latest/concepts/fields/#the-computed_field-decorator)
API Documentation
[`computed_field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.computed_field)  

The [`computed_field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.computed_field) decorator can be used to include 
Note
Properties can be useful for fields that are computed from other fields, or for fields that are expensive to be computed (and thus, are cached if using 
However, note that Pydantic will _not_ perform any additional logic on the wrapped property (validation, cache invalidation, etc.).
Here's an example of the JSON schema (in serialization mode) generated for a model with a computed field:
```
frompydanticimport BaseModel, computed_field


classBox(BaseModel):
    width: float
    height: float
    depth: float

    @computed_field
    @property  [](https://docs.pydantic.dev/latest/concepts/fields/#__code_34_annotation_1)
    defvolume(self) -> float:
        return self.width * self.height * self.depth


print(Box.model_json_schema(mode='serialization'))
"""
{
    'properties': {
        'width': {'title': 'Width', 'type': 'number'},
        'height': {'title': 'Height', 'type': 'number'},
        'depth': {'title': 'Depth', 'type': 'number'},
        'volume': {'readOnly': True, 'title': 'Volume', 'type': 'number'},
    },
    'required': ['width', 'height', 'depth', 'volume'],
    'title': 'Box',
    'type': 'object',
}
"""

```

Here's an example using the `model_dump` method with a computed field:
```
frompydanticimport BaseModel, computed_field


classBox(BaseModel):
    width: float
    height: float
    depth: float

    @computed_field
    @property
    defvolume(self) -> float:
        return self.width * self.height * self.depth


b = Box(width=1, height=2, depth=3)
print(b.model_dump())
#> {'width': 1.0, 'height': 2.0, 'depth': 3.0, 'volume': 6.0}

```

As with regular fields, computed fields can be marked as being deprecated:
```
fromtyping_extensionsimport deprecated

frompydanticimport BaseModel, computed_field


classBox(BaseModel):
    width: float
    height: float
    depth: float

    @computed_field
    @property
    @deprecated("'volume' is deprecated")
    defvolume(self) -> float:
        return self.width * self.height * self.depth

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
