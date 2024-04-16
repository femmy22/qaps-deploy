#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

from Straightness import calculateStraightness, LineLength
from Alignment import calculateAlignment

# <><><><><><><><><><><> Image 10: Two Different Length Vertical Lines <><><><><><><><><><><> 

def ScoreImage10(X_coordinates, Y_coordinates, Time_coordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 10: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
            
        if (len(X_coordinates) > 2) or (len(Y_coordinates) > 2):
            print("\nSCORE IMAGE 10: Too many lists of X or Y coordinates provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # <><><><> Calculate error measures <><><><>
        # Length of the Lines
        first_line_length = LineLength(X_coordinates[0], Y_coordinates[0])
        if first_line_length == "Error" or first_line_length == 0:
            print("Error in ScoreImage10.py, ScoreImage10()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        second_line_length = LineLength(X_coordinates[1], Y_coordinates[1])
        if second_line_length == "Error" or second_line_length == 0:
            print("Error in ScoreImage10.py, ScoreImage10()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        average_line_length = ((first_line_length + second_line_length) / 2)

        # Distance Between the Lines
        gap = abs(np.nanmean(np.asarray(X_coordinates[1]) - np.asarray(X_coordinates[0])))

        # <><><><> Analysis of the ability to copy the shape <><><><>
        # Calculate the Straightness Score
        straightness_score = calculateStraightness(X_coordinates, Y_coordinates)
        if straightness_score == "Error":
            print("Error in ScoreImage10.py, ScoreImage10()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Average of the deviation from straight lines
        average_line_deviation = 1 / straightness_score

        # Calculate the Alignment and Alignment Score
        raw_alignment, alignment_score = calculateAlignment(10, X_coordinates[0], Y_coordinates[0], X_coordinates[1], Y_coordinates[1])
        if raw_alignment == "Error" and alignment_score == "Error":
            print("Error in ScoreImage10.py, ScoreImage10()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Calculate the Line Ratio Score
        line_ratio_score = max((1 - abs(1/3 - (min(first_line_length, second_line_length) / max(first_line_length, second_line_length)) )), 0)

        return (round(straightness_score, 4), round(alignment_score, 4), round(line_ratio_score, 4),
                round(average_line_length, 4), round(average_line_deviation, 4), round(gap, 4), round(raw_alignment, 4))

    except Exception as e:
        print("Error in ScoreImage10.py, ScoreImage10(): " + str(e))
        return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)