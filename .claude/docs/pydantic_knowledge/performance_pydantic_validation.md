---
# Smart Librarian Export (v2.0)
- Page Number: 37
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/performance
- Page Title: Performance - Pydantic Validation
- Semantic Filename: performance_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 7,405 characters
---

# Performance - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/performance/#performance-tips)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Performance tips[¶](https://docs.pydantic.dev/latest/concepts/performance/#performance-tips)
In most cases Pydantic won't be your bottle neck, only follow this if you're sure it's necessary.
## In general, use `model_validate_json()` not `model_validate(json.loads(...))`[¶](https://docs.pydantic.dev/latest/concepts/performance/#in-general-use-model_validate_json-not-model_validatejsonloads)
On `model_validate(json.loads(...))`, the JSON is parsed in Python, then converted to a dict, then it's validated internally. On the other hand, `model_validate_json()` already performs the validation internally.
There are a few cases where `model_validate(json.loads(...))` may be faster. Specifically, when using a `'before'` or `'wrap'` validator on a model, validation may be faster with the two step method. You can read more about these special cases in 
Many performance improvements are currently in the works for `pydantic-core`, see `model_validate_json()` is always faster than `model_validate(json.loads(...))`.
##  `TypeAdapter` instantiated once[¶](https://docs.pydantic.dev/latest/concepts/performance/#typeadapter-instantiated-once)
The idea here is to avoid constructing validators and serializers more than necessary. Each time a `TypeAdapter` is instantiated, it will construct a new validator and serializer. If you're using a `TypeAdapter` in a function, it will be instantiated each time the function is called. Instead, instantiate it once, and reuse it.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Bad](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Good](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_1_2)
```
frompydanticimport TypeAdapter


defmy_func():
    adapter = TypeAdapter(list[int])
    # do something with adapter

```

```
frompydanticimport TypeAdapter

adapter = TypeAdapter(list[int])

defmy_func():
    ...
    # do something with adapter

```

##  `Sequence` vs `list` or `tuple` with `Mapping` vs `dict`[¶](https://docs.pydantic.dev/latest/concepts/performance/#sequence-vs-list-or-tuple-with-mapping-vs-dict)
When using `Sequence`, Pydantic calls `isinstance(value, Sequence)` to check if the value is a sequence. Also, Pydantic will try to validate against different types of sequences, like `list` and `tuple`. If you know the value is a `list` or `tuple`, use `list` or `tuple` instead of `Sequence`.
The same applies to `Mapping` and `dict`. If you know the value is a `dict`, use `dict` instead of `Mapping`.
## Don't do validation when you don't have to, use `Any` to keep the value unchanged[¶](https://docs.pydantic.dev/latest/concepts/performance/#dont-do-validation-when-you-dont-have-to-use-any-to-keep-the-value-unchanged)
If you don't need to validate a value, use `Any` to keep the value unchanged.
```
fromtypingimport Any

frompydanticimport BaseModel


classModel(BaseModel):
    a: Any


model = Model(a=1)

```

## Avoid extra information via subclasses of primitives[¶](https://docs.pydantic.dev/latest/concepts/performance/#avoid-extra-information-via-subclasses-of-primitives)
[Don't do this](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_2_1)[Do this](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_2_2)
```
classCompletedStr(str):
    def__init__(self, s: str):
        self.s = s
        self.done = False

```

```
frompydanticimport BaseModel


classCompletedModel(BaseModel):
    s: str
    done: bool = False

```

## Use tagged union, not union[¶](https://docs.pydantic.dev/latest/concepts/performance/#use-tagged-union-not-union)
Tagged union (or discriminated union) is a union with a field that indicates which type it is.
```
fromtypingimport Any, Literal

frompydanticimport BaseModel, Field


classDivModel(BaseModel):
    el_type: Literal['div'] = 'div'
    class_name: str | None = None
    children: list[Any] | None = None


classSpanModel(BaseModel):
    el_type: Literal['span'] = 'span'
    class_name: str | None = None
    contents: str | None = None


classButtonModel(BaseModel):
    el_type: Literal['button'] = 'button'
    class_name: str | None = None
    contents: str | None = None


classInputModel(BaseModel):
    el_type: Literal['input'] = 'input'
    class_name: str | None = None
    value: str | None = None


classHtml(BaseModel):
    contents: DivModel | SpanModel | ButtonModel | InputModel = Field(
        discriminator='el_type'
    )

```

See [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) for more details.
## Use `TypedDict` over nested models[¶](https://docs.pydantic.dev/latest/concepts/performance/#use-typeddict-over-nested-models)
Instead of using nested models, use `TypedDict` to define the structure of the data.
Performance comparison
With a simple benchmark, `TypedDict` is about ~2.5x faster than nested models:
```
fromtimeitimport timeit

fromtyping_extensionsimport TypedDict

frompydanticimport BaseModel, TypeAdapter


classA(TypedDict):
    a: str
    b: int


classTypedModel(TypedDict):
    a: A


classB(BaseModel):
    a: str
    b: int


classModel(BaseModel):
    b: B


ta = TypeAdapter(TypedModel)
result1 = timeit(
    lambda: ta.validate_python({'a': {'a': 'a', 'b': 2}}), number=10000
)
result2 = timeit(
    lambda: Model.model_validate({'b': {'a': 'a', 'b': 2}}), number=10000
)
print(result2 / result1)

```

## Avoid wrap validators if you really care about performance[¶](https://docs.pydantic.dev/latest/concepts/performance/#avoid-wrap-validators-if-you-really-care-about-performance)
Wrap validators are generally slower than other validators. This is because they require that data is materialized in Python during validation. Wrap validators can be incredibly useful for complex validation logic, but if you're looking for the best performance, you should avoid them.
## Failing early with `FailFast`[¶](https://docs.pydantic.dev/latest/concepts/performance/#failing-early-with-failfast)
Starting in v2.8+, you can apply the `FailFast` annotation to sequence types to fail early if any item in the sequence fails validation. If you use this annotation, you won't get validation errors for the rest of the items in the sequence if one fails, so you're effectively trading off visibility for performance.
```
fromtypingimport Annotated

frompydanticimport FailFast, TypeAdapter, ValidationError

ta = TypeAdapter(Annotated[list[bool], FailFast()])
try:
    ta.validate_python([True, 'invalid', False, 'also invalid'])
except ValidationError as exc:
    print(exc)
"""
    1 validation error for list[bool]
    1
      Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value='invalid', input_type=str]
    """

```

Read more about `FailFast` [here](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FailFast).
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
