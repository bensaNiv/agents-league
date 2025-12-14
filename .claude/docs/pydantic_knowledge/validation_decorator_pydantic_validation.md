---
# Smart Librarian Export (v2.0)
- Page Number: 16
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/validation_decorator
- Page Title: Validation Decorator - Pydantic Validation
- Semantic Filename: validation_decorator_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 12,954 characters
---

# Validation Decorator - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/concepts/validation_decorator/#parameter-types)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Validation Decorator
API Documentation
[`pydantic.validate_call_decorator.validate_call`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call)  

The [`validate_call()`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call) decorator allows the arguments passed to a function to be parsed and validated using the function's annotations before the function is called.
While under the hood this uses the same approach of model creation and initialisation (see [Validators](https://docs.pydantic.dev/latest/concepts/validators/) for more details), it provides an extremely easy way to apply validation to your code with minimal boilerplate.
Example of usage:
```
frompydanticimport ValidationError, validate_call


@validate_call
defrepeat(s: str, count: int, *, separator: bytes = b'') -> bytes:
    b = s.encode()
    return separator.join(b for _ in range(count))


a = repeat('hello', 3)
print(a)
#> b'hellohellohello'

b = repeat('x', '4', separator=b' ')
print(b)
#> b'x x x x'

try:
    c = repeat('hello', 'wrong')
except ValidationError as exc:
    print(exc)
"""
    1 validation error for repeat
    1
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='wrong', input_type=str]
    """

```

## Parameter types[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#parameter-types)
Parameter types are inferred from type annotations on the function, or as [types](https://docs.pydantic.dev/latest/concepts/types/) can be validated, including Pydantic models and [custom types](https://docs.pydantic.dev/latest/concepts/types/#custom-types). As with the rest of Pydantic, types are by default coerced by the decorator before they're passed to the actual function:
```
fromdatetimeimport date

frompydanticimport validate_call


@validate_call
defgreater_than(d1: date, d2: date, *, include_equal=False) -> date:  [](https://docs.pydantic.dev/latest/concepts/validation_decorator/#__code_1_annotation_1)
    if include_equal:
        return d1 >= d2
    else:
        return d1 > d2


d1 = '2000-01-01'  [](https://docs.pydantic.dev/latest/concepts/validation_decorator/#__code_1_annotation_2)
d2 = date(2001, 1, 1)
greater_than(d1, d2, include_equal=True)

```

Type coercion like this can be extremely helpful, but also confusing or not desired (see [model data conversion](https://docs.pydantic.dev/latest/concepts/models/#data-conversion)). [Strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) can be enabled by using a [custom configuration](https://docs.pydantic.dev/latest/concepts/validation_decorator/#custom-configuration).
Validating the return value
By default, the return value of the function is **not** validated. To do so, the `validate_return` argument of the decorator can be set to `True`.
## Function signatures[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#function-signatures)
The [`validate_call()`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call) decorator is designed to work with functions using all possible 
  * Positional or keyword parameters with or without defaults.
  * Keyword-only parameters: parameters after `*,`.
  * Positional-only parameters: parameters before `, /`.
  * Variable positional parameters defined via `*` (often `*args`).
  * Variable keyword parameters defined via `**` (often `**kwargs`).

Example
```
frompydanticimport validate_call


@validate_call
defpos_or_kw(a: int, b: int = 2) -> str:
    return f'a={a} b={b}'


print(pos_or_kw(1, b=3))
#> a=1 b=3


@validate_call
defkw_only(*, a: int, b: int = 2) -> str:
    return f'a={a} b={b}'


print(kw_only(a=1))
#> a=1 b=2
print(kw_only(a=1, b=3))
#> a=1 b=3


@validate_call
defpos_only(a: int, b: int = 2, /) -> str:
    return f'a={a} b={b}'


print(pos_only(1))
#> a=1 b=2


@validate_call
defvar_args(*args: int) -> str:
    return str(args)


print(var_args(1))
#> (1,)
print(var_args(1, 2, 3))
#> (1, 2, 3)


@validate_call
defvar_kwargs(**kwargs: int) -> str:
    return str(kwargs)


print(var_kwargs(a=1))
#> {'a': 1}
print(var_kwargs(a=1, b=2))
#> {'a': 1, 'b': 2}


@validate_call
defarmageddon(
    a: int,
    /,
    b: int,
    *c: int,
    d: int,
    e: int = None,
    **f: int,
) -> str:
    return f'a={a} b={b} c={c} d={d} e={e} f={f}'


print(armageddon(1, 2, d=3))
#> a=1 b=2 c=() d=3 e=None f={}
print(armageddon(1, 2, 3, 4, 5, 6, d=8, e=9, f=10, spam=11))
#> a=1 b=2 c=(3, 4, 5, 6) d=8 e=9 f={'f': 10, 'spam': 11}

```

```
fromtyping_extensionsimport TypedDict, Unpack

frompydanticimport validate_call


classPoint(TypedDict):
    x: int
    y: int


@validate_call
defadd_coords(**kwargs: Unpack[Point]) -> int:
    return kwargs['x'] + kwargs['y']


add_coords(x=1, y=2)

```

For reference, see the 
## Using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function to describe function parameters[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#using-the-field-function-to-describe-function-parameters)
The [`Field()` function](https://docs.pydantic.dev/latest/concepts/fields/) can also be used with the decorator to provide extra information about the field and validations. If you don't make use of the `default` or `default_factory` parameter, it is recommended to use the [annotated pattern](https://docs.pydantic.dev/latest/concepts/fields/#the-annotated-pattern) (so that type checkers infer the parameter as being required). Otherwise, the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function can be used as a default value (again, to trick type checkers into thinking a default value is provided for the parameter).
```
fromtypingimport Annotated

frompydanticimport Field, ValidationError, validate_call


@validate_call
defhow_many(num: Annotated[int, Field(gt=10)]):
    return num


try:
    how_many(1)
except ValidationError as e:
    print(e)
"""
    1 validation error for how_many
    0
      Input should be greater than 10 [type=greater_than, input_value=1, input_type=int]
    """


@validate_call
defreturn_value(value: str = Field(default='default value')):
    return value


print(return_value())
#> default value

```

[Aliases](https://docs.pydantic.dev/latest/concepts/fields/#field-aliases) can be used with the decorator as normal:
```
fromtypingimport Annotated

frompydanticimport Field, validate_call


@validate_call
defhow_many(num: Annotated[int, Field(gt=10, alias='number')]):
    return num


how_many(number=42)

```

## Accessing the original function[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#accessing-the-original-function)
The original function which was decorated can still be accessed by using the `raw_function` attribute. This is useful if in some scenarios you trust your input arguments and want to call the function in the most efficient way (see [notes on performance](https://docs.pydantic.dev/latest/concepts/validation_decorator/#performance) below):
```
frompydanticimport validate_call


@validate_call
defrepeat(s: str, count: int, *, separator: bytes = b'') -> bytes:
    b = s.encode()
    return separator.join(b for _ in range(count))


a = repeat('hello', 3)
print(a)
#> b'hellohellohello'

b = repeat.raw_function('good bye', 2, separator=b', ')
print(b)
#> b'good bye, good bye'

```

## Async functions[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#async-functions)
[`validate_call()`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call) can also be used on async functions:
```
classConnection:
    async defexecute(self, sql, *args):
        return 'testing@example.com'


conn = Connection()
# ignore-above
importasyncio

frompydanticimport PositiveInt, ValidationError, validate_call


@validate_call
async defget_user_email(user_id: PositiveInt):
    # `conn` is some fictional connection to a database
    email = await conn.execute('select email from users where id=$1', user_id)
    if email is None:
        raise RuntimeError('user not found')
    else:
        return email


async defmain():
    email = await get_user_email(123)
    print(email)
    #> testing@example.com
    try:
        await get_user_email(-4)
    except ValidationError as exc:
        print(exc.errors())
"""
        [
            {
                'type': 'greater_than',
                'loc': (0,),
                'msg': 'Input should be greater than 0',
                'input': -4,
                'ctx': {'gt': 0},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        """


asyncio.run(main())
# requires: `conn.execute()` that will return `'testing@example.com'`

```

## Compatibility with type checkers[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#compatibility-with-type-checkers)
As the [`validate_call()`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call) decorator preserves the decorated function's signature, it should be compatible with type checkers (such as mypy and pyright). However, due to current limitations in the Python type system, the [`raw_function`](https://docs.pydantic.dev/latest/concepts/validation_decorator/#accessing-the-original-function) or other attributes won't be recognized and you will need to suppress the error using (usually with a `# type: ignore` comment).
## Custom configuration[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#custom-configuration)
Similarly to Pydantic models, the `config` parameter of the decorator can be used to specify a custom configuration:
```
frompydanticimport ConfigDict, ValidationError, validate_call


classFoobar:
    def__init__(self, v: str):
        self.v = v

    def__add__(self, other: 'Foobar') -> str:
        return f'{self} + {other}'

    def__str__(self) -> str:
        return f'Foobar({self.v})'


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
defadd_foobars(a: Foobar, b: Foobar):
    return a + b


c = add_foobars(Foobar('a'), Foobar('b'))
print(c)
#> Foobar(a) + Foobar(b)

try:
    add_foobars(1, 2)
except ValidationError as e:
    print(e)
"""
    2 validation errors for add_foobars
    0
      Input should be an instance of Foobar [type=is_instance_of, input_value=1, input_type=int]
    1
      Input should be an instance of Foobar [type=is_instance_of, input_value=2, input_type=int]
    """

```

## Extension — validating arguments before calling a function[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#extension-validating-arguments-before-calling-a-function)
In some cases, it may be helpful to separate validation of a function's arguments from the function call itself. This might be useful when a particular function is costly/time consuming.
Here's an example of a workaround you can use for that pattern:
```
frompydanticimport validate_call


@validate_call
defvalidate_foo(a: int, b: int):
    deffoo():
        return a + b

    return foo


foo = validate_foo(a=1, b=2)
print(foo())
#> 3

```

## Limitations[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#limitations)
### Validation exception[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#validation-exception)
Currently upon validation failure, a standard Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) is raised (see [model error handling](https://docs.pydantic.dev/latest/concepts/models/#error-handling) for details). This is also true for missing required arguments, where Python normally raises a 
### Performance[¶](https://docs.pydantic.dev/latest/concepts/validation_decorator/#performance)
We've made a big effort to make Pydantic as performant as possible. While the inspection of the decorated function is only performed once, there will still be a performance impact when making calls to the function compared to using the original function.
In many situations, this will have little or no noticeable effect. However, be aware that [`validate_call()`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call) is not an equivalent or alternative to function definitions in strongly typed languages, and it never will be.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
