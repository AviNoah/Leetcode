# https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15


def func(nums: list[int], k: int):
    # We can always select k houses out of the list
    # If we define the robber to have capability C we have either two outcomes
    # He can steal from at least k houses
    # He can't

    # If he can - His real minimal capability has to be it or less
    # If he cannot - His real minimal capability has to be more than that

    # Since we need to find the minimum capability, we want to find out if he can steal from k houses -
    # so we count how many non-consecutive houses with money C or less there are and if its k or more.

    def can_steal(cap: int) -> bool:
        nonlocal k
        count = 0
        i = 0

        while i < len(nums):
            if nums[i] <= cap:
                count += 1
                i += 2
            else:
                i += 1

        return count >= k

    left, right = min(nums), max(nums)

    while left < right:
        mid = (left + right) // 2

        if can_steal(mid):
            right = mid
        else:
            left = mid + 1

    return right
