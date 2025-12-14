---
# Smart Librarian Export (v2.0)
- Page Number: 40
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/types
- Page Title: Pydantic Types - Pydantic Validation
- Semantic Filename: pydantic_types_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 163,788 characters
---

# Pydantic Types - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/types/#pydantic.types)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Pydantic Types
##  pydantic.types [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types)
The types module contains custom types used by pydantic.
###  StrictBool `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBool)
```
StrictBool = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

A boolean that must be either `True` or `False`.
###  PositiveInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PositiveInt)
```
PositiveInt = [, Gt(0)]

```

An integer that must be greater than zero.
```
frompydanticimport BaseModel, PositiveInt, ValidationError

classModel(BaseModel):
    positive_int: PositiveInt

m = Model(positive_int=1)
print(repr(m))
#> Model(positive_int=1)

try:
    Model(positive_int=-1)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than',
            'loc': ('positive_int',),
            'msg': 'Input should be greater than 0',
            'input': -1,
            'ctx': {'gt': 0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

###  NegativeInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NegativeInt)
```
NegativeInt = [, Lt(0)]

```

An integer that must be less than zero.
```
frompydanticimport BaseModel, NegativeInt, ValidationError

classModel(BaseModel):
    negative_int: NegativeInt

m = Model(negative_int=-1)
print(repr(m))
#> Model(negative_int=-1)

try:
    Model(negative_int=1)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'less_than',
            'loc': ('negative_int',),
            'msg': 'Input should be less than 0',
            'input': 1,
            'ctx': {'lt': 0},
            'url': 'https://errors.pydantic.dev/2/v/less_than',
        }
    ]
    '''

```

###  NonPositiveInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonPositiveInt)
```
NonPositiveInt = [, Le(0)]

```

An integer that must be less than or equal to zero.
```
frompydanticimport BaseModel, NonPositiveInt, ValidationError

classModel(BaseModel):
    non_positive_int: NonPositiveInt

m = Model(non_positive_int=0)
print(repr(m))
#> Model(non_positive_int=0)

try:
    Model(non_positive_int=1)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'less_than_equal',
            'loc': ('non_positive_int',),
            'msg': 'Input should be less than or equal to 0',
            'input': 1,
            'ctx': {'le': 0},
            'url': 'https://errors.pydantic.dev/2/v/less_than_equal',
        }
    ]
    '''

```

###  NonNegativeInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonNegativeInt)
```
NonNegativeInt = [, Ge(0)]

```

An integer that must be greater than or equal to zero.
```
frompydanticimport BaseModel, NonNegativeInt, ValidationError

classModel(BaseModel):
    non_negative_int: NonNegativeInt

m = Model(non_negative_int=0)
print(repr(m))
#> Model(non_negative_int=0)

try:
    Model(non_negative_int=-1)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than_equal',
            'loc': ('non_negative_int',),
            'msg': 'Input should be greater than or equal to 0',
            'input': -1,
            'ctx': {'ge': 0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than_equal',
        }
    ]
    '''

```

###  StrictInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictInt)
```
StrictInt = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

An integer that must be validated in strict mode.
```
frompydanticimport BaseModel, StrictInt, ValidationError

classStrictIntModel(BaseModel):
    strict_int: StrictInt

try:
    StrictIntModel(strict_int=3.14159)
except ValidationError as e:
    print(e)
'''
    1 validation error for StrictIntModel
    strict_int
      Input should be a valid integer [type=int_type, input_value=3.14159, input_type=float]
    '''

```

###  PositiveFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PositiveFloat)
```
PositiveFloat = [, Gt(0)]

```

A float that must be greater than zero.
```
frompydanticimport BaseModel, PositiveFloat, ValidationError

classModel(BaseModel):
    positive_float: PositiveFloat

m = Model(positive_float=1.0)
print(repr(m))
#> Model(positive_float=1.0)

try:
    Model(positive_float=-1.0)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than',
            'loc': ('positive_float',),
            'msg': 'Input should be greater than 0',
            'input': -1.0,
            'ctx': {'gt': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

###  NegativeFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NegativeFloat)
```
NegativeFloat = [, Lt(0)]

```

A float that must be less than zero.
```
frompydanticimport BaseModel, NegativeFloat, ValidationError

classModel(BaseModel):
    negative_float: NegativeFloat

m = Model(negative_float=-1.0)
print(repr(m))
#> Model(negative_float=-1.0)

try:
    Model(negative_float=1.0)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'less_than',
            'loc': ('negative_float',),
            'msg': 'Input should be less than 0',
            'input': 1.0,
            'ctx': {'lt': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/less_than',
        }
    ]
    '''

```

###  NonPositiveFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonPositiveFloat)
```
NonPositiveFloat = [, Le(0)]

```

A float that must be less than or equal to zero.
```
frompydanticimport BaseModel, NonPositiveFloat, ValidationError

classModel(BaseModel):
    non_positive_float: NonPositiveFloat

m = Model(non_positive_float=0.0)
print(repr(m))
#> Model(non_positive_float=0.0)

try:
    Model(non_positive_float=1.0)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'less_than_equal',
            'loc': ('non_positive_float',),
            'msg': 'Input should be less than or equal to 0',
            'input': 1.0,
            'ctx': {'le': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/less_than_equal',
        }
    ]
    '''

```

###  NonNegativeFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonNegativeFloat)
```
NonNegativeFloat = [, Ge(0)]

```

A float that must be greater than or equal to zero.
```
frompydanticimport BaseModel, NonNegativeFloat, ValidationError

classModel(BaseModel):
    non_negative_float: NonNegativeFloat

m = Model(non_negative_float=0.0)
print(repr(m))
#> Model(non_negative_float=0.0)

try:
    Model(non_negative_float=-1.0)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than_equal',
            'loc': ('non_negative_float',),
            'msg': 'Input should be greater than or equal to 0',
            'input': -1.0,
            'ctx': {'ge': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than_equal',
        }
    ]
    '''

```

###  StrictFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictFloat)
```
StrictFloat = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)(True)]

```

A float that must be validated in strict mode.
```
frompydanticimport BaseModel, StrictFloat, ValidationError

classStrictFloatModel(BaseModel):
    strict_float: StrictFloat

try:
    StrictFloatModel(strict_float='1.0')
except ValidationError as e:
    print(e)
'''
    1 validation error for StrictFloatModel
    strict_float
      Input should be a valid number [type=float_type, input_value='1.0', input_type=str]
    '''

```

###  FiniteFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FiniteFloat)
```
FiniteFloat = [, AllowInfNan[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AllowInfNan)(False)]

```

A float that must be finite (not `-inf`, `inf`, or `nan`).
```
frompydanticimport BaseModel, FiniteFloat

classModel(BaseModel):
    finite: FiniteFloat

m = Model(finite=1.0)
print(m)
#> finite=1.0

```

###  StrictBytes `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBytes)
```
StrictBytes = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

A bytes that must be validated in strict mode.
###  StrictStr `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictStr)
```
StrictStr = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

A string that must be validated in strict mode.
###  UUID1 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID1)
```
UUID1 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(1)]

```

A 
```
importuuid

frompydanticimport UUID1, BaseModel

classModel(BaseModel):
    uuid1: UUID1

Model(uuid1=uuid.uuid1())

```

###  UUID3 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID3)
```
UUID3 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(3)]

```

A 
```
importuuid

frompydanticimport UUID3, BaseModel

classModel(BaseModel):
    uuid3: UUID3

Model(uuid3=uuid.uuid3(uuid.NAMESPACE_DNS, 'pydantic.org'))

```

###  UUID4 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID4)
```
UUID4 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(4)]

```

A 
```
importuuid

frompydanticimport UUID4, BaseModel

classModel(BaseModel):
    uuid4: UUID4

Model(uuid4=uuid.uuid4())

```

###  UUID5 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID5)
```
UUID5 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(5)]

```

A 
```
importuuid

frompydanticimport UUID5, BaseModel

classModel(BaseModel):
    uuid5: UUID5

Model(uuid5=uuid.uuid5(uuid.NAMESPACE_DNS, 'pydantic.org'))

```

###  UUID6 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID6)
```
UUID6 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(6)]

```

A 
```
importuuid

frompydanticimport UUID6, BaseModel

classModel(BaseModel):
    uuid6: UUID6

Model(uuid6=uuid.UUID('1efea953-c2d6-6790-aa0a-69db8c87df97'))

```

###  UUID7 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID7)
```
UUID7 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(7)]

```

A 
```
importuuid

frompydanticimport UUID7, BaseModel

classModel(BaseModel):
    uuid7: UUID7

Model(uuid7=uuid.UUID('0194fdcb-1c47-7a09-b52c-561154de0b4a'))

```

###  UUID8 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID8)
```
UUID8 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(8)]

```

A 
```
importuuid

frompydanticimport UUID8, BaseModel

classModel(BaseModel):
    uuid8: UUID8

Model(uuid8=uuid.UUID('81a0b92e-6078-8551-9c81-8ccb666bdab8'))

```

###  FilePath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FilePath)
```
FilePath = [, PathType('file')]

```

A path that must point to a file.
```
frompathlibimport Path

frompydanticimport BaseModel, FilePath, ValidationError

classModel(BaseModel):
    f: FilePath

path = Path('text.txt')
path.touch()
m = Model(f='text.txt')
print(m.model_dump())
#> {'f': PosixPath('text.txt')}
path.unlink()

path = Path('directory')
path.mkdir(exist_ok=True)
try:
    Model(f='directory')  # directory
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    f
      Path does not point to a file [type=path_not_file, input_value='directory', input_type=str]
    '''
path.rmdir()

try:
    Model(f='not-exists-file')
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    f
      Path does not point to a file [type=path_not_file, input_value='not-exists-file', input_type=str]
    '''

```

###  DirectoryPath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.DirectoryPath)
```
DirectoryPath = [, PathType('dir')]

```

A path that must point to a directory.
```
frompathlibimport Path

frompydanticimport BaseModel, DirectoryPath, ValidationError

classModel(BaseModel):
    f: DirectoryPath

path = Path('directory/')
path.mkdir()
m = Model(f='directory/')
print(m.model_dump())
#> {'f': PosixPath('directory')}
path.rmdir()

path = Path('file.txt')
path.touch()
try:
    Model(f='file.txt')  # file
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    f
      Path does not point to a directory [type=path_not_directory, input_value='file.txt', input_type=str]
    '''
path.unlink()

try:
    Model(f='not-exists-directory')
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    f
      Path does not point to a directory [type=path_not_directory, input_value='not-exists-directory', input_type=str]
    '''

```

###  NewPath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NewPath)
```
NewPath = [, PathType('new')]

```

A path for a new file or directory that must not already exist. The parent directory must already exist.
###  SocketPath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SocketPath)
```
SocketPath = [, PathType('socket')]

```

A path to an existing socket file
###  Base64Bytes `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Bytes)
```
Base64Bytes = [
    , EncodedBytes[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes)(encoder=Base64Encoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder))
]

```

A bytes type that is encoded and decoded using the standard (non-URL-safe) base64 encoder.
Note
Under the hood, `Base64Bytes` uses the standard library `base64.b64encode` and `base64.b64decode` functions.
As a result, attempting to decode url-safe base64 data using the `Base64Bytes` type may fail or produce an incorrect decoding.
Warning
In versions of Pydantic prior to v2.10, `Base64Bytes` used 
If you'd still like to use these legacy encoders / decoders, you can achieve this by creating a custom annotated type, like follows:
```
importbase64
fromtypingimport Annotated, Literal

frompydantic_coreimport PydanticCustomError

frompydanticimport EncodedBytes, EncoderProtocol

classLegacyBase64Encoder(EncoderProtocol):
    @classmethod
    defdecode(cls, data: bytes) -> bytes:
        try:
            return base64.decodebytes(data)
        except ValueError as e:
            raise PydanticCustomError(
                'base64_decode',
                "Base64 decoding error: '{error}'",
                {'error': str(e)},
            )

    @classmethod
    defencode(cls, value: bytes) -> bytes:
        return base64.encodebytes(value)

    @classmethod
    defget_json_format(cls) -> Literal['base64']:
        return 'base64'

LegacyBase64Bytes = Annotated[bytes, EncodedBytes(encoder=LegacyBase64Encoder)]

```

```
frompydanticimport Base64Bytes, BaseModel, ValidationError

classModel(BaseModel):
    base64_bytes: Base64Bytes

# Initialize the model with base64 data
m = Model(base64_bytes=b'VGhpcyBpcyB0aGUgd2F5')

# Access decoded value
print(m.base64_bytes)
#> b'This is the way'

# Serialize into the base64 form
print(m.model_dump())
#> {'base64_bytes': b'VGhpcyBpcyB0aGUgd2F5'}

# Validate base64 data
try:
    print(Model(base64_bytes=b'undecodable').base64_bytes)
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    base64_bytes
      Base64 decoding error: 'Incorrect padding' [type=base64_decode, input_value=b'undecodable', input_type=bytes]
    '''

```

###  Base64Str `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Str)
```
Base64Str = [
    , EncodedStr[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr)(encoder=Base64Encoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder))
]

```

A str type that is encoded and decoded using the standard (non-URL-safe) base64 encoder.
Note
Under the hood, `Base64Str` uses the standard library `base64.b64encode` and `base64.b64decode` functions.
As a result, attempting to decode url-safe base64 data using the `Base64Str` type may fail or produce an incorrect decoding.
Warning
In versions of Pydantic prior to v2.10, `Base64Str` used 
See the [`Base64Bytes`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Bytes) type for more information on how to replicate the old behavior with the legacy encoders / decoders.
```
frompydanticimport Base64Str, BaseModel, ValidationError

classModel(BaseModel):
    base64_str: Base64Str

# Initialize the model with base64 data
m = Model(base64_str='VGhlc2UgYXJlbid0IHRoZSBkcm9pZHMgeW91J3JlIGxvb2tpbmcgZm9y')

# Access decoded value
print(m.base64_str)
#> These aren't the droids you're looking for

# Serialize into the base64 form
print(m.model_dump())
#> {'base64_str': 'VGhlc2UgYXJlbid0IHRoZSBkcm9pZHMgeW91J3JlIGxvb2tpbmcgZm9y'}

# Validate base64 data
try:
    print(Model(base64_str='undecodable').base64_str)
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    base64_str
      Base64 decoding error: 'Incorrect padding' [type=base64_decode, input_value='undecodable', input_type=str]
    '''

```

###  Base64UrlBytes `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlBytes)
```
Base64UrlBytes = [
    , EncodedBytes[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes)(encoder=Base64UrlEncoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder))
]

```

A bytes type that is encoded and decoded using the URL-safe base64 encoder.
Note
Under the hood, `Base64UrlBytes` use standard library `base64.urlsafe_b64encode` and `base64.urlsafe_b64decode` functions.
As a result, the `Base64UrlBytes` type can be used to faithfully decode "vanilla" base64 data (using `'+'` and `'/'`).
```
frompydanticimport Base64UrlBytes, BaseModel

classModel(BaseModel):
    base64url_bytes: Base64UrlBytes

# Initialize the model with base64 data
m = Model(base64url_bytes=b'SHc_dHc-TXc==')
print(m)
#> base64url_bytes=b'Hw?tw>Mw'

```

###  Base64UrlStr `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlStr)
```
Base64UrlStr = [
    , EncodedStr[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr)(encoder=Base64UrlEncoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder))
]

```

