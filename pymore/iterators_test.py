import pytest
import pymore


def test_first_no_predicate():
    assert pymore.first([1, 2, 3]) == 1
    assert pymore.first((1, 2, 3)) == 1
    assert pymore.first(x for x in range(4)) == 0


def test_first_predicate():
    assert pymore.first([1, 3, 5], lambda x: x == 3) == 3
    assert pymore.first((1, 3, 5), lambda x: x == 3) == 3
    assert pymore.first((x for x in range(4)), lambda x: x == 3) == 3


def test_first_default():
    assert pymore.first([], default=3) == 3
    assert pymore.first([1, 3, 5], lambda x: x == 2, default=7) == 7
    assert pymore.first((1, 3, 5), lambda x: x == 2, default=7) == 7
    assert pymore.first((x for x in range(3)), lambda x: x == 5, default=7) == 7


def test_first_no_match_no_default():
    with pytest.raises(ValueError, match="no default"):
        _ = pymore.first([])
    with pytest.raises(ValueError, match="no default"):
        _ = pymore.first(tuple())
    with pytest.raises(ValueError, match="no default"):
        _ = pymore.first([1, 3, 5], lambda x: x == 2)
