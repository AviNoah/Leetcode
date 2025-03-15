# https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15


def func(nums: list[int], k: int):
    # We need to construct a sub-array containing non-contiguous elements, and return the max from it.
    # its size must be at least k.
    # Out of all possible sub-arrays, we must find the lowest maximum.

    # Once we find K houses, adding another house will only increase the maximum - we should
    # find exactly K houses for this problem
    
    # To reduce the maximum, we need to swap the largest element out for another non contiguous one
    # that is smaller.

    # Maybe use a max heap queue and find the k-th smallest number?

    pass
