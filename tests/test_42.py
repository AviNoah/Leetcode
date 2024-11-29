import pytest
from problems.prob_42 import sol

tests = [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
    (([4, 2, 3],), 1),
    (([4, 2, 1, 2, 4],), 7),
    (([5, 4, 1, 2],), 1),
]


@pytest.mark.parametrize("args, expected", tests)
def test_1(args, expected):
    assert sol(*args) == expected
