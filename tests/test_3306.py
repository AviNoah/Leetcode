import pytest
from problems.prob_3306 import func

tests = [
    (("aeioqq", 1), 0),
    (("aeiou", 0), 1),
    (("ieaouqqieaouqq", 1), 3),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
