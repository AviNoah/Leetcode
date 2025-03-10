# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10


def func(word: str, k: int):
    # Find all consonant indices
    indices = [-1] + [i for i, c in enumerate(word) if c not in "aeiou"] + [len(word)]

    def valid_count(sub_word, vowels: dict) -> int:
        nonlocal seen
        # Need to trim left, right or both and advance only if still valid
        if not all(vowels.values()):
            return 0
        if sub_word in seen:
            return 0

        seen.add(sub_word)

        count = 1
        copy = vowels.copy()
        if sub_word[0] in "aeiou":
            copy[sub_word[0]] -= 1
            count += valid_count(sub_word[1:], copy)

        copy = vowels.copy()
        if sub_word[-1] in "aeiou":
            copy[sub_word[-1]] -= 1
            count += valid_count(sub_word[:-1], copy)

        return count

    count = 0
    i = 0
    while i + k + 1 < len(indices):
        # Include k consonants
        st = indices[i] + 1
        ed = indices[i + k + 1]

        vowels = {v: 0 for v in "aeiou"}
        sub_word = word[st:ed]

        for char in sub_word:
            if char in "aeiou":
                vowels[char] += 1

        # Ensure uniques
        seen = set()
        count += valid_count(sub_word, vowels)
        i += 1

    return count
