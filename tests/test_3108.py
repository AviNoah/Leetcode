import pytest
from problems.prob_3108 import func

tests = [
    (
        (
            5,
            [[0, 1, 7], [1, 3, 7], [1, 2, 1]],
            [[0, 3], [3, 4]],
        ),
        [1, -1],
    ),
    (
        (
            3,
            [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]],
            [[1, 2]],
        ),
        [0],
    ),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
