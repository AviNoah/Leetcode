# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10


def func(word: str, k: int):
    # We will use a sliding window technique to find at least k consonants with aeiou
    # The count of at least k + 1 - at least k consonants is exactly k consonants
    # Since it remove all the counts where there are more than k consonants
    # at_least(k) = exactly(k) + at_least(k+1) => at_least(k) = exactly(k) - at_least(k+1)

    def at_least(k: int):
        nonlocal word
        count = 0

        vowels = {v: 0 for v in "aeiuo"}
        consonants = 0

        def add_char(char):
            nonlocal vowels, consonants
            if char in "aeiou":
                vowels[char] += 1
            else:
                consonants += 1

        def remove_char(char):
            nonlocal vowels, consonants
            if char in "aeiou":
                vowels[char] -= 1
            else:
                consonants -= 1

        left = 0

        for right, char in enumerate(word):
            add_char(char)

            while consonants >= k and all(vowels.values()):
                count += len(word) - right

                # Trim the left
                remove_char(word[left])
                left += 1

        return count

    return at_least(k) - at_least(k + 1)
