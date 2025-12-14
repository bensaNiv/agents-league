---
# Smart Librarian Export (v2.0)
- Page Number: 47
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/networks
- Page Title: Network Types - Pydantic Validation
- Semantic Filename: network_types_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 23,237 characters
---

# Network Types - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Network Types
The networks module contains types for common network-related fields.
##  MAX_EMAIL_LENGTH `module-attribute` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.MAX_EMAIL_LENGTH)
```
MAX_EMAIL_LENGTH = 2048

```

Maximum length for an email. A somewhat arbitrary but very generous number compared to what is allowed by most implementations.
##  UrlConstraints `dataclass` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.UrlConstraints)
```
UrlConstraints(
    max_length: | None = None,
    allowed_schemes: [] | None = None,
    host_required: | None = None,
    default_host: | None = None,
    default_port: | None = None,
    default_path: | None = None,
    preserve_empty_path: | None = None,
)

```

Url constraints.
Attributes:
Name | Type | Description  
---|---|---  
`max_length` |  |  The maximum length of the url. Defaults to `None`.  
`allowed_schemes` |  |  The allowed schemes. Defaults to `None`.  
`host_required` |  |  Whether the host is required. Defaults to `None`.  
`default_host` |  |  The default host. Defaults to `None`.  
`default_port` |  |  The default port. Defaults to `None`.  
`default_path` |  |  The default path. Defaults to `None`.  
`preserve_empty_path` |  |  Whether to preserve empty URL paths. Defaults to `None`.  
###  defined_constraints `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.UrlConstraints.defined_constraints)
```
defined_constraints: [, ]

```

Fetch a key / value mapping of constraints to values that are not None. Used for core schema updates.
##  AnyUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)
```
AnyUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `_BaseUrl`
Base type for all URLs.
  * Any scheme allowed
  * Top-level domain (TLD) not required
  * Host not required


Assuming an input URL of `http://samuel:pass@example.com:8000/the/path/?query=here#fragment=is;this=bit`, the types export the following properties:
  * `scheme`: the URL scheme (`http`), always set.
  * `host`: the URL host (`example.com`).
  * `username`: optional username if included (`samuel`).
  * `password`: optional password if included (`pass`).
  * `port`: optional port (`8000`).
  * `path`: optional path (`/the/path/`).
  * `query`: optional URL query (for example, `GET` arguments or "search string", such as `query=here`).
  * `fragment`: optional fragment (`fragment=is;this=bit`).

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  AnyHttpUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyHttpUrl)
```
AnyHttpUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any http or https URL.
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  HttpUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.HttpUrl)
```
HttpUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any http or https URL.
  * TLD not required
  * Host not required
  * Max length 2083


```
frompydanticimport BaseModel, HttpUrl, ValidationError

classMyModel(BaseModel):
    url: HttpUrl

m = MyModel(url='http://www.example.com')  [](https://docs.pydantic.dev/latest/api/networks/#__code_8_annotation_1)
print(m.url)
#> http://www.example.com/

try:
    MyModel(url='ftp://invalid.url')
except ValidationError as e:
    print(e)
'''
    1 validation error for MyModel
    url
      URL scheme should be 'http' or 'https' [type=url_scheme, input_value='ftp://invalid.url', input_type=str]
    '''

try:
    MyModel(url='not a url')
except ValidationError as e:
    print(e)
'''
    1 validation error for MyModel
    url
      Input should be a valid URL, relative URL without a base [type=url_parsing, input_value='not a url', input_type=str]
    '''

```

"International domains" (e.g. a URL where the host or TLD includes non-ascii characters) will be encoded via 
```
frompydanticimport BaseModel, HttpUrl

classMyModel(BaseModel):
    url: HttpUrl

m1 = MyModel(url='http://puny£code.com')
print(m1.url)
#> http://xn--punycode-eja.com/
m2 = MyModel(url='https://www.аррӏе.com/')
print(m2.url)
#> https://www.xn--80ak6aa92e.com/
m3 = MyModel(url='https://www.example.珠宝/')
print(m3.url)
#> https://www.example.xn--pbt977c/

```

Underscores in Hostnames
In Pydantic, underscores are allowed in all parts of a domain except the TLD. Technically this might be wrong - in theory the hostname cannot have underscores, but subdomains can.
To explain this; consider the following two cases:
  * `exam_ple.co.uk`: the hostname is `exam_ple`, which should not be allowed since it contains an underscore.
  * `foo_bar.example.com` the hostname is `example`, which should be allowed since the underscore is in the subdomain.


