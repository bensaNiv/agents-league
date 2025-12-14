---
# Smart Librarian Export (v2.0)
- Page Number: 53
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/internals/architecture
- Page Title: Architecture - Pydantic Validation
- Semantic Filename: architecture_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 9,580 characters
---

# Architecture - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/internals/architecture/#model-definition)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Architecture
Note
This section is part of the _internals_ documentation, and is partly targeted to contributors.
Starting with Pydantic V2, part of the codebase is written in Rust in a separate package called `pydantic-core`. This was done partly in order to improve validation and serialization performance (with the cost of limited customization and extendibility of the internal logic).
This architecture documentation will first cover how the two `pydantic` and `pydantic-core` packages interact together, then will go through the architecture specifics for various patterns (model definition, validation, serialization, JSON Schema).
Usage of the Pydantic library can be divided into two parts:
  * Model definition, done in the `pydantic` package.
  * Model validation and serialization, done in the `pydantic-core` package.


## Model definition[¶](https://docs.pydantic.dev/latest/internals/architecture/#model-definition)
Whenever a Pydantic [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) is defined, the metaclass will analyze the body of the model to collect a number of elements:
  * Defined annotations to build model fields (collected in the [`model_fields`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields) attribute).
  * Model configuration, set with [`model_config`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_config).
  * Additional validators/serializers.
  * Private attributes, class variables, identification of generic parametrization, etc.


### Communicating between `pydantic` and `pydantic-core`: the core schema[¶](https://docs.pydantic.dev/latest/internals/architecture/#communicating-between-pydantic-and-pydantic-core-the-core-schema)
We then need a way to communicate the collected information from the model definition to `pydantic-core`, so that validation and serialization is performed accordingly. To do so, Pydantic uses the concept of a core schema: a structured (and serializable) Python dictionary (represented using `pydantic` and `pydantic-core` packages. Every core schema has a required `type` key, and extra properties depending on this `type`.
The generation of a core schema is handled in a single place, by the `GenerateSchema` class (no matter if it is for a Pydantic model or anything else).
Note
It is not possible to define a custom core schema. A core schema needs to be understood by the `pydantic-core` package, and as such we only support a fixed number of core schema types. This is also part of the reason why the `GenerateSchema` isn't truly exposed and properly documented.
The core schema definitions can be found in the [`pydantic_core.core_schema`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema) module.
In the case of a Pydantic model, a core schema will be constructed and set as the [`__pydantic_core_schema__`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.__pydantic_core_schema__) attribute.
To illustrate what a core schema looks like, we will take the example of the [`bool`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.bool_schema) core schema:
```
classBoolSchema(TypedDict, total=False):
    type: Required[Literal['bool']]
    strict: bool
    ref: str
    metadata: Any
    serialization: SerSchema

```

When defining a Pydantic model with a boolean field:
```
frompydanticimport BaseModel, Field


classModel(BaseModel):
    foo: bool = Field(strict=True)

```

The core schema for the `foo` field will look like:
```
{
    'type': 'bool',
    'strict': True,
}

```

As seen in the [`BoolSchema`](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.bool_schema) definition, the serialization logic is also defined in the core schema. If we were to define a custom serialization function for `foo` `serialization` key would look like:
```
{
    'type': 'function-plain',
    'function': <function Model.serialize_foo at 0x111>,
    'is_field_serializer': True,
    'info_arg': False,
    'return_schema': {'type': 'int'},
}

```

Note that this is also a core schema definition, just that it is only relevant for `pydantic-core` during serialization.
Core schemas cover a broad scope, and are used whenever we want to communicate between the Python and Rust side. While the previous examples were related to validation and serialization, it could in theory be used for anything: error management, extra metadata, etc.
### JSON Schema generation[¶](https://docs.pydantic.dev/latest/internals/architecture/#json-schema-generation)
You may have noticed that the previous serialization core schema has a `return_schema` key. This is because the core schema is also used to generate the corresponding JSON Schema.
Similar to how the core schema is generated, the JSON Schema generation is handled by the [`GenerateJsonSchema`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema) class. The [`generate`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate) method is the main entry point and is given the core schema of that model.
Coming back to our `bool` field example, the [`bool_schema`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.bool_schema) method will be given the previously generated [boolean core schema](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.bool_schema) and will return the following JSON Schema:
```
{
{"type":"boolean"}
}

```

### Customizing the core schema and JSON schema[¶](https://docs.pydantic.dev/latest/internals/architecture/#customizing-the-core-schema-and-json-schema)
Usage Documentation
[Custom types](https://docs.pydantic.dev/latest/concepts/types/#custom-types)
[Implementing `__get_pydantic_core_schema__`](https://docs.pydantic.dev/latest/concepts/json_schema/#implementing-__get_pydantic_core_schema__)
[Implementing `__get_pydantic_json_schema__`](https://docs.pydantic.dev/latest/concepts/json_schema/#implementing-__get_pydantic_json_schema__)
While the `GenerateSchema` and [`GenerateJsonSchema`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema) classes handle the creation of the corresponding schemas, Pydantic offers a way to customize them in some cases, following a wrapper pattern. This customization is done through the `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__` methods.
To understand this wrapper pattern, we will take the example of metadata classes used with `__get_pydantic_core_schema__` method can be used:
```
fromtypingimport Annotated, Any

frompydantic_coreimport CoreSchema

frompydanticimport GetCoreSchemaHandler, TypeAdapter


classMyStrict:
    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        schema = handler(source)  [](https://docs.pydantic.dev/latest/internals/architecture/#__code_6_annotation_1)
        schema['strict'] = True
        return schema


classMyGt:
    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        schema = handler(source)  [](https://docs.pydantic.dev/latest/internals/architecture/#__code_6_annotation_2)
        schema['gt'] = 1
        return schema


ta = TypeAdapter(Annotated[int, MyStrict(), MyGt()])

```

When the `GenerateSchema` class builds the core schema for `Annotated[int, MyStrict(), MyGt()]`, it will create an instance of a `GetCoreSchemaHandler` to be passed to the `MyGt.__get_pydantic_core_schema__` method. 
The `source` argument depends on the core schema generation pattern. In the case of `source` will be the type being annotated. When [defining a custom type](https://docs.pydantic.dev/latest/concepts/types/#as-a-method-on-a-custom-type), the `source` will be the actual class where `__get_pydantic_core_schema__` is defined.
## Model validation and serialization[¶](https://docs.pydantic.dev/latest/internals/architecture/#model-validation-and-serialization)
While model definition was scoped to the _class_ level (i.e. when defining your model), model validation and serialization happens at the _instance_ level. Both these concepts are handled in `pydantic-core` (providing a 5 to 20 performance increase compared to Pydantic V1), by using the previously built core schema.
`pydantic-core` exposes a [`SchemaValidator`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator) and [`SchemaSerializer`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer) class to perform these tasks:
```
frompydanticimport BaseModel


classModel(BaseModel):
    foo: int


model = Model.model_validate({'foo': 1})  [](https://docs.pydantic.dev/latest/internals/architecture/#__code_7_annotation_1)
dumped = model.model_dump()  [](https://docs.pydantic.dev/latest/internals/architecture/#__code_7_annotation_2)

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
