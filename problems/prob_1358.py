# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2025-03-11


def func(s: str) -> int:
    # We will use a sliding window approach while keeping track of occurrences
    # If a substring is valid, any suffix or prefix will generate a new substring to count
    # According to example 1, we dont have to enforce uniqueness

    count = 0
    occurrences = {c: 0 for c in "abc"}

    left = 0
    for right, char in enumerate(s):
        occurrences[char] += 1

        while all(occurrences.values()):
            count += len(s) - right
            # trim left-most char, this will still generate len(s) - right new substrings
            occurrences[s[left]] -= 1
            left += 1
    return count
