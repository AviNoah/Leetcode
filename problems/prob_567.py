# https://leetcode.com/problems/permutation-in-string


from collections import Counter
from functools import cache


def naive(s1: str, s2: str) -> bool:
    # Regardless of what you do, because we generate all permutations, its O(n!)
    @cache
    def permute(s: str) -> list[str]:
        # O(n!)
        res = []
        for i in range(len(s)):
            res.extend(
                [s[i] + permutation for permutation in permute(s[:i] + s[i + 1 :])]
                or [s[i]]
            )

        return res

    permutations = permute(s1)

    # O(n^2)
    for x in permutations:
        if x in s2:
            return True

    return False


def not_generating_perms(s1: str, s2: str) -> bool:
    # The key point to solving this is to keep track of the elements we added to our
    # rolling window, if we are short on an element, cut the rolling window from the left
    # on the left most occurrence of that element, if we encounter a char we dont need, discard
    # entire stack
    # if we found the needed permutation (stack len equals s1) we exit immediately with True
    needed = Counter(s1)
    needed_len = len(s1)
    stack: list[str] = []

    for char in s2:
        if len(stack) == needed_len:
            return True

        if char not in needed:
            # Series ruined
            for elem in stack:
                needed[elem] += 1
            stack = []
            continue

        if needed[char] != 0:
            # Add to the stack
            stack.append(char)
            needed[char] -= 1
            continue

        # We need to the use the leftmost occurrence of the char
        index = stack.index(char)

        # Discard anything until that occurrence
        for _ in range(index + 1):
            needed[stack.pop(0)] += 1

        # Add the char
        stack.append(char)
        needed[char] -= 1

    return len(stack) == needed_len
