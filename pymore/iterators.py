from typing import Any, Callable, Iterable, Optional, TypeVar


T = TypeVar("T")


_RaisesIfNoDefault = (0,)  # A default value, if not supplied will causes an error for no match.


def first(
    iterable: Iterable[T],
    predicate: Optional[Callable[[T], bool]] = None,
    default: Any = _RaisesIfNoDefault,
) -> T:
    """Returns the first element of an iterable satisfying a predicate.

    If no predicate is specified, this returns the first element. If there is no element
    found, then this will return the default.  If no default is specified, and no element is
    found, then this will raise a ValueError.

    Args:
        iterable: The iterable to search over.
        predicate: If specified, the predicate to check for the first of. If not specified, then
            this method will try to return the first element.
        default: A default value to return if no element is found.

    Raises:
        ValueError: If there is no first element that satisfies the predicate (or no first element
            when no predicate is specified), and no default has been specified.

    Returns:
        The first element that satisfies the predicate, or if no predicate is given, the first
        element.  If no element is found, then default is return if it is specified, otherwise
        raises a ValueError.
    """
    actual_predicate = predicate if predicate is not None else lambda x: True
    try:
        return next(x for x in iterable if actual_predicate(x))
    except StopIteration:
        if default == _RaisesIfNoDefault:
            raise ValueError("No element matches predicate and no default was supplied.")
        return default
