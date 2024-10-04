import pytest

tests = [
    (([3, 2, 5, 1, 3, 4],), 22),
    (([3, 4],), 12),
    (([1, 1, 2, 3],), -1),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    pass
