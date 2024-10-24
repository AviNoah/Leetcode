# https://leetcode.com/problems/trapping-rain-water

"""
Rain water can be collected only if its between two non-zero numbers,
it ends being collected once the second number is bigger than the first.
"""
from collections import deque


def nge(heights: list[int]) -> list[int]:
    """
    Given a list of heights, return a list of indices, where for elem i,
    is the index to the nge

    nge is the next element that is greater or equal to the element at i

    -1 means no nge was found
    """
    results = [-1] * len(heights)  # By default none have nge

    # We will stack heights in descending order, if the next height
    # is bigger than the top of the stack, we will pop the stack until it isn't
    # marking the height as their nge
    # We will store their indices instead of the height values
    stack: deque[int] = deque()  # Use deque for O(1) popleft

    # O(n)
    for i, h in enumerate(heights):
        if not stack or h < heights[stack[0]]:
            # If still descending, continue
            stack.append(i)  # O(1)
            continue

        while stack and h >= heights[stack[0]]:
            results[stack.popleft()] = i  # O(1)

        stack.appendleft(i)  # O(1)

    return results


def sol(heights: list[int]) -> int:
    # We can implement a nge - next greatest or equal element, method, that will find the index of the
    # next biggest element for every index i

    # Then, to simplify rain collection - for example between two big numbers we may have
    # bars that take the place of a rain water slot, we can deduce that the maximum
    # rain area between them is at most the distance between them, times the height of the first number
    # which is always smaller, we then go along the indices between them and deduct the values
    # of the bars since that is how much space they take

    # We need to know ahead of time the index of the next nge, and if there is one

    indices = nge(heights)  # O(n)

    i = 0
    area = 0
    while i < len(heights):
        if indices[i] == -1:
            # Skip
            i += 1
            continue

        blocked_area = 0

        for j in range(i + 1, indices[i]):
            # Sum blocking heights
            blocked_area += heights[j]

        # Add the maximum possible area (distance between bars times height of first bar)
        # and deduct the blocking bars between them
        area += (indices[i] - i - 1) * heights[i] - blocked_area

        i = indices[i]

    for i in range(len(heights)):
        for i in range(i, indices[i]):
            i += 1

    return area
