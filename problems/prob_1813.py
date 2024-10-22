# https://leetcode.com/problems/sentence-similarity-iii

# A good approach to this solution is two pointers
# Keep going through the characters from both strings char by char
# until a the chars don't match, then approach from the end of both strings and
# keep matching until the chars don't match
# if the left and right indices we just found are actually in order, then they are similar


def sol2(s1: str, s2: str) -> bool:
    # O(1)
    max_len = max(len(s1), len(s2))

    x = list(zip(s1, s2))
    # O(n)
    for left, (c1, c2) in enumerate(x):
        if c1 != c2:
            break

    y = list(zip(reversed(s1), reversed(s2)))
    for right, (c1, c2) in enumerate(y):
        if c1 != c2:
            break

    right = max_len - right - 1

    return left <= right


def sol(s1: str, s2: str) -> bool:
    # Maybe use split?
    # O(n), space time complexity O(n)
    words1 = s1.split()
    words2 = s2.split()

    max_len = max(len(words1), len(words2))

    for i, (w1, w2) in enumerate(zip(words1, words2)):
        if w1 != w2:
            break

    for j, (w1, w2) in enumerate(zip(reversed(words1), reversed(words2))):
        if w1 != w2:
            break

    j = max_len - j - 1

    return i >= j
