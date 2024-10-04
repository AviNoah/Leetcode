import pytest
from problems.prob_1590 import sum_array_approach_naive, map_approach

tests = [
    (([3, 1, 4, 2], 6), 1),
    (([4, 3, 1, 2], 6), 1),
    (([6, 3, 5, 2], 9), 2),
    (([1, 2, 3], 3), 0),
    (([26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3], 26), 3),
    (([8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2], 148), 7),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert sum_array_approach_naive(*args) == expected


@pytest.mark.parametrize("args, expected", tests)
def test_1(args, expected):
    assert map_approach(*args) == expected