A str type that is encoded and decoded using the URL-safe base64 encoder.
Note
Under the hood, `Base64UrlStr` use standard library `base64.urlsafe_b64encode` and `base64.urlsafe_b64decode` functions.
As a result, the `Base64UrlStr` type can be used to faithfully decode "vanilla" base64 data (using `'+'` and `'/'`).
```
frompydanticimport Base64UrlStr, BaseModel

classModel(BaseModel):
    base64url_str: Base64UrlStr

# Initialize the model with base64 data
m = Model(base64url_str='SHc_dHc-TXc==')
print(m)
#> base64url_str='Hw?tw>Mw'

```

###  JsonValue `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.JsonValue)
```
JsonValue: = [
    ["JsonValue"],
    [, "JsonValue"],
    ,
    ,
    ,
    ,
    None,
]

```

A `JsonValue` is used to represent a value that can be serialized to JSON.
It may be one of:
  * `list['JsonValue']`
  * `dict[str, 'JsonValue']`
  * `str`
  * `bool`
  * `int`
  * `float`
  * `None`


The following example demonstrates how to use `JsonValue` to validate JSON data, and what kind of errors to expect when input data is not json serializable.
```
importjson

frompydanticimport BaseModel, JsonValue, ValidationError

classModel(BaseModel):
    j: JsonValue

valid_json_data = {'j': {'a': {'b': {'c': 1, 'd': [2, None]}}}}
invalid_json_data = {'j': {'a': {'b': ...}}}

print(repr(Model.model_validate(valid_json_data)))
#> Model(j={'a': {'b': {'c': 1, 'd': [2, None]}}})
print(repr(Model.model_validate_json(json.dumps(valid_json_data))))
#> Model(j={'a': {'b': {'c': 1, 'd': [2, None]}}})

try:
    Model.model_validate(invalid_json_data)
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    j.dict.a.dict.b
      input was not a valid JSON value [type=invalid-json-value, input_value=Ellipsis, input_type=ellipsis]
    '''

```

###  OnErrorOmit `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.OnErrorOmit)
```
OnErrorOmit = [T, _OnErrorOmit]

```

