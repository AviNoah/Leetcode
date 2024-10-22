import pytest
from problems.prob_215 import my_heapq, python_heapq

tests = [
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert my_heapq(*args) == expected
    pass


@pytest.mark.parametrize("args, expected", tests)
def test_1(args, expected):
    assert python_heapq(*args) == expected
    pass
