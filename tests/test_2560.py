import pytest
from problems.prob_2560 import func

tests = [
    (([2, 3, 5, 9], 2), 5),
    (([2, 7, 9, 3, 1], 2), 2),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
