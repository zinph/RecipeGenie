"""
#Reference: https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606

Programmers: Phyo Phyo Kyaw Zin & Tripti Samal

"""
#from ChooseRecipe import *
from imageai.Detection import ObjectDetection
import os
import time
import itertools
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import shutil


def convert_time(second):
    day = second/86400
    hour = (day - int(day))*24
    minute = (hour - int(hour))*60
    second = round((minute - int(minute))*60,4)
    return(str(int(day)) + ' DAYS: '+ str(int(hour)) + ' HOURS: '+ str(int(minute)) + ' MINUTES: ' + str(second) + ' SECONDS')


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
    
def main():
    print('Choose your pantry folder:')
    
    directory = filedialog.askdirectory()
    file_list = os.listdir(directory)
    print('Pantry Folder selected at ', directory)
    
    #execution_path = os.getcwd()
    
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    #detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    print('Load the model.')
    detector.setModelPath(askopenfilename())
    detector.loadModel()
    
    my_pantry = []
    print('Detecting items in the images from your pantry...')
    #newfolderpath = directory + '/boundingbox'
    #if not os.path.exists(newfolderpath):
    #    os.mkdir(newfolderpath)
    start_time = time.time()
    for i in file_list:
        #detections = detector.detectObjectsFromImage(input_image=os.path.join(directory , i), output_image_path=os.path.join(newfolderpath, i[:-4]+"-new.jpg"))
        detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(directory , i), output_image_path=os.path.join(directory , i[:-4]+"-new.jpg"), extract_detected_objects=True)
        all_items = []
        for j in detections:
            all_items.append(j["name"])
        each_photo = list(set(all_items))
        my_pantry.append(each_photo)
    
    
    newfolder = directory + '/ingredients'
    if not os.path.exists(newfolder):
        os.mkdir(newfolder)
    
    for i in file_list:
        src = directory + '/' + i[:-4]+ "-new.jpg" + "-objects"
        src_files = os.listdir(src)
        for files in src_files:
            full_file_name = os.path.join(src, files)
            if (os.path.isfile(full_file_name)):
                try:
                    shutil.copy(full_file_name, newfolder)
                except shutil.SameFileError:
                    # code when Exception occur
                    pass
                else:
                    # code if the exception does not occur
                    pass
                finally:
                    shutil.rmtree(src)
                    # code which is executed always
                #shutil.copy(full_file_name, newfolder)
    
    ingredients_in_possession = list(set(list(itertools.chain(*my_pantry))))
    print('Here are the ingredients we detected in your pantry:')
    for r in ingredients_in_possession:
        print(r)
    
    #ingredients_in_possession = ['romaine lettuce', 'black olives', 'grape tomatoes', 'garlic', 'pepper', 'purple onion', 'seasoning', 'garbanzo beans', 'feta cheese crumbles', 'yellow corn meal', 'boiling water', 'butter', 'fresh parmesan cheese', 'sea salt', '', 'cajun_creole35', 'chicken broth', 'chicken breasts', 'hot sauce', 'red bell pepper', 'potatoes', 'bacon', 'garlic cloves', 'fresh parsley', 'andouille sausage', 'cajun seasoning', 'peanut oil', 'celery', 'ground red pepper', 'all-purpose flour', 'shrimp', 'onion', 'lemongrass', 'large garlic cloves', 'rice', 'unsweetened coconut milk', 'fresh ginger', 'peanut sauce', 'spareribs', 'sesame oil', 'tamari soy sauce', 'golden brown sugar', 'dry sherry', 'boiling water']
    
    sample = ChooseRecipe()
    dishes = sample.find_cuisines(ingredients_in_possession)
    
    
    print('Here are the possible dishes or cuisines you can make with what you have: ')
    print(','.join(dishes))
    duration = convert_time(time.time()-start_time)
    print('Time Elapsed: ' + str(duration))
    
    print( 'Recipes for the above dishes: ')
    for j in dishes:
        print(j, '\n***************')
        print(''.join(sample.recipe_dict[j]))
    
main()


##    for eachObject in detections:
##        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


