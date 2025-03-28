# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=daily-question&envId=2025-03-21


from functools import cache


def func(recipes: list[str], ingredients: list[list[str]], supplies: list[str]):
    # We can either loop over all recipes, adding them to available supplies when crafted
    # and stop when no new recipes are added, or we can simplify the recipe of each recursively
    # and then check if it is a subset of supplies.

    # We can simplify the recipes list to a set of their base ingredients,
    # if a recipe includes another recipe, simplify
    # At the end, check if base ingredients set is contained with in ingredients

    cookbook = {recipe: frozenset(ings) for recipe, ings in zip(recipes, ingredients)}

    # Use dp to memoize
    @cache
    def simplify(ingredients) -> set[str]:
        nonlocal cookbook
        base_ing: set[str] = set()

        for ing in ingredients:
            if ing in cookbook:
                base_ing |= simplify(cookbook[ing])
            else:
                base_ing.add(ing)

        return base_ing

    x = set(
        recipe
        for recipe, ingredients in cookbook.items()
        if simplify(ingredients).issubset(supplies)
    )
    return x
