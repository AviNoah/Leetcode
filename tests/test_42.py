import pytest
from problems.prob_42 import sol, nge

tests = [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert sol(*args) == expected


def test_nge():
    expected = [4, 3, 3, 4, -1]
    assert nge([3, 2, 1, 2, 3]) == expected

    expected = [1, 3, 3, 7, 6, 6, 7, -1, 10, 10, -1]
    assert nge([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == expected
