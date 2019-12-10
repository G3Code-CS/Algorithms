#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = [math.floor(ingredients.get(key)/value) if (ingredients.get(key)) else 0 for key, value in recipe.items()]
    print(batches)
    batches.sort()
    return batches[0]



if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5, 'nuts': 10}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
