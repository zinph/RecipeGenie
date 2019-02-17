"""
#Reference: https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606

@author: Tripti
"""
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "fruit.jpeg"), output_image_path=os.path.join(execution_path , "fruitnew.jpg"))
print(detections)
#for eachObject in detections:
#    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


