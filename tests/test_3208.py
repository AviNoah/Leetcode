import pytest
from problems.prob_3208 import func


tests = [
    (([0, 1, 0, 1, 0], 3), 3),
    (([0, 1, 0, 0, 1, 0, 1], 6), 2),
    (([1, 1, 0, 1], 4), 0),
    (([0, 1, 1], 3), 1),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
