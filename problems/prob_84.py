# https://leetcode.com/problems/largest-rectangle-in-histogram/


def naive_sol(heights: list[int]) -> int:
    "For every element, march forward until you are met with a smaller height"
    # O(n^3)
    max_area = 0
    for i, height in enumerate(heights):
        for sub_height in range(1, height + 1):
            count = 1

            for next_height in heights[i + 1 :]:
                if next_height < sub_height:
                    break
                count += 1
            max_area = max(max_area, count * sub_height)

    return max_area


def count_appearances(heights: list[int]) -> int:
    "The longest sub-sequence of a row times its row num"
    # O(n^2), Space-cplx O(n)
    max_area = 0
    rows = max(heights)  # O(n)

    def count_greatest_sub_series(bools: list[bool]) -> int:
        # O(n)
        count = 0
        max_count = 0
        for _bool in bools:
            if _bool:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)

    # O(n^2)
    for row in range(1, rows + 1):
        last_line = [height >= row for height in heights]
        count = count_greatest_sub_series(last_line)
        max_area = max(max_area, row * count)

    return max_area


def nse(heights: list[int]) -> list[int]:
    "Return a list of indices where for each index we know the index of the nse"
    result = [len(heights) for _ in range(len(heights))]
    indices_stack: list[int] = []

    for i, height in enumerate(heights):
        while indices_stack and height < heights[indices_stack[-1]]:
            index = indices_stack.pop(-1)
            result[index] = i

        indices_stack.append(i)

    return result


def pse(heights: list[int]) -> list[int]:
    "Return a list of indices where for each index we know the index of the pse"
    results = nse(list(reversed(heights)))
    results = [-1 * (result - len(heights) + 1) for result in results]
    return list(reversed(results))


def nse_and_pse(heights: list[int]) -> int:
    """
    For every height element at i, find the index where the next smallest element (nse) is
    and the index where the previous smallest element (pse) is -
    this will be the biggest rectangle it can make
    """

    max_area = 0
    nse_arr = nse(heights)
    pse_arr = pse(heights)

    # O(n)
    for i, height in enumerate(heights):
        base = nse_arr[i] - pse_arr[i] - 1
        max_area = max(max_area, base * height)

    return max_area
