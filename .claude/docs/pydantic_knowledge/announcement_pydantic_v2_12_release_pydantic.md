---
# Smart Librarian Export (v2.0)
- Page Number: 65
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/articles/pydantic-v2-12-release
- Page Title: Announcement: Pydantic v2.12 Release | Pydantic
- Semantic Filename: announcement_pydantic_v2_12_release_pydantic.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 17,483 characters
---

# Announcement: Pydantic v2.12 Release | Pydantic

/Release
# Announcement: Pydantic v2.12 Release
![Victorien Plot avatar](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://avatars.githubusercontent.com/u/65306057)
Victorien Plot
20 mins
2025/10/07
The long awaited 
```
pip install --upgrade pydantic

```

This release features the work of over 20 external contributors and provides useful new features, along with initial Python 3.14 support. Several minor changes (considered non-breaking changes according to our [versioning policy](https://docs.pydantic.dev/2.12/version-policy/#pydantic-v2)) are also included in this release. Make sure to look into them before upgrading.
Highlights include:
  * [Support for Python 3.14](https://pydantic.dev/articles/pydantic-v2-12-release#support-for-python-314)
  * [A new `MISSING` sentinel](https://pydantic.dev/articles/pydantic-v2-12-release#missing-sentinel)
  * [PEP 728 support – TypedDict with Typed Extra Items](https://pydantic.dev/articles/pydantic-v2-12-release#pep-728-support--typeddict-with-typed-extra-items)
  * [Preserve empty URL paths](https://pydantic.dev/articles/pydantic-v2-12-release#preserve-empty-url-paths)


You can see the full changelog on 
Success
This release ships with a complete rewrite of the serialization and types support documentation, do not hesitate to check them out!
##  [#](https://pydantic.dev/articles/pydantic-v2-12-release#quick-reference)Quick Reference:
  * [New Features](https://pydantic.dev/articles/pydantic-v2-12-release#new-features)
  * [Changes](https://pydantic.dev/articles/pydantic-v2-12-release#changes)


##  [#](https://pydantic.dev/articles/pydantic-v2-12-release#new-features)New Features
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#support-for-python-314)Support for Python 3.14
Python 3.14 ships with new type annotations semantics, introduced by 
Here is an example demonstrating the new behavior:
```
class Model(BaseModel):
    f: ForwardType  # No quotes required.


type ForwardType = int

m = Model(f=1)

```

Note
Deferred annotations allow more complex cases (mainly involving nested scopes) to work, while it was previously really hard if not impossible to support them in previous Python versions. Pydantic still has limited support for such cases, and progress can be tracked in 
Pydantic V1
Pydantic V1 core functionality will _not_ work properly with Python 3.14 or greater. As such, Python 3.13 is the latest supported Python version for V1.
PR references:
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#missing-sentinel)`MISSING` sentinel
A highly requested Pydantic feature is having the ability to differentiate between a default value and value provided during the model creation, especially if `None` has a specific meaning in the context it is used. Until now, Pydantic provided the [`model_fields_set`](https://docs.pydantic.dev/2.12/api/base_model/#pydantic.BaseModel.model_fields_set) property, but its usage was proven difficult.
Pydantic 2.12 introduces an experimental [`MISSING` sentinel](https://docs.pydantic.dev/2.12/concepts/experimental/#missing-sentinel): a singleton indicating a field value was not provided during validation. During serialization, any field with `MISSING` as a value is excluded from the output.
```
from pydantic import BaseModel
from pydantic.experimental.missing_sentinel import MISSING


class Configuration(BaseModel):
    timeout: int | None | MISSING = MISSING


# configuration defaults, stored somewhere else:
defaults = {'timeout': 200}

conf = Configuration()

# `timeout` is excluded from the serialization output:
conf.model_dump()
# {}

# The `MISSING` value doesn't appear in the JSON Schema:
Configuration.model_json_schema()['properties']['timeout']
#> {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Timeout'}}

```

This feature is marked as experimental because it relies on the draft 
See the [documentation](https://docs.pydantic.dev/2.12/concepts/experimental/#missing-sentinel) for more details.
PR reference: 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#pep-728-support--typeddict-with-typed-extra-items)PEP 728 support – TypedDict with Typed Extra Items
Back in August, `closed` and `extra_items` to type the extra items on a `dict` while permitting additional items of a specified type.
```
from typing_extensions import TypedDict

from pydantic import TypeAdapter


class TD(TypedDict, extra_items=int):
    a: str


ta = TypeAdapter(TD)

print(ta.validate_python({'a': 'test', 'extra': 1}))
#> {'a': 'test', 'extra': 1}

```

Such behavior was partially achievable using the [`extra`](https://docs.pydantic.dev/2.12/api/config/#pydantic.config.ConfigDict.extra) configuration value. It is now recommended to use PEP 728 capabilities.
Note that PEP 728 is currently only implemented in `TypedDict` from there if you want to make use of this feature.
The `closed`/`extra_items` specification (`False` if closed, `True` if `extra_items` is `Any` or `object`, matching the schema of the `extra_items` type otherwise).
PR reference: 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#preserve-empty-url-paths)Preserve empty URL paths
The [URL types](https://docs.pydantic.dev/2.12/api/networks/#pydantic.networks.AnyUrl) had a behavior change in V2, where a trailing slash would be added if the path was empty. In many cases, this is unwanted.
Pydantic 2.12 adds a new [`url_preserve_empty_path`](https://docs.pydantic.dev/2.12/api/config/#pydantic.config.ConfigDict.url_preserve_empty_path) configuration value to opt-out of this behavior:
```
from pydantic import AnyUrl, BaseModel, ConfigDict


class Model(BaseModel):
    u: AnyUrl

    model_config = ConfigDict(url_preserve_empty_path=True)


print(Model(u='https://example.com').u)
#> Before: 'https://example/com/'
#> After: 'https://example/com'

```

This is also configurable per-field using the [`UrlConstraints`](https://docs.pydantic.dev/2.12/api/networks/#pydantic.networks.UrlConstraints) metadata class:
```
from typing import Annotated

from pydantic import TypeAdapter, UrlConstraints

ta = TypeAdapter(Annotated[AnyUrl, UrlConstraints(preserve_empty_path=True)])
print(ta.validate_python('https://example.com'))
#> https://example.com

```

This configuration value may default to `True` in V3.
PR references:
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#control-validation-behavior-of-timestamps)Control validation behavior of timestamps
Pydantic uses to guess if a timestamp was provided in seconds or milliseconds for temporal types (such as [`val_temporal_unit`](https://docs.pydantic.dev/2.12/api/config/#pydantic.config.ConfigDict.val_temporal_unit) configuration value can now be used to force validation as seconds, milliseconds, or by inferring as before.
```
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Model(BaseModel):
    d: datetime

    model_config = ConfigDict(val_temporal_unit='milliseconds')


print(Model(d=datetime(1970, 4, 11, 19, 13).timestamp() * 1000))
#> d=datetime.datetime(1970, 4, 11, 18, 13)), would be somewhere around year 2245 in 'infer' mode.

```

A new [`ser_json_temporal`](https://docs.pydantic.dev/2.12/api/config/#pydantic.config.ConfigDict.ser_json_temporal) configuration value is also introduced, generalizing the existing [`ser_json_timedelta`](https://docs.pydantic.dev/2.12/api/config/#pydantic.config.ConfigDict.ser_json_timedelta) one.
Contributed by 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#exclude_if-field-option)`exclude_if` field option
A new `exclude_if` option was added, which can be used at the field level.
```
from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: int
    value: int = Field(ge=0, exclude_if=lambda v: v == 0)


print(Transaction(id=1, value=0).model_dump())
#> {'id': 1}

```

Contributed by 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#ensure_ascii-json-serialization-option)`ensure_ascii` JSON serialization option
A new `ensure_ascii` option was added to the [JSON serialization methods](https://docs.pydantic.dev/2.12/concepts/serialization/#json-mode) (such as `model_dump_json()`), to ensure non-ASCII characters will be Unicode-encoded. For backwards compatibility, this option defaults to `False`.
```
from pydantic import TypeAdapter

ta = TypeAdapter(str)

ta.dump_json('🔥', ensure_ascii=True)
#> b'"\\ud83d\\udd25"'

```

PR reference: 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#extra-configuration-per-validation)`extra` configuration per validation
It is now possible to control the [`extra`](https://docs.pydantic.dev/2.12/concepts/models/#extra-data) behavior per validation call:
```
from pydantic import BaseModel


class Model(BaseModel):
    x: int

    model_config = ConfigDict(extra='allow')


# Validates fine:
m = Model(x=1, y='a')
# Raises a validation error:
m = Model.model_validate({'x': 1, 'y': 'a'}, extra='forbid')

```

Contributed by 
##  [#](https://pydantic.dev/articles/pydantic-v2-12-release#changes)Changes
This release contains some minor changes that may affect existing code. Make sure to go over through them before upgrading.
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#error-when-using-incompatible-pydantic-core-versions)Error when using incompatible `pydantic-core` versions
Pydantic is meant to work with one and only one `pydantic-core` version. However, many users reported errors caused by an incompatible `pydantic-core` version being used. Starting in 2.12, Pydantic raises an explicit error at startup if this is the case. Note that most dependency bots (such as GitHub's _not_ understand the `pydantic-core` exact constraint, which might be the source of such issues.
PR reference: 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#remove-warning-for-experimental-features)Remove warning for experimental features
Pydantic has a set of [experimental features](https://docs.pydantic.dev/2.12/concepts/experimental/), exposed under the `pydantic.experimental` module. Until now, a `PydanticExperimentalWarning` was emitted whenever the module was imported. We decided to remove this warning, as the module name already conveys that it is experimental. As such, it is no longer required to [filter the warning](https://docs.pydantic.dev/2.11/concepts/experimental/#warnings-on-import) on import.
PR reference: 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#field-changes)Field changes
Small changes and bug fixes affect [Pydantic fields](https://docs.pydantic.dev/2.12/concepts/fields/) and the `Field()` function.
  * Warning emitted when field-specific metadata is used in invalid contexts:
Using field-specific metadata (e.g. `alias` or `exclude`) in invalid contexts will now raise a warning. Previously, it was silently ignored and was a common source of confusion. In particular, these two examples don't behave as expected:
```
from typing import Annotated, Optional

from pydantic import BaseModel, Field

# ❌ `alias` can't be used on type aliases:
type AliasedInt = Annotated[int, Field(alias='b')]


class Model(BaseModel):
    a: AliasedInt
    # ❌ Instead use: Annotated[Optional[int], Field(exclude=True)]
    c: Optional[Annotated[int, Field(exclude=True)]]

```

(for type aliases, see more details in the [documentation](https://docs.pydantic.dev/2.12/concepts/types/#metadata-type-alias-warning)).
  * Refactor of the `FieldInfo` class:
The `FieldInfo` class (created by the `Field()` function and used to store information about each field) underwent a complete refactor to fix many related bugs. While this shouldn't affect anything in theory, there is always a small change that it can break some edge cases. Do not hesitate to report any issues that may be occur from this refactor.
As a result, the undocumented `FieldInfo.merge_field_infos()` is deprecated. If you made use of this function previously, please 
  * Dataclasses fields inconsistencies:
Two small inconsistencies were found when mixing dataclasses and the Pydantic [`Field()`] function. These two bugs were fixed in 2.12, but may result in a behavior change in your code. The two issues can be found in issue 


PR references:
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#unify-serialize_as_anyserializeasany-behavior)Unify `serialize_as_any`/`SerializeAsAny` behavior
Pydantic provides a way to serialize values as if they were typed as `Any`. In this case, Pydantic does _not_ make use of the type annotation to infer how to serialize the value, but instead inspects the actual type of the value to do so.
This `serialize_as_any` behavior is useful when you want "duck typing" behavior with model subclasses (as per [the documentation](https://docs.pydantic.dev/latest/concepts/serialization/#subclasses-of-model-like-types)):
```
from pydantic import BaseModel, SerializeAsAny


class User(BaseModel):
    name: str


class UserLogin(User):
    password: str


class OuterModel(BaseModel):
    user: User


user = UserLogin(name='pydantic', password='password')

print(OuterModel(user=user).model_dump(serialize_as_any=True))
"""
{
    'user': {'name': 'pydantic', 'password': 'password'}
}
"""

```

If `serialize_as_any` wasn't set, the `password` field wouldn't have been included in the output, because it isn't present in the `User` annotation.
Such behavior can also be enabled at the field level, by using annotating `user` as `SerializeAsAny[User]` instead.
Before 2.12, the `serialize_as_any` parameter was behaving quite differently from the [`SerializeAsAny`](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.SerializeAsAny) annotation, and such behavior has been unified in this release. This may result in serialization errors when using the `serialize_as_any` flag, which would have happened already if using the `SerializeAsAny` annotation. To mitigate the issue, you can apply the `SerializeAsAny` annotation only on the relevant fields (as `serialize_as_any` will apply the behavior to _every_ value, which in most cases isn't wanted).
If you still require `serialize_as_any` to be set, please refer to 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#json-schema-changes)JSON Schema changes
While not breaking, some JSON Schema changes in this release might affect your tests if you make assertions on the generated JSON Schemas for your data. Here are the potential changes thay may affect you:
  * Add regex patterns to JSON schema for `Decimal` type (contributed by 
  * Respect custom title in functions JSON Schema (in 
  * When manually creating [TypedDict schemas](https://docs.pydantic.dev/2.12/api/pydantic_core_schema/#pydantic_core.core_schema.typed_dict_schema), the `extra_behavior` key is now used to populate the 


###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#after-model-validators)After model validators
[Model _after_ validators](https://docs.pydantic.dev/2.12/concepts/validators/#model-validators) are documented as being instance methods. However, class methods used to be accepted:
```
class Model(BaseModel):
    @model_validator(mode='after')
    @classmethod
    def validator(cls, model, info): ...

```

Starting in 2.12, using this signature will now raise a deprecation warning. Instead, make sure to define the validator as an _instance_ method:
```
class Model(BaseModel):
    @model_validator(mode='after')
    def validator(self, info): ...

```

Note
In the initial 2.12 release, using the invalid signature would error. However, we realized it broke such signatures _without_ the `info` parameter, and we underestimated the amount of occurrences of this invalid signature. In 2.12.3, this was changed to a deprecation warning instead.
PR references:
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#mypy-version-support)Mypy version support
Until now, Pydantic supported the mypy versions released less than 6 months ago to work with the mypy plugin. This incurred extra maintenance cost on our side, and as such we now only explicitly support the latest mypy released version.
PR reference: 
###  [#](https://pydantic.dev/articles/pydantic-v2-12-release#disable-virtual-subclassing-capabilities-on-pydantic-models)Disable virtual subclassing capabilities on Pydantic models
Note
This issue is not likely to affect any user, but is documented for completeness.
The CPython implementation has a long-standing `BaseModel` class uses 
To work around this issue, Pydantic implemented partial optimization in `isinstance()`/`issubclass()` model checks. However, this ended up breaking virtual subclasses (see the 
As such, we restored the `isinstance()`/`issubclass()` behavior to how it is normally implemented, and using the 
PR reference: 
## Related content
[View all articles](https://pydantic.dev/articles)
[ /Release Announcement: Pydantic v2.11 Release ![Sydney Runkle](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/54324534)Sydney Runkle 2025/03/27 ](https://pydantic.dev/articles/pydantic-v2-11-release)[ /Release Announcement: Pydantic v2.10 Release ![Sydney Runkle](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/54324534)Sydney Runkle 2024/11/13 ](https://pydantic.dev/articles/pydantic-v2-10-release)
### Explore Logfire
[Get started Get started](https://pydantic.dev/contact)
