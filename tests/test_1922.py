import pytest
from problems.prob_1922 import func

tests = [
    ((1,), 5),
    ((4,), 400),
    ((50,), 564908303),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
