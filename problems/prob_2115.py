# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=daily-question&envId=2025-03-21


def func(recipes: list[str], ingredients: list[list[str]], supplies: list[str]):
    # We can either loop over all recipes, adding them to available supplies when crafted
    # and stop when no new recipes are added, or we can simplify the recipe of each recursively
    # and then check if it is a subset of supplies.

    # We can simplify the recipes list to a set of their base ingredients,
    # if a recipe includes another recipe, simplify
    # At the end, check if base ingredients set is contained with in ingredients

    cookbook = dict(zip(recipes, ingredients))

    def simplify(ingredients) -> set[str]:
        nonlocal cookbook
        base_ing: set[str] = set()

        for ing in ingredients:
            if ing in cookbook:
                base_ing.union(simplify(cookbook[ing]))
            base_ing.add(ing)

        return base_ing

    return set(
        recipe
        for recipe, ingredients in cookbook.items()
        if simplify(ingredients).issubset(supplies)
    )
