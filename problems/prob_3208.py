# https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09

# 0 = red
# 1 = blue


def func(colors: list[int], k: int):
    # Maybe bit manipulation can enhance performance? we will task with that l8r.
    # for now a sliding window approach of size K seems to work in theory

    count = 0

    start = 0
    end = 0

    for i in range(1, len(colors) + k):
        if end - start == k - 1:
            count += 1
            start += 1

        if colors[i % len(colors)] != colors[(i - 1) % len(colors)]:
            end += 1
        else:
            start = end = i

    return count
