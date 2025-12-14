---
# Smart Librarian Export (v2.0)
- Page Number: 12
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/dataclasses
- Page Title: Dataclasses - Pydantic Validation
- Semantic Filename: dataclasses_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 15,158 characters
---

# Dataclasses - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Dataclasses
API Documentation
[`@pydantic.dataclasses.dataclass`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.dataclass)  

If you don't want to use Pydantic's [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) you can instead get the same data validation on standard 
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_1_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_1_2)
```
fromdatetimeimport datetime
fromtypingimport Optional

frompydantic.dataclassesimport dataclass


@dataclass
classUser:
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None


user = User(id='42', signup_ts='2032-06-21T12:00')
print(user)
"""
User(id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0))
"""

```

```
fromdatetimeimport datetime

frompydantic.dataclassesimport dataclass


@dataclass
classUser:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None


user = User(id='42', signup_ts='2032-06-21T12:00')
print(user)
"""
User(id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0))
"""

```

Note
Keep in mind that Pydantic dataclasses are **not** a replacement for [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/). They provide a similar functionality to stdlib dataclasses with the addition of Pydantic validation.
There are cases where subclassing using Pydantic models is the better choice.
For more information and discussion see 
Similarities between Pydantic dataclasses and models include support for:
  * [Configuration](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config) support
  * [Nested](https://docs.pydantic.dev/latest/concepts/models/#nested-models) classes
  * [Generics](https://docs.pydantic.dev/latest/concepts/models/#generic-models)


Some differences between Pydantic dataclasses and models include:
  * [validators](https://docs.pydantic.dev/latest/concepts/dataclasses/#validators-and-initialization-hooks)
  * The behavior with the [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) configuration value


Similarly to Pydantic models, arguments used to instantiate the dataclass are [copied](https://docs.pydantic.dev/latest/concepts/models/#attribute-copies).
To make use of the [various methods](https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties) to validate, dump and generate a JSON Schema, you can wrap the dataclass with a [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) and make use of its methods.
You can use both the Pydantic's [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) and the stdlib's 
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_2_2)
```
importdataclasses
fromtypingimport Optional

frompydanticimport Field
frompydantic.dataclassesimport dataclass


@dataclass
classUser:
    id: int
    name: str = 'John Doe'
    friends: list[int] = dataclasses.field(default_factory=lambda: [0])
    age: Optional[int] = dataclasses.field(
        default=None,
        metadata={'title': 'The age of the user', 'description': 'do not lie!'},
    )
    height: Optional[int] = Field(
        default=None, title='The height in cm', ge=50, le=300
    )


user = User(id='42', height='250')
print(user)
#> User(id=42, name='John Doe', friends=[0], age=None, height=250)

```

```
importdataclasses

frompydanticimport Field
frompydantic.dataclassesimport dataclass


@dataclass
classUser:
    id: int
    name: str = 'John Doe'
    friends: list[int] = dataclasses.field(default_factory=lambda: [0])
    age: int | None = dataclasses.field(
        default=None,
        metadata={'title': 'The age of the user', 'description': 'do not lie!'},
    )
    height: int | None = Field(
        default=None, title='The height in cm', ge=50, le=300
    )


user = User(id='42', height='250')
print(user)
#> User(id=42, name='John Doe', friends=[0], age=None, height=250)

```

The Pydantic [`@dataclass`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.dataclass) decorator accepts the same arguments as the standard decorator, with the addition of a `config` parameter.
## Dataclass config[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config)
If you want to modify the configuration like you would with a [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel), you have two options:
  * Use the `config` argument of the decorator.
  * Define the configuration with the `__pydantic_config__` attribute.


```
frompydanticimport ConfigDict
frompydantic.dataclassesimport dataclass


# Option 1 -- using the decorator argument:
@dataclass(config=ConfigDict(validate_assignment=True))  [](https://docs.pydantic.dev/latest/concepts/dataclasses/#__code_4_annotation_1)
classMyDataclass1:
    a: int


# Option 2 -- using an attribute:
@dataclass
classMyDataclass2:
    a: int

    __pydantic_config__ = ConfigDict(validate_assignment=True)

```

Note
While Pydantic dataclasses support the [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) configuration value, some default behavior of stdlib dataclasses may prevail. For example, any extra fields present on a Pydantic dataclass with [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) set to `'allow'` are omitted in the dataclass' string representation. There is also no way to provide validation [using the `__pydantic_extra__` attribute](https://docs.pydantic.dev/latest/concepts/models/#extra-data).
## Rebuilding dataclass schema[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#rebuilding-dataclass-schema)
The [`rebuild_dataclass()`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.rebuild_dataclass) function can be used to rebuild the core schema of the dataclass. See the [rebuilding model schema](https://docs.pydantic.dev/latest/concepts/models/#rebuilding-model-schema) section for more details.
## Stdlib dataclasses and Pydantic dataclasses[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#stdlib-dataclasses-and-pydantic-dataclasses)
### Inherit from stdlib dataclasses[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#inherit-from-stdlib-dataclasses)
Stdlib dataclasses (nested or not) can also be inherited and Pydantic will automatically validate all the inherited fields.
```
importdataclasses

importpydantic


@dataclasses.dataclass
classZ:
    z: int


@dataclasses.dataclass
classY(Z):
    y: int = 0


@pydantic.dataclasses.dataclass
classX(Y):
    x: int = 0


foo = X(x=b'1', y='2', z='3')
print(foo)
#> X(z=3, y=2, x=1)

try:
    X(z='pika')
except pydantic.ValidationError as e:
    print(e)
"""
    1 validation error for X
    z
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='pika', input_type=str]
    """

```

The decorator can also be applied directly on a stdlib dataclass, in which case a new subclass will be created:
```
importdataclasses

importpydantic


@dataclasses.dataclass
classA:
    a: int


PydanticA = pydantic.dataclasses.dataclass(A)
print(PydanticA(a='1'))
#> A(a=1)

```

### Usage of stdlib dataclasses with `BaseModel`[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#usage-of-stdlib-dataclasses-with-basemodel)
When a standard library dataclass is used within a Pydantic model, a Pydantic dataclass or a [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter), validation will be applied (and the [configuration](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config) stays the same). This means that using a stdlib or a Pydantic dataclass as a field annotation is functionally equivalent.
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_3_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_3_2)
```
importdataclasses
fromtypingimport Optional

frompydanticimport BaseModel, ConfigDict, ValidationError


@dataclasses.dataclass(frozen=True)
classUser:
    name: str


classFoo(BaseModel):
    # Required so that pydantic revalidates the model attributes:
    model_config = ConfigDict(revalidate_instances='always')

    user: Optional[User] = None


# nothing is validated as expected:
user = User(name=['not', 'a', 'string'])
print(user)
#> User(name=['not', 'a', 'string'])


try:
    Foo(user=user)
except ValidationError as e:
    print(e)
"""
    1 validation error for Foo
    user.name
      Input should be a valid string [type=string_type, input_value=['not', 'a', 'string'], input_type=list]
    """

foo = Foo(user=User(name='pika'))
try:
    foo.user.name = 'bulbi'
except dataclasses.FrozenInstanceError as e:
    print(e)
    #> cannot assign to field 'name'

```

```
importdataclasses

frompydanticimport BaseModel, ConfigDict, ValidationError


@dataclasses.dataclass(frozen=True)
classUser:
    name: str


classFoo(BaseModel):
    # Required so that pydantic revalidates the model attributes:
    model_config = ConfigDict(revalidate_instances='always')

    user: User | None = None


# nothing is validated as expected:
user = User(name=['not', 'a', 'string'])
print(user)
#> User(name=['not', 'a', 'string'])


try:
    Foo(user=user)
except ValidationError as e:
    print(e)
"""
    1 validation error for Foo
    user.name
      Input should be a valid string [type=string_type, input_value=['not', 'a', 'string'], input_type=list]
    """

foo = Foo(user=User(name='pika'))
try:
    foo.user.name = 'bulbi'
except dataclasses.FrozenInstanceError as e:
    print(e)
    #> cannot assign to field 'name'

```

### Using custom types[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#using-custom-types)
As said above, validation is applied on standard library dataclasses. If you make use of custom types, you will get an error when trying to refer to the dataclass. To circumvent the issue, you can set the [`arbitrary_types_allowed`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.arbitrary_types_allowed) configuration value on the dataclass:
```
importdataclasses

frompydanticimport BaseModel, ConfigDict
frompydantic.errorsimport PydanticSchemaGenerationError


classArbitraryType:
    def__init__(self, value):
        self.value = value

    def__repr__(self):
        return f'ArbitraryType(value={self.value!r})'


@dataclasses.dataclass
classDC:
    a: ArbitraryType
    b: str


# valid as it is a stdlib dataclass without validation:
my_dc = DC(a=ArbitraryType(value=3), b='qwe')

try:

    classModel(BaseModel):
        dc: DC
        other: str

    # invalid as dc is now validated with pydantic, and ArbitraryType is not a known type
    Model(dc=my_dc, other='other')

except PydanticSchemaGenerationError as e:
    print(e.message)
"""
    Unable to generate pydantic-core schema for <class '__main__.ArbitraryType'>. Set `arbitrary_types_allowed=True` in the model_config to ignore this error or implement `__get_pydantic_core_schema__` on your type to fully support it.

    If you got this error by calling handler(<some type>) within `__get_pydantic_core_schema__` then you likely need to call `handler.generate_schema(<some type>)` since we do not call `__get_pydantic_core_schema__` on `<some type>` otherwise to avoid infinite recursion.
    """


# valid as we set arbitrary_types_allowed=True, and that config pushes down to the nested vanilla dataclass
classModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    dc: DC
    other: str


m = Model(dc=my_dc, other='other')
print(repr(m))
#> Model(dc=DC(a=ArbitraryType(value=3), b='qwe'), other='other')

```

### Checking if a dataclass is a Pydantic dataclass[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#checking-if-a-dataclass-is-a-pydantic-dataclass)
Pydantic dataclasses are still considered dataclasses, so using `True`. To check if a type is specifically a Pydantic dataclass you can use the [`is_pydantic_dataclass()`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.is_pydantic_dataclass) function.
```
importdataclasses

importpydantic


@dataclasses.dataclass
classStdLibDataclass:
    id: int


PydanticDataclass = pydantic.dataclasses.dataclass(StdLibDataclass)

print(dataclasses.is_dataclass(StdLibDataclass))
#> True
print(pydantic.dataclasses.is_pydantic_dataclass(StdLibDataclass))
#> False

print(dataclasses.is_dataclass(PydanticDataclass))
#> True
print(pydantic.dataclasses.is_pydantic_dataclass(PydanticDataclass))
#> True

```

## Validators and initialization hooks[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#validators-and-initialization-hooks)
Validators also work with Pydantic dataclasses:
```
frompydanticimport field_validator
frompydantic.dataclassesimport dataclass


@dataclass
classDemoDataclass:
    product_id: str  # should be a five-digit string, may have leading zeros

    @field_validator('product_id', mode='before')
    @classmethod
    defconvert_int_serial(cls, v):
        if isinstance(v, int):
            v = str(v).zfill(5)
        return v


print(DemoDataclass(product_id='01234'))
#> DemoDataclass(product_id='01234')
print(DemoDataclass(product_id=2468))
#> DemoDataclass(product_id='02468')

```

The dataclass _before_ and _after_ model validators.
Example
```
frompydantic_coreimport ArgsKwargs
fromtyping_extensionsimport Self

frompydanticimport model_validator
frompydantic.dataclassesimport dataclass


@dataclass
classBirth:
    year: int
    month: int
    day: int


@dataclass
classUser:
    birth: Birth

    @model_validator(mode='before')
    @classmethod
    defbefore(cls, values: ArgsKwargs) -> ArgsKwargs:
        print(f'First: {values}')  [](https://docs.pydantic.dev/latest/concepts/dataclasses/#__code_12_annotation_1)
"""
        First: ArgsKwargs((), {'birth': {'year': 1995, 'month': 3, 'day': 2}})
        """
        return values

    @model_validator(mode='after')
    defafter(self) -> Self:
        print(f'Third: {self}')
        #> Third: User(birth=Birth(year=1995, month=3, day=2))
        return self

    def__post_init__(self):
        print(f'Second: {self.birth}')
        #> Second: Birth(year=1995, month=3, day=2)


user = User(**{'birth': {'year': 1995, 'month': 3, 'day': 2}})

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
