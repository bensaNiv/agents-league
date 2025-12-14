---
# Smart Librarian Export (v2.0)
- Page Number: 32
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/config
- Page Title: Configuration - Pydantic Validation
- Semantic Filename: configuration_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 7,177 characters
---

# Configuration - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-pydantic-models)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Configuration
The behaviour of Pydantic can be controlled via a variety of configuration values, documented on the [`ConfigDict`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) class. This page describes how configuration can be specified for Pydantic's supported types.
## Configuration on Pydantic models[¶](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-pydantic-models)
On Pydantic models, configuration can be specified in two ways:
  * Using the [`model_config`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_config) class attribute:
```
frompydanticimport BaseModel, ConfigDict, ValidationError


classModel(BaseModel):
    model_config = ConfigDict(str_max_length=5)  [](https://docs.pydantic.dev/latest/concepts/config/#__code_0_annotation_1)

    v: str


try:
    m = Model(v='abcdef')
except ValidationError as e:
    print(e)
"""
    1 validation error for Model
    v
      String should have at most 5 characters [type=string_too_long, input_value='abcdef', input_type=str]
    """

```

Note
In Pydantic V1, the `Config` class was used. This is still supported, but **deprecated**.
  * Using class arguments:
```
frompydanticimport BaseModel


classModel(BaseModel, frozen=True):
    a: str

```



Unlike the [`model_config`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_config) class attribute, static type checkers will recognize class arguments. For `frozen`, any instance mutation will be flagged as an type checking error.
## Configuration on Pydantic dataclasses[¶](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-pydantic-dataclasses)
[Pydantic dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/) also support configuration (read more in the [dedicated section](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config)).
```
frompydanticimport ConfigDict, ValidationError
frompydantic.dataclassesimport dataclass


@dataclass(config=ConfigDict(str_max_length=10, validate_assignment=True))
classUser:
    name: str


user = User(name='John Doe')
try:
    user.name = 'x' * 20
except ValidationError as e:
    print(e)
"""
    1 validation error for User
    name
      String should have at most 10 characters [type=string_too_long, input_value='xxxxxxxxxxxxxxxxxxxx', input_type=str]
    """

```

## Configuration on `TypeAdapter`[¶](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-typeadapter)
[Type adapters](https://docs.pydantic.dev/latest/concepts/type_adapter/) (using the [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) class) support configuration, by providing the `config` argument.
```
frompydanticimport ConfigDict, TypeAdapter

ta = TypeAdapter(list[str], config=ConfigDict(coerce_numbers_to_str=True))

print(ta.validate_python([1, 2]))
#> ['1', '2']

```

Configuration can't be provided if the type adapter directly wraps a type that support it, and a [usage error](https://docs.pydantic.dev/latest/errors/usage_errors/) is raised in this case. The [configuration propagation](https://docs.pydantic.dev/latest/concepts/config/#configuration-propagation) rules also apply.
## Configuration on other supported types[¶](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-other-supported-types)
If you are using 
  * Using the `__pydantic_config__` class attribute:
```
fromdataclassesimport dataclass

frompydanticimport ConfigDict


@dataclass
classUser:
    __pydantic_config__ = ConfigDict(strict=True)

    id: int
    name: str = 'John Doe'

```

  * Using the [`@with_config`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.with_config) decorator (this avoids static type checking errors with 
```
fromtyping_extensionsimport TypedDict

frompydanticimport ConfigDict, with_config


@with_config(ConfigDict(str_to_lower=True))
classModel(TypedDict):
    x: str

```



## Configuration on the `@validate_call` decorator[¶](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-the-validate_call-decorator)
The [`@validate_call`](https://docs.pydantic.dev/latest/concepts/validation_decorator/) also supports setting custom configuration. See the [dedicated section](https://docs.pydantic.dev/latest/concepts/validation_decorator/#custom-configuration) for more details.
## Change behaviour globally[¶](https://docs.pydantic.dev/latest/concepts/config/#change-behaviour-globally)
If you wish to change the behaviour of Pydantic globally, you can create your own custom parent class with a custom configuration, as the configuration is inherited:
```
frompydanticimport BaseModel, ConfigDict


classParent(BaseModel):
    model_config = ConfigDict(extra='allow')


classModel(Parent):
    x: str


m = Model(x='foo', y='bar')
print(m.model_dump())
#> {'x': 'foo', 'y': 'bar'}

```

If you provide configuration to the subclasses, it will be _merged_ with the parent configuration:
```
frompydanticimport BaseModel, ConfigDict


classParent(BaseModel):
    model_config = ConfigDict(extra='allow', str_to_lower=False)


classModel(Parent):
    model_config = ConfigDict(str_to_lower=True)

    x: str


m = Model(x='FOO', y='bar')
print(m.model_dump())
#> {'x': 'foo', 'y': 'bar'}
print(Model.model_config)
#> {'extra': 'allow', 'str_to_lower': True}

```

Warning
If your model inherits from multiple bases, Pydantic currently _doesn't_ follow the 
## Configuration propagation[¶](https://docs.pydantic.dev/latest/concepts/config/#configuration-propagation)
When using types that support configuration as field annotations, configuration may not be propagated:
  * For Pydantic models and dataclasses, configuration will _not_ be propagated, each model has its own "configuration boundary":
```
frompydanticimport BaseModel, ConfigDict


classUser(BaseModel):
    name: str


classParent(BaseModel):
    user: User

    model_config = ConfigDict(str_to_lower=True)


print(Parent(user={'name': 'JOHN'}))
#> user=User(name='JOHN')

```

  * For stdlib types (dataclasses and typed dictionaries), configuration will be propagated, unless the type has its own configuration set:
```
fromdataclassesimport dataclass

frompydanticimport BaseModel, ConfigDict, with_config


@dataclass
classUserWithoutConfig:
    name: str


@dataclass
@with_config(str_to_lower=False)
classUserWithConfig:
    name: str


classParent(BaseModel):
    user_1: UserWithoutConfig
    user_2: UserWithConfig

    model_config = ConfigDict(str_to_lower=True)


print(Parent(user_1={'name': 'JOHN'}, user_2={'name': 'JOHN'}))
#> user_1=UserWithoutConfig(name='john') user_2=UserWithConfig(name='JOHN')

```


Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
