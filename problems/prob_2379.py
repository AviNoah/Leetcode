# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08


def func(blocks: str, k: int):
    # We will take a sliding window approach and keep track of white and black counts
    # start and end will both advance by 1

    whites = 0
    blacks = 0

    # O(k)
    for i in range(k):
        if blocks[i] == "W":
            whites += 1
        else:
            blacks += 1

    min_count = whites

    start, end = 0, k - 1

    # O(n-k)
    for i in range(k, len(blocks)):
        if blocks[start] == "B":
            # Lost a black
            blacks -= 1
        else:
            # Lost a white
            whites -= 1

        if blocks[end + 1] == "B":
            # Gained a black
            blacks += 1
        else:
            # Gained a white
            whites += 1

        # Advance
        start += 1
        end += 1

        # compare
        min_count = min(min_count, whites)

    return min_count