Without having an exhaustive list of TLDs, it would be impossible to differentiate between these two. Therefore underscores are allowed, but you can always do further validation in a validator if desired.
Also, Chrome, Firefox, and Safari all currently accept `http://exam_ple.com` as a URL, so we're in good (or at least big) company.
Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  AnyWebsocketUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyWebsocketUrl)
```
AnyWebsocketUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any ws or wss URL.
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  WebsocketUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.WebsocketUrl)
```
WebsocketUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any ws or wss URL.
  * TLD not required
  * Host not required
  * Max length 2083

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  FileUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.FileUrl)
```
FileUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any file URL.
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  FtpUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.FtpUrl)
```
FtpUrl(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept ftp URL.
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  PostgresDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.PostgresDsn)
```
PostgresDsn(url: | MultiHostUrl[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl) | _BaseMultiHostUrl)

```

Bases: `_BaseMultiHostUrl`
A type that will accept any Postgres DSN.
  * User info required
  * TLD not required
  * Host required
  * Supports multiple hosts


If further validation is required, these properties can be used by validators to enforce specific behaviour:
```
frompydanticimport (
    BaseModel,
    HttpUrl,
    PostgresDsn,
    ValidationError,
    field_validator,
)

classMyModel(BaseModel):
    url: HttpUrl

m = MyModel(url='http://www.example.com')

# the repr() method for a url will display all properties of the url
print(repr(m.url))
#> HttpUrl('http://www.example.com/')
print(m.url.scheme)
#> http
print(m.url.host)
#> www.example.com
print(m.url.port)
#> 80

classMyDatabaseModel(BaseModel):
    db: PostgresDsn

    @field_validator('db')
    defcheck_db_name(cls, v):
        assert v.path and len(v.path) > 1, 'database must be provided'
        return v

m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
print(m.db)
#> postgres://user:pass@localhost:5432/foobar

try:
    MyDatabaseModel(db='postgres://user:pass@localhost:5432')
except ValidationError as e:
    print(e)
'''
    1 validation error for MyDatabaseModel
    db
      Assertion failed, database must be provided
    assert (None)
     +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
    '''

```

Source code in `pydantic/networks.py`
```
350
351
```
| ```
def__init__(self, url: str | _CoreMultiHostUrl | _BaseMultiHostUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.PostgresDsn.host)
```
host: 
```

The required URL host.
##  CockroachDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.CockroachDsn)
```
CockroachDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any Cockroach DSN.
  * User info required
  * TLD not required
  * Host required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.CockroachDsn.host)
```
host: 
```

The required URL host.
##  AmqpDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AmqpDsn)
```
AmqpDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any AMQP DSN.
  * User info required
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  RedisDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.RedisDsn)
```
RedisDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any Redis DSN.
  * User info required
  * TLD not required
  * Host required (e.g., `rediss://:pass@localhost`)

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.RedisDsn.host)
```
host: 
```

The required URL host.
##  MongoDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.MongoDsn)
```
MongoDsn(url: | MultiHostUrl[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl) | _BaseMultiHostUrl)

```

Bases: `_BaseMultiHostUrl`
A type that will accept any MongoDB DSN.
  * User info not required
  * Database name not required
  * Port not required
  * User info may be passed without user part (e.g., `mongodb://mongodb0.example.com:27017`).


Warning
If a port isn't specified, the default MongoDB port `27017` will be used. If this behavior is undesirable, you can use the following:
```
fromtypingimport Annotated

frompydanticimport UrlConstraints
frompydantic_coreimport MultiHostUrl

MongoDsnNoDefaultPort = Annotated[
    MultiHostUrl,
    UrlConstraints(allowed_schemes=['mongodb', 'mongodb+srv']),
]

```

Source code in `pydantic/networks.py`
```
350
351
```
| ```
def__init__(self, url: str | _CoreMultiHostUrl | _BaseMultiHostUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  KafkaDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.KafkaDsn)
```
KafkaDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any Kafka DSN.
  * User info required
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  NatsDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.NatsDsn)
```
NatsDsn(url: | MultiHostUrl[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl) | _BaseMultiHostUrl)

```

Bases: `_BaseMultiHostUrl`
A type that will accept any NATS DSN.
NATS is a connective technology built for the ever increasingly hyper-connected world. It is a single technology that enables applications to securely communicate across any combination of cloud vendors, on-premise, edge, web and mobile, and devices. More: https://nats.io
Source code in `pydantic/networks.py`
```
350
351
```
| ```
def__init__(self, url: str | _CoreMultiHostUrl | _BaseMultiHostUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  MySQLDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.MySQLDsn)
```
MySQLDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any MySQL DSN.
  * User info required
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  MariaDBDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.MariaDBDsn)
```
MariaDBDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any MariaDB DSN.
  * User info required
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  ClickHouseDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.ClickHouseDsn)
```
ClickHouseDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any ClickHouse DSN.
  * User info required
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
##  SnowflakeDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.SnowflakeDsn)
```
SnowflakeDsn(url: | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url) | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl)`
A type that will accept any Snowflake DSN.
  * User info required
  * TLD not required
  * Host required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def__init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```
  
---|---  
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.SnowflakeDsn.host)
```
host: 
```

The required URL host.
##  EmailStr [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.EmailStr)
Info
To use this type, you need to install the optional 
```
pip
```

Validate email addresses.
```
frompydanticimport BaseModel, EmailStr

