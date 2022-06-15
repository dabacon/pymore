# pymore

`pymore` is a collection of useful utilities for Python.

![Test all the code](https://github.com/dabacon/pymore/workflows/Continuous%20Integration/badge.svg)
[![PyPI version](https://badge.fury.io/py/pymore.svg)](https://badge.fury.io/py/pymore)

This includes

* EqualsTester: a helper for testing the equality contract in Python (originally developed
for [Cirq](https://github.com/quantumlib/cirq))

```python
import pymore

tester = pymore.EqualsTester()

# This tests that the added elements all satisfy the equals contract
# between themselves.
tester.add_equality_group(MyObject("a"), MyObject("a"))

# Each new addition of an equality group also tests that the elements
# in this new group are not equal to those in the previously added group.
# So, for example, this would raise an `AssertionError` if it was
# true that `MyObject("a")` was equal to `MyObject("b")`.
tester.add_equality_group(MyObject("b"), MyObject("b"))
```

* first: Return the first element that matches a predicate, or a default.

```python
import pymore

is_even = lambda x: x % 2 == 0
# Returns the first element that is even.
first = pymore.first([1, 3, 6, 7], is_even)
assert first == 6
```

# License

This package is licensed under an Apache 2.0 license. This code is derived from work in
other frameworks.  See [LICENSE](https://github.com/dabacon/pymore/blob/main/LICENSE)
and [NOTICES](https://github.com/dabacon/pymore/blob/main/NOTICES) for details.
