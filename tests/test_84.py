from problems.prob_84 import naive_sol, count_appearances, nse, pse, nse_and_pse
import pytest

tests = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([2, 1, 2], 3),
    ([2, 2, 2, 0, 7], 7),
]


@pytest.mark.parametrize("heights, expected_area", tests)
def test_0(heights, expected_area):
    area = naive_sol(heights)
    assert area == expected_area, f"Expected {expected_area} got {area} instead"


@pytest.mark.parametrize("heights, expected_area", tests)
def test_1(heights, expected_area):
    area = count_appearances(heights)
    assert area == expected_area, f"Expected {expected_area} got {area} instead"


@pytest.mark.parametrize("heights, expected_area", tests)
def test_2(heights, expected_area):
    area = nse_and_pse(heights)
    assert area == expected_area, f"Expected {expected_area} got {area} instead"


def test_nse():
    heights = [1, 2, 2, 1, 3, 1]
    result = nse(heights)
    assert result == [6, 3, 3, 6, 5, 6]


def test_pse():
    heights = [1, 2, 1, 2]
    result = pse(heights)
    assert result == [-1, 0, -1, 2]
