---
# Smart Librarian Export (v2.0)
- Page Number: 3
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/why
- Page Title: Why use Pydantic - Pydantic Validation
- Semantic Filename: why_use_pydantic_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 17,654 characters
---

# Why use Pydantic - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/why/#why-use-pydantic-validation)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Why use Pydantic Validation?[¶](https://docs.pydantic.dev/latest/why/#why-use-pydantic-validation)
Today, Pydantic is downloaded 552M times a month and used by some of the largest and most recognisable organisations in the world.
It's hard to know why so many people have adopted Pydantic since its inception six years ago, but here are a few guesses.
## Type hints powering schema validation[¶](https://docs.pydantic.dev/latest/why/#type-hints)
The schema that Pydantic validates against is generally defined by Python 
Type hints are great for this since, if you're writing modern Python, you already know how to use them. Using type hints also means that Pydantic integrates well with static typing tools (like 
Example - just type hints
```
fromtypingimport Annotated, Literal

fromannotated_typesimport Gt

frompydanticimport BaseModel


classFruit(BaseModel):
    name: str  [](https://docs.pydantic.dev/latest/why/#__code_0_annotation_1)
    color: Literal['red', 'green']  [](https://docs.pydantic.dev/latest/why/#__code_0_annotation_2)
    weight: Annotated[float, Gt(0)]  [](https://docs.pydantic.dev/latest/why/#__code_0_annotation_3)
    bazam: dict[str, list[tuple[int, bool, float]]]  [](https://docs.pydantic.dev/latest/why/#__code_0_annotation_4)


print(
    Fruit(
        name='Apple',
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)
#> name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}

```

