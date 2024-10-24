import pytest
from problems.prob_42 import sol, nge

tests = [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
    (([4, 2, 3],), 1),
    # This test fails because i am searching for a number that is 4 or greater,
    # missing the rain cell that can be created between 4 and 3
    # if this test were reversed this would of worked because 3 would recognize 4 as its
    # nge
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert sol(*args) == expected


def test_nge():
    expected = [4, 3, 3, 4, -1]
    assert nge([3, 2, 1, 2, 3]) == expected

    expected = [1, 3, 3, 7, 6, 6, 7, -1, 10, 10, -1, -1]
    assert nge([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == expected
