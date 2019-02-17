#-------------------------------------------------------------------------------
# Name:        foodfinder
# Purpose:     Based on ingredients detected, will suggest dishes/cuisines
#
# Author:      Phyo Phyo Zin
#
# Created:     16/02/2019
# Copyright:   (c) kzphy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

class ChooseRecipe:
    def __init__(self):
        file = 'recipes/result_fake_recipes.csv'
        self.reader(file)
        self.cuisine_recipe(file)
        self.ingredient_list =  list(self.food_dict.values())
        self.cuisine_recipe(file)

    def reader(self, file):
        '''
        Read the ingredient csv file formatted as: ID,cuisine,ingredients.
        Returns a dictionary containing cuisine and respective ingredients in dictionary format.
        '''
        f = open(file, 'r')
        #self.food_dict = {e[0]:' '.join(e[2:]).split() for e in [i.rstrip().split(',') for i in f.readlines()[1:]]}
        #self.food_dict = {e[1]:sorted([x for x in e[2:] if x]) for e in [i.rstrip().split(',') for i in f.readlines()[1:]]}
        self.food_dict = {e[1]:[x for x in e[2:] if x] for e in [i.split(',') for i in f.read().splitlines()[1:]]}

    def cuisine_recipe(self, file):
        '''
        Read the ingredient csv file formatted as: ID,cuisine,ingredients.
        Returns a dictionary containing cuisine and respective ingredients in dictionary format.
        '''
        f = open(file, 'r')
        self.recipe_dict = {e[0]:e[1] for e in [i.split(',') for i in f.read().splitlines()[1:]]}


##def numIngredients_cuisine(self):

##    self.ids = list(food_dict.keys())
##    temp = {}   # for each cuisine, generate a number of ingredients associated
##    for i in self.ids:
##        temp[i]=len(food_dict[i])
##    unique_num_ingredients = set(list(temp.values()))   # different numbers of ingredients
##    self.numIngredients_cuisine_dict = dict()
##    for i in unique_num_ingredients:
##        self.numIngredients_cuisine_dict[i] += []

    def find_cuisines(self,target):
        possible_recipes = []
        for i in self.ingredient_list:
            # if all the required ingredients of the possible recipe is in target list (which is the food you actually have)
##            if set(i) <= set(target):
            if set(i).issubset(target):
                possible_recipes.append(list(self.food_dict.keys())[list(self.food_dict.values()).index(i)])
        return list(set(possible_recipes))


