import pytest
from conftest import values, pairs


@pytest.mark.parametrize('value', values)
def test_canCreateCxxJson(cxxjson, value):
    json = cxxjson(value)
    assert json == value


@pytest.mark.parametrize('values', pairs)
def test_canCompareCxxJsonWithRawValues(cxxjson, values):
    a, b = values
    self = cxxjson(a)

    assert self == a
    assert (self != a) is False

    assert (self == b) is False
    assert self != b


@pytest.mark.parametrize('values', pairs)
def test_canCompareCxxJsonWithOtherJsons(cxxjson, values):
    a, b = values
    self = cxxjson(a)
    same = cxxjson(a)
    other = cxxjson(b)

    assert self == self
    assert (self != self) is False

    assert self == same
    assert (self != same) is False

    assert (self == other) is False
    assert self != other


def test_raisesTypeErrorWhenUnsupportedTypeGivenToCreateCxxJson(cxxjson):
    class Unsupported:
        pass
    with pytest.raises(TypeError):
        cxxjson(Unsupported())
