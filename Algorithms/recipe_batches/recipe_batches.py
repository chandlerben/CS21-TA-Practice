#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Start out with an infinite amount of recipes being made
    # Iterate through the recipe and get both the ingredient name and amount of that ingredient
    # If the ingredient in the recipe is NOT in the ingredients, return 0
    # the new ratio is going to equal the math.floor of the ingredients[ingredient] (amount of that ingredient we have) / amount the recipe calls for.
    # if the new ratio is smaller than the infinite max number of recipes possible, that is the new max ratio.
    # print(recipe.values())
    max_ratio = math.inf

    for ingredient, amount in recipe.items():
        if ingredient not in ingredients:
            return 0
        new_ratio = (ingredients[ingredient] // amount)
        max_ratio = min(new_ratio, max_ratio)
    return max_ratio


recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
    'milk': 1288, 'flour': 9, 'sugar': 95})


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
