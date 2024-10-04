# https://leetcode.com/problems/xor-queries-of-a-subarray


def naive(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    N = len(arr)

    results: list[int] = []

    # O(n^2)
    for i in range(N):
        l, r = queries[i]
        res = 0
        # O(n)
        for j in range(l, r + 1):
            res ^= arr[j]

        results.append(res)

    return results


def store_results(arr: list[int], queries: list[tuple[int, int]]) -> list[int]:
    # XOR applied twice will grant the same parameter we gave it
    # if we accumulate XOR statements, we can nullify the effect of a subarray
    # by applying XOR again

    xor_arr = []
    xor_arr_reversed = []
    res = 0
    # O(n)
    for num in arr:
        res ^= num
        xor_arr.append(res)

    res = 0
    for num in reversed(arr):
        res ^= num
        xor_arr_reversed.append(res)

    xor_arr_reversed = xor_arr_reversed[::-1]  # So access is easy

    results = []
    # For the XOR result of l to r, we want the value in r, if 0 to l-1 did were nullified
    # O(n)
    z = xor_arr[-1]
    for l, r in queries:
        #    x     y     w
        # a  ^  b  ^  c  ^  d  = z

        # y^w = z^x
        # y = y^w^w

        x = xor_arr[l - 1] if l != 0 else 0
        w = xor_arr_reversed[r + 1] if r + 1 != len(xor_arr_reversed) else 0
        y_w = z ^ x
        y = y_w ^ w
        results.append(y)

    return results
