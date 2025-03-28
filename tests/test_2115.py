import pytest
from problems.prob_2115 import func

tests = [
    ((["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]), set(["bread"])),
    (
        (
            ["bread", "sandwich"],
            [["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"],
        ),
        set(["bread", "sandwich"]),
    ),
    (
        (
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
            ["yeast", "flour", "meat"],
        ),
        set(["bread", "sandwich", "burger"]),
    ),
]


@pytest.mark.parametrize("args, expected", tests)
def test_0(args, expected):
    assert set(func(*args)) == expected
    pass
