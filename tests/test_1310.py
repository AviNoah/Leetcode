import pytest
from problems.prob_1310 import naive, store_results

tests = [
    (
        (
            [1, 3, 4, 8],
            [[0, 1], [1, 2], [0, 3], [3, 3]],
        ),
        [2, 7, 14, 8],
    ),
    (
        (
            [4, 8, 2, 10],
            [[2, 3], [1, 3], [0, 0], [0, 3]],
        ),
        [8, 0, 4, 4],
    ),
    (
        (
            [1, 1, 1, 0],
            [[2, 3], [1, 3], [0, 0], [0, 3]],
        ),
        [1, 0, 1, 1],
    ),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert naive(*args) == expected


@pytest.mark.parametrize("args, expected", tests)
def test_1(args, expected):
    assert store_results(*args) == expected
