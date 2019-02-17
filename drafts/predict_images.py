#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Phyo Phyo Kyaw Zin
#
# Created:     17/02/2019
# Copyright:   (c) kzphy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import numpy as np
import os
import matplotlib.pyplot as plt
from keras.layers import Dense,GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.models import load_model
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import itertools

class ChooseRecipe:
    def __init__(self):
        file = 'recipes/result.csv'
        self.reader(file)
        self.ingredient_list =  list(self.food_dict.values())
        self.recipe()

    def reader(self, file):
        '''
        Read the ingredient csv file formatted as: ID,cuisine,ingredients.
        Returns a dictionary containing cuisine and respective ingredients in dictionary format.
        '''
        f = open(file, 'r')
        #self.food_dict = {e[0]:' '.join(e[2:]).split() for e in [i.rstrip().split(',') for i in f.readlines()[1:]]}
        #self.food_dict = {e[1]:sorted([x for x in e[2:] if x]) for e in [i.rstrip().split(',') for i in f.readlines()[1:]]}
        self.food_dict = {e[1]:[x for x in e[2:] if x] for e in [i.split(',') for i in f.read().splitlines()[1:]]}

    def recipe(self):
        f = open('recipes/fake-recipes.csv', 'r')
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

# Load model

model = load_model("all_groceries_model.h5")

os.environ["CUDA_VISIBLE_DEVICES"]="0,1"

