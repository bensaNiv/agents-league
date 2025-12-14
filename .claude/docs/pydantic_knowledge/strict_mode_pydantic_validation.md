---
# Smart Librarian Export (v2.0)
- Page Number: 14
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/strict_mode
- Page Title: Strict Mode - Pydantic Validation
- Semantic Filename: strict_mode_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 7,359 characters
---

# Strict Mode - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/strict_mode/#as-a-validation-parameter)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Strict Mode
API Documentation
[`pydantic.types.Strict`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)  

By default, Pydantic will attempt to coerce values to the desired type when possible. For example, you can pass the string `'123'` as the input for the [`int` number type](https://docs.pydantic.dev/latest/api/standard_library_types/#integers), and it will be converted to the value `123`. This coercion behavior is useful in many scenarios — think: UUIDs, URL parameters, HTTP headers, environment variables, dates, etc.
However, there are also situations where this is not desirable, and you want Pydantic to error instead of coercing data.
To better support this use case, Pydantic provides a "strict mode". When strict mode is enabled, Pydantic will be much less lenient when coercing data, and will instead error if the data is not of the correct type.
Most of the time, strict mode will only allow instances of the type to be provided, although looser rules may apply to JSON input (for instance, the [date and time types](https://docs.pydantic.dev/latest/api/standard_library_types/#date-and-time-types) allow strings even in strict mode).
The strict behavior for each type can be found in the [standard library types](https://docs.pydantic.dev/latest/api/standard_library_types/) documentation, and is summarized in the [conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/).
Here is a brief example showing the validation behavior difference in strict and the default lax mode:
```
frompydanticimport BaseModel, ValidationError


classMyModel(BaseModel):
    x: int


print(MyModel.model_validate({'x': '123'}))  # lax mode
#> x=123

try:
    MyModel.model_validate({'x': '123'}, strict=True)  # strict mode
except ValidationError as exc:
    print(exc)
"""
    1 validation error for MyModel
    x
      Input should be a valid integer [type=int_type, input_value='123', input_type=str]
    """

```

Strict mode can be enabled in various ways:
  * [As a validation parameter](https://docs.pydantic.dev/latest/concepts/strict_mode/#as-a-validation-parameter), such as when using [`model_validate()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate), on Pydantic models.
  * [At the field level](https://docs.pydantic.dev/latest/concepts/strict_mode/#at-the-field-level).
  * [At the configuration level](https://docs.pydantic.dev/latest/concepts/strict_mode/#as-a-configuration-value) (with the possibility to override at the field level).


[](https://docs.pydantic.dev/latest/concepts/strict_mode/)
## As a validation parameter[¶](https://docs.pydantic.dev/latest/concepts/strict_mode/#as-a-validation-parameter)
Strict mode can be enaled on a per-validation-call basis, when using the [validation methods](https://docs.pydantic.dev/latest/concepts/models/#validating-data) on [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) and [type adapters](https://docs.pydantic.dev/latest/concepts/type_adapter/).
```
fromdatetimeimport date

frompydanticimport TypeAdapter, ValidationError

print(TypeAdapter(date).validate_python('2000-01-01'))  # OK: lax
#> 2000-01-01

try:
    # Not OK: strict:
    TypeAdapter(date).validate_python('2000-01-01', strict=True)
except ValidationError as exc:
    print(exc)
"""
    1 validation error for date
      Input should be a valid date [type=date_type, input_value='2000-01-01', input_type=str]
    """

TypeAdapter(date).validate_json('"2000-01-01"', strict=True)  [](https://docs.pydantic.dev/latest/concepts/strict_mode/#__code_1_annotation_1)
#> 2000-01-01

```

[](https://docs.pydantic.dev/latest/concepts/strict_mode/)
## At the field level[¶](https://docs.pydantic.dev/latest/concepts/strict_mode/#at-the-field-level)
Strict mode can be enabled on specific fields, by setting the `strict` parameter of the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function to `True`. Strict mode will be applied for such fields, even when the [validation methods](https://docs.pydantic.dev/latest/concepts/models/#validating-data) are called in lax mode.
```
frompydanticimport BaseModel, Field, ValidationError


classUser(BaseModel):
    name: str
    age: int = Field(strict=True)  [](https://docs.pydantic.dev/latest/concepts/strict_mode/#__code_2_annotation_1)


user = User(name='John', age=42)
print(user)
#> name='John' age=42


try:
    another_user = User(name='John', age='42')
except ValidationError as e:
    print(e)
"""
    1 validation error for User
    age
      Input should be a valid integer [type=int_type, input_value='42', input_type=str]
    """

```

[](https://docs.pydantic.dev/latest/concepts/strict_mode/)
### Using the `Strict()` metadata class[¶](https://docs.pydantic.dev/latest/concepts/strict_mode/#using-the-strict-metadata-class)
API Documentation
[`pydantic.types.Strict`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)  

As an alternative to the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function, Pydantic provides the [`Strict`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict) metadata class, meant to be used with the [annotated pattern](https://docs.pydantic.dev/latest/concepts/fields/#the-annotated-pattern). It also provides convenience aliases for the most common types (namely [`StrictBool`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBool), [`StrictInt`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictInt), [`StrictFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictFloat), [`StrictStr`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictStr) and [`StrictBytes`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBytes)).
```
fromtypingimport Annotated
fromuuidimport UUID

frompydanticimport BaseModel, Strict, StrictInt


classUser(BaseModel):
    id: Annotated[UUID, Strict()]
    age: StrictInt  [](https://docs.pydantic.dev/latest/concepts/strict_mode/#__code_3_annotation_1)

```

[](https://docs.pydantic.dev/latest/concepts/strict_mode/)
## As a configuration value[¶](https://docs.pydantic.dev/latest/concepts/strict_mode/#as-a-configuration-value)
Strict mode behavior can be controlled at the [configuration](https://docs.pydantic.dev/latest/concepts/config/) level. When used on a Pydantic model (or model like class such as [dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/)), strictness can still be overridden at the [field level](https://docs.pydantic.dev/latest/concepts/strict_mode/#at-the-field-level):
```
frompydanticimport BaseModel, ConfigDict, Field


classUser(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str
    age: int = Field(strict=False)


print(User(name='John', age='18'))
#> name='John' age=18

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
