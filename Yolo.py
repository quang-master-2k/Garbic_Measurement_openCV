import cv2
import os
from ultralytics import YOLO
from skimage.filters.thresholding import threshold_isodata
import time

class YoloModel:
    def __init__(self, model_path = 'models/best640_3.pt', threshold_type = cv2.THRESH_BINARY):
        # This is the constructor method
        # Initialize instance variables here
        self.model_path = model_path
        self.model = YOLO(model_path)
        self.threshold_type = threshold_type
        self.keypoints_yolo = None
        self.image = None
        self.image_binary = None

    def image_gray(self, input_image):
        imgGray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
        return imgGray

    def binary_contours(self, input_imgGray, threshold_type):
        binaryThreshold = threshold_isodata(input_imgGray)
        _, threshold = cv2.threshold(input_imgGray, binaryThreshold, 255, threshold_type)
        return threshold

    def process(self, image_path):
        self.image_binary =  cv2.cvtColor(self.binary_contours(self.image_gray(image_path), self.threshold_type), cv2.COLOR_GRAY2RGB)

        self.keypoints_yolo = self.model(self.image_binary)[0].keypoints.xy.tolist()
        self.image = image_path
    
        for point_indx, point in enumerate(self.keypoints_yolo[0]):
            cv2.circle(self.image_binary, tuple([int(point[0]), int(point[1])]), 1, (0, 0, 255), -1)
            cv2.putText(self.image_binary, str(point_indx), (int(point[0]), int(point[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)

    def plotting(self, outputFolder):
        cv2.imwrite(os.path.join(outputFolder, "yolo.png"), self.image_binary)



  

