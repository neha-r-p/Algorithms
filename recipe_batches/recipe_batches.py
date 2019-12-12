#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # print(recipe.items())
    batches = None
    #if the recipe has ingredients that are unavailable, return 0
    if len(recipe.items()) > len(ingredients.items()):
        batches = 0
    #check each value of recipe to ingredient and ingredient//recipe. Number of whole batches is smallest number?
    else:
        for k1,v1 in recipe.items():
            # print("k1:",k1)
            for k2,v2 in ingredients.items():
                # print("k2:", k2)
                if k1 == k2:
                    if v2 > v1 and batches == None:
                        batches = v2//v1
                    elif v2//v1 < batches:
                        batches = v2//v1
                    # elif v2<v1: #if recipe requires more than ingredients has, return 0
                    #     batches = 0
    #return maximum number of whole batches
    return batches
    

# print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10 }, { 'milk': 1288, 'flour': 3, 'sugar': 95 }))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))