When used as an item in a list, the key type in a dict, optional values of a TypedDict, etc. this annotation omits the item from the iteration if there is any error validating it. That is, instead of a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) being propagated up and the entire iterable being discarded any invalid items are discarded and the valid ones are returned.
###  Strict `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)
Bases: `PydanticMetadata`, `BaseMetadata`
Usage Documentation
[Strict Mode with `Annotated` `Strict`](https://docs.pydantic.dev/latest/concepts/strict_mode/#strict-mode-with-annotated-strict)
A field metadata class to indicate that a field should be validated in strict mode. Use this class as an annotation via 
Attributes:
Name | Type | Description  
---|---|---  
`strict` |  |  Whether to validate the field in strict mode.  
Example
```
fromtypingimport Annotated

frompydantic.typesimport Strict

StrictBool = Annotated[bool, Strict()]

```

Source code in `pydantic/types.py`
```
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
```
| ```
@_dataclasses.dataclass
classStrict(_fields.PydanticMetadata, BaseMetadata):
"""!!! abstract "Usage Documentation"
        [Strict Mode with `Annotated` `Strict`](../concepts/strict_mode.md#strict-mode-with-annotated-strict)

    A field metadata class to indicate that a field should be validated in strict mode.
    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        strict: Whether to validate the field in strict mode.

    Example:
    ```python
        from typing import Annotated

        from pydantic.types import Strict

        StrictBool = Annotated[bool, Strict()]
    ```
    """

    strict: bool = True

    def__hash__(self) -> int:
        return hash(self.strict)

```
  
---|---  
###  AllowInfNan `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AllowInfNan)
Bases: `PydanticMetadata`
A field metadata class to indicate that a field should allow `-inf`, `inf`, and `nan`.
Use this class as an annotation via 
Attributes:
Name | Type | Description  
---|---|---  
`allow_inf_nan` |  |  Whether to allow `-inf`, `inf`, and `nan`. Defaults to `True`.  
Example
```
fromtypingimport Annotated

frompydantic.typesimport AllowInfNan

LaxFloat = Annotated[float, AllowInfNan()]

```

Source code in `pydantic/types.py`
```
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
```
| ```
@_dataclasses.dataclass
classAllowInfNan(_fields.PydanticMetadata):
"""A field metadata class to indicate that a field should allow `-inf`, `inf`, and `nan`.

    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`. Defaults to `True`.

    Example:
    ```python
        from typing import Annotated

        from pydantic.types import AllowInfNan

        LaxFloat = Annotated[float, AllowInfNan()]
    ```
    """

    allow_inf_nan: bool = True

    def__hash__(self) -> int:
        return hash(self.allow_inf_nan)

```
  
---|---  
###  StringConstraints `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StringConstraints)
Bases: `GroupedMetadata`
Usage Documentation
[String types](https://docs.pydantic.dev/latest/api/standard_library_types/#strings)
A field metadata class to apply constraints to `str` types. Use this class as an annotation via 
Attributes:
Name | Type | Description  
---|---|---  
`strip_whitespace` |  |  Whether to remove leading and trailing whitespace.  
`to_upper` |  |  Whether to convert the string to uppercase.  
`to_lower` |  |  Whether to convert the string to lowercase.  
`strict` |  |  Whether to validate the string in strict mode.  
`min_length` |  |  The minimum length of the string.  
`max_length` |  |  The maximum length of the string.  
`pattern` |  |  A regex pattern that the string must match.  
Example
```
fromtypingimport Annotated

frompydantic.typesimport StringConstraints

ConstrainedStr = Annotated[str, StringConstraints(min_length=1, max_length=10)]

```

Source code in `pydantic/types.py`
```
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
```
| ```
@_dataclasses.dataclass(frozen=True)
classStringConstraints(annotated_types.GroupedMetadata):
"""!!! abstract "Usage Documentation"
        [String types](./standard_library_types.md#strings)

    A field metadata class to apply constraints to `str` types.
    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to convert the string to uppercase.
        to_lower: Whether to convert the string to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern that the string must match.

    Example:
    ```python
        from typing import Annotated

        from pydantic.types import StringConstraints

        ConstrainedStr = Annotated[str, StringConstraints(min_length=1, max_length=10)]
    ```
    """

    strip_whitespace: bool | None = None
    to_upper: bool | None = None
    to_lower: bool | None = None
    strict: bool | None = None
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | Pattern[str] | None = None

    def__iter__(self) -> Iterator[BaseMetadata]:
        if self.min_length is not None:
            yield MinLen(self.min_length)
        if self.max_length is not None:
            yield MaxLen(self.max_length)
        if self.strict is not None:
            yield Strict(self.strict)
        if (
            self.strip_whitespace is not None
            or self.pattern is not None
            or self.to_lower is not None
            or self.to_upper is not None
        ):
            yield _fields.pydantic_general_metadata(
                strip_whitespace=self.strip_whitespace,
                to_upper=self.to_upper,
                to_lower=self.to_lower,
                pattern=self.pattern,
            )

```
  
---|---  
###  ImportString [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ImportString)
A type that can be used to import a Python object from a string.
`ImportString` expects a string and loads the Python object importable at that dotted path. Attributes of modules may be separated from the module by `:` or `.`, e.g. if `'math:cos'` is provided, the resulting field value would be the function `cos`. If a `.` is used and both an attribute and submodule are present at the same path, the module will be preferred.
On model instantiation, pointers will be evaluated and imported. There is some nuance to this behavior, demonstrated in the examples below.
```
importmath

frompydanticimport BaseModel, Field, ImportString, ValidationError

classImportThings(BaseModel):
    obj: ImportString

# A string value will cause an automatic import
my_cos = ImportThings(obj='math.cos')

# You can use the imported function as you would expect
cos_of_0 = my_cos.obj(0)
assert cos_of_0 == 1

# A string whose value cannot be imported will raise an error
try:
    ImportThings(obj='foo.bar')
except ValidationError as e:
    print(e)
'''
    1 validation error for ImportThings
    obj
      Invalid python path: No module named 'foo.bar' [type=import_error, input_value='foo.bar', input_type=str]
    '''

# Actual python objects can be assigned as well
my_cos = ImportThings(obj=math.cos)
my_cos_2 = ImportThings(obj='math.cos')
my_cos_3 = ImportThings(obj='math:cos')
assert my_cos == my_cos_2 == my_cos_3

# You can set default field value either as Python object:
classImportThingsDefaultPyObj(BaseModel):
    obj: ImportString = math.cos

# or as a string value (but only if used with `validate_default=True`)
classImportThingsDefaultString(BaseModel):
    obj: ImportString = Field(default='math.cos', validate_default=True)

my_cos_default1 = ImportThingsDefaultPyObj()
my_cos_default2 = ImportThingsDefaultString()
assert my_cos_default1.obj == my_cos_default2.obj == math.cos

# note: this will not work!
classImportThingsMissingValidateDefault(BaseModel):
    obj: ImportString = 'math.cos'

my_cos_default3 = ImportThingsMissingValidateDefault()
assert my_cos_default3.obj == 'math.cos'  # just string, not evaluated

```

Serializing an `ImportString` type to json is also possible.
```
frompydanticimport BaseModel, ImportString

classImportThings(BaseModel):
    obj: ImportString

# Create an instance
m = ImportThings(obj='math.cos')
print(m)
#> obj=<built-in function cos>
print(m.model_dump_json())
#> {"obj":"math.cos"}

```

Source code in `pydantic/types.py`
```
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
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
 936
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
 949
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
 963
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
 974
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
 985
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
1020
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
1031
1032
1033
1034
```
| ```
classImportString:
"""A type that can be used to import a Python object from a string.

    `ImportString` expects a string and loads the Python object importable at that dotted path.
    Attributes of modules may be separated from the module by `:` or `.`, e.g. if `'math:cos'` is provided,
    the resulting field value would be the function `cos`. If a `.` is used and both an attribute and submodule
    are present at the same path, the module will be preferred.

    On model instantiation, pointers will be evaluated and imported. There is
    some nuance to this behavior, demonstrated in the examples below.

```python
    import math

    from pydantic import BaseModel, Field, ImportString, ValidationError

    class ImportThings(BaseModel):
        obj: ImportString

    # A string value will cause an automatic import
    my_cos = ImportThings(obj='math.cos')

    # You can use the imported function as you would expect
    cos_of_0 = my_cos.obj(0)
    assert cos_of_0 == 1

    # A string whose value cannot be imported will raise an error
    try:
        ImportThings(obj='foo.bar')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for ImportThings
        obj
          Invalid python path: No module named 'foo.bar' [type=import_error, input_value='foo.bar', input_type=str]
        '''

    # Actual python objects can be assigned as well
    my_cos = ImportThings(obj=math.cos)
    my_cos_2 = ImportThings(obj='math.cos')
    my_cos_3 = ImportThings(obj='math:cos')
    assert my_cos == my_cos_2 == my_cos_3

    # You can set default field value either as Python object:
    class ImportThingsDefaultPyObj(BaseModel):
        obj: ImportString = math.cos

    # or as a string value (but only if used with `validate_default=True`)
    class ImportThingsDefaultString(BaseModel):
        obj: ImportString = Field(default='math.cos', validate_default=True)

    my_cos_default1 = ImportThingsDefaultPyObj()
    my_cos_default2 = ImportThingsDefaultString()
    assert my_cos_default1.obj == my_cos_default2.obj == math.cos

    # note: this will not work!
    class ImportThingsMissingValidateDefault(BaseModel):
        obj: ImportString = 'math.cos'

    my_cos_default3 = ImportThingsMissingValidateDefault()
    assert my_cos_default3.obj == 'math.cos'  # just string, not evaluated
```

    Serializing an `ImportString` type to json is also possible.

```python
    from pydantic import BaseModel, ImportString

    class ImportThings(BaseModel):
        obj: ImportString

    # Create an instance
    m = ImportThings(obj='math.cos')
    print(m)
    #> obj=<built-in function cos>
    print(m.model_dump_json())
    #> {"obj":"math.cos"}
```
    """

    @classmethod
    def__class_getitem__(cls, item: AnyType) -> AnyType:
        return Annotated[item, cls()]

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        serializer = core_schema.plain_serializer_function_ser_schema(cls._serialize, when_used='json')
        if cls is source:
            # Treat bare usage of ImportString (`schema is None`) as the same as ImportString[Any]
            return core_schema.no_info_plain_validator_function(
                function=_validators.import_string, serialization=serializer
            )
        else:
            return core_schema.no_info_before_validator_function(
                function=_validators.import_string, schema=handler(source), serialization=serializer
            )

    @classmethod
    def__get_pydantic_json_schema__(cls, cs: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return handler(core_schema.str_schema())

    @staticmethod
    def_serialize(v: Any) -> str:
        if isinstance(v, ModuleType):
            return v.__name__
        elif hasattr(v, '__module__') and hasattr(v, '__name__'):
            return f'{v.__module__}.{v.__name__}'
        # Handle special cases for sys.XXX streams
        # if we see more of these, we should consider a more general solution
        elif hasattr(v, 'name'):
            if v.name == '<stdout>':
                return 'sys.stdout'
            elif v.name == '<stdin>':
                return 'sys.stdin'
            elif v.name == '<stderr>':
                return 'sys.stderr'
        return v

    def__repr__(self) -> str:
        return 'ImportString'

```
  
---|---  
###  UuidVersion `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)
A field metadata class to indicate a 
Use this class as an annotation via 
Attributes:
Name | Type | Description  
---|---|---  
`uuid_version` |  |  The version of the UUID. Must be one of 1, 3, 4, 5, 6, 7 or 8.  
Example
```
fromtypingimport Annotated
fromuuidimport UUID

frompydantic.typesimport UuidVersion

UUID1 = Annotated[UUID, UuidVersion(1)]

```

Source code in `pydantic/types.py`
```
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
1151
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
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
classUuidVersion:
"""A field metadata class to indicate a [UUID](https://docs.python.org/3/library/uuid.html) version.

    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        uuid_version: The version of the UUID. Must be one of 1, 3, 4, 5, 6, 7 or 8.

    Example:
    ```python
        from typing import Annotated
        from uuid import UUID

        from pydantic.types import UuidVersion

        UUID1 = Annotated[UUID, UuidVersion(1)]
    ```
    """

    uuid_version: Literal[1, 3, 4, 5, 6, 7, 8]

    def__get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.pop('anyOf', None)  # remove the bytes/str union
        field_schema.update(type='string', format=f'uuid{self.uuid_version}')
        return field_schema

    def__get_pydantic_core_schema__(self, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        schema = handler(source)
        _check_annotated_type(schema['type'], 'uuid', self.__class__.__name__)
        schema['version'] = self.uuid_version  # type: ignore
        return schema

    def__hash__(self) -> int:
        return hash(type(self.uuid_version))

```
  
---|---  
###  Json [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Json)
A special type wrapper which loads JSON before parsing.
You can use the `Json` data type to make Pydantic first load a raw JSON string before validating the loaded data into the parametrized type:
```
fromtypingimport Any

frompydanticimport BaseModel, Json, ValidationError

classAnyJsonModel(BaseModel):
    json_obj: Json[Any]

classConstrainedJsonModel(BaseModel):
    json_obj: Json[list[int]]

print(AnyJsonModel(json_obj='{"b": 1}'))
#> json_obj={'b': 1}
print(ConstrainedJsonModel(json_obj='[1, 2, 3]'))
#> json_obj=[1, 2, 3]

try:
    ConstrainedJsonModel(json_obj=12)
except ValidationError as e:
    print(e)
'''
    1 validation error for ConstrainedJsonModel
    json_obj
      JSON input should be string, bytes or bytearray [type=json_type, input_value=12, input_type=int]
    '''

try:
    ConstrainedJsonModel(json_obj='[a, b]')
except ValidationError as e:
    print(e)
'''
    1 validation error for ConstrainedJsonModel
    json_obj
      Invalid JSON: expected value at line 1 column 2 [type=json_invalid, input_value='[a, b]', input_type=str]
    '''

try:
    ConstrainedJsonModel(json_obj='["a", "b"]')
except ValidationError as e:
    print(e)
'''
    2 validation errors for ConstrainedJsonModel
    json_obj.0
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    json_obj.1
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='b', input_type=str]
    '''

```

When you dump the model using `model_dump` or `model_dump_json`, the dumped value will be the result of validation, not the original JSON string. However, you can use the argument `round_trip=True` to get the original JSON string back:
```
frompydanticimport BaseModel, Json

classConstrainedJsonModel(BaseModel):
    json_obj: Json[list[int]]

print(ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json())
#> {"json_obj":[1,2,3]}
print(
    ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json(round_trip=True)
)
#> {"json_obj":"[1,2,3]"}

```

Source code in `pydantic/types.py`
```
1436
1437
1438
1439
1440
1441
1442
1443
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
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
```
| ```
classJson:
"""A special type wrapper which loads JSON before parsing.

    You can use the `Json` data type to make Pydantic first load a raw JSON string before
    validating the loaded data into the parametrized type:

```python
    from typing import Any

    from pydantic import BaseModel, Json, ValidationError

    class AnyJsonModel(BaseModel):
        json_obj: Json[Any]

    class ConstrainedJsonModel(BaseModel):
        json_obj: Json[list[int]]

    print(AnyJsonModel(json_obj='{"b": 1}'))
    #> json_obj={'b': 1}
    print(ConstrainedJsonModel(json_obj='[1, 2, 3]'))
    #> json_obj=[1, 2, 3]

    try:
        ConstrainedJsonModel(json_obj=12)
    except ValidationError as e:
        print(e)
        '''
        1 validation error for ConstrainedJsonModel
        json_obj
          JSON input should be string, bytes or bytearray [type=json_type, input_value=12, input_type=int]
        '''

    try:
        ConstrainedJsonModel(json_obj='[a, b]')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for ConstrainedJsonModel
        json_obj
          Invalid JSON: expected value at line 1 column 2 [type=json_invalid, input_value='[a, b]', input_type=str]
        '''

    try:
        ConstrainedJsonModel(json_obj='["a", "b"]')
    except ValidationError as e:
        print(e)
        '''
        2 validation errors for ConstrainedJsonModel
        json_obj.0
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
        json_obj.1
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='b', input_type=str]
        '''
```

    When you dump the model using `model_dump` or `model_dump_json`, the dumped value will be the result of validation,
    not the original JSON string. However, you can use the argument `round_trip=True` to get the original JSON string back:

```python
    from pydantic import BaseModel, Json

    class ConstrainedJsonModel(BaseModel):
        json_obj: Json[list[int]]

    print(ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json())
    #> {"json_obj":[1,2,3]}
    print(
        ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json(round_trip=True)
    )
    #> {"json_obj":"[1,2,3]"}
```
    """

    @classmethod
    def__class_getitem__(cls, item: AnyType) -> AnyType:
        return Annotated[item, cls()]

    @classmethod
    def__get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        if cls is source:
            return core_schema.json_schema(None)
        else:
            return core_schema.json_schema(handler(source))

    def__repr__(self) -> str:
        return 'Json'

    def__hash__(self) -> int:
        return hash(type(self))

    def__eq__(self, other: Any) -> bool:
        return type(other) is type(self)

```
  
---|---  
###  Secret [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Secret)
Bases: `_SecretBase[SecretType]`
A generic base class used for defining a field with sensitive information that you do not want to be visible in logging or tracebacks.
You may either directly parametrize `Secret` with a type, or subclass from `Secret` with a parametrized type. The benefit of subclassing is that you can define a custom `_display` method, which will be used for `repr()` and `str()` methods. The examples below demonstrate both ways of using `Secret` to create a new secret type.
  1. Directly parametrizing `Secret` with a type:


```
frompydanticimport BaseModel, Secret

SecretBool = Secret[bool]

classModel(BaseModel):
    secret_bool: SecretBool

m = Model(secret_bool=True)
print(m.model_dump())
#> {'secret_bool': Secret('**********')}

print(m.model_dump_json())
#> {"secret_bool":"**********"}

print(m.secret_bool.get_secret_value())
#> True

```

  1. Subclassing from parametrized `Secret`:


```
fromdatetimeimport date

frompydanticimport BaseModel, Secret

classSecretDate(Secret[date]):
    def_display(self) -> str:
        return '****/**/**'

classModel(BaseModel):
    secret_date: SecretDate

m = Model(secret_date=date(2022, 1, 1))
print(m.model_dump())
#> {'secret_date': SecretDate('****/**/**')}

print(m.model_dump_json())
#> {"secret_date":"****/**/**"}

print(m.secret_date.get_secret_value())
#> 2022-01-01

```

The value returned by the `_display` method will be used for `repr()` and `str()`.
You can enforce constraints on the underlying type through annotations: For example:
```
fromtypingimport Annotated

frompydanticimport BaseModel, Field, Secret, ValidationError

SecretPosInt = Secret[Annotated[int, Field(gt=0, strict=True)]]

classModel(BaseModel):
    sensitive_int: SecretPosInt

m = Model(sensitive_int=42)
print(m.model_dump())
#> {'sensitive_int': Secret('**********')}

try:
    m = Model(sensitive_int=-42)  [](https://docs.pydantic.dev/latest/api/types/#__code_73_annotation_1)
except ValidationError as exc_info:
    print(exc_info.errors(include_url=False, include_input=False))
'''
    [
        {
            'type': 'greater_than',
            'loc': ('sensitive_int',),
            'msg': 'Input should be greater than 0',
            'ctx': {'gt': 0},
        }
    ]
    '''

try:
    m = Model(sensitive_int='42')  [](https://docs.pydantic.dev/latest/api/types/#__code_73_annotation_2)
except ValidationError as exc_info:
    print(exc_info.errors(include_url=False, include_input=False))
'''
    [
        {
            'type': 'int_type',
            'loc': ('sensitive_int',),
            'msg': 'Input should be a valid integer',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
1571
1572
1573
1574
1575
1576
1577
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
1588
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
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
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
1700
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
1723
1724
1725
1726
1727
1728
```
| ```
classSecret(_SecretBase[SecretType]):
"""A generic base class used for defining a field with sensitive information that you do not want to be visible in logging or tracebacks.

    You may either directly parametrize `Secret` with a type, or subclass from `Secret` with a parametrized type. The benefit of subclassing
    is that you can define a custom `_display` method, which will be used for `repr()` and `str()` methods. The examples below demonstrate both
    ways of using `Secret` to create a new secret type.

    1. Directly parametrizing `Secret` with a type:

```python
    from pydantic import BaseModel, Secret

    SecretBool = Secret[bool]

    class Model(BaseModel):
        secret_bool: SecretBool

    m = Model(secret_bool=True)
    print(m.model_dump())
    #> {'secret_bool': Secret('**********')}

    print(m.model_dump_json())
    #> {"secret_bool":"**********"}

    print(m.secret_bool.get_secret_value())
    #> True
```

    2. Subclassing from parametrized `Secret`:

```python
    from datetime import date

    from pydantic import BaseModel, Secret

    class SecretDate(Secret[date]):
        def _display(self) -> str:
            return '****/**/**'

    class Model(BaseModel):
        secret_date: SecretDate

    m = Model(secret_date=date(2022, 1, 1))
    print(m.model_dump())
    #> {'secret_date': SecretDate('****/**/**')}

    print(m.model_dump_json())
    #> {"secret_date":"****/**/**"}

    print(m.secret_date.get_secret_value())
    #> 2022-01-01
```

    The value returned by the `_display` method will be used for `repr()` and `str()`.

    You can enforce constraints on the underlying type through annotations:
    For example:

```python
    from typing import Annotated

    from pydantic import BaseModel, Field, Secret, ValidationError

    SecretPosInt = Secret[Annotated[int, Field(gt=0, strict=True)]]

    class Model(BaseModel):
        sensitive_int: SecretPosInt

    m = Model(sensitive_int=42)
    print(m.model_dump())
    #> {'sensitive_int': Secret('**********')}

    try:
        m = Model(sensitive_int=-42)  # (1)!
    except ValidationError as exc_info:
        print(exc_info.errors(include_url=False, include_input=False))
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('sensitive_int',),
                'msg': 'Input should be greater than 0',
                'ctx': {'gt': 0},
            }
        ]
        '''

    try:
        m = Model(sensitive_int='42')  # (2)!
    except ValidationError as exc_info:
        print(exc_info.errors(include_url=False, include_input=False))
        '''
        [
            {
                'type': 'int_type',
                'loc': ('sensitive_int',),
                'msg': 'Input should be a valid integer',
            }
        ]
        '''
```

    1. The input value is not greater than 0, so it raises a validation error.
    2. The input value is not an integer, so it raises a validation error because the `SecretPosInt` type has strict mode enabled.
    """

    def_display(self) -> str | bytes:
        return '**********' if self.get_secret_value() else ''

    @classmethod
    def__get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        inner_type = None
        # if origin_type is Secret, then cls is a GenericAlias, and we can extract the inner type directly
        origin_type = get_origin(source)
        if origin_type is not None:
            inner_type = get_args(source)[0]
        # otherwise, we need to get the inner type from the base class
        else:
            bases = getattr(cls, '__orig_bases__', getattr(cls, '__bases__', []))
            for base in bases:
                if get_origin(base) is Secret:
                    inner_type = get_args(base)[0]
            if bases == [] or inner_type is None:
                raise TypeError(
                    f"Can't get secret type from {cls.__name__}. "
                    'Please use Secret[<type>], or subclass from Secret[<type>] instead.'
                )

        inner_schema = handler.generate_schema(inner_type)  # type: ignore

        defvalidate_secret_value(value, handler) -> Secret[SecretType]:
            if isinstance(value, Secret):
                value = value.get_secret_value()
            validated_inner = handler(value)
            return cls(validated_inner)

        return core_schema.json_or_python_schema(
            python_schema=core_schema.no_info_wrap_validator_function(
                validate_secret_value,
                inner_schema,
            ),
            json_schema=core_schema.no_info_after_validator_function(lambda x: cls(x), inner_schema),
            serialization=core_schema.plain_serializer_function_ser_schema(
                _serialize_secret,
                info_arg=True,
                when_used='always',
            ),
        )

    __pydantic_serializer__ = SchemaSerializer(
        core_schema.any_schema(
            serialization=core_schema.plain_serializer_function_ser_schema(
                _serialize_secret,
                info_arg=True,
                when_used='always',
            )
        )
    )

```
  
---|---  
###  SecretStr [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr)
Bases: `_SecretField[`
A string used for storing sensitive information that you do not want to be visible in logging or tracebacks.
When the secret value is nonempty, it is displayed as `'**********'` instead of the underlying value in calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `''`.
```
frompydanticimport BaseModel, SecretStr

classUser(BaseModel):
    username: str
    password: SecretStr

user = User(username='scolvin', password='password1')

print(user)
#> username='scolvin' password=SecretStr('**********')
print(user.password.get_secret_value())
#> password1
print((SecretStr('password'), SecretStr('')))
#> (SecretStr('**********'), SecretStr(''))

```

As seen above, by default, [`SecretStr`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr) (and [`SecretBytes`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretBytes)) will be serialized as `**********` when serializing to json.
You can use the [`field_serializer`](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.field_serializer) to dump the secret as plain-text when serializing to json.
```
frompydanticimport BaseModel, SecretBytes, SecretStr, field_serializer

classModel(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes

    @field_serializer('password', 'password_bytes', when_used='json')
    defdump_secret(self, v):
        return v.get_secret_value()

model = Model(password='IAmSensitive', password_bytes=b'IAmSensitiveBytes')
print(model)
#> password=SecretStr('**********') password_bytes=SecretBytes(b'**********')
print(model.password)
#> **********
print(model.model_dump())
'''
{
    'password': SecretStr('**********'),
    'password_bytes': SecretBytes(b'**********'),
}
'''
print(model.model_dump_json())
#> {"password":"IAmSensitive","password_bytes":"IAmSensitiveBytes"}

```

Source code in `pydantic/types.py`
```
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
1820
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
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
```
| ```
classSecretStr(_SecretField[str]):
"""A string used for storing sensitive information that you do not want to be visible in logging or tracebacks.

    When the secret value is nonempty, it is displayed as `'**********'` instead of the underlying value in
    calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `''`.

```python
    from pydantic import BaseModel, SecretStr

    class User(BaseModel):
        username: str
        password: SecretStr

    user = User(username='scolvin', password='password1')

    print(user)
    #> username='scolvin' password=SecretStr('**********')
    print(user.password.get_secret_value())
    #> password1
    print((SecretStr('password'), SecretStr('')))
    #> (SecretStr('**********'), SecretStr(''))
```

    As seen above, by default, [`SecretStr`][pydantic.types.SecretStr] (and [`SecretBytes`][pydantic.types.SecretBytes])
    will be serialized as `**********` when serializing to json.

    You can use the [`field_serializer`][pydantic.functional_serializers.field_serializer] to dump the
    secret as plain-text when serializing to json.

```python
    from pydantic import BaseModel, SecretBytes, SecretStr, field_serializer

    class Model(BaseModel):
        password: SecretStr
        password_bytes: SecretBytes

        @field_serializer('password', 'password_bytes', when_used='json')
        def dump_secret(self, v):
            return v.get_secret_value()

    model = Model(password='IAmSensitive', password_bytes=b'IAmSensitiveBytes')
    print(model)
    #> password=SecretStr('**********') password_bytes=SecretBytes(b'**********')
    print(model.password)
    #> **********
    print(model.model_dump())
    '''
    {
        'password': SecretStr('**********'),
        'password_bytes': SecretBytes(b'**********'),
    }
    '''
    print(model.model_dump_json())
    #> {"password":"IAmSensitive","password_bytes":"IAmSensitiveBytes"}
```
    """

    _inner_schema: ClassVar[CoreSchema] = core_schema.str_schema()
    _error_kind: ClassVar[str] = 'string_type'

    def__len__(self) -> int:
        return len(self._secret_value)

    def_display(self) -> str:
        return _secret_display(self._secret_value)

```
  
---|---  
###  SecretBytes [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretBytes)
Bases: `_SecretField[`
A bytes used for storing sensitive information that you do not want to be visible in logging or tracebacks.
It displays `b'**********'` instead of the string value on `repr()` and `str()` calls. When the secret value is nonempty, it is displayed as `b'**********'` instead of the underlying value in calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `b''`.
```
frompydanticimport BaseModel, SecretBytes

classUser(BaseModel):
    username: str
    password: SecretBytes

user = User(username='scolvin', password=b'password1')
#> username='scolvin' password=SecretBytes(b'**********')
print(user.password.get_secret_value())
#> b'password1'
print((SecretBytes(b'password'), SecretBytes(b'')))
#> (SecretBytes(b'**********'), SecretBytes(b''))

```

Source code in `pydantic/types.py`
```
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
1894
1895
1896
1897
1898
```
| ```
classSecretBytes(_SecretField[bytes]):
"""A bytes used for storing sensitive information that you do not want to be visible in logging or tracebacks.

    It displays `b'**********'` instead of the string value on `repr()` and `str()` calls.
    When the secret value is nonempty, it is displayed as `b'**********'` instead of the underlying value in
    calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `b''`.

```python
    from pydantic import BaseModel, SecretBytes

    class User(BaseModel):
        username: str
        password: SecretBytes

    user = User(username='scolvin', password=b'password1')
    #> username='scolvin' password=SecretBytes(b'**********')
    print(user.password.get_secret_value())
    #> b'password1'
    print((SecretBytes(b'password'), SecretBytes(b'')))
    #> (SecretBytes(b'**********'), SecretBytes(b''))
```
    """

    _inner_schema: ClassVar[CoreSchema] = core_schema.bytes_schema()
    _error_kind: ClassVar[str] = 'bytes_type'

    def__len__(self) -> int:
        return len(self._secret_value)

    def_display(self) -> bytes:
        return _secret_display(self._secret_value).encode()

```
  
---|---  
###  PaymentCardNumber [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber)
Bases: 
Based on: https://en.wikipedia.org/wiki/Payment_card_number.
Source code in `pydantic/types.py`
```
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
1937
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
1955
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
1994
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
2005
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
2016
2017
2018
2019
```
| ```
@deprecated(
    'The `PaymentCardNumber` class is deprecated, use `pydantic_extra_types` instead. '
    'See https://docs.pydantic.dev/latest/api/pydantic_extra_types_payment/#pydantic_extra_types.payment.PaymentCardNumber.',
    category=PydanticDeprecatedSince20,
)
classPaymentCardNumber(str):
"""Based on: https://en.wikipedia.org/wiki/Payment_card_number."""

    strip_whitespace: ClassVar[bool] = True
    min_length: ClassVar[int] = 12
    max_length: ClassVar[int] = 19
    bin: str
    last4: str
    brand: PaymentCardBrand

    def__init__(self, card_number: str):
        self.validate_digits(card_number)

        card_number = self.validate_luhn_check_digit(card_number)

        self.bin = card_number[:6]
        self.last4 = card_number[-4:]
        self.brand = self.validate_brand(card_number)

    @classmethod
    def__get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.with_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(
                min_length=cls.min_length, max_length=cls.max_length, strip_whitespace=cls.strip_whitespace
            ),
        )

    @classmethod
    defvalidate(cls, input_value: str, /, _: core_schema.ValidationInfo) -> PaymentCardNumber:
"""Validate the card number and return a `PaymentCardNumber` instance."""
        return cls(input_value)

    @property
    defmasked(self) -> str:
"""Mask all but the last 4 digits of the card number.

        Returns:
            A masked card number string.
        """
        num_masked = len(self) - 10  # len(bin) + len(last4) == 10
        return f'{self.bin}{"*"*num_masked}{self.last4}'

    @classmethod
    defvalidate_digits(cls, card_number: str) -> None:
"""Validate that the card number is all digits."""
        if not card_number.isdigit():
            raise PydanticCustomError('payment_card_number_digits', 'Card number is not all digits')

    @classmethod
    defvalidate_luhn_check_digit(cls, card_number: str) -> str:
"""Based on: https://en.wikipedia.org/wiki/Luhn_algorithm."""
        sum_ = int(card_number[-1])
        length = len(card_number)
        parity = length % 2
        for i in range(length - 1):
            digit = int(card_number[i])
            if i % 2 == parity:
                digit *= 2
            if digit > 9:
                digit -= 9
            sum_ += digit
        valid = sum_ % 10 == 0
        if not valid:
            raise PydanticCustomError('payment_card_number_luhn', 'Card number is not luhn valid')
        return card_number

    @staticmethod
    defvalidate_brand(card_number: str) -> PaymentCardBrand:
"""Validate length based on BIN for major brands:
        https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN).
        """
        if card_number[0] == '4':
            brand = PaymentCardBrand.visa
        elif 51 <= int(card_number[:2]) <= 55:
            brand = PaymentCardBrand.mastercard
        elif card_number[:2] in {'34', '37'}:
            brand = PaymentCardBrand.amex
        else:
            brand = PaymentCardBrand.other

        required_length: None | int | str = None
        if brand in PaymentCardBrand.mastercard:
            required_length = 16
            valid = len(card_number) == required_length
        elif brand == PaymentCardBrand.visa:
            required_length = '13, 16 or 19'
            valid = len(card_number) in {13, 16, 19}
        elif brand == PaymentCardBrand.amex:
            required_length = 15
            valid = len(card_number) == required_length
        else:
            valid = True

        if not valid:
            raise PydanticCustomError(
                'payment_card_number_brand',
                'Length for a {brand} card must be {required_length}',
                {'brand': brand, 'required_length': required_length},
            )
        return brand

```
  
---|---  
####  masked `property` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.masked)
```
masked: 
```

Mask all but the last 4 digits of the card number.
Returns:
Type | Description  
---|---  
|  A masked card number string.  
####  validate `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate)
```
validate(
    input_value: , /, _: ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)
) -> PaymentCardNumber[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber)

```

Validate the card number and return a `PaymentCardNumber` instance.
Source code in `pydantic/types.py`
```
1947
1948
1949
1950
```
| ```
@classmethod
defvalidate(cls, input_value: str, /, _: core_schema.ValidationInfo) -> PaymentCardNumber:
"""Validate the card number and return a `PaymentCardNumber` instance."""
    return cls(input_value)

```
  
---|---  
####  validate_digits `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate_digits)
```
validate_digits(card_number: ) -> None

```

Validate that the card number is all digits.
Source code in `pydantic/types.py`
```
1962
1963
1964
1965
1966
```
| ```
@classmethod
defvalidate_digits(cls, card_number: str) -> None:
"""Validate that the card number is all digits."""
    if not card_number.isdigit():
        raise PydanticCustomError('payment_card_number_digits', 'Card number is not all digits')

```
  
---|---  
####  validate_luhn_check_digit `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate_luhn_check_digit)
```
validate_luhn_check_digit(card_number: ) -> 
```

Based on: https://en.wikipedia.org/wiki/Luhn_algorithm.
Source code in `pydantic/types.py`
```
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
```
| ```
@classmethod
defvalidate_luhn_check_digit(cls, card_number: str) -> str:
"""Based on: https://en.wikipedia.org/wiki/Luhn_algorithm."""
    sum_ = int(card_number[-1])
    length = len(card_number)
    parity = length % 2
    for i in range(length - 1):
        digit = int(card_number[i])
        if i % 2 == parity:
            digit *= 2
        if digit > 9:
            digit -= 9
        sum_ += digit
    valid = sum_ % 10 == 0
    if not valid:
        raise PydanticCustomError('payment_card_number_luhn', 'Card number is not luhn valid')
    return card_number

```
  
---|---  
####  validate_brand `staticmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate_brand)
```
validate_brand(card_number: ) -> PaymentCardBrand

```

Validate length based on BIN for major brands: https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN).
Source code in `pydantic/types.py`
```
1986
1987
1988
1989
1990
1991
1992
1993
1994
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
2005
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
2016
2017
2018
2019
```
| ```
@staticmethod
defvalidate_brand(card_number: str) -> PaymentCardBrand:
"""Validate length based on BIN for major brands:
    https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN).
    """
    if card_number[0] == '4':
        brand = PaymentCardBrand.visa
    elif 51 <= int(card_number[:2]) <= 55:
        brand = PaymentCardBrand.mastercard
    elif card_number[:2] in {'34', '37'}:
        brand = PaymentCardBrand.amex
    else:
        brand = PaymentCardBrand.other

    required_length: None | int | str = None
    if brand in PaymentCardBrand.mastercard:
        required_length = 16
        valid = len(card_number) == required_length
    elif brand == PaymentCardBrand.visa:
        required_length = '13, 16 or 19'
        valid = len(card_number) in {13, 16, 19}
    elif brand == PaymentCardBrand.amex:
        required_length = 15
        valid = len(card_number) == required_length
    else:
        valid = True

    if not valid:
        raise PydanticCustomError(
            'payment_card_number_brand',
            'Length for a {brand} card must be {required_length}',
            {'brand': brand, 'required_length': required_length},
        )
    return brand

```
  
