# https://leetcode.com/problems/apply-operations-to-maximize-score/description/?envType=daily-question&envId=2025-03-29


from math import sqrt


def prime_score(num):
    "Prime score is num of distinct prime factors"
    prime_set = set()

    while num % 2 == 0:
        prime_set.add(2)
        num /= 2

    # Skip even numbers
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            num /= i
            prime_set.add(i)

    if num > 1:
        # is prime
        prime_set.add(num)

    return len(prime_set)


def nle(scores: list[int]):
    "return array r where r[i] is the index of the nearest left element with scores[r[i]] >= scores[i]"
    results = [-1] * len(scores)

    # Descending monotonic stack
    stack: list[int] = []

    for i, score in enumerate(scores):
        while stack and scores[stack[-1]] <= score:
            stack.pop()

        if stack:
            results[i] = stack[-1]

        stack.append(i)

    return results


def nre(scores: list[int]):
    "return array r where r[i] is the index of the nearest right element with scores[r[i]] >= scores[i]"
    results = [len(scores)] * len(scores)

    # Descending monotonic stack
    stack: list[int] = []

    for i, score in enumerate(scores):
        while stack and scores[stack[-1]] <= score:
            index = stack.pop()
            results[index] = i

        stack.append(i)

    return results


def func(nums: list[str], k: int):
    # We have some quality - prime score which all numbers have in the array
    # Select the left-most maximum one out of unique sub arrays k times - overlap?, and multiply with score
    # return max possible score

    # We first need to calculate all prime scores
    scores = [prime_score(num) for num in nums]

    # We then find maximum possible prime score multiplication
    left = nle(scores)
    right = nre(scores)
    score = ...
    return score % (10**9 + 7)
