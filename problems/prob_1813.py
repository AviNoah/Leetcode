# https://leetcode.com/problems/sentence-similarity-iii


def sol(s1: str, s2: str) -> bool:
    words1 = s1.split()
    words2 = s2.split()

    # Find the range of non-similarity between left and right
    # left is where the non-similarity begins, inclusive
    # right is where the non-similarity ends, exclusive

    for left, (w1, w2) in enumerate(zip(words1, words2)):
        if w1 != w2:
            break

    for right, (w1, w2) in enumerate(zip(reversed(words1), reversed(words2))):
        if w1 != w2:
            break

    return
