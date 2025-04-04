import pytest
from problems.prob_2818 import func

tests = [
    (([8, 3, 9, 3, 8], 2), 81),
    (([19, 12, 14, 6, 10, 18], 3), 4788),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
