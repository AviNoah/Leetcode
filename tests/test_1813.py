import pytest
from problems.prob_1813 import sol

tests = [
    (("My name is Haley", "My Haley"), True),
    (("of", "A lot of words"), False),
    (("Frog cool", "Frogs are cool"), False),
    (("Eating right now", "Eating"), True),
    (("Eating right now", "now"), True),
    (("hello world", "hello world"), True),
    (("c h p Ny", "c BDQ r h p Ny"), True),
    (("Ogn WtWj HneS", "Ogn WtWj HneS"), True),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert sol(*args) == expected
