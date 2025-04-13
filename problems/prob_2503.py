# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/?envType=daily-question&envId=2025-04-13
import heapq


def func(grid: list[list[int]], queries: list[int]) -> list[int]:
    # We basically have to count how many nodes we visited that are greater than query
    # Since we can have multiple queries for the same matrix set, we probably can cache answers.

    # We can use a stack to do flood-fill, we need a way to cache answers for performance too

    ROWS = len(grid)
    COLS = len(grid[0])

    QUERIES_DICT: dict[int, int] = {}

    # Use a min-heap to always process the lowest-valued cell first
    heap = [(grid[0][0], 0, 0)]  # Min-heap with (value, row, col)
    count = 0
    visited = set()
    visited.add((0, 0))

    # O(N*M) - count of queries don't really matter
    for query in sorted(queries):
        # Process all reachable cells with value < query
        while heap and heap[0][0] < query:
            val, row, col = heapq.heappop(heap)

            count += 1
            # Visit all neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        QUERIES_DICT[query] = count

    # O(q)
    return [QUERIES_DICT[query] for query in queries]
