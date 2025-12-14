---
# Smart Librarian Export (v2.0)
- Page Number: 35
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest/concepts/conversion_table
- Page Title: Conversion Table - Pydantic Validation
- Semantic Filename: conversion_table_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 27,698 characters
---

# Conversion Table - Pydantic Validation

What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Conversion Table
The following table provides details on how Pydantic converts data during validation in both strict and lax modes.
The "Strict" column contains checkmarks for type conversions that are allowed when validating in [Strict Mode](https://docs.pydantic.dev/latest/concepts/strict_mode/).
[All](https://docs.pydantic.dev/latest/concepts/conversion_table/#__tabbed_1_1)[JSON](https://docs.pydantic.dev/latest/concepts/conversion_table/#__tabbed_1_2)[JSON - Strict](https://docs.pydantic.dev/latest/concepts/conversion_table/#__tabbed_1_3)[Python](https://docs.pydantic.dev/latest/concepts/conversion_table/#__tabbed_1_4)[Python - Strict](https://docs.pydantic.dev/latest/concepts/conversion_table/#__tabbed_1_5)
Field Type | Input | Strict | Input Source | Conditions  
---|---|---|---|---  
`bool` | `bool` | ✓ | Python & JSON |   
`bool` | `float` |  | Python & JSON | Allowed values: `0.0, 1.0`.  
`bool` | `int` |  | Python & JSON | Allowed values: `0, 1`.  
`bool` | `str` |  | Python & JSON | Allowed values: `'f'`, `'n'`, `'no'`, `'off'`, `'false'`, `'False'`, `'t'`, `'y'`, `'on'`, `'yes'`, `'true'`, `'True'`.  
`bool` | `Decimal` |  | Python | Allowed values: `Decimal(0), Decimal(1)`.  
`bytes` | `bytearray` |  | Python |   
`bytes` | `bytes` | ✓ | Python |   
`bytes` | `str` | ✓ | JSON |   
`bytes` | `str` |  | Python |   
`callable` | `-` |  | JSON | Never valid.  
`callable` | `Any` | ✓ | Python |  `callable()` check must return `True`.  
`date` | `bytes` |  | Python | Format: `YYYY-MM-DD` (UTF-8).  
`date` | `date` | ✓ | Python |   
`date` | `datetime` |  | Python | Must be exact date, eg. no `H`, `M`, `S`, `f`.  
`date` | `float` |  | Python & JSON | Interpreted as seconds or ms from epoch. See   
`date` | `int` |  | Python & JSON | Interpreted as seconds or ms from epoch. See   
`date` | `str` |  | Python & JSON | Format: `YYYY-MM-DD`.  
`date` | `Decimal` |  | Python | Interpreted as seconds or ms from epoch. See   
`datetime` | `bytes` |  | Python | Format: `YYYY-MM-DDTHH:MM:SS.f` or `YYYY-MM-DD`. See   
`datetime` | `date` |  | Python |   
`datetime` | `datetime` | ✓ | Python |   
`datetime` | `float` |  | Python & JSON | Interpreted as seconds or ms from epoch, see   
`datetime` | `int` |  | Python & JSON | Interpreted as seconds or ms from epoch, see   
`datetime` | `str` |  | Python & JSON | Format: `YYYY-MM-DDTHH:MM:SS.f` or `YYYY-MM-DD`. See   
`datetime` | `Decimal` |  | Python | Interpreted as seconds or ms from epoch, see   
`deque` | `deque` | ✓ | Python |   
`deque` | `frozenset` |  | Python |   
`deque` | `list` |  | Python |   
`deque` | `set` |  | Python |   
`deque` | `tuple` |  | Python |   
`deque` | `Array` | ✓ | JSON |   
`dict` | `dict` | ✓ | Python |   
`dict` | `Mapping` |  | Python | Must implement the mapping interface and have an `items()` method.  
`dict` | `Object` | ✓ | JSON |   
`float` | `bool` |  | Python & JSON |   
`float` | `bytes` |  | Python | Must match `[0-9]+(\.[0-9]+)?`.  
`float` | `float` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`float` | `int` | ✓ | Python & JSON |   
`float` | `str` |  | Python & JSON | Must match `[0-9]+(\.[0-9]+)?`.  
`float` | `Decimal` |  | Python |   
`frozenset` | `deque` |  | Python |   
`frozenset` | `dict_keys` |  | Python |   
`frozenset` | `dict_values` |  | Python |   
`frozenset` | `frozenset` | ✓ | Python |   
`frozenset` | `list` |  | Python |   
`frozenset` | `set` |  | Python |   
`frozenset` | `tuple` |  | Python |   
`frozenset` | `Array` | ✓ | JSON |   
`int` | `bool` |  | Python & JSON |   
`int` | `bytes` |  | Python | Must be numeric only, e.g. `[0-9]+`.  
`int` | `float` |  | Python & JSON | Must be exact int, e.g. `val % 1 == 0`, raises error for `nan`, `inf`.  
`int` | `int` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`int` | `int` |  | Python & JSON |   
`int` | `str` |  | Python & JSON | Must be numeric only, e.g. `[0-9]+`.  
`int` | `Decimal` |  | Python | Must be exact int, e.g. `val % 1 == 0`.  
`list` | `deque` |  | Python |   
`list` | `dict_keys` |  | Python |   
`list` | `dict_values` |  | Python |   
`list` | `frozenset` |  | Python |   
`list` | `list` | ✓ | Python |   
`list` | `set` |  | Python |   
`list` | `tuple` |  | Python |   
`list` | `Array` | ✓ | JSON |   
`namedtuple` | `dict` | ✓ | Python |   
`namedtuple` | `list` | ✓ | Python |   
`namedtuple` | `namedtuple` | ✓ | Python |   
`namedtuple` | `tuple` | ✓ | Python |   
`namedtuple` | `Array` | ✓ | JSON |   
`namedtuple` | `NamedTuple` | ✓ | Python |   
`set` | `deque` |  | Python |   
`set` | `dict_keys` |  | Python |   
`set` | `dict_values` |  | Python |   
`set` | `frozenset` |  | Python |   
`set` | `list` |  | Python |   
`set` | `set` | ✓ | Python |   
`set` | `tuple` |  | Python |   
`set` | `Array` | ✓ | JSON |   
`str` | `bytearray` |  | Python | Assumes UTF-8, error on unicode decoding error.  
`str` | `bytes` |  | Python | Assumes UTF-8, error on unicode decoding error.  
`str` | `str` | ✓ | Python & JSON |   
`time` | `bytes` |  | Python | Format: `HH:MM:SS.FFFFFF`. See   
`time` | `float` |  | Python & JSON | Interpreted as seconds, range `0 - 86399.9*`.  
`time` | `int` |  | Python & JSON | Interpreted as seconds, range `0 - 86399`.  
`time` | `str` |  | Python & JSON | Format: `HH:MM:SS.FFFFFF`. See   
`time` | `time` | ✓ | Python |   
`time` | `Decimal` |  | Python | Interpreted as seconds, range `0 - 86399.9*`.  
`timedelta` | `bytes` |  | Python | Format: `ISO8601`. See   
`timedelta` | `float` |  | Python & JSON | Interpreted as seconds.  
`timedelta` | `int` |  | Python & JSON | Interpreted as seconds.  
`timedelta` | `str` |  | Python & JSON | Format: `ISO8601`. See   
`timedelta` | `timedelta` | ✓ | Python |   
`timedelta` | `Decimal` |  | Python | Interpreted as seconds.  
`tuple` | `deque` |  | Python |   
`tuple` | `dict_keys` |  | Python |   
`tuple` | `dict_values` |  | Python |   
`tuple` | `frozenset` |  | Python |   
`tuple` | `list` |  | Python |   
`tuple` | `set` |  | Python |   
`tuple` | `tuple` | ✓ | Python |   
`tuple` | `Array` | ✓ | JSON |   
`type` | `type` | ✓ | Python |   
`Any` | `Any` | ✓ | Python & JSON |   
`ByteSize` | `float` | ✓ | Python & JSON |   
`ByteSize` | `int` | ✓ | Python & JSON |   
`ByteSize` | `str` | ✓ | Python & JSON |   
`ByteSize` | `Decimal` | ✓ | Python |   
`Decimal` | `float` | ✓ | JSON |   
`Decimal` | `float` |  | Python & JSON |   
`Decimal` | `int` | ✓ | JSON |   
`Decimal` | `int` |  | Python & JSON |   
`Decimal` | `str` | ✓ | JSON |   
`Decimal` | `str` |  | Python & JSON | Must match `[0-9]+(\.[0-9]+)?`.  
`Decimal` | `Decimal` | ✓ | Python |   
`Enum` | `Any` | ✓ | JSON | Input value must be convertible to enum values.  
`Enum` | `Any` |  | Python | Input value must be convertible to enum values.  
`Enum` | `Enum` | ✓ | Python |   
`IPv4Address` | `bytes` |  | Python |   
`IPv4Address` | `int` |  | Python | integer representing the IP address, must be less than `2**32`  
`IPv4Address` | `str` | ✓ | JSON |   
`IPv4Address` | `str` |  | Python & JSON |   
`IPv4Address` | `IPv4Address` | ✓ | Python |   
`IPv4Address` | `IPv4Interface` | ✓ | Python |   
`IPv4Interface` | `bytes` |  | Python |   
`IPv4Interface` | `int` |  | Python | integer representing the IP address, must be less than `2**32`  
`IPv4Interface` | `str` | ✓ | JSON |   
`IPv4Interface` | `str` |  | Python & JSON |   
`IPv4Interface` | `tuple` |  | Python |   
`IPv4Interface` | `IPv4Address` |  | Python |   
`IPv4Interface` | `IPv4Interface` | ✓ | Python |   
`IPv4Network` | `bytes` |  | Python |   
`IPv4Network` | `int` |  | Python | integer representing the IP network, must be less than `2**32`  
`IPv4Network` | `str` | ✓ | JSON |   
`IPv4Network` | `str` |  | Python & JSON |   
`IPv4Network` | `IPv4Address` |  | Python |   
`IPv4Network` | `IPv4Interface` |  | Python |   
`IPv4Network` | `IPv4Network` | ✓ | Python |   
`IPv6Address` | `bytes` |  | Python |   
`IPv6Address` | `int` |  | Python | integer representing the IP address, must be less than `2**128`  
`IPv6Address` | `str` | ✓ | JSON |   
`IPv6Address` | `str` |  | Python & JSON |   
`IPv6Address` | `IPv6Address` | ✓ | Python |   
`IPv6Address` | `IPv6Interface` | ✓ | Python |   
`IPv6Interface` | `bytes` |  | Python |   
`IPv6Interface` | `int` |  | Python | integer representing the IP address, must be less than `2**128`  
`IPv6Interface` | `str` | ✓ | JSON |   
`IPv6Interface` | `str` |  | Python & JSON |   
`IPv6Interface` | `tuple` |  | Python |   
`IPv6Interface` | `IPv6Address` |  | Python |   
`IPv6Interface` | `IPv6Interface` | ✓ | Python |   
`IPv6Network` | `bytes` |  | Python |   
`IPv6Network` | `int` |  | Python | integer representing the IP address, must be less than `2**128`  
`IPv6Network` | `str` | ✓ | JSON |   
`IPv6Network` | `str` |  | Python & JSON |   
`IPv6Network` | `IPv6Address` |  | Python |   
`IPv6Network` | `IPv6Interface` |  | Python |   
`IPv6Network` | `IPv6Network` | ✓ | Python |   
`InstanceOf` | `-` |  | JSON | Never valid.  
`InstanceOf` | `Any` | ✓ | Python |  `isinstance()` check must return `True`.  
`IntEnum` | `Any` | ✓ | JSON | Input value must be convertible to enum values.  
`IntEnum` | `Any` |  | Python | Input value must be convertible to enum values.  
`IntEnum` | `IntEnum` | ✓ | Python |   
`Iterable` | `deque` | ✓ | Python |   
`Iterable` | `frozenset` | ✓ | Python |   
`Iterable` | `list` | ✓ | Python |   
`Iterable` | `set` | ✓ | Python |   
`Iterable` | `tuple` | ✓ | Python |   
`Iterable` | `Array` | ✓ | JSON |   
`NamedTuple` | `dict` | ✓ | Python |   
`NamedTuple` | `list` | ✓ | Python |   
`NamedTuple` | `namedtuple` | ✓ | Python |   
`NamedTuple` | `tuple` | ✓ | Python |   
`NamedTuple` | `Array` | ✓ | JSON |   
`NamedTuple` | `NamedTuple` | ✓ | Python |   
`None` | `None` | ✓ | Python & JSON |   
`Path` | `str` | ✓ | JSON |   
`Path` | `str` |  | Python |   
`Path` | `Path` | ✓ | Python |   
`Pattern` | `bytes` | ✓ | Python | Input must be a valid pattern.  
`Pattern` | `str` | ✓ | Python & JSON | Input must be a valid pattern.  
`Sequence` | `deque` |  | Python |   
`Sequence` | `list` | ✓ | Python |   
`Sequence` | `tuple` |  | Python |   
`Sequence` | `Array` | ✓ | JSON |   
`TypedDict` | `dict` | ✓ | Python |   
`TypedDict` | `Any` | ✓ | Python |   
`TypedDict` | `Mapping` |  | Python | Must implement the mapping interface and have an `items()` method.  
`TypedDict` | `Object` | ✓ | JSON |   
`UUID` | `str` | ✓ | JSON |   
`UUID` | `str` |  | Python |   
`UUID` | `UUID` | ✓ | Python |   
Field Type | Input | Strict | Input Source | Conditions  
---|---|---|---|---  
`bool` | `bool` | ✓ | Python & JSON |   
`bool` | `float` |  | Python & JSON | Allowed values: `0.0, 1.0`.  
`bool` | `int` |  | Python & JSON | Allowed values: `0, 1`.  
`bool` | `str` |  | Python & JSON | Allowed values: `'f'`, `'n'`, `'no'`, `'off'`, `'false'`, `'False'`, `'t'`, `'y'`, `'on'`, `'yes'`, `'true'`, `'True'`.  
`bytes` | `str` | ✓ | JSON |   
`callable` | `-` |  | JSON | Never valid.  
`date` | `float` |  | Python & JSON | Interpreted as seconds or ms from epoch. See   
`date` | `int` |  | Python & JSON | Interpreted as seconds or ms from epoch. See   
`date` | `str` |  | Python & JSON | Format: `YYYY-MM-DD`.  
`datetime` | `float` |  | Python & JSON | Interpreted as seconds or ms from epoch, see   
`datetime` | `int` |  | Python & JSON | Interpreted as seconds or ms from epoch, see   
`datetime` | `str` |  | Python & JSON | Format: `YYYY-MM-DDTHH:MM:SS.f` or `YYYY-MM-DD`. See   
`deque` | `Array` | ✓ | JSON |   
`dict` | `Object` | ✓ | JSON |   
`float` | `bool` |  | Python & JSON |   
`float` | `float` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`float` | `int` | ✓ | Python & JSON |   
`float` | `str` |  | Python & JSON | Must match `[0-9]+(\.[0-9]+)?`.  
`frozenset` | `Array` | ✓ | JSON |   
`int` | `bool` |  | Python & JSON |   
`int` | `float` |  | Python & JSON | Must be exact int, e.g. `val % 1 == 0`, raises error for `nan`, `inf`.  
`int` | `int` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`int` | `int` |  | Python & JSON |   
`int` | `str` |  | Python & JSON | Must be numeric only, e.g. `[0-9]+`.  
`list` | `Array` | ✓ | JSON |   
`namedtuple` | `Array` | ✓ | JSON |   
`set` | `Array` | ✓ | JSON |   
`str` | `str` | ✓ | Python & JSON |   
`time` | `float` |  | Python & JSON | Interpreted as seconds, range `0 - 86399.9*`.  
`time` | `int` |  | Python & JSON | Interpreted as seconds, range `0 - 86399`.  
`time` | `str` |  | Python & JSON | Format: `HH:MM:SS.FFFFFF`. See   
`timedelta` | `float` |  | Python & JSON | Interpreted as seconds.  
`timedelta` | `int` |  | Python & JSON | Interpreted as seconds.  
`timedelta` | `str` |  | Python & JSON | Format: `ISO8601`. See   
`tuple` | `Array` | ✓ | JSON |   
`Any` | `Any` | ✓ | Python & JSON |   
`ByteSize` | `float` | ✓ | Python & JSON |   
`ByteSize` | `int` | ✓ | Python & JSON |   
`ByteSize` | `str` | ✓ | Python & JSON |   
`Decimal` | `float` | ✓ | JSON |   
`Decimal` | `float` |  | Python & JSON |   
`Decimal` | `int` | ✓ | JSON |   
`Decimal` | `int` |  | Python & JSON |   
`Decimal` | `str` | ✓ | JSON |   
`Decimal` | `str` |  | Python & JSON | Must match `[0-9]+(\.[0-9]+)?`.  
`Enum` | `Any` | ✓ | JSON | Input value must be convertible to enum values.  
`IPv4Address` | `str` | ✓ | JSON |   
`IPv4Address` | `str` |  | Python & JSON |   
`IPv4Interface` | `str` | ✓ | JSON |   
`IPv4Interface` | `str` |  | Python & JSON |   
`IPv4Network` | `str` | ✓ | JSON |   
`IPv4Network` | `str` |  | Python & JSON |   
`IPv6Address` | `str` | ✓ | JSON |   
`IPv6Address` | `str` |  | Python & JSON |   
`IPv6Interface` | `str` | ✓ | JSON |   
`IPv6Interface` | `str` |  | Python & JSON |   
`IPv6Network` | `str` | ✓ | JSON |   
`IPv6Network` | `str` |  | Python & JSON |   
`InstanceOf` | `-` |  | JSON | Never valid.  
`IntEnum` | `Any` | ✓ | JSON | Input value must be convertible to enum values.  
`Iterable` | `Array` | ✓ | JSON |   
`NamedTuple` | `Array` | ✓ | JSON |   
`None` | `None` | ✓ | Python & JSON |   
`Path` | `str` | ✓ | JSON |   
`Pattern` | `str` | ✓ | Python & JSON | Input must be a valid pattern.  
`Sequence` | `Array` | ✓ | JSON |   
`TypedDict` | `Object` | ✓ | JSON |   
`UUID` | `str` | ✓ | JSON |   
Field Type | Input | Strict | Input Source | Conditions  
---|---|---|---|---  
`bool` | `bool` | ✓ | Python & JSON |   
`bytes` | `str` | ✓ | JSON |   
`deque` | `Array` | ✓ | JSON |   
`dict` | `Object` | ✓ | JSON |   
`float` | `float` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`float` | `int` | ✓ | Python & JSON |   
`frozenset` | `Array` | ✓ | JSON |   
`int` | `int` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`list` | `Array` | ✓ | JSON |   
`namedtuple` | `Array` | ✓ | JSON |   
`set` | `Array` | ✓ | JSON |   
`str` | `str` | ✓ | Python & JSON |   
`tuple` | `Array` | ✓ | JSON |   
`Any` | `Any` | ✓ | Python & JSON |   
`ByteSize` | `float` | ✓ | Python & JSON |   
`ByteSize` | `int` | ✓ | Python & JSON |   
`ByteSize` | `str` | ✓ | Python & JSON |   
`Decimal` | `float` | ✓ | JSON |   
`Decimal` | `int` | ✓ | JSON |   
`Decimal` | `str` | ✓ | JSON |   
`Enum` | `Any` | ✓ | JSON | Input value must be convertible to enum values.  
`IPv4Address` | `str` | ✓ | JSON |   
`IPv4Interface` | `str` | ✓ | JSON |   
`IPv4Network` | `str` | ✓ | JSON |   
`IPv6Address` | `str` | ✓ | JSON |   
`IPv6Interface` | `str` | ✓ | JSON |   
`IPv6Network` | `str` | ✓ | JSON |   
`IntEnum` | `Any` | ✓ | JSON | Input value must be convertible to enum values.  
`Iterable` | `Array` | ✓ | JSON |   
`NamedTuple` | `Array` | ✓ | JSON |   
`None` | `None` | ✓ | Python & JSON |   
`Path` | `str` | ✓ | JSON |   
`Pattern` | `str` | ✓ | Python & JSON | Input must be a valid pattern.  
`Sequence` | `Array` | ✓ | JSON |   
`TypedDict` | `Object` | ✓ | JSON |   
`UUID` | `str` | ✓ | JSON |   
Field Type | Input | Strict | Input Source | Conditions  
---|---|---|---|---  
`bool` | `bool` | ✓ | Python & JSON |   
`bool` | `float` |  | Python & JSON | Allowed values: `0.0, 1.0`.  
`bool` | `int` |  | Python & JSON | Allowed values: `0, 1`.  
`bool` | `str` |  | Python & JSON | Allowed values: `'f'`, `'n'`, `'no'`, `'off'`, `'false'`, `'False'`, `'t'`, `'y'`, `'on'`, `'yes'`, `'true'`, `'True'`.  
`bool` | `Decimal` |  | Python | Allowed values: `Decimal(0), Decimal(1)`.  
`bytes` | `bytearray` |  | Python |   
`bytes` | `bytes` | ✓ | Python |   
`bytes` | `str` |  | Python |   
`callable` | `Any` | ✓ | Python |  `callable()` check must return `True`.  
`date` | `bytes` |  | Python | Format: `YYYY-MM-DD` (UTF-8).  
`date` | `date` | ✓ | Python |   
`date` | `datetime` |  | Python | Must be exact date, eg. no `H`, `M`, `S`, `f`.  
`date` | `float` |  | Python & JSON | Interpreted as seconds or ms from epoch. See   
`date` | `int` |  | Python & JSON | Interpreted as seconds or ms from epoch. See   
`date` | `str` |  | Python & JSON | Format: `YYYY-MM-DD`.  
`date` | `Decimal` |  | Python | Interpreted as seconds or ms from epoch. See   
`datetime` | `bytes` |  | Python | Format: `YYYY-MM-DDTHH:MM:SS.f` or `YYYY-MM-DD`. See   
`datetime` | `date` |  | Python |   
`datetime` | `datetime` | ✓ | Python |   
`datetime` | `float` |  | Python & JSON | Interpreted as seconds or ms from epoch, see   
`datetime` | `int` |  | Python & JSON | Interpreted as seconds or ms from epoch, see   
`datetime` | `str` |  | Python & JSON | Format: `YYYY-MM-DDTHH:MM:SS.f` or `YYYY-MM-DD`. See   
`datetime` | `Decimal` |  | Python | Interpreted as seconds or ms from epoch, see   
`deque` | `deque` | ✓ | Python |   
`deque` | `frozenset` |  | Python |   
`deque` | `list` |  | Python |   
`deque` | `set` |  | Python |   
`deque` | `tuple` |  | Python |   
`dict` | `dict` | ✓ | Python |   
`dict` | `Mapping` |  | Python | Must implement the mapping interface and have an `items()` method.  
`float` | `bool` |  | Python & JSON |   
`float` | `bytes` |  | Python | Must match `[0-9]+(\.[0-9]+)?`.  
`float` | `float` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`float` | `int` | ✓ | Python & JSON |   
`float` | `str` |  | Python & JSON | Must match `[0-9]+(\.[0-9]+)?`.  
`float` | `Decimal` |  | Python |   
`frozenset` | `deque` |  | Python |   
`frozenset` | `dict_keys` |  | Python |   
`frozenset` | `dict_values` |  | Python |   
`frozenset` | `frozenset` | ✓ | Python |   
`frozenset` | `list` |  | Python |   
`frozenset` | `set` |  | Python |   
`frozenset` | `tuple` |  | Python |   
`int` | `bool` |  | Python & JSON |   
`int` | `bytes` |  | Python | Must be numeric only, e.g. `[0-9]+`.  
`int` | `float` |  | Python & JSON | Must be exact int, e.g. `val % 1 == 0`, raises error for `nan`, `inf`.  
`int` | `int` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`int` | `int` |  | Python & JSON |   
`int` | `str` |  | Python & JSON | Must be numeric only, e.g. `[0-9]+`.  
`int` | `Decimal` |  | Python | Must be exact int, e.g. `val % 1 == 0`.  
`list` | `deque` |  | Python |   
`list` | `dict_keys` |  | Python |   
`list` | `dict_values` |  | Python |   
`list` | `frozenset` |  | Python |   
`list` | `list` | ✓ | Python |   
`list` | `set` |  | Python |   
`list` | `tuple` |  | Python |   
`namedtuple` | `dict` | ✓ | Python |   
`namedtuple` | `list` | ✓ | Python |   
`namedtuple` | `namedtuple` | ✓ | Python |   
`namedtuple` | `tuple` | ✓ | Python |   
`namedtuple` | `NamedTuple` | ✓ | Python |   
`set` | `deque` |  | Python |   
`set` | `dict_keys` |  | Python |   
`set` | `dict_values` |  | Python |   
`set` | `frozenset` |  | Python |   
`set` | `list` |  | Python |   
`set` | `set` | ✓ | Python |   
`set` | `tuple` |  | Python |   
`str` | `bytearray` |  | Python | Assumes UTF-8, error on unicode decoding error.  
`str` | `bytes` |  | Python | Assumes UTF-8, error on unicode decoding error.  
`str` | `str` | ✓ | Python & JSON |   
`time` | `bytes` |  | Python | Format: `HH:MM:SS.FFFFFF`. See   
`time` | `float` |  | Python & JSON | Interpreted as seconds, range `0 - 86399.9*`.  
`time` | `int` |  | Python & JSON | Interpreted as seconds, range `0 - 86399`.  
`time` | `str` |  | Python & JSON | Format: `HH:MM:SS.FFFFFF`. See   
`time` | `time` | ✓ | Python |   
`time` | `Decimal` |  | Python | Interpreted as seconds, range `0 - 86399.9*`.  
`timedelta` | `bytes` |  | Python | Format: `ISO8601`. See   
`timedelta` | `float` |  | Python & JSON | Interpreted as seconds.  
`timedelta` | `int` |  | Python & JSON | Interpreted as seconds.  
`timedelta` | `str` |  | Python & JSON | Format: `ISO8601`. See   
`timedelta` | `timedelta` | ✓ | Python |   
`timedelta` | `Decimal` |  | Python | Interpreted as seconds.  
`tuple` | `deque` |  | Python |   
`tuple` | `dict_keys` |  | Python |   
`tuple` | `dict_values` |  | Python |   
`tuple` | `frozenset` |  | Python |   
`tuple` | `list` |  | Python |   
`tuple` | `set` |  | Python |   
`tuple` | `tuple` | ✓ | Python |   
`type` | `type` | ✓ | Python |   
`Any` | `Any` | ✓ | Python & JSON |   
`ByteSize` | `float` | ✓ | Python & JSON |   
`ByteSize` | `int` | ✓ | Python & JSON |   
`ByteSize` | `str` | ✓ | Python & JSON |   
`ByteSize` | `Decimal` | ✓ | Python |   
`Decimal` | `float` |  | Python & JSON |   
`Decimal` | `int` |  | Python & JSON |   
`Decimal` | `str` |  | Python & JSON | Must match `[0-9]+(\.[0-9]+)?`.  
`Decimal` | `Decimal` | ✓ | Python |   
`Enum` | `Any` |  | Python | Input value must be convertible to enum values.  
`Enum` | `Enum` | ✓ | Python |   
`IPv4Address` | `bytes` |  | Python |   
`IPv4Address` | `int` |  | Python | integer representing the IP address, must be less than `2**32`  
`IPv4Address` | `str` |  | Python & JSON |   
`IPv4Address` | `IPv4Address` | ✓ | Python |   
`IPv4Address` | `IPv4Interface` | ✓ | Python |   
`IPv4Interface` | `bytes` |  | Python |   
`IPv4Interface` | `int` |  | Python | integer representing the IP address, must be less than `2**32`  
`IPv4Interface` | `str` |  | Python & JSON |   
`IPv4Interface` | `tuple` |  | Python |   
`IPv4Interface` | `IPv4Address` |  | Python |   
`IPv4Interface` | `IPv4Interface` | ✓ | Python |   
`IPv4Network` | `bytes` |  | Python |   
`IPv4Network` | `int` |  | Python | integer representing the IP network, must be less than `2**32`  
`IPv4Network` | `str` |  | Python & JSON |   
`IPv4Network` | `IPv4Address` |  | Python |   
`IPv4Network` | `IPv4Interface` |  | Python |   
`IPv4Network` | `IPv4Network` | ✓ | Python |   
`IPv6Address` | `bytes` |  | Python |   
`IPv6Address` | `int` |  | Python | integer representing the IP address, must be less than `2**128`  
`IPv6Address` | `str` |  | Python & JSON |   
`IPv6Address` | `IPv6Address` | ✓ | Python |   
`IPv6Address` | `IPv6Interface` | ✓ | Python |   
`IPv6Interface` | `bytes` |  | Python |   
`IPv6Interface` | `int` |  | Python | integer representing the IP address, must be less than `2**128`  
`IPv6Interface` | `str` |  | Python & JSON |   
`IPv6Interface` | `tuple` |  | Python |   
`IPv6Interface` | `IPv6Address` |  | Python |   
`IPv6Interface` | `IPv6Interface` | ✓ | Python |   
`IPv6Network` | `bytes` |  | Python |   
`IPv6Network` | `int` |  | Python | integer representing the IP address, must be less than `2**128`  
`IPv6Network` | `str` |  | Python & JSON |   
`IPv6Network` | `IPv6Address` |  | Python |   
`IPv6Network` | `IPv6Interface` |  | Python |   
`IPv6Network` | `IPv6Network` | ✓ | Python |   
`InstanceOf` | `Any` | ✓ | Python |  `isinstance()` check must return `True`.  
`IntEnum` | `Any` |  | Python | Input value must be convertible to enum values.  
`IntEnum` | `IntEnum` | ✓ | Python |   
`Iterable` | `deque` | ✓ | Python |   
`Iterable` | `frozenset` | ✓ | Python |   
`Iterable` | `list` | ✓ | Python |   
`Iterable` | `set` | ✓ | Python |   
`Iterable` | `tuple` | ✓ | Python |   
`NamedTuple` | `dict` | ✓ | Python |   
`NamedTuple` | `list` | ✓ | Python |   
`NamedTuple` | `namedtuple` | ✓ | Python |   
`NamedTuple` | `tuple` | ✓ | Python |   
`NamedTuple` | `NamedTuple` | ✓ | Python |   
`None` | `None` | ✓ | Python & JSON |   
`Path` | `str` |  | Python |   
`Path` | `Path` | ✓ | Python |   
`Pattern` | `bytes` | ✓ | Python | Input must be a valid pattern.  
`Pattern` | `str` | ✓ | Python & JSON | Input must be a valid pattern.  
`Sequence` | `deque` |  | Python |   
`Sequence` | `list` | ✓ | Python |   
`Sequence` | `tuple` |  | Python |   
`TypedDict` | `dict` | ✓ | Python |   
`TypedDict` | `Any` | ✓ | Python |   
`TypedDict` | `Mapping` |  | Python | Must implement the mapping interface and have an `items()` method.  
`UUID` | `str` |  | Python |   
`UUID` | `UUID` | ✓ | Python |   
Field Type | Input | Strict | Input Source | Conditions  
---|---|---|---|---  
`bool` | `bool` | ✓ | Python & JSON |   
`bytes` | `bytes` | ✓ | Python |   
`callable` | `Any` | ✓ | Python |  `callable()` check must return `True`.  
`date` | `date` | ✓ | Python |   
`datetime` | `datetime` | ✓ | Python |   
`deque` | `deque` | ✓ | Python |   
`dict` | `dict` | ✓ | Python |   
`float` | `float` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`float` | `int` | ✓ | Python & JSON |   
`frozenset` | `frozenset` | ✓ | Python |   
`int` | `int` | ✓ | Python & JSON |  `bool` is explicitly forbidden.  
`list` | `list` | ✓ | Python |   
`namedtuple` | `dict` | ✓ | Python |   
`namedtuple` | `list` | ✓ | Python |   
`namedtuple` | `namedtuple` | ✓ | Python |   
`namedtuple` | `tuple` | ✓ | Python |   
`namedtuple` | `NamedTuple` | ✓ | Python |   
`set` | `set` | ✓ | Python |   
`str` | `str` | ✓ | Python & JSON |   
`time` | `time` | ✓ | Python |   
`timedelta` | `timedelta` | ✓ | Python |   
`tuple` | `tuple` | ✓ | Python |   
`type` | `type` | ✓ | Python |   
`Any` | `Any` | ✓ | Python & JSON |   
`ByteSize` | `float` | ✓ | Python & JSON |   
`ByteSize` | `int` | ✓ | Python & JSON |   
`ByteSize` | `str` | ✓ | Python & JSON |   
`ByteSize` | `Decimal` | ✓ | Python |   
`Decimal` | `Decimal` | ✓ | Python |   
`Enum` | `Enum` | ✓ | Python |   
`IPv4Address` | `IPv4Address` | ✓ | Python |   
`IPv4Address` | `IPv4Interface` | ✓ | Python |   
`IPv4Interface` | `IPv4Interface` | ✓ | Python |   
`IPv4Network` | `IPv4Network` | ✓ | Python |   
`IPv6Address` | `IPv6Address` | ✓ | Python |   
`IPv6Address` | `IPv6Interface` | ✓ | Python |   
`IPv6Interface` | `IPv6Interface` | ✓ | Python |   
`IPv6Network` | `IPv6Network` | ✓ | Python |   
`InstanceOf` | `Any` | ✓ | Python |  `isinstance()` check must return `True`.  
`IntEnum` | `IntEnum` | ✓ | Python |   
`Iterable` | `deque` | ✓ | Python |   
`Iterable` | `frozenset` | ✓ | Python |   
`Iterable` | `list` | ✓ | Python |   
`Iterable` | `set` | ✓ | Python |   
`Iterable` | `tuple` | ✓ | Python |   
`NamedTuple` | `dict` | ✓ | Python |   
`NamedTuple` | `list` | ✓ | Python |   
`NamedTuple` | `namedtuple` | ✓ | Python |   
`NamedTuple` | `tuple` | ✓ | Python |   
`NamedTuple` | `NamedTuple` | ✓ | Python |   
`None` | `None` | ✓ | Python & JSON |   
`Path` | `Path` | ✓ | Python |   
`Pattern` | `bytes` | ✓ | Python | Input must be a valid pattern.  
`Pattern` | `str` | ✓ | Python & JSON | Input must be a valid pattern.  
`Sequence` | `list` | ✓ | Python |   
`TypedDict` | `dict` | ✓ | Python |   
`TypedDict` | `Any` | ✓ | Python |   
`UUID` | `UUID` | ✓ | Python |   
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
