---
# Smart Librarian Export (v2.0)
- Page Number: 56
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/examples/dynamic_models
- Page Title: Dynamic models - Pydantic Validation
- Semantic Filename: dynamic_models_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 8,539 characters
---

# Dynamic models - Pydantic Validation

What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Dynamic models
Models can be [created dynamically](https://docs.pydantic.dev/latest/concepts/models/#dynamic-model-creation) using the [`create_model()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.create_model) factory function.
In this example, we will show how to dynamically derive a model from an existing one, making every field optional. To achieve this, we will make use of the [`model_fields`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields) model class attribute, and derive new annotations from the field definitions to be passed to the [`create_model()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.create_model) factory. Of course, this example can apply to any use case where you need to derive a new model from another (remove default values, add aliases, etc).
[Python 3.9](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_1_1)[Python 3.10](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_1_2)[Python 3.11 and above](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_1_3)
```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
```
| ```
fromtypingimport Annotated, Union

frompydanticimport BaseModel, Field, create_model


defmake_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
    new_fields = {}

    for f_name, f_info in model_cls.model_fields.items():
        f_dct = f_info.asdict()
        new_fields[f_name] = (
            Annotated[(Union[f_dct['annotation'], None], *f_dct['metadata'], Field(**f_dct['attributes']))],
            None,
        )

    return create_model(
        f'{type.__name__}Optional',
        __base__=model_cls,  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_0_annotation_1)
        **new_fields,
    )

```
  
---|---  
```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
```
| ```
fromtypingimport Annotated

frompydanticimport BaseModel, Field, create_model


defmake_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
    new_fields = {}

    for f_name, f_info in model_cls.model_fields.items():
        f_dct = f_info.asdict()
        new_fields[f_name] = (
            Annotated[(f_dct['annotation'] | None, *f_dct['metadata'], Field(**f_dct['attributes']))],
            None,
        )

    return create_model(
        f'{type.__name__}Optional',
        __base__=model_cls,  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_1_annotation_1)
        **new_fields,
    )

```
  
---|---  
  1. Using the original model as a base will inherit the [validators](https://docs.pydantic.dev/latest/concepts/validators/), [computed fields](https://docs.pydantic.dev/latest/concepts/fields/#the-computed_field-decorator), etc. The parent fields are overridden by the ones we define.


```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
```
| ```
fromtypingimport Annotated

frompydanticimport BaseModel, Field, create_model


defmake_fields_optional(model_cls: type[BaseModel]) -> type[BaseModel]:
    new_fields = {}

    for f_name, f_info in model_cls.model_fields.items():
        f_dct = f_info.asdict()
        new_fields[f_name] = (
            Annotated[f_dct['annotation'] | None, *f_dct['metadata'], Field(**f_dct['attributes'])],
            None,
        )

    return create_model(
        f'{type.__name__}Optional',
        __base__=model_cls,  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_2_annotation_1)
        **new_fields,
    )

```
  
---|---  
  1. Using the original model as a base will inherit the [validators](https://docs.pydantic.dev/latest/concepts/validators/), [computed fields](https://docs.pydantic.dev/latest/concepts/fields/#the-computed_field-decorator), etc. The parent fields are overridden by the ones we define.


For each field, we generate a dictionary representation of the [`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) instance using the [`asdict()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo.asdict) method, containing the annotation, metadata and attributes.
With the following model:
```
classModel(BaseModel):
    f: Annotated[int, Field(gt=1), WithJsonSchema({'extra': 'data'}), Field(title='F')] = 1

```

The [`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) instance of `f` will have three items in its dictionary representation:
  * `annotation`: `int`.
  * `metadata`: A list containing the type-specific constraints and other metadata: `[Gt(1), WithJsonSchema({'extra': 'data'})]`.
  * `attributes`: The remaining field-specific attributes: `{'title': 'F'}`.


With that in mind, we can recreate an annotation that "simulates" the one from the original model:
[Python 3.9 and above](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_2_1)[Python 3.11 and above](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_2_2)
```
new_annotation = Annotated[(
    f_dct['annotation'] | None,  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_4_annotation_1)
    *f_dct['metadata'],  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_4_annotation_2)
    Field(**f_dct['attributes']),  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_4_annotation_3)
)]

```

```
new_annotation = Annotated[
    f_dct['annotation'] | None,  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_5_annotation_1)
    *f_dct['metadata'],  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_5_annotation_2)
    Field(**f_dct['attributes']),  [](https://docs.pydantic.dev/latest/examples/dynamic_models/#__code_5_annotation_3)
]

```

  1. We create a new annotation from the existing one, but adding `None` as an allowed value (in our previous example, this is equivalent to `int | None`).
  2. We unpack the metadata to be reused (in our previous example, this is equivalent to specifying `Field(gt=1)` and `WithJsonSchema({'extra': 'data'})` as 
  3. We specify the field-specific attributes by using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function (in our previous example, this is equivalent to `Field(title='F')`).


and specify `None` as a default value (the second element of the tuple for the field definition accepted by [`create_model()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.create_model)).
Here is a demonstration of our factory function:
```
frompydanticimport BaseModel, Field


classModel(BaseModel):
    a: Annotated[int, Field(gt=1)]


ModelOptional = make_fields_optional(Model)

m = ModelOptional()
print(m.a)
#> None

```

A couple notes on the implementation:
  * Our `make_fields_optional()` function is defined as returning an arbitrary Pydantic model class (`-> type[BaseModel]`). An alternative solution can be to use a type variable to preserve the input class:
[Python 3.9 and above](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_3_1)[Python 3.12 and above](https://docs.pydantic.dev/latest/examples/dynamic_models/#__tabbed_3_2)
```
ModelTypeT = TypeVar('ModelTypeT', bound=type[BaseModel])

defmake_fields_optional(model_cls: ModelTypeT) -> ModelTypeT:
    ...

```

```
defmake_fields_optional[ModelTypeT: type[BaseModel]](model_cls: ModelTypeT) -> ModelTypeT:
    ...

```

However, note that static type checkers _won't_ be able to understand that all fields are now optional.
  * The experimental [`MISSING` sentinel](https://docs.pydantic.dev/latest/concepts/experimental/#missing-sentinel) can be used as an alternative to `None` for the default values. Simply replace `None` by `MISSING` in the new annotation and default value.
  * You might be tempted to make a copy of the original [`FieldInfo`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) instances, add a default and/or perform other mutations, to then reuse it as **not** a supported pattern, and could break or be deprecated at any point. We strongly encourage using the pattern from this example instead.

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
