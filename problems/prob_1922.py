# https://leetcode.com/problems/count-good-numbers/description/?envType=daily-question&envId=2025-04-13


def func(n: int):
    # This is a combinatorics problem, since we are greedy and want ALL possible unique
    # solutions, we can just select even and prime digits

    # even_digits: 0,2,4,6,8
    # prime_digits: 2,3,5,7

    # for a length of n, each even spot nets us *5 more possibilities
    # and each odd spot nets us *4 possibilities

    # We need to use modular exponentiation since the numbers get increasingly large

    odd = n // 2
    even = n - odd
    MOD = 10**9 + 7
    prod = pow(5, even, MOD) * pow(4, odd, MOD)

    return prod % MOD
