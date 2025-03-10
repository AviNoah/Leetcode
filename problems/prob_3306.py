# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10


def func(word: str, k: int):
    # Since we can have multiple aeiou's and only k consonants, we need a two pointer method

    # The key is to only account for the start index when advancing
    # and keep track if we have a complete aeiou and consonant count

    count = 0
    vowels = {v: 0 for v in "aeiou"}
    consonants = 0

    start = 0

    def remove_char(char: str):
        nonlocal vowels, consonants
        if char in "aeiou":
            vowels[char] -= 1
        else:
            consonants -= 1

    def add_char(char: str):
        nonlocal vowels, consonants
        if char in "aeiou":
            vowels[char] += 1
        else:
            consonants += 1

    for i in range(len(word)):
        if all(vowels.values()) and consonants == k:
            remove_char(word[start])
            count += 1
            start += 1
        elif consonants > k:
            for _ in range(k, consonants):
                remove_char(word[start])
                start += 1

        add_char(word[i])

    if all(vowels.values()) and consonants == k:
        count += 1
    return count
