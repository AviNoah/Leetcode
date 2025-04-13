# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/?envType=daily-question&envId=2025-04-13


def func(grid: list[list[int]], queries: list[int]) -> list[int]:
    # We basically have to count how many nodes we visited that are greater than query
    # Since we can have multiple queries for the same matrix set, we probably can cache answers.

    # We can use a stack to do flood-fill, we need a way to cache answers for performance too

    ROWS = len(grid)
    COLS = len(grid[0])

    QUERIES_DICT: dict[int, int] = {}

    stack = [(0, 0)]
    count = 0
    visited = set()

    # O(N*M) - count of queries don't really matter
    for query in sorted(queries):
        next_stack = []

        while stack:
            row, col = stack.pop()

            if (row, col) in visited:
                continue

            if query <= grid[row][col]:
                next_stack.append((row, col))
                continue

            count += 1
            visited.add((row, col))

            if row > 0:
                stack.append((row - 1, col))
            if row < ROWS - 1:
                stack.append((row + 1, col))
            if col > 0:
                stack.append((row, col - 1))
            if col < COLS - 1:
                stack.append((row, col + 1))

        QUERIES_DICT[query] = count
        stack = next_stack

    # O(q)
    return [QUERIES_DICT[query] for query in queries]