---|---  
###  ByteSize [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize)
Bases: 
Converts a string representing a number of bytes with units (such as `'1KB'` or `'11.5MiB'`) into an integer.
You can use the `ByteSize` data type to (case-insensitively) convert a string representation of a number of bytes into an integer, and also to print out human-readable strings representing a number of bytes.
In conformance with `'1KB'` to mean 1000 bytes, and `'1KiB'` to mean 1024 bytes. In general, including a middle `'i'` will cause the unit to be interpreted as a power of 2, rather than a power of 10 (so, for example, `'1 MB'` is treated as `1_000_000` bytes, whereas `'1 MiB'` is treated as `1_048_576` bytes).
Info
Note that `1b` will be parsed as "1 byte" and not "1 bit".
```
frompydanticimport BaseModel, ByteSize

classMyModel(BaseModel):
    size: ByteSize

print(MyModel(size=52000).size)
#> 52000
print(MyModel(size='3000 KiB').size)
#> 3072000

m = MyModel(size='50 PB')
print(m.size.human_readable())
#> 44.4PiB
print(m.size.human_readable(decimal=True))
#> 50.0PB
print(m.size.human_readable(separator=' '))
#> 44.4 PiB

print(m.size.to('TiB'))
#> 45474.73508864641

```

Source code in `pydantic/types.py`
```
2025
2026
2027
2028
2029
2030
2031
2032
2033
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
2046
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
2060
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
2071
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
2089
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
2102
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
2127
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
2143
2144
2145
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
2156
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
```
| ```
classByteSize(int):
"""Converts a string representing a number of bytes with units (such as `'1KB'` or `'11.5MiB'`) into an integer.

    You can use the `ByteSize` data type to (case-insensitively) convert a string representation of a number of bytes into
    an integer, and also to print out human-readable strings representing a number of bytes.

    In conformance with [IEC 80000-13 Standard](https://en.wikipedia.org/wiki/ISO/IEC_80000) we interpret `'1KB'` to mean 1000 bytes,
    and `'1KiB'` to mean 1024 bytes. In general, including a middle `'i'` will cause the unit to be interpreted as a power of 2,
    rather than a power of 10 (so, for example, `'1 MB'` is treated as `1_000_000` bytes, whereas `'1 MiB'` is treated as `1_048_576` bytes).

    !!! info
        Note that `1b` will be parsed as "1 byte" and not "1 bit".

```python
    from pydantic import BaseModel, ByteSize

    class MyModel(BaseModel):
        size: ByteSize

    print(MyModel(size=52000).size)
    #> 52000
    print(MyModel(size='3000 KiB').size)
    #> 3072000

    m = MyModel(size='50 PB')
    print(m.size.human_readable())
    #> 44.4PiB
    print(m.size.human_readable(decimal=True))
    #> 50.0PB
    print(m.size.human_readable(separator=' '))
    #> 44.4 PiB

    print(m.size.to('TiB'))
    #> 45474.73508864641
```
    """

    byte_sizes = {
        'b': 1,
        'kb': 10**3,
        'mb': 10**6,
        'gb': 10**9,
        'tb': 10**12,
        'pb': 10**15,
        'eb': 10**18,
        'kib': 2**10,
        'mib': 2**20,
        'gib': 2**30,
        'tib': 2**40,
        'pib': 2**50,
        'eib': 2**60,
        'bit': 1 / 8,
        'kbit': 10**3 / 8,
        'mbit': 10**6 / 8,
        'gbit': 10**9 / 8,
        'tbit': 10**12 / 8,
        'pbit': 10**15 / 8,
        'ebit': 10**18 / 8,
        'kibit': 2**10 / 8,
        'mibit': 2**20 / 8,
        'gibit': 2**30 / 8,
        'tibit': 2**40 / 8,
        'pibit': 2**50 / 8,
        'eibit': 2**60 / 8,
    }
    byte_sizes.update({k.lower()[0]: v for k, v in byte_sizes.items() if 'i' not in k})

    byte_string_pattern = r'^\s*(\d*\.?\d+)\s*(\w+)?'
    byte_string_re = re.compile(byte_string_pattern, re.IGNORECASE)

    @classmethod
    def__get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.with_info_after_validator_function(
            function=cls._validate,
            schema=core_schema.union_schema(
                [
                    core_schema.str_schema(pattern=cls.byte_string_pattern),
                    core_schema.int_schema(ge=0),
                ],
                custom_error_type='byte_size',
                custom_error_message='could not parse value and unit from byte string',
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                int, return_schema=core_schema.int_schema(ge=0)
            ),
        )

    @classmethod
    def_validate(cls, input_value: Any, /, _: core_schema.ValidationInfo) -> ByteSize:
        try:
            return cls(int(input_value))
        except ValueError:
            pass

        str_match = cls.byte_string_re.match(str(input_value))
        if str_match is None:
            raise PydanticCustomError('byte_size', 'could not parse value and unit from byte string')

        scalar, unit = str_match.groups()
        if unit is None:
            unit = 'b'

        try:
            unit_mult = cls.byte_sizes[unit.lower()]
        except KeyError:
            raise PydanticCustomError('byte_size_unit', 'could not interpret byte unit: {unit}', {'unit': unit})

        return cls(int(float(scalar) * unit_mult))

    defhuman_readable(self, decimal: bool = False, separator: str = '') -> str:
"""Converts a byte size to a human readable string.

        Args:
            decimal: If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units
                (e.g. 1024 bytes per KiB).
            separator: A string used to split the value and unit. Defaults to an empty string ('').

        Returns:
            A human readable string representation of the byte size.
        """
        if decimal:
            divisor = 1000
            units = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
            final_unit = 'EB'
        else:
            divisor = 1024
            units = 'B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB'
            final_unit = 'EiB'

        num = float(self)
        for unit in units:
            if abs(num) < divisor:
                if unit == 'B':
                    return f'{num:0.0f}{separator}{unit}'
                else:
                    return f'{num:0.1f}{separator}{unit}'
            num /= divisor

        return f'{num:0.1f}{separator}{final_unit}'

    defto(self, unit: str) -> float:
"""Converts a byte size to another unit, including both byte and bit units.

        Args:
            unit: The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB,
                KiB, MiB, GiB, TiB, PiB, EiB (byte units) and
                bit, kbit, mbit, gbit, tbit, pbit, ebit,
                kibit, mibit, gibit, tibit, pibit, eibit (bit units).

        Returns:
            The byte size in the new unit.
        """
        try:
            unit_div = self.byte_sizes[unit.lower()]
        except KeyError:
            raise PydanticCustomError('byte_size_unit', 'Could not interpret byte unit: {unit}', {'unit': unit})

        return self / unit_div

```
  
---|---  
####  human_readable [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize.human_readable)
```
human_readable(
    decimal: = False, separator: = ""
) -> 
```

Converts a byte size to a human readable string.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`decimal` |  |  If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units (e.g. 1024 bytes per KiB). |  `False`  
`separator` |  |  A string used to split the value and unit. Defaults to an empty string (''). |  `''`  
Returns:
Type | Description  
---|---  
|  A human readable string representation of the byte size.  
Source code in `pydantic/types.py`
```
2134
2135
2136
2137
2138
2139
2140
2141
2142
2143
2144
2145
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
2156
2157
2158
2159
2160
2161
2162
2163
```
| ```
defhuman_readable(self, decimal: bool = False, separator: str = '') -> str:
"""Converts a byte size to a human readable string.

    Args:
        decimal: If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units
            (e.g. 1024 bytes per KiB).
        separator: A string used to split the value and unit. Defaults to an empty string ('').

    Returns:
        A human readable string representation of the byte size.
    """
    if decimal:
        divisor = 1000
        units = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
        final_unit = 'EB'
    else:
        divisor = 1024
        units = 'B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB'
        final_unit = 'EiB'

    num = float(self)
    for unit in units:
        if abs(num) < divisor:
            if unit == 'B':
                return f'{num:0.0f}{separator}{unit}'
            else:
                return f'{num:0.1f}{separator}{unit}'
        num /= divisor

    return f'{num:0.1f}{separator}{final_unit}'

```
  
