# https://leetcode.com/problems/sentence-similarity-iii


def sol(s1: str, s2: str) -> bool:
    words1 = s1.split()  # Bigger
    words2 = s2.split()  # Smaller

    # The key point here is to assign each word from the shorter sentence to either
    # the longer sentence's prefix, and then to its suffix.

    # The prefix and suffix variables mean the amount of words in prefix and suffix respectively.
    # if the sum of amount of words in prefix and suffix is greater than the shorter sentence or equal -
    # then they are similar
    # If greater, that just means prefix and suffix overlap, and either of them can take those words.
    # only if they are less than we cannot call them similar because there will have to be a word in between
    # them that is not common.

    prefix = 0
    for w1, w2 in zip(words1, words2):
        if w1 != w2:
            break
        prefix += 1

    suffix = 0
    for w1, w2 in zip(reversed(words1), reversed(words2)):
        if w1 != w2:
            break
        suffix += 1

    return prefix + suffix >= min(len(words1), len(words2))
