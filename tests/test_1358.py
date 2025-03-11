import pytest
from problems.prob_1358 import func

tests = [
    (("abcabc",), 10),
    (("aaacb",), 3),
    (("abc",), 1),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert func(*args) == expected
    pass
