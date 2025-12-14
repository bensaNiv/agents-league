---
# Smart Librarian Export (v2.0)
- Page Number: 44
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/forward_annotations
- Page Title: Forward Annotations - Pydantic Validation
- Semantic Filename: forward_annotations_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 7,781 characters
---

# Forward Annotations - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/forward_annotations/#self-referencing-or-recursive-models)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Forward Annotations
Forward annotations (wrapped in quotes) or using the `from __future__ import annotations`
```
from__future__import annotations

frompydanticimport BaseModel

MyInt = int


classModel(BaseModel):
    a: MyInt
    # Without the future import, equivalent to:
    # a: 'MyInt'


print(Model(a='1'))
#> a=1

```

As shown in the following sections, forward annotations are useful when you want to reference a type that is not yet defined in your code.
The internal logic to resolve forward annotations is described in detail in [this section](https://docs.pydantic.dev/latest/internals/resolving_annotations/).
## Self-referencing (or "Recursive") Models[¶](https://docs.pydantic.dev/latest/concepts/forward_annotations/#self-referencing-or-recursive-models)
Models with self-referencing fields are also supported. These annotations will be resolved during model creation.
Within the model, you can either add the `from __future__ import annotations` import or wrap the annotation in a string:
```
fromtypingimport Optional

frompydanticimport BaseModel


classFoo(BaseModel):
    a: int = 123
    sibling: 'Optional[Foo]' = None


print(Foo())
#> a=123 sibling=None
print(Foo(sibling={'a': '321'}))
#> a=123 sibling=Foo(a=321, sibling=None)

```

### Cyclic references[¶](https://docs.pydantic.dev/latest/concepts/forward_annotations/#cyclic-references)
When working with self-referencing recursive models, it is possible that you might encounter cyclic references in validation inputs. For example, this can happen when validating ORM instances with back-references from attributes.
Rather than raising a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError):
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/forward_annotations/#__tabbed_1_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/forward_annotations/#__tabbed_1_2)
```
fromtypingimport Optional

frompydanticimport BaseModel, ValidationError


classModelA(BaseModel):
    b: 'Optional[ModelB]' = None


classModelB(BaseModel):
    a: Optional[ModelA] = None


cyclic_data = {}
cyclic_data['a'] = {'b': cyclic_data}
print(cyclic_data)
#> {'a': {'b': {...}}}

try:
    ModelB.model_validate(cyclic_data)
except ValidationError as exc:
    print(exc)
"""
    1 validation error for ModelB
    a.b
      Recursion error - cyclic reference detected [type=recursion_loop, input_value={'a': {'b': {...}}}, input_type=dict]
    """

```

```
fromtypingimport Optional

frompydanticimport BaseModel, ValidationError


classModelA(BaseModel):
    b: 'Optional[ModelB]' = None


classModelB(BaseModel):
    a: ModelA | None = None


cyclic_data = {}
cyclic_data['a'] = {'b': cyclic_data}
print(cyclic_data)
#> {'a': {'b': {...}}}

try:
    ModelB.model_validate(cyclic_data)
except ValidationError as exc:
    print(exc)
"""
    1 validation error for ModelB
    a.b
      Recursion error - cyclic reference detected [type=recursion_loop, input_value={'a': {'b': {...}}}, input_type=dict]
    """

```

Because this error is raised without actually exceeding the maximum recursion depth, you can catch and handle the raised [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) without needing to worry about the limited remaining recursion depth:
```
from__future__import annotations

fromcollections.abcimport Generator
fromcontextlibimport contextmanager
fromdataclassesimport field

frompydanticimport BaseModel, ValidationError, field_validator


defis_recursion_validation_error(exc: ValidationError) -> bool:
    errors = exc.errors()
    return len(errors) == 1 and errors[0]['type'] == 'recursion_loop'


@contextmanager
defsuppress_recursion_validation_error() -> Generator[None]:
    try:
        yield
    except ValidationError as exc:
        if not is_recursion_validation_error(exc):
            raise exc


classNode(BaseModel):
    id: int
    children: list[Node] = field(default_factory=list)

    @field_validator('children', mode='wrap')
    @classmethod
    defdrop_cyclic_references(cls, children, h):
        try:
            return h(children)
        except ValidationError as exc:
            if not (
                is_recursion_validation_error(exc)
                and isinstance(children, list)
            ):
                raise exc

            value_without_cyclic_refs = []
            for child in children:
                with suppress_recursion_validation_error():
                    value_without_cyclic_refs.extend(h([child]))
            return h(value_without_cyclic_refs)


# Create data with cyclic references representing the graph 1 -> 2 -> 3 -> 1
node_data = {'id': 1, 'children': [{'id': 2, 'children': [{'id': 3}]}]}
node_data['children'][0]['children'][0]['children'] = [node_data]

print(Node.model_validate(node_data))
#> id=1 children=[Node(id=2, children=[Node(id=3, children=[])])]

```

Similarly, if Pydantic encounters a recursive reference during _serialization_ , rather than waiting for the maximum recursion depth to be exceeded, a 
```
frompydanticimport TypeAdapter

# Create data with cyclic references representing the graph 1 -> 2 -> 3 -> 1
node_data = {'id': 1, 'children': [{'id': 2, 'children': [{'id': 3}]}]}
node_data['children'][0]['children'][0]['children'] = [node_data]

try:
    # Try serializing the circular reference as JSON
    TypeAdapter(dict).dump_json(node_data)
except ValueError as exc:
    print(exc)
"""
    Error serializing to JSON: ValueError: Circular reference detected (id repeated)
    """

```

This can also be handled if desired:
```
fromdataclassesimport field
fromtypingimport Any

frompydanticimport (
    SerializerFunctionWrapHandler,
    TypeAdapter,
    field_serializer,
)
frompydantic.dataclassesimport dataclass


@dataclass
classNodeReference:
    id: int


@dataclass
classNode(NodeReference):
    children: list['Node'] = field(default_factory=list)

    @field_serializer('children', mode='wrap')
    defserialize(
        self, children: list['Node'], handler: SerializerFunctionWrapHandler
    ) -> Any:
"""
        Serialize a list of nodes, handling circular references by excluding the children.
        """
        try:
            return handler(children)
        except ValueError as exc:
            if not str(exc).startswith('Circular reference'):
                raise exc

            result = []
            for node in children:
                try:
                    serialized = handler([node])
                except ValueError as exc:
                    if not str(exc).startswith('Circular reference'):
                        raise exc
                    result.append({'id': node.id})
                else:
                    result.append(serialized)
            return result


# Create a cyclic graph:
nodes = [Node(id=1), Node(id=2), Node(id=3)]
nodes[0].children.append(nodes[1])
nodes[1].children.append(nodes[2])
nodes[2].children.append(nodes[0])

print(nodes[0])
#> Node(id=1, children=[Node(id=2, children=[Node(id=3, children=[...])])])

# Serialize the cyclic graph:
print(TypeAdapter(Node).dump_python(nodes[0]))
"""
{
    'id': 1,
    'children': [{'id': 2, 'children': [{'id': 3, 'children': [{'id': 1}]}]}],
}
"""

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
