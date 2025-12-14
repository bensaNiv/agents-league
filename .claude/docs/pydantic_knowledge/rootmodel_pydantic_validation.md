---
# Smart Librarian Export (v2.0)
- Page Number: 46
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/api/root_model
- Page Title: RootModel - Pydantic Validation
- Semantic Filename: rootmodel_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 5,783 characters
---

# RootModel - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/api/root_model/#pydantic.root_model)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# RootModel
RootModel class and type definitions.
##  RootModel [¶](https://docs.pydantic.dev/latest/api/root_model/#pydantic.root_model.RootModel)
```
RootModel(
    root: RootModelRootType = PydanticUndefined, **data
)

```

Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)`, `RootModelRootType]`
Usage Documentation
[`RootModel` and Custom Root Types](https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types)
A Pydantic `BaseModel` for the root object of the model.
Attributes:
Name | Type | Description  
---|---|---  
`root` |  `RootModelRootType` |  The root object of the model.  
`__pydantic_root_model__` |  |  Whether the model is a RootModel.  
`__pydantic_private__` |  |  Private fields in the model.  
`__pydantic_extra__` |  |  Extra fields in the model.  
Source code in `pydantic/root_model.py`
```
60
61
62
63
64
65
66
67
68
```
| ```
def__init__(self, /, root: RootModelRootType = PydanticUndefined, **data) -> None:  # type: ignore
    __tracebackhide__ = True
    if data:
        if root is not PydanticUndefined:
            raise ValueError(
                '"RootModel.__init__" accepts either a single positional argument or arbitrary keyword arguments'
            )
        root = data  # type: ignore
    self.__pydantic_validator__.validate_python(root, self_instance=self)

```
  
---|---  
###  model_construct `classmethod` [¶](https://docs.pydantic.dev/latest/api/root_model/#pydantic.root_model.RootModel.model_construct)
```
model_construct(
    root: RootModelRootType,
    _fields_set: [] | None = None,
) -> 
```

Create a new model using the provided root object and update fields set.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`root` |  `RootModelRootType` |  The root object of the model. |  _required_  
`_fields_set` |  |  The set of fields to be updated. |  `None`  
Returns:
Type | Description  
---|---  
|  The new model.  
Raises:
Type | Description  
---|---  
|  If the model is not a subclass of `RootModel`.  
Source code in `pydantic/root_model.py`
```
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
```
| ```
@classmethod
defmodel_construct(cls, root: RootModelRootType, _fields_set: set[str] | None = None) -> Self:  # type: ignore
"""Create a new model using the provided root object and update fields set.

    Args:
        root: The root object of the model.
        _fields_set: The set of fields to be updated.

    Returns:
        The new model.

    Raises:
        NotImplemented: If the model is not a subclass of `RootModel`.
    """
    return super().model_construct(root=root, _fields_set=_fields_set)

```
  
---|---  
###  model_dump [¶](https://docs.pydantic.dev/latest/api/root_model/#pydantic.root_model.RootModel.model_dump)
```
model_dump(
    *,
    mode: ["json", "python"] | = "python",
    include: = None,
    exclude: = None,
    context: [, ] | None = None,
    by_alias: | None = None,
    exclude_unset: = False,
    exclude_defaults: = False,
    exclude_none: = False,
    exclude_computed_fields: = False,
    round_trip: = False,
    warnings: (
        | ["none", "warn", "error"]
    ) = True,
    serialize_as_any: = False
) -> 
```

This method is included just to get a more accurate return type for type checkers. It is included in this `if TYPE_CHECKING:` block since no override is actually necessary.
See the documentation of `BaseModel.model_dump` for more details about the arguments.
Generally, this method will have a return type of `RootModelRootType`, assuming that `RootModelRootType` is not a `BaseModel` subclass. If `RootModelRootType` is a `BaseModel` subclass, then the return type will likely be `dict[str, Any]`, as `model_dump` calls are recursive. The return type could even be something different, in the case of a custom serializer. Thus, `Any` is used here to catch all of these cases.
Source code in `pydantic/root_model.py`
```
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
141
142
143
144
145
```
| ```
defmodel_dump(  # type: ignore
    self,
    *,
    mode: Literal['json', 'python'] | str = 'python',
    include: Any = None,
    exclude: Any = None,
    context: dict[str, Any] | None = None,
    by_alias: bool | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    exclude_computed_fields: bool = False,
    round_trip: bool = False,
    warnings: bool | Literal['none', 'warn', 'error'] = True,
    serialize_as_any: bool = False,
) -> Any:
"""This method is included just to get a more accurate return type for type checkers.
    It is included in this `if TYPE_CHECKING:` block since no override is actually necessary.

    See the documentation of `BaseModel.model_dump` for more details about the arguments.

    Generally, this method will have a return type of `RootModelRootType`, assuming that `RootModelRootType` is
    not a `BaseModel` subclass. If `RootModelRootType` is a `BaseModel` subclass, then the return
    type will likely be `dict[str, Any]`, as `model_dump` calls are recursive. The return type could
    even be something different, in the case of a custom serializer.
    Thus, `Any` is used here to catch all of these cases.
    """
    ...

```
  
---|---  
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