def main():
    labels = {0: 'Apple Braeburn',
     1: 'Apple Golden 1',
     2: 'Apple Golden 2',
     3: 'Apple Golden 3',
     4: 'Apple Granny Smith',
     5: 'Apple Red 1',
     6: 'Apple Red 2',
     7: 'Apple Red 3',
     8: 'Apple Red Delicious',
     9: 'Apple Red Yellow 1',
     10: 'Apple Red Yellow 2',
     11: 'Apricot',
     12: 'Asparagus',
     13: 'Aubergine',
     14: 'Avocado',
     15: 'Avocado ripe',
     16: 'Banana',
     17: 'Banana Lady Finger',
     18: 'Banana Red',
     19: 'Brown-Cap-Mushroom',
     20: 'Cabbage',
     21: 'Cactus fruit',
     22: 'Cantaloupe 1',
     23: 'Cantaloupe 2',
     24: 'Carambula',
     25: 'Carrots',
     26: 'Cherry 1',
     27: 'Cherry 2',
     28: 'Cherry Rainier',
     29: 'Cherry Wax Black',
     30: 'Cherry Wax Red',
     31: 'Cherry Wax Yellow',
     32: 'Chestnut',
     33: 'Clementine',
     34: 'Cocos',
     35: 'Cucumber',
     36: 'Dates',
     37: 'Garlic',
     38: 'Ginger',
     39: 'Granadilla',
     40: 'Grape Blue',
     41: 'Grape Pink',
     42: 'Grape White',
     43: 'Grape White 2',
     44: 'Grape White 3',
     45: 'Grape White 4',
     46: 'Grapefruit Pink',
     47: 'Grapefruit White',
     48: 'Guava',
     49: 'Hazelnut',
     50: 'Huckleberry',
     51: 'Juice',
     52: 'Kaki',
     53: 'Kiwi',
     54: 'Kumquats',
     55: 'Leek',
     56: 'Lemon',
     57: 'Lemon Meyer',
     58: 'Limes',
     59: 'Lychee',
     60: 'Mandarine',
     61: 'Mango',
     62: 'Mangostan',
     63: 'Maracuja',
     64: 'Melon Piel de Sapo',
     65: 'Milk',
     66: 'Mulberry',
     67: 'Nectarine',
     68: 'Oat-Milk',
     69: 'Oatghurt',
     70: 'Onion',
     71: 'Orange',
     72: 'Papaya',
     73: 'Passion Fruit',
     74: 'Peach',
     75: 'Peach 2',
     76: 'Peach Flat',
     77: 'Pear',
     78: 'Pear Abate',
     79: 'Pear Kaiser',
     80: 'Pear Monster',
     81: 'Pear Williams',
     82: 'Pepino',
     83: 'Pepper',
     84: 'Physalis',
     85: 'Physalis with Husk',
     86: 'Pineapple',
     87: 'Pineapple Mini',
     88: 'Pitahaya Red',
     89: 'Plum',
     90: 'Plum 2',
     91: 'Plum 3',
     92: 'Pomegranate',
     93: 'Pomelo Sweetie',
     94: 'Potato',
     95: 'Quince',
     96: 'Rambutan',
     97: 'Raspberry',
     98: 'Red-Beet',
     99: 'Redcurrant',
     100: 'Salak',
     101: 'Sour-Cream',
     102: 'Sour-Milk',
     103: 'Soy-Milk',
     104: 'Soyghurt',
     105: 'Strawberry',
     106: 'Strawberry Wedge',
     107: 'Tamarillo',
     108: 'Tangelo',
     109: 'Tomato',
     110: 'Tomato 1',
     111: 'Tomato 2',
     112: 'Tomato 3',
     113: 'Tomato 4',
     114: 'Tomato Cherry Red',
     115: 'Tomato Maroon',
     116: 'Walnut',
     117: 'Yoghurt',
     118: 'Zucchini'}

    photo_datagen = ImageDataGenerator(rescale=1. / 255)

    directory = filedialog.askdirectory()

    ##pred_dir = 'RecipeCoach/scripts/ToPredict/'

    photo_generator=photo_datagen.flow_from_directory(directory=directory,
                                                     target_size=(224,224),
                                                     color_mode='rgb',
                                                     batch_size=32,
                                                     class_mode='categorical',
                                                     shuffle=True)

    photo_generator.reset()
    pred=model.predict_generator(photo_generator,verbose=1,steps=1)
    predicted_class_indices=np.argmax(pred,axis=1)
    predictions = [labels[k] for k in predicted_class_indices]

    ingredients_in_possession = list(set(list(itertools.chain(*predictions))))
    print('Here are the ingredients we detected in your pantry:')
    for r in ingredients_in_possession:
        print(r)

    #ingredients_in_possession = ['romaine lettuce', 'black olives', 'grape tomatoes', 'garlic', 'pepper', 'purple onion', 'seasoning', 'garbanzo beans', 'feta cheese crumbles', 'yellow corn meal', 'boiling water', 'butter', 'fresh parmesan cheese', 'sea salt', '', 'cajun_creole35', 'chicken broth', 'chicken breasts', 'hot sauce', 'red bell pepper', 'potatoes', 'bacon', 'garlic cloves', 'fresh parsley', 'andouille sausage', 'cajun seasoning', 'peanut oil', 'celery', 'ground red pepper', 'all-purpose flour', 'shrimp', 'onion', 'lemongrass', 'large garlic cloves', 'rice', 'unsweetened coconut milk', 'fresh ginger', 'peanut sauce', 'spareribs', 'sesame oil', 'tamari soy sauce', 'golden brown sugar', 'dry sherry', 'boiling water']

    sample = ChooseRecipe()
    dishes = sample.find_cuisines(ingredients_in_possession)

    print('Here are the possible dishes or cuisines you can make with what you have: ')
    print(dishes)

main()


##    for eachObject in detections:
##        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


##def main():
##
##    # Load model
##    model = load_model("all_groceries_model.h5")
##
##
##    img_width, img_height = 224, 224
##
##
##    # Get test image ready
##    test_image = image.load_img('/test/3_100.jpg', target_size=(img_width, img_height))
##    test_image = image.img_to_array(test_image)
##    test_image = np.expand_dims(test_image, axis=0)
##
##    test_image = test_image.reshape(img_width, img_height)    # Ambiguity!
##    # Should this instead be: test_image.reshape(img_width, img_height, 3) ??
##
####    result = model.predict(test_image, batch_size=1)
####    #step_size_test=test_generator.n//test_generator.batch_size
####    filenames = test_generator.filenames[:20]
####    nb_samples = len(filenames)
##    predict = model.predict(test_image)
##    predicted_class_indices=np.argmax(predict,axis=1)
##    predictions = [labels[k] for k in predicted_class_indices]
##    print(predictions)
##
##if __name__ == '__main__':
##    main()
