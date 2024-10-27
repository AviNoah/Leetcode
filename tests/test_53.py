import pytest
from problems.prob_53 import sol

tests = [
    (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6),
    (([1],), 1),
    (([-1],), -1),
    (([5, 4, -1, 7, 8],), 23),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert sol(*args) == expected
