# https://leetcode.com/problems/apply-operations-to-maximize-score/description/?envType=daily-question&envId=2025-03-29


MOD = 10**9 + 7


def sieve_prime_factors(limit):
    spf = list(range(limit + 1))  # Smallest prime factor for each number
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:  # i is a prime number
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def prime_score(num, spf):
    prime_factors = set()
    while num != 1:
        prime_factors.add(spf[num])
        num //= spf[num]
    return len(prime_factors)


def nle(scores: list[int]):
    "return array r where r[i] is the index of the nearest left element with scores[r[i]] >= scores[i]"
    results = [-1] * len(scores)

    # Descending monotonic stack
    stack: list[int] = []

    for i, score in enumerate(scores):
        while stack and scores[stack[-1]] < score:
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
        while stack and scores[stack[-1]] < score:
            index = stack.pop()
            results[index] = i

        stack.append(i)

    return results


def func(nums: list[int], k: int):
    # We have some quality - prime score which all numbers have in the array
    # Select the left-most maximum one out of unique sub arrays k times - overlap?, and multiply with score
    # return max possible score

    # We first need to calculate all prime scores
    spf = sieve_prime_factors(max(nums))
    scores = [prime_score(num, spf) for num in nums]

    left = nle(scores)
    right = nre(scores)

    # Contributions guaranteed to be unique - since we use nle and nre
    contributions = []

    for i, num in enumerate(nums):
        left_count = i - left[i]
        right_count = right[i] - i
        count = left_count * right_count

        contributions.append((num, count))

    contributions.sort(reverse=True, key=lambda x: x[0])

    result = 1
    remaining_operations = k

    for num, count in contributions:
        if remaining_operations <= 0:
            break

        # We can either use all or some of the count
        use_count = min(remaining_operations, count)
        result = (result * pow(num, use_count, MOD)) % MOD

        remaining_operations -= use_count

    return result
