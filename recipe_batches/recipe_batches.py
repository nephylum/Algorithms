#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    #set a min_batches
    min_batches = None
    for item in recipe:
        #check if we have the ingredients
        if item not in ingredients:
            return 0
        #check if there is enough of the ingredient for 1 batch
        if ingredients[item] < recipe[item]:
            return 0
        #set initial min_batches
        if min_batches == None:
            min_batches = ingredients[item] / recipe[item]
        #check if it's smaller than previous min
        elif (ingredients[item] / recipe[item]) < min_batches:
            min_batches = ingredients[item] / recipe[item]
    return int(min_batches) # a whole number

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 58, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
