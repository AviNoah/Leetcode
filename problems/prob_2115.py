# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=daily-question&envId=2025-03-21


from collections import defaultdict, deque


def func(recipes: list[str], ingredients: list[list[str]], supplies: list[str]):
    # Supplies can be used to hold our resources and anything we can craft.
    # If a recipe is dependent on another, we would like to defer it to the end of the list,
    # hopefully that recipe would be created by then - we can do this only if the recipe is queued to be
    # crafted.

    # If we encounter an available supply, all recipes dependent on it now have it

    graph: dict[str, list] = defaultdict(list)  # Ingredient to list of recipes
    in_degree = {}  # How far the recipe is from being crafted

    for recipe, ing_list in zip(recipes, ingredients):
        in_degree[recipe] = len(ing_list)
        for ing in ing_list:
            graph[ing].append(recipe)

    queue = deque(supplies)
    craftable: list[str] = []

    # We dont really need to care how many of a supply we need, we know a recipe of 3
    # ingredients has degree 3 recipe, when we encounter the necessary ingredients, we can simply
    # decrease the degree since we can make sure a supply doesn't appear twice in the queue
    while queue:
        item = queue.popleft()

        if item in in_degree:
            # Recipe is already available as a supply, add to craftables
            craftable.append(item)

        # Supply available, reduce degree counter for each recipe dependent on it
        for recipe in graph[item]:
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                # Now a supply
                queue.append(recipe)

    return craftable
