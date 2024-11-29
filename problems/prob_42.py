# https://leetcode.com/problems/trapping-rain-water
"""
We will use a monotonic stack to find the Next Greater Element (NGE) for indices in the array. 
There are two key scenarios during this process:

Scenario A: The current index has an NGE (i.e., the NGE is not -1).
Scenario B: The current index does not have an NGE (i.e., the NGE is -1).

Starting at index i = 0, we will continue processing indices until i is out of bounds:
    If Scenario A: Traverse from the current index i to its NGE and calculate the trapped 
        rainwater in this range. Update i to the NGE after processing.
    If Scenario B: Skip to the next index whose NGE is also -1 (the next occurrence of Scenario B), 
        and calculate the trapped rainwater in this section. Update i accordingly.
"""


# O(n) Monotonic stack
def arr_of_nge(heights: list[int]) -> list[int]:
    
    "Return a list of nge - next greatest or equal, for each element at index i; -1 means no nge"
    results = [-1] * len(heights)
    # stack of indices
    stack: list[int] = []

    for i in range(len(heights)):
        while stack and heights[i] >= heights[stack[-1]]:
            results[stack.pop()] = i

        stack.append(i)

    return results


def sol(heights: list[int]) -> int:
    # If encounter -1, continue until next -1.

    nge_arr = arr_of_nge(heights)
    area = 0
    i = 0

    while i < len(nge_arr):
        nge_index = nge_arr[i]
        if nge_index != -1:
            # Max possible potential
            potential_area = (nge_index - i - 1) * heights[i]
            # Remove blocking heights
            for i in range(i + 1, nge_index):
                potential_area -= heights[i]

            area += potential_area

        else:
            j = i + 1
            potential_area = 0
            while j < len(nge_arr):
                if nge_arr[j] != -1:
                    potential_area -= heights[j]
                else:
                    potential_area += (j - i - 1) * heights[j]
                    area += potential_area
                    i = j - 1
                    break
                j += 1
        i += 1

    return area
