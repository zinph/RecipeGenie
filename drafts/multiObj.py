"""
#Reference: https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606

@author: Tripti

# Phyo Phyo #added the directory picker
"""
from imageai.Detection import ObjectDetection
import os
from tkinter import filedialog

#
#def get_photos():
#    '''Prompt the user for the folder path, and read all the files with it.'''
#    #location = input('Please indicate whether right or left you want to label (r, l): ').lower()
#    directory = filedialog.askdirectory()
#    file_list = os.listdir(directory)
#    
#    return file_list

directory = filedialog.askdirectory()
file_list = os.listdir(directory)

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

#all_photos = get_photos()
for i in file_list:
    
    detections = detector.detectObjectsFromImage(input_image=os.path.join(directory , i), output_image_path=os.path.join(directory , i[:-4]+"-new.jpg"))
#    unique_groceries = list(set(detections["name"]))
#    print(unique_groceries)
    all_items = []
    for j in detections:
        all_items.append(j["name"])
    print(i, ',', list(set(all_items)))
##    for eachObject in detections:
##        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