Learn more
See the [documentation on supported types](https://docs.pydantic.dev/latest/concepts/types/).
## Performance[¶](https://docs.pydantic.dev/latest/why/#performance)
Pydantic's core validation logic is implemented in a separate package (
As a result, Pydantic is among the fastest data validation libraries for Python.
Performance Example - Pydantic vs. dedicated code
In general, dedicated code should be much faster than a general-purpose validator, but in this example Pydantic is >300% faster than dedicated code when parsing JSON and validating URLs.
Performance Example```
importjson
importtimeit
fromurllib.parseimport urlparse

importrequests

frompydanticimport HttpUrl, TypeAdapter

reps = 7
number = 100
r = requests.get('https://api.github.com/emojis')
r.raise_for_status()
emojis_json = r.content


defemojis_pure_python(raw_data):
    data = json.loads(raw_data)
    output = {}
    for key, value in data.items():
        assert isinstance(key, str)
        url = urlparse(value)
        assert url.scheme in ('https', 'http')
        output[key] = url


emojis_pure_python_times = timeit.repeat(
    'emojis_pure_python(emojis_json)',
    globals={
        'emojis_pure_python': emojis_pure_python,
        'emojis_json': emojis_json,
    },
    repeat=reps,
    number=number,
)
print(f'pure python: {min(emojis_pure_python_times)/number*1000:0.2f}ms')
#> pure python: 5.32ms

type_adapter = TypeAdapter(dict[str, HttpUrl])
emojis_pydantic_times = timeit.repeat(
    'type_adapter.validate_json(emojis_json)',
    globals={
        'type_adapter': type_adapter,
        'HttpUrl': HttpUrl,
        'emojis_json': emojis_json,
    },
    repeat=reps,
    number=number,
)
print(f'pydantic: {min(emojis_pydantic_times)/number*1000:0.2f}ms')
#> pydantic: 1.54ms

print(
    f'Pydantic {min(emojis_pure_python_times)/min(emojis_pydantic_times):0.2f}x faster'
)
#> Pydantic 3.45x faster

```

Unlike other performance-centric libraries written in compiled languages, Pydantic also has excellent support for customizing validation via [functional validators](https://docs.pydantic.dev/latest/why/#customisation).
Learn more
Samuel Colvin's 
## Serialization[¶](https://docs.pydantic.dev/latest/why/#serialization)
Pydantic provides functionality to serialize model in three ways:
  1. To a Python `dict` made up of the associated Python objects.
  2. To a Python `dict` made up only of "jsonable" types.
  3. To a JSON string.


In all three modes, the output can be customized by excluding specific fields, excluding unset fields, excluding default values, and excluding `None` values.
Example - Serialization 3 ways
```
fromdatetimeimport datetime

frompydanticimport BaseModel


classMeeting(BaseModel):
    when: datetime
    where: bytes
    why: str = 'No idea'


m = Meeting(when='2020-01-01T12:00', where='home')
print(m.model_dump(exclude_unset=True))
#> {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
print(m.model_dump(exclude={'where'}, mode='json'))
#> {'when': '2020-01-01T12:00:00', 'why': 'No idea'}
print(m.model_dump_json(exclude_defaults=True))
#> {"when":"2020-01-01T12:00:00","where":"home"}

```

Learn more
See the [documentation on serialization](https://docs.pydantic.dev/latest/concepts/serialization/).
## JSON Schema[¶](https://docs.pydantic.dev/latest/why/#json-schema)
A 
Example - JSON Schema
```
fromdatetimeimport datetime

frompydanticimport BaseModel


classAddress(BaseModel):
    street: str
    city: str
    zipcode: str


classMeeting(BaseModel):
    when: datetime
    where: Address
    why: str = 'No idea'


print(Meeting.model_json_schema())
"""
{
    '$defs': {
        'Address': {
            'properties': {
                'street': {'title': 'Street', 'type': 'string'},
                'city': {'title': 'City', 'type': 'string'},
                'zipcode': {'title': 'Zipcode', 'type': 'string'},
            },
            'required': ['street', 'city', 'zipcode'],
            'title': 'Address',
            'type': 'object',
        }
    },
    'properties': {
        'when': {'format': 'date-time', 'title': 'When', 'type': 'string'},
        'where': {'$ref': '#/$defs/Address'},
        'why': {'default': 'No idea', 'title': 'Why', 'type': 'string'},
    },
    'required': ['when', 'where'],
    'title': 'Meeting',
    'type': 'object',
}
"""

```

Pydantic is compliant with the latest version of JSON Schema specification (
Learn more
See the [documentation on JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/).
## Strict mode and data coercion[¶](https://docs.pydantic.dev/latest/why/#strict-lax)
By default, Pydantic is tolerant to common incorrect types and coerces data to the right type — e.g. a numeric string passed to an `int` field will be parsed as an `int`.
Pydantic also has as [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), where types are not coerced and a validation error is raised unless the input data exactly matches the expected schema.
But strict mode would be pretty useless when validating JSON data since JSON doesn't have types matching many common Python types like 
To solve this, Pydantic can parse and validate JSON in one step. This allows sensible data conversion (e.g. when parsing strings into 
Example - Strict mode that's actually useful
```
fromdatetimeimport datetime

frompydanticimport BaseModel, ValidationError


classMeeting(BaseModel):
    when: datetime
    where: bytes


m = Meeting.model_validate({'when': '2020-01-01T12:00', 'where': 'home'})
print(m)
#> when=datetime.datetime(2020, 1, 1, 12, 0) where=b'home'
try:
    m = Meeting.model_validate(
        {'when': '2020-01-01T12:00', 'where': 'home'}, strict=True
    )
except ValidationError as e:
    print(e)
"""
    2 validation errors for Meeting
    when
      Input should be a valid datetime [type=datetime_type, input_value='2020-01-01T12:00', input_type=str]
    where
      Input should be a valid bytes [type=bytes_type, input_value='home', input_type=str]
    """

m_json = Meeting.model_validate_json(
    '{"when": "2020-01-01T12:00", "where": "home"}'
)
print(m_json)
#> when=datetime.datetime(2020, 1, 1, 12, 0) where=b'home'

```

Learn more
See the [documentation on strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/).
## Dataclasses, TypedDicts, and more[¶](https://docs.pydantic.dev/latest/why/#dataclasses-typeddict-more)
Pydantic provides four ways to create schemas and perform validation and serialization:
  1. [`BaseModel`](https://docs.pydantic.dev/latest/concepts/models/) — Pydantic's own super class with many common utilities available via instance methods.
  2. [Pydantic dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/) — a wrapper around standard dataclasses with additional validation performed.
  3. [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) — a general way to adapt any type for validation and serialization. This allows types like [`TypedDict`](https://docs.pydantic.dev/latest/api/standard_library_types/#typeddict) and [`NamedTuple`](https://docs.pydantic.dev/latest/api/standard_library_types/#named-tuples) to be validated as well as simple types (like [all types](https://docs.pydantic.dev/latest/concepts/types/) supported can be used with [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter).
  4. [`validate_call`](https://docs.pydantic.dev/latest/concepts/validation_decorator/) — a decorator to perform validation when calling a function.

Example - schema based on a 
```
fromdatetimeimport datetime

fromtyping_extensionsimport NotRequired, TypedDict

frompydanticimport TypeAdapter


classMeeting(TypedDict):
    when: datetime
    where: bytes
    why: NotRequired[str]


meeting_adapter = TypeAdapter(Meeting)
m = meeting_adapter.validate_python(  [](https://docs.pydantic.dev/latest/why/#__code_5_annotation_1)
    {'when': '2020-01-01T12:00', 'where': 'home'}
)
print(m)
#> {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
meeting_adapter.dump_python(m, exclude={'where'})  [](https://docs.pydantic.dev/latest/why/#__code_5_annotation_2)

print(meeting_adapter.json_schema())  [](https://docs.pydantic.dev/latest/why/#__code_5_annotation_3)
"""
{
    'properties': {
        'when': {'format': 'date-time', 'title': 'When', 'type': 'string'},
        'where': {'format': 'binary', 'title': 'Where', 'type': 'string'},
        'why': {'title': 'Why', 'type': 'string'},
    },
    'required': ['when', 'where'],
    'title': 'Meeting',
    'type': 'object',
}
"""

```

## Customisation[¶](https://docs.pydantic.dev/latest/why/#customisation)
Functional validators and serializers, as well as a powerful protocol for custom types, means the way Pydantic operates can be customized on a per-field or per-type basis.
Customisation Example - wrap validators
"wrap validators" are new in Pydantic V2 and are one of the most powerful ways to customize validation.
```
fromdatetimeimport datetime, timezone
fromtypingimport Any

frompydantic_core.core_schemaimport ValidatorFunctionWrapHandler

frompydanticimport BaseModel, field_validator


classMeeting(BaseModel):
    when: datetime

    @field_validator('when', mode='wrap')
    defwhen_now(
        cls, input_value: Any, handler: ValidatorFunctionWrapHandler
    ) -> datetime:
        if input_value == 'now':
            return datetime.now()
        when = handler(input_value)
        # in this specific application we know tz naive datetimes are in UTC
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        return when


print(Meeting(when='2020-01-01T12:00+01:00'))
#> when=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=TzInfo(3600))
print(Meeting(when='now'))
#> when=datetime.datetime(2032, 1, 2, 3, 4, 5, 6)
print(Meeting(when='2020-01-01T12:00'))
#> when=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)

```

Learn more
See the documentation on [validators](https://docs.pydantic.dev/latest/concepts/validators/), [custom serializers](https://docs.pydantic.dev/latest/concepts/serialization/#serializers), and [custom types](https://docs.pydantic.dev/latest/concepts/types/#custom-types).
## Ecosystem[¶](https://docs.pydantic.dev/latest/why/#ecosystem)
At the time of writing there are 466,400 repositories on GitHub and 8,119 packages on PyPI that depend on Pydantic.
Some notable libraries that depend on Pydantic:
More libraries using Pydantic can be found at 
## Organisations using Pydantic[¶](https://docs.pydantic.dev/latest/why/#using-pydantic)
Some notable companies and organisations using Pydantic together with comments on why/how we know they're using Pydantic.
The organisations below are included because they match one or more of the following criteria:
  * Using Pydantic as a dependency in a public repository.
  * Referring traffic to the Pydantic documentation site from an organization-internal domain — specific referrers are not included since they're generally not in the public domain.
  * Direct communication between the Pydantic team and engineers employed by the organization about usage of Pydantic within the organization.


We've included some extra detail where appropriate and already in the public domain.
### Adobe[¶](https://docs.pydantic.dev/latest/why/#org-adobe)
### Amazon and AWS[¶](https://docs.pydantic.dev/latest/why/#org-amazon)
  * AWS 


### Anthropic[¶](https://docs.pydantic.dev/latest/why/#org-anthropic)
### Apple[¶](https://docs.pydantic.dev/latest/why/#org-apple)
_(Based on the criteria described above)_
### ASML[¶](https://docs.pydantic.dev/latest/why/#org-asml)
_(Based on the criteria described above)_
### AstraZeneca[¶](https://docs.pydantic.dev/latest/why/#org-astrazeneca)
`AstraZeneca` GitHub org depend on Pydantic.
### Cisco Systems[¶](https://docs.pydantic.dev/latest/why/#org-cisco)
  * Pydantic is listed in their report of 


### Comcast[¶](https://docs.pydantic.dev/latest/why/#org-comcast)
_(Based on the criteria described above)_
### Datadog[¶](https://docs.pydantic.dev/latest/why/#org-datadog)
  * Extensive use of Pydantic in 
  * Communication with engineers from Datadog about how they use Pydantic.


### Facebook[¶](https://docs.pydantic.dev/latest/why/#org-facebook)
`facebookresearch` GitHub org depend on Pydantic.
### GitHub[¶](https://docs.pydantic.dev/latest/why/#org-github)
GitHub sponsored Pydantic $750 in 2022
### Google[¶](https://docs.pydantic.dev/latest/why/#org-google)
Extensive use of Pydantic in 
### HSBC[¶](https://docs.pydantic.dev/latest/why/#org-hsbc)
_(Based on the criteria described above)_
### IBM[¶](https://docs.pydantic.dev/latest/why/#org-ibm)
`IBM` GitHub org depend on Pydantic.
### Intel[¶](https://docs.pydantic.dev/latest/why/#org-intel)
_(Based on the criteria described above)_
### Intuit[¶](https://docs.pydantic.dev/latest/why/#org-intuit)
_(Based on the criteria described above)_
### Intergovernmental Panel on Climate Change[¶](https://docs.pydantic.dev/latest/why/#org-ipcc)
### JPMorgan[¶](https://docs.pydantic.dev/latest/why/#org-jpmorgan)
_(Based on the criteria described above)_
### Jupyter[¶](https://docs.pydantic.dev/latest/why/#org-jupyter)
  * The developers of the Jupyter notebook are using Pydantic 
  * Through the FastAPI-based Jupyter server 


### Microsoft[¶](https://docs.pydantic.dev/latest/why/#org-microsoft)
  * `microsoft` GitHub org depend on Pydantic, in particular their
  * Pydantic is also `Azure` GitHub org


### Molecular Science Software Institute[¶](https://docs.pydantic.dev/latest/why/#org-molssi)
`MolSSI` GitHub org depend on Pydantic.
### NASA[¶](https://docs.pydantic.dev/latest/why/#org-nasa)
`NASA` GitHub org depend on Pydantic.
NASA are also using Pydantic via FastAPI in their JWST project to process images from the James Webb Space Telescope, see 
### Netflix[¶](https://docs.pydantic.dev/latest/why/#org-netflix)
`Netflix` GitHub org depend on Pydantic.
### NSA[¶](https://docs.pydantic.dev/latest/why/#org-nsa)
The 
### NVIDIA[¶](https://docs.pydantic.dev/latest/why/#org-nvidia)
`NVIDIA` GitHub org depend on Pydantic.
Their "Omniverse Services" depends on Pydantic according to 
### OpenAI[¶](https://docs.pydantic.dev/latest/why/#org-openai)
OpenAI use Pydantic for their ChatCompletions API, as per 
Anecdotally, OpenAI use Pydantic extensively for their internal services.
### Oracle[¶](https://docs.pydantic.dev/latest/why/#org-oracle)
_(Based on the criteria described above)_
### Palantir[¶](https://docs.pydantic.dev/latest/why/#org-palantir)
_(Based on the criteria described above)_
### Qualcomm[¶](https://docs.pydantic.dev/latest/why/#org-qualcomm)
_(Based on the criteria described above)_
### Red Hat[¶](https://docs.pydantic.dev/latest/why/#org-redhat)
_(Based on the criteria described above)_
### Revolut[¶](https://docs.pydantic.dev/latest/why/#org-revolut)
Anecdotally, all internal services at Revolut are built with FastAPI and therefore Pydantic.
### Robusta[¶](https://docs.pydantic.dev/latest/why/#org-robusta)
The 
### Salesforce[¶](https://docs.pydantic.dev/latest/why/#org-salesforce)
Salesforce 
### Starbucks[¶](https://docs.pydantic.dev/latest/why/#org-starbucks)
_(Based on the criteria described above)_
### Texas Instruments[¶](https://docs.pydantic.dev/latest/why/#org-ti)
_(Based on the criteria described above)_
### Twilio[¶](https://docs.pydantic.dev/latest/why/#org-twilio)
_(Based on the criteria described above)_
### Twitter[¶](https://docs.pydantic.dev/latest/why/#org-twitter)
Twitter's 
### UK Home Office[¶](https://docs.pydantic.dev/latest/why/#org-ukhomeoffice)
_(Based on the criteria described above)_
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
