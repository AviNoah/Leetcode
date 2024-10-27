# https://leetcode.com/problems/maximum-subarray/


from math import inf


def sol(nums: list[int]) -> int:
    # We will use two pointer, we will advance the left pointer once
    # the current sum is not beneficial for us - if it is negative,
    # discarding the entire part would be 0 instead of negative which is greater,
    # We will then advance the right pointer forward until we get a maximal sum.

    current_max = -inf
    current = 0

    for i in range(len(nums)):
        current += nums[i]

        # Since we must use a sub array, before discarding current, try
        # to check even if it is negative, if it is better than what we currently have
        if current > current_max:
            current_max = current

        # If, at any point the current total is less than 0, discard entire left sub arr
        if current < 0:
            current = 0

    return current_max  # type: ignore
