# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10


def func(word: str, k: int):
    # Find all consonant indices
    indices = [0] + [i for i, c in enumerate(word) if c not in "aeiou"] + [len(word)]

    def valid_count(sub_word: str) -> int:
        # Run two pointers between them and count all valid substrings

        # This sub word contains only k consonants and vowels
        count = 0
        vowels = {v: 0 for v in "aeiou"}

        for char in sub_word:
            if char in "aeiou":
                vowels[char] += 1

        vowels_copy = vowels.copy()

        if not all(vowels_copy.values()):
            # Return early no way to cut.
            return 0

        count += 1

        # Left trim
        for char in sub_word:
            if char not in "aeiou":
                break

            vowels_copy[char] -= 1

            if not all(vowels_copy.values()):
                break

            count += 1

        vowels_copy = vowels.copy()

        # Right trim
        for char in sub_word[::-1]:
            if char not in "aeiou":
                break

            vowels_copy[char] -= 1

            if not all(vowels_copy.values()):
                break

            count += 1

        return count

    count = 0
    i = 0
    while i + k + 1 < len(indices):
        # Include k consonants
        st = indices[i]
        ed = indices[i + k + 1]
        count += valid_count(word[st:ed])
        i += 1

    return count
