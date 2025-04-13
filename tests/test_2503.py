import pytest

from problems.prob_2503 import func

tests = [
    (
        (
            [[1, 2, 3], [2, 5, 7], [3, 5, 1]],
            [5, 6, 2],
        ),
        [5, 8, 1],
    ),
    (
        ([[5, 2, 1], [1, 1, 2]], [3]),
        [0],
    ),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