---|---  
####  to [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize.to)
```
to(unit: ) -> 
```

Converts a byte size to another unit, including both byte and bit units.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`unit` |  |  The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB, KiB, MiB, GiB, TiB, PiB, EiB (byte units) and bit, kbit, mbit, gbit, tbit, pbit, ebit, kibit, mibit, gibit, tibit, pibit, eibit (bit units). |  _required_  
Returns:
Type | Description  
---|---  
|  The byte size in the new unit.  
Source code in `pydantic/types.py`
```
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
```
| ```
defto(self, unit: str) -> float:
"""Converts a byte size to another unit, including both byte and bit units.

    Args:
        unit: The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB,
            KiB, MiB, GiB, TiB, PiB, EiB (byte units) and
            bit, kbit, mbit, gbit, tbit, pbit, ebit,
            kibit, mibit, gibit, tibit, pibit, eibit (bit units).

    Returns:
        The byte size in the new unit.
    """
    try:
        unit_div = self.byte_sizes[unit.lower()]
    except KeyError:
        raise PydanticCustomError('byte_size_unit', 'Could not interpret byte unit: {unit}', {'unit': unit})

    return self / unit_div

```
  
---|---  
###  PastDate [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PastDate)
A date in the past.
Source code in `pydantic/types.py`
```
2198
2199
2200
2201
2202
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
```
| ```
classPastDate:
"""A date in the past."""

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.date_schema(now_op='past')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'date', cls.__name__)
            schema['now_op'] = 'past'
            return schema

    def__repr__(self) -> str:
        return 'PastDate'

```
  
---|---  
###  FutureDate [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FutureDate)
A date in the future.
Source code in `pydantic/types.py`
```
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
```
| ```
classFutureDate:
"""A date in the future."""

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.date_schema(now_op='future')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'date', cls.__name__)
            schema['now_op'] = 'future'
            return schema

    def__repr__(self) -> str:
        return 'FutureDate'

```
  
---|---  
###  AwareDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AwareDatetime)
A datetime that requires timezone info.
Source code in `pydantic/types.py`
```
2274
2275
2276
2277
2278
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
```
| ```
classAwareDatetime:
"""A datetime that requires timezone info."""

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(tz_constraint='aware')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['tz_constraint'] = 'aware'
            return schema

    def__repr__(self) -> str:
        return 'AwareDatetime'

```
  
---|---  
###  NaiveDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NaiveDatetime)
A datetime that doesn't require timezone info.
Source code in `pydantic/types.py`
```
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
2305
2306
2307
2308
2309
2310
```
| ```
classNaiveDatetime:
"""A datetime that doesn't require timezone info."""

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(tz_constraint='naive')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['tz_constraint'] = 'naive'
            return schema

    def__repr__(self) -> str:
        return 'NaiveDatetime'

```
  
---|---  
###  PastDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PastDatetime)
A datetime that must be in the past.
Source code in `pydantic/types.py`
```
2312
2313
2314
2315
2316
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
```
| ```
classPastDatetime:
"""A datetime that must be in the past."""

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(now_op='past')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['now_op'] = 'past'
            return schema

    def__repr__(self) -> str:
        return 'PastDatetime'

```
  
---|---  
###  FutureDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FutureDatetime)
A datetime that must be in the future.
Source code in `pydantic/types.py`
```
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
2345
2346
2347
2348
```
| ```
classFutureDatetime:
"""A datetime that must be in the future."""

    @classmethod
    def__get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(now_op='future')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['now_op'] = 'future'
            return schema

    def__repr__(self) -> str:
        return 'FutureDatetime'

```
  
---|---  
###  EncoderProtocol [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol)
Bases: 
Protocol for encoding and decoding data to and from bytes.
Source code in `pydantic/types.py`
```
2354
2355
2356
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
2368
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
2380
2381
2382
2383
2384
2385
2386
2387
2388
```
| ```
classEncoderProtocol(Protocol):
"""Protocol for encoding and decoding data to and from bytes."""

    @classmethod
    defdecode(cls, data: bytes) -> bytes:
"""Decode the data using the encoder.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        ...

    @classmethod
    defencode(cls, value: bytes) -> bytes:
"""Encode the data using the encoder.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        ...

    @classmethod
    defget_json_format(cls) -> str:
"""Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        ...

```
  
---|---  
####  decode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol.decode)
```
decode(data: ) -> 
```

Decode the data using the encoder.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`data` |  |  The data to decode. |  _required_  
Returns:
Type | Description  
---|---  
|  The decoded data.  
Source code in `pydantic/types.py`
```
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
```
| ```
@classmethod
defdecode(cls, data: bytes) -> bytes:
"""Decode the data using the encoder.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    ...

```
  
---|---  
####  encode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol.encode)
```
encode(value: ) -> 
```

Encode the data using the encoder.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The data to encode. |  _required_  
Returns:
Type | Description  
---|---  
|  The encoded data.  
Source code in `pydantic/types.py`
```
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
```
| ```
@classmethod
defencode(cls, value: bytes) -> bytes:
"""Encode the data using the encoder.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    ...

```
  
---|---  
####  get_json_format `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol.get_json_format)
```
get_json_format() -> 
```

Get the JSON format for the encoded data.
Returns:
Type | Description  
---|---  
|  The JSON format for the encoded data.  
Source code in `pydantic/types.py`
```
2381
2382
2383
2384
2385
2386
2387
2388
```
| ```
@classmethod
defget_json_format(cls) -> str:
"""Get the JSON format for the encoded data.

    Returns:
        The JSON format for the encoded data.
    """
    ...

```
  
---|---  
###  Base64Encoder [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder)
Bases: `EncoderProtocol[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol)`
Standard (non-URL-safe) Base64 encoder.
Source code in `pydantic/types.py`
```
2391
2392
2393
2394
2395
2396
2397
2398
2399
2400
2401
2402
2403
2404
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
```
| ```
classBase64Encoder(EncoderProtocol):
"""Standard (non-URL-safe) Base64 encoder."""

    @classmethod
    defdecode(cls, data: bytes) -> bytes:
"""Decode the data from base64 encoded bytes to original bytes data.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        try:
            return base64.b64decode(data)
        except ValueError as e:
            raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

    @classmethod
    defencode(cls, value: bytes) -> bytes:
"""Encode the data from bytes to a base64 encoded bytes.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return base64.b64encode(value)

    @classmethod
    defget_json_format(cls) -> Literal['base64']:
"""Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        return 'base64'

```
  
---|---  
####  decode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder.decode)
```
decode(data: ) -> 
```

Decode the data from base64 encoded bytes to original bytes data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`data` |  |  The data to decode. |  _required_  
Returns:
Type | Description  
---|---  
|  The decoded data.  
Source code in `pydantic/types.py`
```
2394
2395
2396
2397
2398
2399
2400
2401
2402
2403
2404
2405
2406
2407
```
| ```
@classmethod
defdecode(cls, data: bytes) -> bytes:
"""Decode the data from base64 encoded bytes to original bytes data.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    try:
        return base64.b64decode(data)
    except ValueError as e:
        raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

```
  
---|---  
####  encode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder.encode)
```
encode(value: ) -> 
```

Encode the data from bytes to a base64 encoded bytes.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The data to encode. |  _required_  
Returns:
Type | Description  
---|---  
|  The encoded data.  
Source code in `pydantic/types.py`
```
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
```
| ```
@classmethod
defencode(cls, value: bytes) -> bytes:
"""Encode the data from bytes to a base64 encoded bytes.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return base64.b64encode(value)

```
  
---|---  
####  get_json_format `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder.get_json_format)
```
get_json_format() -> ['base64']

```

Get the JSON format for the encoded data.
Returns:
Type | Description  
---|---  
|  The JSON format for the encoded data.  
Source code in `pydantic/types.py`
```
2421
2422
2423
2424
2425
2426
2427
2428
```
| ```
@classmethod
defget_json_format(cls) -> Literal['base64']:
"""Get the JSON format for the encoded data.

    Returns:
        The JSON format for the encoded data.
    """
    return 'base64'

```
  
---|---  
###  Base64UrlEncoder [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder)
Bases: `EncoderProtocol[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol)`
URL-safe Base64 encoder.
Source code in `pydantic/types.py`
```
2431
2432
2433
2434
2435
2436
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
2448
2449
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
```
| ```
classBase64UrlEncoder(EncoderProtocol):
"""URL-safe Base64 encoder."""

    @classmethod
    defdecode(cls, data: bytes) -> bytes:
"""Decode the data from base64 encoded bytes to original bytes data.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        try:
            return base64.urlsafe_b64decode(data)
        except ValueError as e:
            raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

    @classmethod
    defencode(cls, value: bytes) -> bytes:
"""Encode the data from bytes to a base64 encoded bytes.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return base64.urlsafe_b64encode(value)

    @classmethod
    defget_json_format(cls) -> Literal['base64url']:
"""Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        return 'base64url'

```
  
---|---  
####  decode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder.decode)
```
decode(data: ) -> 
```

Decode the data from base64 encoded bytes to original bytes data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`data` |  |  The data to decode. |  _required_  
Returns:
Type | Description  
---|---  
|  The decoded data.  
Source code in `pydantic/types.py`
```
2434
2435
2436
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
```
| ```
@classmethod
defdecode(cls, data: bytes) -> bytes:
"""Decode the data from base64 encoded bytes to original bytes data.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    try:
        return base64.urlsafe_b64decode(data)
    except ValueError as e:
        raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

```
  
---|---  
####  encode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder.encode)
```
encode(value: ) -> 
```

Encode the data from bytes to a base64 encoded bytes.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The data to encode. |  _required_  
Returns:
Type | Description  
---|---  
|  The encoded data.  
Source code in `pydantic/types.py`
```
2449
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
```
| ```
@classmethod
defencode(cls, value: bytes) -> bytes:
"""Encode the data from bytes to a base64 encoded bytes.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return base64.urlsafe_b64encode(value)

```
  
---|---  
####  get_json_format `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder.get_json_format)
```
get_json_format() -> ['base64url']

```

Get the JSON format for the encoded data.
Returns:
Type | Description  
---|---  
|  The JSON format for the encoded data.  
Source code in `pydantic/types.py`
```
2461
2462
2463
2464
2465
2466
2467
2468
```
| ```
@classmethod
defget_json_format(cls) -> Literal['base64url']:
"""Get the JSON format for the encoded data.

    Returns:
        The JSON format for the encoded data.
    """
    return 'base64url'

```
  
---|---  
###  EncodedBytes `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes)
A bytes type that is encoded and decoded using the specified encoder.
`EncodedBytes` needs an encoder that implements `EncoderProtocol` to operate.
```
fromtypingimport Annotated

frompydanticimport BaseModel, EncodedBytes, EncoderProtocol, ValidationError

classMyEncoder(EncoderProtocol):
    @classmethod
    defdecode(cls, data: bytes) -> bytes:
        if data == b'**undecodable**':
            raise ValueError('Cannot decode data')
        return data[13:]

    @classmethod
    defencode(cls, value: bytes) -> bytes:
        return b'**encoded**: ' + value

    @classmethod
    defget_json_format(cls) -> str:
        return 'my-encoder'

MyEncodedBytes = Annotated[bytes, EncodedBytes(encoder=MyEncoder)]

classModel(BaseModel):
    my_encoded_bytes: MyEncodedBytes

# Initialize the model with encoded data
m = Model(my_encoded_bytes=b'**encoded**: some bytes')

# Access decoded value
print(m.my_encoded_bytes)
#> b'some bytes'

# Serialize into the encoded form
print(m.model_dump())
#> {'my_encoded_bytes': b'**encoded**: some bytes'}

# Validate encoded data
try:
    Model(my_encoded_bytes=b'**undecodable**')
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    my_encoded_bytes
      Value error, Cannot decode data [type=value_error, input_value=b'**undecodable**', input_type=bytes]
    '''

```

Source code in `pydantic/types.py`
```
2471
2472
2473
2474
2475
2476
2477
2478
2479
2480
2481
2482
2483
2484
2485
2486
2487
2488
2489
2490
2491
2492
2493
2494
2495
2496
2497
2498
2499
2500
2501
2502
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
2549
2550
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
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
classEncodedBytes:
"""A bytes type that is encoded and decoded using the specified encoder.

    `EncodedBytes` needs an encoder that implements `EncoderProtocol` to operate.

```python
    from typing import Annotated

    from pydantic import BaseModel, EncodedBytes, EncoderProtocol, ValidationError

    class MyEncoder(EncoderProtocol):
        @classmethod
        def decode(cls, data: bytes) -> bytes:
            if data == b'**undecodable**':
                raise ValueError('Cannot decode data')
            return data[13:]

        @classmethod
        def encode(cls, value: bytes) -> bytes:
            return b'**encoded**: ' + value

        @classmethod
        def get_json_format(cls) -> str:
            return 'my-encoder'

    MyEncodedBytes = Annotated[bytes, EncodedBytes(encoder=MyEncoder)]

    class Model(BaseModel):
        my_encoded_bytes: MyEncodedBytes

    # Initialize the model with encoded data
    m = Model(my_encoded_bytes=b'**encoded**: some bytes')

    # Access decoded value
    print(m.my_encoded_bytes)
    #> b'some bytes'

    # Serialize into the encoded form
    print(m.model_dump())
    #> {'my_encoded_bytes': b'**encoded**: some bytes'}

    # Validate encoded data
    try:
        Model(my_encoded_bytes=b'**undecodable**')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Model
        my_encoded_bytes
          Value error, Cannot decode data [type=value_error, input_value=b'**undecodable**', input_type=bytes]
        '''
```
    """

    encoder: type[EncoderProtocol]

    def__get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(type='string', format=self.encoder.get_json_format())
        return field_schema

    def__get_pydantic_core_schema__(self, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        schema = handler(source)
        _check_annotated_type(schema['type'], 'bytes', self.__class__.__name__)
        return core_schema.with_info_after_validator_function(
            function=self.decode,
            schema=schema,
            serialization=core_schema.plain_serializer_function_ser_schema(function=self.encode),
        )

    defdecode(self, data: bytes, _: core_schema.ValidationInfo) -> bytes:
"""Decode the data using the specified encoder.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        return self.encoder.decode(data)

    defencode(self, value: bytes) -> bytes:
"""Encode the data using the specified encoder.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return self.encoder.encode(value)

    def__hash__(self) -> int:
        return hash(self.encoder)

```
  
---|---  
####  decode [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes.decode)
```
decode(data: , _: ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)) -> 
```

Decode the data using the specified encoder.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`data` |  |  The data to decode. |  _required_  
Returns:
Type | Description  
---|---  
|  The decoded data.  
Source code in `pydantic/types.py`
```
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
```
| ```
defdecode(self, data: bytes, _: core_schema.ValidationInfo) -> bytes:
"""Decode the data using the specified encoder.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    return self.encoder.decode(data)

```
  
---|---  
####  encode [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes.encode)
```
encode(value: ) -> 
```

Encode the data using the specified encoder.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The data to encode. |  _required_  
Returns:
Type | Description  
---|---  
|  The encoded data.  
Source code in `pydantic/types.py`
```
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
```
| ```
defencode(self, value: bytes) -> bytes:
"""Encode the data using the specified encoder.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return self.encoder.encode(value)

```
  
---|---  
###  EncodedStr `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr)
A str type that is encoded and decoded using the specified encoder.
`EncodedStr` needs an encoder that implements `EncoderProtocol` to operate.
```
fromtypingimport Annotated

frompydanticimport BaseModel, EncodedStr, EncoderProtocol, ValidationError

classMyEncoder(EncoderProtocol):
    @classmethod
    defdecode(cls, data: bytes) -> bytes:
        if data == b'**undecodable**':
            raise ValueError('Cannot decode data')
        return data[13:]

    @classmethod
    defencode(cls, value: bytes) -> bytes:
        return b'**encoded**: ' + value

    @classmethod
    defget_json_format(cls) -> str:
        return 'my-encoder'

MyEncodedStr = Annotated[str, EncodedStr(encoder=MyEncoder)]

classModel(BaseModel):
    my_encoded_str: MyEncodedStr

# Initialize the model with encoded data
m = Model(my_encoded_str='**encoded**: some str')

# Access decoded value
print(m.my_encoded_str)
#> some str

# Serialize into the encoded form
print(m.model_dump())
#> {'my_encoded_str': '**encoded**: some str'}

# Validate encoded data
try:
    Model(my_encoded_str='**undecodable**')
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    my_encoded_str
      Value error, Cannot decode data [type=value_error, input_value='**undecodable**', input_type=str]
    '''

