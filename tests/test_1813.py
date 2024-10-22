import pytest
from problems.prob_1813 import sol

tests = [
    (("My name is Haley", "My Haley"), True),
    (("of", "A lot of words"), False),
    (("Frog cool", "Frogs are cool"), False),
    (("Eating right now", "Eating"), True),
    (("hello world", "hello world"), True),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert sol(*args) == expected
