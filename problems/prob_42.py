# https://leetcode.com/problems/trapping-rain-water


# O(n)
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


# Find the next -1
# old_i = i
# potential_area = 0
# for i in range(i + 1, len(nge_arr)):
#     if nge_arr[i] != -1:
#         potential_area -= heights[i]
#     else:
#         potential_area += (i - old_i - 1) * heights[i]
#         area += potential_area
#         break
# i += 1
# if nge_index != -1:
#             # maximum possible area this range could cover
#             area += (nge_index - i - 1) * heights[i]
#             # Deduct blocking heights from the area
#             for i in range(i + 1, nge_index):
#                 area -= heights[i]
#         else:
#             # Advance until the next -1
#             blocked_area = 0
#             for j in range(i + 1, len(nge_arr)):
#                 if nge_arr[j] == -1:
#                     area += (j - i - 1) * heights[j] - blocked_area
#                     j = i
#                     break
#                 else:
#                     blocked_area += heights[j]
#         i += 1