```

Source code in `pydantic/types.py`
```
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
2606
2607
2608
2609
2610
2611
2612
2613
2614
2615
2616
2617
2618
2619
2620
2621
2622
2623
2624
2625
2626
2627
2628
2629
2630
2631
2632
2633
2634
2635
2636
2637
2638
2639
2640
2641
2642
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
2653
2654
2655
2656
2657
2658
2659
2660
2661
2662
2663
2664
2665
2666
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
classEncodedStr:
"""A str type that is encoded and decoded using the specified encoder.

    `EncodedStr` needs an encoder that implements `EncoderProtocol` to operate.

```python
    from typing import Annotated

    from pydantic import BaseModel, EncodedStr, EncoderProtocol, ValidationError

    class MyEncoder(EncoderProtocol):
        @classmethod
        def decode(cls, data: bytes) -> bytes:
            if data == b'**undecodable**':
                raise ValueError('Cannot decode data')
            return data[13:]

        @classmethod
        def encode(cls, value: bytes) -> bytes:
            return b'**encoded**: ' + value

        @classmethod
        def get_json_format(cls) -> str:
            return 'my-encoder'

    MyEncodedStr = Annotated[str, EncodedStr(encoder=MyEncoder)]

    class Model(BaseModel):
        my_encoded_str: MyEncodedStr

    # Initialize the model with encoded data
    m = Model(my_encoded_str='**encoded**: some str')

    # Access decoded value
    print(m.my_encoded_str)
    #> some str

    # Serialize into the encoded form
    print(m.model_dump())
    #> {'my_encoded_str': '**encoded**: some str'}

    # Validate encoded data
    try:
        Model(my_encoded_str='**undecodable**')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Model
        my_encoded_str
          Value error, Cannot decode data [type=value_error, input_value='**undecodable**', input_type=str]
        '''
```
    """

    encoder: type[EncoderProtocol]

    def__get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(type='string', format=self.encoder.get_json_format())
        return field_schema

    def__get_pydantic_core_schema__(self, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        schema = handler(source)
        _check_annotated_type(schema['type'], 'str', self.__class__.__name__)
        return core_schema.with_info_after_validator_function(
            function=self.decode_str,
            schema=schema,
            serialization=core_schema.plain_serializer_function_ser_schema(function=self.encode_str),
        )

    defdecode_str(self, data: str, _: core_schema.ValidationInfo) -> str:
"""Decode the data using the specified encoder.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        return self.encoder.decode(data.encode()).decode()

    defencode_str(self, value: str) -> str:
"""Encode the data using the specified encoder.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return self.encoder.encode(value.encode()).decode()  # noqa: UP008

    def__hash__(self) -> int:
        return hash(self.encoder)

```
  
---|---  
####  decode_str [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr.decode_str)
```
decode_str(data: , _: ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)) -> 
```

Decode the data using the specified encoder.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`data` |  |  The data to decode. |  _required_  
Returns:
Type | Description  
---|---  
|  The decoded data.  
Source code in `pydantic/types.py`
```
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
```
| ```
defdecode_str(self, data: str, _: core_schema.ValidationInfo) -> str:
"""Decode the data using the specified encoder.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    return self.encoder.decode(data.encode()).decode()

```
  
---|---  
####  encode_str [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr.encode_str)
```
encode_str(value: ) -> 
```

Encode the data using the specified encoder.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`value` |  |  The data to encode. |  _required_  
Returns:
Type | Description  
---|---  
|  The encoded data.  
Source code in `pydantic/types.py`
```
2654
2655
2656
2657
2658
2659
2660
2661
2662
2663
```
| ```
defencode_str(self, value: str) -> str:
"""Encode the data using the specified encoder.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return self.encoder.encode(value.encode()).decode()  # noqa: UP008

