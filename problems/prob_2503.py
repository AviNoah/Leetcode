# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/?envType=daily-question&envId=2025-04-13


def func(grid: list[list[int]], queries: list[int]) -> list[int]:
    # We basically have to count how many nodes we visited that are greater than query
    # Since we can have multiple queries for the same matrix set, we probably can cache answers.

    # We can use a stack to do flood-fill, we need a way to cache answers for performance too

    ROWS = len(grid)
    COLS = len(grid[0])

    def compute_query(query: int):
        stack = [(0, 0)]
        count = 0
        visited = set()

        while stack:
            row, col = stack.pop()

            if (row, col) in visited:
                continue

            if query <= grid[row][col]:
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

        return count

    # Unoptimized first revision - does not use cache, re-runs flood fill on matrix for each query

    return [compute_query(q) for q in queries]