classModel(BaseModel):
    email: EmailStr

print(Model(email='contact@mail.com'))
#> email='contact@mail.com'

```

##  NameEmail [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.NameEmail)
```
NameEmail(name: , email: )

```

Bases: `Representation`
Info
To use this type, you need to install the optional 
```
pip
```

Validate a name and email address combination, as specified by 
The `NameEmail` has two properties: `name` and `email`. In case the `name` is not provided, it's inferred from the email address.
```
frompydanticimport BaseModel, NameEmail

classUser(BaseModel):
    email: NameEmail

user = User(email='Fred Bloggs <fred.bloggs@example.com>')
print(user.email)
#> Fred Bloggs <fred.bloggs@example.com>
print(user.email.name)
#> Fred Bloggs

user = User(email='fred.bloggs@example.com')
print(user.email)
#> fred.bloggs <fred.bloggs@example.com>
print(user.email.name)
#> fred.bloggs

```

Source code in `pydantic/networks.py`
```
1059
1060
1061
```
| ```
def__init__(self, name: str, email: str):
    self.name = name
    self.email = email

```
  
---|---  
##  IPvAnyAddress [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyAddress)
Validate an IPv4 or IPv6 address.
```
frompydanticimport BaseModel
frompydantic.networksimport IPvAnyAddress

classIpModel(BaseModel):
    ip: IPvAnyAddress

print(IpModel(ip='127.0.0.1'))
#> ip=IPv4Address('127.0.0.1')

try:
    IpModel(ip='http://www.example.com')
except ValueError as e:
    print(e.errors())
'''
    [
        {
            'type': 'ip_any_address',
            'loc': ('ip',),
            'msg': 'value is not a valid IPv4 or IPv6 address',
            'input': 'http://www.example.com',
        }
    ]
    '''

```

##  IPvAnyInterface [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyInterface)
Validate an IPv4 or IPv6 interface.
##  IPvAnyNetwork [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyNetwork)
Validate an IPv4 or IPv6 network.
##  validate_email [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.validate_email)
```
validate_email(value: ) -> [, ]

```

Email address validation using 
Returns:
Type | Description  
---|---  
|  A tuple containing the local part of the email (or the name for "pretty" email addresses) and the normalized email.  
Raises:
Type | Description  
---|---  
`PydanticCustomError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError)` |  If the email is invalid.  
Note
Note that:
  * Raw IP address (literal) domain parts are not allowed.
  * `"John Doe <local_part@domain.com>"` style "pretty" email addresses are processed.
  * Spaces are striped from the beginning and end of addresses, but no error is raised.

Source code in `pydantic/networks.py`
```
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
```
| ```
defvalidate_email(value: str) -> tuple[str, str]:
"""Email address validation using [email-validator](https://pypi.org/project/email-validator/).

    Returns:
        A tuple containing the local part of the email (or the name for "pretty" email addresses)
            and the normalized email.

    Raises:
        PydanticCustomError: If the email is invalid.

    Note:
        Note that:

        * Raw IP address (literal) domain parts are not allowed.
        * `"John Doe <local_part@domain.com>"` style "pretty" email addresses are processed.
        * Spaces are striped from the beginning and end of addresses, but no error is raised.
    """
    if email_validator is None:
        import_email_validator()

    if len(value) > MAX_EMAIL_LENGTH:
        raise PydanticCustomError(
            'value_error',
            'value is not a valid email address: {reason}',
            {'reason': f'Length must not exceed {MAX_EMAIL_LENGTH} characters'},
        )

    m = pretty_email_regex.fullmatch(value)
    name: str | None = None
    if m:
        unquoted_name, quoted_name, value = m.groups()
        name = unquoted_name or quoted_name

    email = value.strip()

    try:
        parts = email_validator.validate_email(email, check_deliverability=False)
    except email_validator.EmailNotValidError as e:
        raise PydanticCustomError(
            'value_error', 'value is not a valid email address: {reason}', {'reason': str(e.args[0])}
        ) frome

    email = parts.normalized
    assert email is not None
    name = name or parts.local_part
    return name, email

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
