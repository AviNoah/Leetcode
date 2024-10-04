# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

# Make teams of two out of N participants
# The power of each team must all be equal
# Return the sum of the product of each team


def set_approach(skill: list[int]) -> int:
    # The first team should always be the best and the worst participants
    target = max(skill) + min(skill)  # O(n)

    # Pick available partner from the partner dict if available
    partner_map: dict[int, int] = dict()
    product = 0

    # O(n)
    for num in skill:
        needed = target - num

        if needed in partner_map and partner_map[needed] > 0:
            partner_map[needed] -= 1
            product += needed * num
        else:
            # Add as an available partner
            if num not in partner_map:
                partner_map[num] = 0

            partner_map[num] += 1

    return product if all([val == 0 for val in partner_map.values()]) else -1
