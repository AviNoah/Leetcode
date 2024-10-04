import pytest

tests = [
    ((None,), None),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    # assert func(*args) == expected
    pass