```
  
---|---  
###  GetPydanticSchema `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.GetPydanticSchema)
Usage Documentation
[Using `GetPydanticSchema` to Reduce Boilerplate](https://docs.pydantic.dev/latest/concepts/types/#using-getpydanticschema-to-reduce-boilerplate)
A convenience class for creating an annotation that provides pydantic custom type hooks.
This class is intended to eliminate the need to create a custom "marker" which defines the `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__` custom hook methods.
For example, to have a field treated by type checkers as `int`, but by pydantic as `Any`, you can do: 
```
fromtypingimport Annotated, Any

frompydanticimport BaseModel, GetPydanticSchema

HandleAsAny = GetPydanticSchema(lambda _s, h: h(Any))

classModel(BaseModel):
    x: Annotated[int, HandleAsAny]  # pydantic sees `x: Any`

print(repr(Model(x='abc').x))
#> 'abc'

```

Source code in `pydantic/types.py`
```
2842
2843
2844
2845
2846
2847
2848
2849
2850
2851
2852
2853
2854
2855
2856
2857
2858
2859
2860
2861
2862
2863
2864
2865
2866
2867
2868
2869
2870
2871
2872
2873
2874
2875
2876
2877
2878
2879
2880
2881
2882
2883
2884
2885
2886
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
classGetPydanticSchema:
"""!!! abstract "Usage Documentation"
        [Using `GetPydanticSchema` to Reduce Boilerplate](../concepts/types.md#using-getpydanticschema-to-reduce-boilerplate)

    A convenience class for creating an annotation that provides pydantic custom type hooks.

    This class is intended to eliminate the need to create a custom "marker" which defines the
     `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__` custom hook methods.

    For example, to have a field treated by type checkers as `int`, but by pydantic as `Any`, you can do:
```python
    from typing import Annotated, Any

    from pydantic import BaseModel, GetPydanticSchema

    HandleAsAny = GetPydanticSchema(lambda _s, h: h(Any))

    class Model(BaseModel):
        x: Annotated[int, HandleAsAny]  # pydantic sees `x: Any`

    print(repr(Model(x='abc').x))
    #> 'abc'
```
    """

    get_pydantic_core_schema: Callable[[Any, GetCoreSchemaHandler], CoreSchema] | None = None
    get_pydantic_json_schema: Callable[[Any, GetJsonSchemaHandler], JsonSchemaValue] | None = None

    # Note: we may want to consider adding a convenience staticmethod `def for_type(type_: Any) -> GetPydanticSchema:`
    #   which returns `GetPydanticSchema(lambda _s, h: h(type_))`

    if not TYPE_CHECKING:
        # We put `__getattr__` in a non-TYPE_CHECKING block because otherwise, mypy allows arbitrary attribute access

        def__getattr__(self, item: str) -> Any:
"""Use this rather than defining `__get_pydantic_core_schema__` etc. to reduce the number of nested calls."""
            if item == '__get_pydantic_core_schema__' and self.get_pydantic_core_schema:
                return self.get_pydantic_core_schema
            elif item == '__get_pydantic_json_schema__' and self.get_pydantic_json_schema:
                return self.get_pydantic_json_schema
            else:
                return object.__getattribute__(self, item)

    __hash__ = object.__hash__

```
  
---|---  
###  Tag `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag)
Provides a way to specify the expected tag to use for a case of a (callable) discriminated union.
Also provides a way to label a union case in error messages.
When using a callable `Discriminator`, attach a `Tag` to each case in the `Union` to specify the tag that should be used to identify that case. For example, in the below example, the `Tag` is used to specify that if `get_discriminator_value` returns `'apple'`, the input should be validated as an `ApplePie`, and if it returns `'pumpkin'`, the input should be validated as a `PumpkinPie`.
The primary role of the `Tag` here is to map the return value from the callable `Discriminator` function to the appropriate member of the `Union` in question.
```
fromtypingimport Annotated, Any, Literal, Union

frompydanticimport BaseModel, Discriminator, Tag

classPie(BaseModel):
    time_to_cook: int
    num_ingredients: int

classApplePie(Pie):
    fruit: Literal['apple'] = 'apple'

classPumpkinPie(Pie):
    filling: Literal['pumpkin'] = 'pumpkin'

defget_discriminator_value(v: Any) -> str:
    if isinstance(v, dict):
        return v.get('fruit', v.get('filling'))
    return getattr(v, 'fruit', getattr(v, 'filling', None))

classThanksgivingDinner(BaseModel):
    dessert: Annotated[
        Union[
            Annotated[ApplePie, Tag('apple')],
            Annotated[PumpkinPie, Tag('pumpkin')],
        ],
        Discriminator(get_discriminator_value),
    ]

apple_variation = ThanksgivingDinner.model_validate(
    {'dessert': {'fruit': 'apple', 'time_to_cook': 60, 'num_ingredients': 8}}
)
print(repr(apple_variation))
'''
ThanksgivingDinner(dessert=ApplePie(time_to_cook=60, num_ingredients=8, fruit='apple'))
'''

pumpkin_variation = ThanksgivingDinner.model_validate(
    {
        'dessert': {
            'filling': 'pumpkin',
            'time_to_cook': 40,
            'num_ingredients': 6,
        }
    }
)
print(repr(pumpkin_variation))
'''
ThanksgivingDinner(dessert=PumpkinPie(time_to_cook=40, num_ingredients=6, filling='pumpkin'))
'''

```

Note
You must specify a `Tag` for every case in a `Tag` that is associated with a callable `Discriminator`. Failing to do so will result in a `PydanticUserError` with code [`callable-discriminator-no-tag`](https://docs.pydantic.dev/latest/errors/usage_errors/#callable-discriminator-no-tag).
See the [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) concepts docs for more details on how to use `Tag`s.
Source code in `pydantic/types.py`
```
2889
2890
2891
2892
2893
2894
2895
2896
2897
2898
2899
2900
2901
2902
2903
2904
2905
2906
2907
2908
2909
2910
2911
2912
2913
2914
2915
2916
2917
2918
2919
2920
2921
2922
2923
2924
2925
2926
2927
2928
2929
2930
2931
2932
2933
2934
2935
2936
2937
2938
2939
2940
2941
2942
2943
2944
2945
2946
2947
2948
2949
2950
2951
2952
2953
2954
2955
2956
2957
2958
2959
2960
2961
2962
2963
2964
2965
2966
2967
2968
2969
2970
2971
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true, frozen=True)
classTag:
"""Provides a way to specify the expected tag to use for a case of a (callable) discriminated union.

    Also provides a way to label a union case in error messages.

    When using a callable `Discriminator`, attach a `Tag` to each case in the `Union` to specify the tag that
    should be used to identify that case. For example, in the below example, the `Tag` is used to specify that
    if `get_discriminator_value` returns `'apple'`, the input should be validated as an `ApplePie`, and if it
    returns `'pumpkin'`, the input should be validated as a `PumpkinPie`.

    The primary role of the `Tag` here is to map the return value from the callable `Discriminator` function to
    the appropriate member of the `Union` in question.

```python
    from typing import Annotated, Any, Literal, Union

    from pydantic import BaseModel, Discriminator, Tag

    class Pie(BaseModel):
        time_to_cook: int
        num_ingredients: int

    class ApplePie(Pie):
        fruit: Literal['apple'] = 'apple'

    class PumpkinPie(Pie):
        filling: Literal['pumpkin'] = 'pumpkin'

    def get_discriminator_value(v: Any) -> str:
        if isinstance(v, dict):
            return v.get('fruit', v.get('filling'))
        return getattr(v, 'fruit', getattr(v, 'filling', None))

    class ThanksgivingDinner(BaseModel):
        dessert: Annotated[
            Union[
                Annotated[ApplePie, Tag('apple')],
                Annotated[PumpkinPie, Tag('pumpkin')],
            ],
            Discriminator(get_discriminator_value),
        ]

    apple_variation = ThanksgivingDinner.model_validate(
        {'dessert': {'fruit': 'apple', 'time_to_cook': 60, 'num_ingredients': 8}}
    )
    print(repr(apple_variation))
    '''
    ThanksgivingDinner(dessert=ApplePie(time_to_cook=60, num_ingredients=8, fruit='apple'))
    '''

    pumpkin_variation = ThanksgivingDinner.model_validate(
        {
            'dessert': {
                'filling': 'pumpkin',
                'time_to_cook': 40,
                'num_ingredients': 6,
            }
        }
    )
    print(repr(pumpkin_variation))
    '''
    ThanksgivingDinner(dessert=PumpkinPie(time_to_cook=40, num_ingredients=6, filling='pumpkin'))
    '''
```

    !!! note
        You must specify a `Tag` for every case in a `Tag` that is associated with a
        callable `Discriminator`. Failing to do so will result in a `PydanticUserError` with code
        [`callable-discriminator-no-tag`](../errors/usage_errors.md#callable-discriminator-no-tag).

    See the [Discriminated Unions] concepts docs for more details on how to use `Tag`s.

    [Discriminated Unions]: ../concepts/unions.md#discriminated-unions
    """

    tag: str

    def__get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        schema = handler(source_type)
        metadata = cast('CoreMetadata', schema.setdefault('metadata', {}))
        metadata['pydantic_internal_union_tag_key'] = self.tag
        return schema

```
  
---|---  
###  Discriminator `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator)
Usage Documentation
[Discriminated Unions with `Callable` `Discriminator`](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions-with-callable-discriminator)
Provides a way to use a custom callable as the way to extract the value of a union discriminator.
This allows you to get validation behavior like you'd get from `Field(discriminator=<field_name>)`, but without needing to have a single shared field across all the union choices. This also makes it possible to handle unions of models and primitive types with discriminated-union-style validation errors. Finally, this allows you to use a custom callable as the way to identify which member of a union a value belongs to, while still seeing all the performance benefits of a discriminated union.
Consider this example, which is much more performant with the use of `Discriminator` and thus a `TaggedUnion` than it would be as a normal `Union`.
```
fromtypingimport Annotated, Any, Literal, Union

frompydanticimport BaseModel, Discriminator, Tag

classPie(BaseModel):
    time_to_cook: int
    num_ingredients: int

classApplePie(Pie):
    fruit: Literal['apple'] = 'apple'

classPumpkinPie(Pie):
    filling: Literal['pumpkin'] = 'pumpkin'

defget_discriminator_value(v: Any) -> str:
    if isinstance(v, dict):
        return v.get('fruit', v.get('filling'))
    return getattr(v, 'fruit', getattr(v, 'filling', None))

classThanksgivingDinner(BaseModel):
    dessert: Annotated[
        Union[
            Annotated[ApplePie, Tag('apple')],
            Annotated[PumpkinPie, Tag('pumpkin')],
        ],
        Discriminator(get_discriminator_value),
    ]

apple_variation = ThanksgivingDinner.model_validate(
    {'dessert': {'fruit': 'apple', 'time_to_cook': 60, 'num_ingredients': 8}}
)
print(repr(apple_variation))
'''
ThanksgivingDinner(dessert=ApplePie(time_to_cook=60, num_ingredients=8, fruit='apple'))
'''

pumpkin_variation = ThanksgivingDinner.model_validate(
    {
        'dessert': {
            'filling': 'pumpkin',
            'time_to_cook': 40,
            'num_ingredients': 6,
        }
    }
)
print(repr(pumpkin_variation))
'''
ThanksgivingDinner(dessert=PumpkinPie(time_to_cook=40, num_ingredients=6, filling='pumpkin'))
'''

```

See the [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) concepts docs for more details on how to use `Discriminator`s.
Source code in `pydantic/types.py`
```
2974
2975
2976
2977
2978
2979
2980
2981
2982
2983
2984
2985
2986
2987
2988
2989
2990
2991
2992
2993
2994
2995
2996
2997
2998
2999
3000
3001
3002
3003
3004
3005
3006
3007
3008
3009
3010
3011
3012
3013
3014
3015
3016
3017
3018
3019
3020
3021
3022
3023
3024
3025
3026
3027
3028
3029
3030
3031
3032
3033
3034
3035
3036
3037
3038
3039
3040
3041
3042
3043
3044
3045
3046
3047
3048
3049
3050
3051
3052
3053
3054
3055
3056
3057
3058
3059
3060
3061
3062
3063
3064
3065
3066
3067
3068
3069
3070
3071
3072
3073
3074
3075
3076
3077
3078
3079
3080
3081
3082
3083
3084
3085
3086
3087
3088
3089
3090
3091
3092
3093
3094
3095
3096
3097
3098
3099
3100
3101
3102
3103
3104
3105
3106
3107
3108
3109
3110
3111
3112
3113
3114
3115
3116
3117
3118
3119
3120
3121
3122
3123
3124
3125
3126
3127
3128
3129
3130
3131
3132
3133
3134
3135
3136
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true, frozen=True)
classDiscriminator:
"""!!! abstract "Usage Documentation"
        [Discriminated Unions with `Callable` `Discriminator`](../concepts/unions.md#discriminated-unions-with-callable-discriminator)

    Provides a way to use a custom callable as the way to extract the value of a union discriminator.

    This allows you to get validation behavior like you'd get from `Field(discriminator=<field_name>)`,
    but without needing to have a single shared field across all the union choices. This also makes it
    possible to handle unions of models and primitive types with discriminated-union-style validation errors.
    Finally, this allows you to use a custom callable as the way to identify which member of a union a value
    belongs to, while still seeing all the performance benefits of a discriminated union.

    Consider this example, which is much more performant with the use of `Discriminator` and thus a `TaggedUnion`
    than it would be as a normal `Union`.

```python
    from typing import Annotated, Any, Literal, Union

    from pydantic import BaseModel, Discriminator, Tag

    class Pie(BaseModel):
        time_to_cook: int
        num_ingredients: int

    class ApplePie(Pie):
        fruit: Literal['apple'] = 'apple'

    class PumpkinPie(Pie):
        filling: Literal['pumpkin'] = 'pumpkin'

    def get_discriminator_value(v: Any) -> str:
        if isinstance(v, dict):
            return v.get('fruit', v.get('filling'))
        return getattr(v, 'fruit', getattr(v, 'filling', None))

    class ThanksgivingDinner(BaseModel):
        dessert: Annotated[
            Union[
                Annotated[ApplePie, Tag('apple')],
                Annotated[PumpkinPie, Tag('pumpkin')],
            ],
            Discriminator(get_discriminator_value),
        ]

    apple_variation = ThanksgivingDinner.model_validate(
        {'dessert': {'fruit': 'apple', 'time_to_cook': 60, 'num_ingredients': 8}}
    )
    print(repr(apple_variation))
    '''
    ThanksgivingDinner(dessert=ApplePie(time_to_cook=60, num_ingredients=8, fruit='apple'))
    '''

    pumpkin_variation = ThanksgivingDinner.model_validate(
        {
            'dessert': {
                'filling': 'pumpkin',
                'time_to_cook': 40,
                'num_ingredients': 6,
            }
        }
    )
    print(repr(pumpkin_variation))
    '''
    ThanksgivingDinner(dessert=PumpkinPie(time_to_cook=40, num_ingredients=6, filling='pumpkin'))
    '''
```

    See the [Discriminated Unions] concepts docs for more details on how to use `Discriminator`s.

    [Discriminated Unions]: ../concepts/unions.md#discriminated-unions
    """

    discriminator: str | Callable[[Any], Hashable]
"""The callable or field name for discriminating the type in a tagged union.

    A `Callable` discriminator must extract the value of the discriminator from the input.
    A `str` discriminator must be the name of a field to discriminate against.
    """
    custom_error_type: str | None = None
"""Type to use in [custom errors](../errors/errors.md) replacing the standard discriminated union
    validation errors.
    """
    custom_error_message: str | None = None
"""Message to use in custom errors."""
    custom_error_context: dict[str, int | str | float] | None = None
"""Context to use in custom errors."""

    def__get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        if not is_union_origin(get_origin(source_type)):
            raise TypeError(f'{type(self).__name__} must be used with a Union type, not {source_type}')

        if isinstance(self.discriminator, str):
            frompydanticimport Field

            return handler(Annotated[source_type, Field(discriminator=self.discriminator)])
        else:
            original_schema = handler(source_type)
            return self._convert_schema(original_schema, handler)

    def_convert_schema(
        self, original_schema: core_schema.CoreSchema, handler: GetCoreSchemaHandler | None = None
    ) -> core_schema.TaggedUnionSchema:
        if original_schema['type'] != 'union':
            # This likely indicates that the schema was a single-item union that was simplified.
            # In this case, we do the same thing we do in
            # `pydantic._internal._discriminated_union._ApplyInferredDiscriminator._apply_to_root`, namely,
            # package the generated schema back into a single-item union.
            original_schema = core_schema.union_schema([original_schema])

        tagged_union_choices = {}
        for choice in original_schema['choices']:
            tag = None
            if isinstance(choice, tuple):
                choice, tag = choice
            metadata = cast('CoreMetadata | None', choice.get('metadata'))
            if metadata is not None:
                tag = metadata.get('pydantic_internal_union_tag_key') or tag
            if tag is None:
                # `handler` is None when this method is called from `apply_discriminator()` (deferred discriminators)
                if handler is not None and choice['type'] == 'definition-ref':
                    # If choice was built from a PEP 695 type alias, try to resolve the def:
                    try:
                        choice = handler.resolve_ref_schema(choice)
                    except LookupError:
                        pass
                    else:
                        metadata = cast('CoreMetadata | None', choice.get('metadata'))
                        if metadata is not None:
                            tag = metadata.get('pydantic_internal_union_tag_key')

                if tag is None:
                    raise PydanticUserError(
                        f'`Tag` not provided for choice {choice} used with `Discriminator`',
                        code='callable-discriminator-no-tag',
                    )
            tagged_union_choices[tag] = choice

        # Have to do these verbose checks to ensure falsy values ('' and {}) don't get ignored
        custom_error_type = self.custom_error_type
        if custom_error_type is None:
            custom_error_type = original_schema.get('custom_error_type')

        custom_error_message = self.custom_error_message
        if custom_error_message is None:
            custom_error_message = original_schema.get('custom_error_message')

        custom_error_context = self.custom_error_context
        if custom_error_context is None:
            custom_error_context = original_schema.get('custom_error_context')

        custom_error_type = original_schema.get('custom_error_type') if custom_error_type is None else custom_error_type
        return core_schema.tagged_union_schema(
            tagged_union_choices,
            self.discriminator,
            custom_error_type=custom_error_type,
            custom_error_message=custom_error_message,
            custom_error_context=custom_error_context,
            strict=original_schema.get('strict'),
            ref=original_schema.get('ref'),
            metadata=original_schema.get('metadata'),
            serialization=original_schema.get('serialization'),
        )

```
  
---|---  
####  discriminator `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.discriminator)
```
discriminator: | [[], ]

```

The callable or field name for discriminating the type in a tagged union.
A `Callable` discriminator must extract the value of the discriminator from the input. A `str` discriminator must be the name of a field to discriminate against.
####  custom_error_type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.custom_error_type)
```
custom_error_type: | None = None

```

Type to use in [custom errors](https://docs.pydantic.dev/latest/errors/errors/) replacing the standard discriminated union validation errors.
####  custom_error_message `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.custom_error_message)
```
custom_error_message: | None = None

```

Message to use in custom errors.
####  custom_error_context `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.custom_error_context)
```
custom_error_context: (
    [, | | ] | None
) = None

```

Context to use in custom errors.
###  FailFast `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FailFast)
Bases: `PydanticMetadata`, `BaseMetadata`
A `FailFast` annotation can be used to specify that validation should stop at the first error.
This can be useful when you want to validate a large amount of data and you only need to know if it's valid or not.
You might want to enable this setting if you want to validate your data faster (basically, if you use this, validation will be more performant with the caveat that you get less information).
```
fromtypingimport Annotated

frompydanticimport BaseModel, FailFast, ValidationError

classModel(BaseModel):
    x: Annotated[list[int], FailFast()]

# This will raise a single error for the first invalid value and stop validation
try:
    obj = Model(x=[1, 2, 'a', 4, 5, 'b', 7, 8, 9, 'c'])
except ValidationError as e:
    print(e)
'''
    1 validation error for Model
    x.2
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    '''

```

Source code in `pydantic/types.py`
```
3265
3266
3267
3268
3269
3270
3271
3272
3273
3274
3275
3276
3277
3278
3279
3280
3281
3282
3283
3284
3285
3286
3287
3288
3289
3290
3291
3292
3293
3294
3295
```
| ```
@_dataclasses.dataclass
classFailFast(_fields.PydanticMetadata, BaseMetadata):
"""A `FailFast` annotation can be used to specify that validation should stop at the first error.

    This can be useful when you want to validate a large amount of data and you only need to know if it's valid or not.

    You might want to enable this setting if you want to validate your data faster (basically, if you use this,
    validation will be more performant with the caveat that you get less information).

```python
    from typing import Annotated

    from pydantic import BaseModel, FailFast, ValidationError

    class Model(BaseModel):
        x: Annotated[list[int], FailFast()]

    # This will raise a single error for the first invalid value and stop validation
    try:
        obj = Model(x=[1, 2, 'a', 4, 5, 'b', 7, 8, 9, 'c'])
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Model
        x.2
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
        '''
```
    """

    fail_fast: bool = True

```
  
---|---  
###  conint [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conint)
```
conint(
    *,
    strict: | None = None,
    gt: | None = None,
    ge: | None = None,
    lt: | None = None,
    le: | None = None,
    multiple_of: | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `conint` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conint--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conint--__tabbed_1_2)
```
frompydanticimport BaseModel, conint

classFoo(BaseModel):
    bar: conint(strict=True, gt=0)

```

```
fromtypingimport Annotated

frompydanticimport BaseModel, Field

classFoo(BaseModel):
    bar: Annotated[int, Field(strict=True, gt=0)]

```

A wrapper around `int` that allows for additional constraints.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether to validate the integer in strict mode. Defaults to `None`. |  `None`  
`gt` |  |  The value must be greater than this. |  `None`  
`ge` |  |  The value must be greater than or equal to this. |  `None`  
`lt` |  |  The value must be less than this. |  `None`  
`le` |  |  The value must be less than or equal to this. |  `None`  
`multiple_of` |  |  The value must be a multiple of this. |  `None`  
Returns:
Type | Description  
---|---  
|  The wrapped integer type.  
```
frompydanticimport BaseModel, ValidationError, conint

classConstrainedExample(BaseModel):
    constrained_int: conint(gt=1)

m = ConstrainedExample(constrained_int=2)
print(repr(m))
#> ConstrainedExample(constrained_int=2)

try:
    ConstrainedExample(constrained_int=0)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_int',),
            'msg': 'Input should be greater than 1',
            'input': 0,
            'ctx': {'gt': 1},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
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
```
| ```
defconint(
    *,
    strict: bool | None = None,
    gt: int | None = None,
    ge: int | None = None,
    lt: int | None = None,
    le: int | None = None,
    multiple_of: int | None = None,
) -> type[int]:
"""
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `conint` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, conint

            class Foo(BaseModel):
                bar: conint(strict=True, gt=0)
        ```

        === ":white_check_mark: Do this"
        ```python
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[int, Field(strict=True, gt=0)]
        ```

    A wrapper around `int` that allows for additional constraints.

    Args:
        strict: Whether to validate the integer in strict mode. Defaults to `None`.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.

    Returns:
        The wrapped integer type.

```python
    from pydantic import BaseModel, ValidationError, conint

    class ConstrainedExample(BaseModel):
        constrained_int: conint(gt=1)

    m = ConstrainedExample(constrained_int=2)
    print(repr(m))
    #> ConstrainedExample(constrained_int=2)

    try:
        ConstrainedExample(constrained_int=0)
    except ValidationError as e:
        print(e.errors())
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('constrained_int',),
                'msg': 'Input should be greater than 1',
                'input': 0,
                'ctx': {'gt': 1},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        '''
```

    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        int,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
        annotated_types.MultipleOf(multiple_of) if multiple_of is not None else None,
    ]

```
  
---|---  
###  confloat [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confloat)
```
confloat(
    *,
    strict: | None = None,
    gt: | None = None,
    ge: | None = None,
    lt: | None = None,
    le: | None = None,
    multiple_of: | None = None,
    allow_inf_nan: | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `confloat` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confloat--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confloat--__tabbed_1_2)
```
frompydanticimport BaseModel, confloat

classFoo(BaseModel):
    bar: confloat(strict=True, gt=0)

```

```
fromtypingimport Annotated

frompydanticimport BaseModel, Field

classFoo(BaseModel):
    bar: Annotated[float, Field(strict=True, gt=0)]

```

A wrapper around `float` that allows for additional constraints.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether to validate the float in strict mode. |  `None`  
`gt` |  |  The value must be greater than this. |  `None`  
`ge` |  |  The value must be greater than or equal to this. |  `None`  
`lt` |  |  The value must be less than this. |  `None`  
`le` |  |  The value must be less than or equal to this. |  `None`  
`multiple_of` |  |  The value must be a multiple of this. |  `None`  
`allow_inf_nan` |  |  Whether to allow `-inf`, `inf`, and `nan`. |  `None`  
Returns:
Type | Description  
---|---  
|  The wrapped float type.  
```
frompydanticimport BaseModel, ValidationError, confloat

classConstrainedExample(BaseModel):
    constrained_float: confloat(gt=1.0)

m = ConstrainedExample(constrained_float=1.1)
print(repr(m))
#> ConstrainedExample(constrained_float=1.1)

try:
    ConstrainedExample(constrained_float=0.9)
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_float',),
            'msg': 'Input should be greater than 1',
            'input': 0.9,
            'ctx': {'gt': 1.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
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
```
| ```
defconfloat(
    *,
    strict: bool | None = None,
    gt: float | None = None,
    ge: float | None = None,
    lt: float | None = None,
    le: float | None = None,
    multiple_of: float | None = None,
    allow_inf_nan: bool | None = None,
) -> type[float]:
"""
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `confloat` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, confloat

            class Foo(BaseModel):
                bar: confloat(strict=True, gt=0)
        ```

        === ":white_check_mark: Do this"
        ```python
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[float, Field(strict=True, gt=0)]
        ```

    A wrapper around `float` that allows for additional constraints.

    Args:
        strict: Whether to validate the float in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.
        allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`.

    Returns:
        The wrapped float type.

```python
    from pydantic import BaseModel, ValidationError, confloat

    class ConstrainedExample(BaseModel):
        constrained_float: confloat(gt=1.0)

    m = ConstrainedExample(constrained_float=1.1)
    print(repr(m))
    #> ConstrainedExample(constrained_float=1.1)

    try:
        ConstrainedExample(constrained_float=0.9)
    except ValidationError as e:
        print(e.errors())
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('constrained_float',),
                'msg': 'Input should be greater than 1',
                'input': 0.9,
                'ctx': {'gt': 1.0},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        '''
```
    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        float,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
        annotated_types.MultipleOf(multiple_of) if multiple_of is not None else None,
        AllowInfNan(allow_inf_nan) if allow_inf_nan is not None else None,
    ]

```
  
---|---  
###  conbytes [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conbytes)
```
conbytes(
    *,
    min_length: | None = None,
    max_length: | None = None,
    strict: | None = None
) -> []

```

A wrapper around `bytes` that allows for additional constraints.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`min_length` |  |  The minimum length of the bytes. |  `None`  
`max_length` |  |  The maximum length of the bytes. |  `None`  
`strict` |  |  Whether to validate the bytes in strict mode. |  `None`  
Returns:
Type | Description  
---|---  
|  The wrapped bytes type.  
Source code in `pydantic/types.py`
```
663
664
665
666
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
680
681
682
683
```
| ```
defconbytes(
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    strict: bool | None = None,
) -> type[bytes]:
"""A wrapper around `bytes` that allows for additional constraints.

    Args:
        min_length: The minimum length of the bytes.
        max_length: The maximum length of the bytes.
        strict: Whether to validate the bytes in strict mode.

    Returns:
        The wrapped bytes type.
    """
    return Annotated[  # pyright: ignore[reportReturnType]
        bytes,
        Strict(strict) if strict is not None else None,
        annotated_types.Len(min_length or 0, max_length),
    ]

```
  
---|---  
###  constr [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr)
```
constr(
    *,
    strip_whitespace: | None = None,
    to_upper: | None = None,
    to_lower: | None = None,
    strict: | None = None,
    min_length: | None = None,
    max_length: | None = None,
    pattern: | [] | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`StringConstraints`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StringConstraints) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `constr` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr--__tabbed_1_2)
```
frompydanticimport BaseModel, constr

classFoo(BaseModel):
    bar: constr(strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$')

```

```
fromtypingimport Annotated

frompydanticimport BaseModel, StringConstraints

classFoo(BaseModel):
    bar: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$'
        ),
    ]

```

A wrapper around `str` that allows for additional constraints.
```
frompydanticimport BaseModel, constr

classFoo(BaseModel):
    bar: constr(strip_whitespace=True, to_upper=True)

foo = Foo(bar='  hello  ')
print(foo)
#> bar='HELLO'

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strip_whitespace` |  |  Whether to remove leading and trailing whitespace. |  `None`  
`to_upper` |  |  Whether to turn all characters to uppercase. |  `None`  
`to_lower` |  |  Whether to turn all characters to lowercase. |  `None`  
`strict` |  |  Whether to validate the string in strict mode. |  `None`  
`min_length` |  |  The minimum length of the string. |  `None`  
`max_length` |  |  The maximum length of the string. |  `None`  
`pattern` |  |  A regex pattern to validate the string against. |  `None`  
Returns:
Type | Description  
---|---  
|  The wrapped string type.  
Source code in `pydantic/types.py`
```
749
750
751
752
753
754
755
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
771
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
784
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
795
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
806
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
817
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
```
| ```
defconstr(
    *,
    strip_whitespace: bool | None = None,
    to_upper: bool | None = None,
    to_lower: bool | None = None,
    strict: bool | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    pattern: str | Pattern[str] | None = None,
) -> type[str]:
"""
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`StringConstraints`][pydantic.types.StringConstraints] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `constr` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, constr

            class Foo(BaseModel):
                bar: constr(strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$')
        ```

        === ":white_check_mark: Do this"
        ```python
            from typing import Annotated

            from pydantic import BaseModel, StringConstraints

            class Foo(BaseModel):
                bar: Annotated[
                    str,
                    StringConstraints(
                        strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$'
                    ),
                ]
        ```

    A wrapper around `str` that allows for additional constraints.

```python
    from pydantic import BaseModel, constr

    class Foo(BaseModel):
        bar: constr(strip_whitespace=True, to_upper=True)

    foo = Foo(bar='  hello  ')
    print(foo)
    #> bar='HELLO'
```

    Args:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to turn all characters to uppercase.
        to_lower: Whether to turn all characters to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern to validate the string against.

    Returns:
        The wrapped string type.
    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        str,
        StringConstraints(
            strip_whitespace=strip_whitespace,
            to_upper=to_upper,
            to_lower=to_lower,
            strict=strict,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
        ),
    ]

```
  
---|---  
###  conset [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conset)
```
conset(
    item_type: [HashableItemType],
    *,
    min_length: | None = None,
    max_length: | None = None
) -> [[HashableItemType]]

```

A wrapper around `typing.Set` that allows for additional constraints.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`item_type` |  `HashableItemType]` |  The type of the items in the set. |  _required_  
`min_length` |  |  The minimum length of the set. |  `None`  
`max_length` |  |  The maximum length of the set. |  `None`  
Returns:
Type | Description  
---|---  
`HashableItemType]]` |  The wrapped set type.  
Source code in `pydantic/types.py`
```
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
```
| ```
defconset(
    item_type: type[HashableItemType], *, min_length: int | None = None, max_length: int | None = None
) -> type[set[HashableItemType]]:
"""A wrapper around `typing.Set` that allows for additional constraints.

    Args:
        item_type: The type of the items in the set.
        min_length: The minimum length of the set.
        max_length: The maximum length of the set.

    Returns:
        The wrapped set type.
    """
    return Annotated[set[item_type], annotated_types.Len(min_length or 0, max_length)]  # pyright: ignore[reportReturnType]

```
  
---|---  
###  confrozenset [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confrozenset)
```
confrozenset(
    item_type: [HashableItemType],
    *,
    min_length: | None = None,
    max_length: | None = None
) -> [[HashableItemType]]

```

A wrapper around `typing.FrozenSet` that allows for additional constraints.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`item_type` |  `HashableItemType]` |  The type of the items in the frozenset. |  _required_  
`min_length` |  |  The minimum length of the frozenset. |  `None`  
`max_length` |  |  The maximum length of the frozenset. |  `None`  
Returns:
Type | Description  
---|---  
`HashableItemType]]` |  The wrapped frozenset type.  
Source code in `pydantic/types.py`
```
855
856
857
858
859
860
861
862
863
864
865
866
867
868
```
| ```
defconfrozenset(
    item_type: type[HashableItemType], *, min_length: int | None = None, max_length: int | None = None
) -> type[frozenset[HashableItemType]]:
"""A wrapper around `typing.FrozenSet` that allows for additional constraints.

    Args:
        item_type: The type of the items in the frozenset.
        min_length: The minimum length of the frozenset.
        max_length: The maximum length of the frozenset.

    Returns:
        The wrapped frozenset type.
    """
    return Annotated[frozenset[item_type], annotated_types.Len(min_length or 0, max_length)]  # pyright: ignore[reportReturnType]

```
  
---|---  
###  conlist [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conlist)
```
conlist(
    item_type: [AnyItemType],
    *,
    min_length: | None = None,
    max_length: | None = None,
    unique_items: | None = None
) -> [[AnyItemType]]

```

A wrapper around 
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`item_type` |  `AnyItemType]` |  The type of the items in the list. |  _required_  
`min_length` |  |  The minimum length of the list. Defaults to None. |  `None`  
`max_length` |  |  The maximum length of the list. Defaults to None. |  `None`  
`unique_items` |  |  Whether the items in the list must be unique. Defaults to None. Warning The `unique_items` parameter is deprecated, use `Set` instead. See  |  `None`  
Returns:
Type | Description  
---|---  
`AnyItemType]]` |  The wrapped list type.  
Source code in `pydantic/types.py`
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
```
| ```
defconlist(
    item_type: type[AnyItemType],
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    unique_items: bool | None = None,
) -> type[list[AnyItemType]]:
"""A wrapper around [`list`][] that adds validation.

    Args:
        item_type: The type of the items in the list.
        min_length: The minimum length of the list. Defaults to None.
        max_length: The maximum length of the list. Defaults to None.
        unique_items: Whether the items in the list must be unique. Defaults to None.
            !!! warning Deprecated
                The `unique_items` parameter is deprecated, use `Set` instead.
                See [this issue](https://github.com/pydantic/pydantic-core/issues/296) for more details.

    Returns:
        The wrapped list type.
    """
    if unique_items is not None:
        raise PydanticUserError(
            (
                '`unique_items` is removed, use `Set` instead'
                '(this feature is discussed in https://github.com/pydantic/pydantic-core/issues/296)'
            ),
            code='removed-kwargs',
        )
    return Annotated[list[item_type], annotated_types.Len(min_length or 0, max_length)]  # pyright: ignore[reportReturnType]

```
  
---|---  
###  condecimal [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condecimal)
```
condecimal(
    *,
    strict: | None = None,
    gt: | | None = None,
    ge: | | None = None,
    lt: | | None = None,
    le: | | None = None,
    multiple_of: | | None = None,
    max_digits: | None = None,
    decimal_places: | None = None,
    allow_inf_nan: | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `condecimal` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condecimal--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condecimal--__tabbed_1_2)
```
frompydanticimport BaseModel, condecimal

classFoo(BaseModel):
    bar: condecimal(strict=True, allow_inf_nan=True)

```

```
fromdecimalimport Decimal
fromtypingimport Annotated

frompydanticimport BaseModel, Field

classFoo(BaseModel):
    bar: Annotated[Decimal, Field(strict=True, allow_inf_nan=True)]

```

A wrapper around Decimal that adds validation.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether to validate the value in strict mode. Defaults to `None`. |  `None`  
`gt` |  |  The value must be greater than this. Defaults to `None`. |  `None`  
`ge` |  |  The value must be greater than or equal to this. Defaults to `None`. |  `None`  
`lt` |  |  The value must be less than this. Defaults to `None`. |  `None`  
`le` |  |  The value must be less than or equal to this. Defaults to `None`. |  `None`  
`multiple_of` |  |  The value must be a multiple of this. Defaults to `None`. |  `None`  
`max_digits` |  |  The maximum number of digits. Defaults to `None`. |  `None`  
`decimal_places` |  |  The number of decimal places. Defaults to `None`. |  `None`  
`allow_inf_nan` |  |  Whether to allow infinity and NaN. Defaults to `None`. |  `None`  
```
fromdecimalimport Decimal

frompydanticimport BaseModel, ValidationError, condecimal

classConstrainedExample(BaseModel):
    constrained_decimal: condecimal(gt=Decimal('1.0'))

m = ConstrainedExample(constrained_decimal=Decimal('1.1'))
print(repr(m))
#> ConstrainedExample(constrained_decimal=Decimal('1.1'))

try:
    ConstrainedExample(constrained_decimal=Decimal('0.9'))
except ValidationError as e:
    print(e.errors())
'''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_decimal',),
            'msg': 'Input should be greater than 1.0',
            'input': Decimal('0.9'),
            'ctx': {'gt': Decimal('1.0')},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
1040
1041
1042
1043
1044
1045
1046
1047
1048
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
1062
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
1110
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
1124
1125
1126
1127
1128
1129
1130
1131
```
| ```
defcondecimal(
    *,
    strict: bool | None = None,
    gt: int | Decimal | None = None,
    ge: int | Decimal | None = None,
    lt: int | Decimal | None = None,
    le: int | Decimal | None = None,
    multiple_of: int | Decimal | None = None,
    max_digits: int | None = None,
    decimal_places: int | None = None,
    allow_inf_nan: bool | None = None,
) -> type[Decimal]:
"""
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `condecimal` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, condecimal

            class Foo(BaseModel):
                bar: condecimal(strict=True, allow_inf_nan=True)
        ```

        === ":white_check_mark: Do this"
        ```python
            from decimal import Decimal
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[Decimal, Field(strict=True, allow_inf_nan=True)]
        ```

    A wrapper around Decimal that adds validation.

    Args:
        strict: Whether to validate the value in strict mode. Defaults to `None`.
        gt: The value must be greater than this. Defaults to `None`.
        ge: The value must be greater than or equal to this. Defaults to `None`.
        lt: The value must be less than this. Defaults to `None`.
        le: The value must be less than or equal to this. Defaults to `None`.
        multiple_of: The value must be a multiple of this. Defaults to `None`.
        max_digits: The maximum number of digits. Defaults to `None`.
        decimal_places: The number of decimal places. Defaults to `None`.
        allow_inf_nan: Whether to allow infinity and NaN. Defaults to `None`.

```python
    from decimal import Decimal

    from pydantic import BaseModel, ValidationError, condecimal

    class ConstrainedExample(BaseModel):
        constrained_decimal: condecimal(gt=Decimal('1.0'))

    m = ConstrainedExample(constrained_decimal=Decimal('1.1'))
    print(repr(m))
    #> ConstrainedExample(constrained_decimal=Decimal('1.1'))

    try:
        ConstrainedExample(constrained_decimal=Decimal('0.9'))
    except ValidationError as e:
        print(e.errors())
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('constrained_decimal',),
                'msg': 'Input should be greater than 1.0',
                'input': Decimal('0.9'),
                'ctx': {'gt': Decimal('1.0')},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        '''
```
    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        Decimal,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
        annotated_types.MultipleOf(multiple_of) if multiple_of is not None else None,
        _fields.pydantic_general_metadata(max_digits=max_digits, decimal_places=decimal_places),
        AllowInfNan(allow_inf_nan) if allow_inf_nan is not None else None,
    ]

```
  
---|---  
###  condate [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condate)
```
condate(
    *,
    strict: | None = None,
    gt: | None = None,
    ge: | None = None,
    lt: | None = None,
    le: | None = None
) -> []

```

A wrapper for date that adds constraints.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`strict` |  |  Whether to validate the date value in strict mode. Defaults to `None`. |  `None`  
`gt` |  |  The value must be greater than this. Defaults to `None`. |  `None`  
`ge` |  |  The value must be greater than or equal to this. Defaults to `None`. |  `None`  
`lt` |  |  The value must be less than this. Defaults to `None`. |  `None`  
`le` |  |  The value must be less than or equal to this. Defaults to `None`. |  `None`  
Returns:
Type | Description  
---|---  
|  A date type with the specified constraints.  
Source code in `pydantic/types.py`
```
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
2250
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
```
| ```
defcondate(
    *,
    strict: bool | None = None,
    gt: date | None = None,
    ge: date | None = None,
    lt: date | None = None,
    le: date | None = None,
) -> type[date]:
"""A wrapper for date that adds constraints.

    Args:
        strict: Whether to validate the date value in strict mode. Defaults to `None`.
        gt: The value must be greater than this. Defaults to `None`.
        ge: The value must be greater than or equal to this. Defaults to `None`.
        lt: The value must be less than this. Defaults to `None`.
        le: The value must be less than or equal to this. Defaults to `None`.

    Returns:
        A date type with the specified constraints.
    """
    return Annotated[  # pyright: ignore[reportReturnType]
        date,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
    ]

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
