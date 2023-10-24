import cv2
import numpy as np
import os

from skimage import filters
from skimage.filters.thresholding import threshold_isodata

class CalculateEdgeLength:
    def __init__(self, mask, corners, image):
        # This is the constructor method
        # Initialize instance variables here
        self.mask = mask
        self.corners = corners

        if len(image.shape) == 2:
            self.image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        elif len(image.shape) == 3:
            self.image = image

        self.final_length_list = []
        self.edge_image = None
        self.contours_image = None
        self.corners_image = None
        self.color = [
            (0, 215, 255), 
            (128, 0, 0),
            (0, 165, 255),
             (128, 128, 128),
            (230, 216, 173),
            (0, 201, 87),
            (100, 218, 255),
            (79, 79, 47)
        ]
        
        self.edge_points_list = []

    def binary_contours(self, input_imgGray, thresholdType):
        binaryThreshold = threshold_isodata(input_imgGray)
        _, threshold = cv2.threshold(input_imgGray, binaryThreshold, 255, thresholdType)
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return threshold, contours

    def euclidean_distance(self, point1, point2):
        return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def find_closest_position_corner(self, corner_x, contours):
        # Find the closest point in contours to the given corner
        min_distance = float('inf')
        closest_index = -1

        for i, point in enumerate(contours):
            distance = self.euclidean_distance(point[0], corner_x[0])
            if distance < min_distance:
                min_distance = distance
                closest_index = i

        return closest_index
        
    def create_line_iterator(self, P1, P2, img):
        """
        Produces an array that consists of the coordinates and intensities of each pixel in a line between two points

        Parameters:
            -P1: a numpy array that consists of the coordinate of the first point (x,y)
            -P2: a numpy array that consists of the coordinate of the second point (x,y)
            -img: the image being processed

        Returns:
            -it: a numpy array that consists of the coordinates and intensities of each pixel in the radii (shape: [numPixels, 3], row = [x,y,intensity])     
        """
    #define local variables for readability
        imageH = img.shape[0]
        imageW = img.shape[1]
        P1X = P1[0]
        P1Y = P1[1]
        P2X = P2[0]
        P2Y = P2[1]

        #difference and absolute difference between points
        #used to calculate slope and relative location between points
        dX = P2X - P1X
        dY = P2Y - P1Y
        dXa = np.abs(dX)
        dYa = np.abs(dY)

        #predefine numpy array for output based on distance between points
        itbuffer = np.empty(shape=(np.maximum(dYa,dXa),2),dtype=np.float32)
        itbuffer.fill(np.nan)

        #Obtain coordinates along the line using a form of Bresenham's algorithm
        negY = P1Y > P2Y
        negX = P1X > P2X
        if P1X == P2X: #vertical line segment
            itbuffer[:,0] = P1X
            if negY:
                itbuffer[:,1] = np.arange(P1Y - 1,P1Y - dYa - 1,-1)
            else:
                itbuffer[:,1] = np.arange(P1Y+1,P1Y+dYa+1)              
        elif P1Y == P2Y: #horizontal line segment
            itbuffer[:,1] = P1Y
            if negX:
                itbuffer[:,0] = np.arange(P1X-1,P1X-dXa-1,-1)
            else:
                itbuffer[:,0] = np.arange(P1X+1,P1X+dXa+1)
        else: #diagonal line segment
            steepSlope = dYa > dXa
            if steepSlope:
                slope = dX.astype(np.float32)/dY.astype(np.float32)
                if negY:
                    itbuffer[:,1] = np.arange(P1Y-1,P1Y-dYa-1,-1)
                else:
                    itbuffer[:,1] = np.arange(P1Y+1,P1Y+dYa+1)
                itbuffer[:,0] = (slope*(itbuffer[:,1]-P1Y)).astype(int) + P1X
            else:
                slope = dY.astype(np.float32)/dX.astype(np.float32)
                if negX:
                    itbuffer[:,0] = np.arange(P1X-1,P1X-dXa-1,-1)
                else:
                    itbuffer[:,0] = np.arange(P1X+1,P1X+dXa+1)
                itbuffer[:,1] = (slope*(itbuffer[:,0]-P1X)).astype(int) + P1Y

        #Remove points outside of image
        colX = itbuffer[:,0]
        colY = itbuffer[:,1]
        itbuffer = itbuffer[(colX >= 0) & (colY >=0) & (colX<imageW) & (colY<imageH)]

        return itbuffer

    def process(self):
        self.edge_image = self.image.copy()
        self.contours_image = self.image.copy()
        self.corners_image = self.mask.copy()

        for value in self.corners:
            self.corners_image = cv2.circle(self.corners_image, value, 2, (255,0,255), -1)

        tempCornerFinal = self.corners
        imgGrayMask = cv2.cvtColor(self.mask, cv2.COLOR_BGR2GRAY)
        threshold, contours = self.binary_contours(imgGrayMask, cv2.THRESH_BINARY)
        contourCalculate = contours[0]

        lengthList = []
        #contourCalculate = cutpartContours_2

        tempContour = []
        for i in contours[0]:
            tempContour.append([i[0]])

        tempCorner = []
        positionCornerList = []

        for i in range(len(tempCornerFinal)):
            positionCornerList.append(self.find_closest_position_corner([tempCornerFinal[i]], tempContour))
            tempCorner.append([np.array(tempCornerFinal[i]), self.find_closest_position_corner([tempCornerFinal[i]], tempContour)])

        colorCount = 0
        
        for index in range(len(tempCorner)):
            if tempCorner[index % len(tempCorner)][1] < tempCorner[(index+1) % len(tempCorner)][1]:
                pointsList = []
                #length = cv2.arcLength(contourCalculate[tempCorner[index % len(tempCorner)][1]:tempCorner[(index+1) % len(tempCorner)][1]], False)
                
                pointsContours1 = np.array([point[0] for point in contourCalculate[tempCorner[index % len(tempCorner)][1]:tempCorner[(index+1) % len(tempCorner)][1]]], dtype=np.int32)
                pointsContours2 = np.array([[contourCalculate[tempCorner[(index+1) % len(tempCorner)][1]][0][0], contourCalculate[tempCorner[(index+1) % len(tempCorner)][1]][0][1]]], dtype=np.int32)
                pointsContours = np.concatenate((pointsContours1, pointsContours2))

                pointsList.append([pointsContours[0][0], pointsContours[0][1]])
                for i in range(len(pointsContours)-1):
                    tempList = self.create_line_iterator(pointsContours[i], pointsContours[i+1], self.mask)
                    for j in tempList:
                       pointsList.append([j[0], j[1]])
                self.edge_points_list.append([pointsList, colorCount])  
                
                length = cv2.arcLength(np.array(pointsList, dtype=int).reshape(-1, 1, 2), False)
                #print(length)

                for points in pointsList:
                    self.edge_image = cv2.circle(self.edge_image, (int(points[0]), int(points[1])), 1,  self.color[colorCount], -1)
                
                for points in pointsContours:
                   self.contours_image = cv2.circle(self.contours_image, (points[0], points[1]), 1, self.color[colorCount], -1)
            else:
                pointsList = []
                #length = cv2.arcLength(contourCalculate[tempCorner[index % len(tempCorner)][1]:], False) + cv2.arcLength(contourCalculate[:tempCorner[(index+1) % len(tempCorner)][1]], False)
                
                pointsContours1 = np.array([point[0] for point in contourCalculate[tempCorner[index % len(tempCorner)][1]::]], dtype=np.int32)
                pointsContours2 = np.array([point[0] for point in contourCalculate[:tempCorner[(index+1) % len(tempCorner)][1]]], dtype=np.int32)
                pointsContours3 = np.array([[contourCalculate[tempCorner[(index+1) % len(tempCorner)][1]][0][0], contourCalculate[tempCorner[(index+1) % len(tempCorner)][1]][0][1]]], dtype=np.int32)

                if(len(pointsContours2) != 0):
                    pointsContours = np.concatenate((pointsContours1, pointsContours2, pointsContours3))
                else:
                    pointsContours = np.concatenate((pointsContours1, pointsContours3))

                pointsList.append([pointsContours1[0][0], pointsContours1[0][1]])
                for i in range(len(pointsContours)-1):
                    tempList = self.create_line_iterator(pointsContours[i], pointsContours[i+1], self.mask)   
                    for j in tempList:
                        pointsList.append([j[0], j[1]])
                
                length = cv2.arcLength(np.array(pointsList, dtype=int).reshape(-1, 1, 2), False)

                for points in pointsList:
                    self.edge_image = cv2.circle(self.edge_image, (int(points[0]), int(points[1])), 1,  self.color[colorCount], -1)
                for points in pointsContours:
                    self.contours_image = cv2.circle(self.contours_image, (points[0], points[1]), 1, self.color[colorCount], -1)

                self.edge_points_list.append([pointsList, colorCount])
            
            colorCount += 1
            lengthList.append(length)

        for index, value in enumerate(lengthList):
            if index == 2 or index == 5: 
                self.final_length_list.append(value/(35*2))
                self.final_length_list.append(value/(35*2))
                # self.final_length_list.append(value/35)
            else:
                self.final_length_list.append(value/35)

    def plotting(self, outputFolder):
        cv2.imwrite(os.path.join(outputFolder, "contour points on each edge.png"), self.contours_image)
        cv2.imwrite(os.path.join(outputFolder, "all points on each edge.png"), self.edge_image)
        

        

    
