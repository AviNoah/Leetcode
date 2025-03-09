import pytest
from problems.prob_2379 import func

tests = [
    (("WBBWWBBWBW", 7), 3),
    (("WBWBBBW", 2), 0),
    (("WWBBBWBBBBBWWBWWWB", 16), 6),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
