from Yolo import YoloModel
from TraditionalCV import TraditionalCV
from CombineModel import CombineModel
from CalculateEdge import CalculateEdgeLength
import cv2
import time

image_path = 'image_2.jpg'
plot_path = 'plot'

# Yolo Model
Yolo = YoloModel()
Yolo.process(image_path)
yolo_corners = Yolo.keypoints_yolo
Yolo.plotting(plot_path)
#yolo_corners = []

# CV Model
TradCV = TraditionalCV(threshold_type = cv2.THRESH_BINARY, num_corners = 6, position_that_have_two_corners=[1,4])
TradCV.process(image_path)
cv_corners, mask = TradCV.final_corner, TradCV.mask_accurate
TradCV.plotting(plot_path)

# Combine Yolo and CV to find orientation
Combine = CombineModel(yolo_corners, cv_corners, TradCV.threshold, mask = None)
Combine.process(num_corners = 6, mode = 'B')
Combine.plotting(plot_path)

# Calculate the length of edge
Edge = CalculateEdgeLength(mask, Combine.combine_corners, TradCV.threshold)
Edge.process()
Edge.plotting(plot_path)
print(Edge.final_length_list)

