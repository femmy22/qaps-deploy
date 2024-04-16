#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np

from LineLength import LineLength

# <><><><><><><><><><><> Line Straightness <><><><><><><><><><><> 
def lineStraightness(X, Y):
    try:
        # Method: Get the ratio between distance traveled and the 
        # length of a straight line drawn between the endpoints of the line segment.
        # If this ratio equals 1, the line segment is a perfectly straight line.

        # <><><><> Straight line distance <><><><>
        nan_Ix = np.isnan(X)
        nan_Iy = np.isnan(Y)

        # If no x coordinates were NaN, the last viable coordinate is at the end of the list of X coordinates
        # Otherwise, we get the coordinate directly prior to the first NaN value.
        if not (True in nan_Ix):
            last_index_x = len(X) - 1 
        else:
            last_index_x = np.asarray(X).argmax() - 1
            if (last_index_x == -1):
                last_index_x = 0

        # If no y coordinates were NaN, the last viable coordinate is at the end of the list of Y coordinates
        # Otherwise, we get the coordinate directly prior to the first NaN value.
        if not (True in nan_Iy):
            last_index_y = len(Y) - 1
        else:
            last_index_y = np.asarray(Y).argmax() - 1
            if(last_index_y == -1):
                last_index_y = 0

        # Find the location of the last useable point that will be a real number in both lists of coordinates
        last_index = min(last_index_x, last_index_y)

        # Calculate the linear length of the line between the last usable coordinate and the first coordinate
        # This is L_Shortdist
        L_Shortdist = np.sqrt( (X[last_index] - X[0])**2 + (Y[last_index] - Y[0])**2 )

        # <><><><> Actual Linear Distance Travelled <><><><>
        L_Actual = LineLength(X,Y)
        if L_Actual == "Error":
            print("Error in Straightness.py, lineStraightness()")
            return "Error"

        # Line Straightness Score
        straightness = L_Shortdist/L_Actual

        return straightness
    
    except Exception as e:
        print("Error In Straightness.py, lineStraightness(): " + str(e))
        return "Error"

# For images that contain multiple lines, the average line straightness is returned
# X_coordinates and YCoordinates should be 2D-lists of coordinates where each row represents a line in a given image
def calculateStraightness(X_coordinates, Y_coordinates):
    try:
        straightness_score = 0
        for index in range(len(X_coordinates)):
            line_straightness = lineStraightness(X_coordinates[index], Y_coordinates[index])
            if line_straightness == "Error":
                print("Error in Straightness.py, calculateStraightness()")
                return "Error"

            straightness_score += line_straightness

        straightness_score = straightness_score / len(X_coordinates)

        return straightness_score

    except Exception as e:
        print("Error In Straightness.py, calculateStraightness(): " + str(e))
        return "Error"