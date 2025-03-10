# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10


def func(word: str, k: int):
    # Since we can have multiple aeiou's and only k consonants, we need a two pointer method

    # The key is to only account for the start index when advancing
    # and keep track if we have a complete aeiou and consonant count

    count = 0

    start = 0
    end = 0

    vowels = {v: 0 for v in "aeiou"}
    consonants = 0

    def remove_char(char):
        nonlocal vowels, consonants
        if char in "aeiou":
            vowels[char] -= 1
        else:
            consonants -= 1

    def add_char(char):
        nonlocal vowels, consonants
        if char in "aeiou":
            vowels[char] += 1
        else:
            consonants += 1

    while start <= end and end < len(word):
        add_char(word[end])
        end += 1

        if consonants > k:
            remove_char(word[start])
            start += 1
        if consonants == k and all(vowels.values()):
            count += 1

    # Start trimming from the start to make sure we can get all sub strings
    while start <= end:
        remove_char(word[start])
        start += 1
        if consonants == k and all(vowels.values()):
            count += 1
        else:
            break

    return count
