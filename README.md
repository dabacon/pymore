# pymore

`pymore` is a collection of useful utilities for Python.

![Test all the code](https://github.com/dabacon/pymore/workflows/Continuous%20Integration/badge.svg)

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
# in this new group are not equal to those in the perviously added group.
# So, for example, this would raise an `AssertionError` if it was
# true that `MyObject("a")` was equal to `MyObject("b")`.
tester.add_equality_group(MyObject("b"), MyObject("b")
```


# License

This package is licensed under an Apache 2.0 license. This code is derived from work in
other frameworks.  See [LICNESE](LICENSE) and [NOTICES](NOTICES) for details.
