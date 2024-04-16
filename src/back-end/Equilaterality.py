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

# <><><><><><><><><><><> Equilaterality <><><><><><><><><><><> 
# X_coordinates and Y_coordinates should be 2D-lists of coordinates where each row represents a line in a given image
def calculateEquilaterality(X_coordinates, Y_coordinates):
    try:
        lengths_of_all_lines = []

        # Calculate the lengths of all the lines
        for index in range(len(X_coordinates)):
            line_length = LineLength(X_coordinates[index], Y_coordinates[index])
            if line_length == "Error":
                print("Error in Equilaterality.py, calculateEquilaterality()")
                return "Error"

            lengths_of_all_lines.append(line_length)

        # Find the length of the shortest and the longest lines
        l_short = min(lengths_of_all_lines)
        l_long = max(lengths_of_all_lines)

        # Calculate Equilaterality
        equilaterality_score = l_short / l_long

        return equilaterality_score
        
    except Exception as e:
        print("Error in Equilaterality.py, calculateEquilaterality()" + str(e))
        return "Error"
    