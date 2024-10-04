# https://leetcode.com/problems/make-sum-divisible-by-p
from typing import List


def sum_array_approach_naive(nums: List[int], p: int) -> int:

    def make_sum_array(nums: List[int]) -> List[int]:
        # O(n)
        sum_array: List[int] = []
        for num in nums:
            if sum_array:
                sum_array.append(sum_array[-1] + num)
            else:
                sum_array.append(num)

        return sum_array

    N = len(nums)

    sum_array = make_sum_array(nums)

    if sum_array[-1] < p:
        return -1

    remainder = sum_array[-1] % p

    if remainder == 0:
        return 0

    sum_array.insert(0, 0)

    min_len = N
    # O(n^2)
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            if (sum_array[j] - sum_array[i]) % p == remainder:
                min_len = min(min_len, j - i)
                break  # no point in continuing, this is the min

    if min_len == N:
        return -1
    return min_len


def map_approach(nums: List[int], p: int) -> int:
    # The key would be a number between 0 to p-1 - the needed remainder
    # the value would be its index
    # NOTE: this will override remainders so it always has the greatest index
    # where that remainder is, which in our case is good since we want to minimize it
    my_map: dict[int, int] = {
        0: -1,  # Not adding anything makes a remainder of 0
    }

    target_remainder = sum(nums) % p  # O(n)

    # Special case where nums is already divisible by p
    if target_remainder == 0:
        return 0

    N = len(nums)
    min_len = N
    current_remainder = 0

    # Make an accumulating sum
    # store in the map the index of the current_remainder,
    # this will be used as the start of the sub-array, meaning if the current total
    # makes a needed remainder, search the map if a point previously needed it to complete it

    for i in range(N):
        current_remainder = (current_remainder + nums[i]) % p

        # How much is needed to remove from current remainder to get remainder
        needed = (current_remainder - target_remainder + p) % p

        if needed in my_map:
            min_len = min(min_len, i - my_map[needed])

        my_map[current_remainder] = i

    return -1 if min_len == N else min_len
