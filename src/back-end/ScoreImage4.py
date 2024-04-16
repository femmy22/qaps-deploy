#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np

from Straightness import calculateStraightness, LineLength
from Alignment import calculateAlignment
from Equilaterality import calculateEquilaterality

# <><><><><><><><><><><> Image 4: Three Horizontal Lines <><><><><><><><><><><> 

def ScoreImage4(X_coordinates, Y_coordinates, TimeCoordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 4: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        if (len(X_coordinates) < 3) or (len(Y_coordinates) < 3):
            print("\nSCORE IMAGE 4: Not enough lists of X or Y coordinates provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # <><><><> Calculate Error Measures <><><><>     
        # Length of lines
        lengths_of_lines = []

        first_line_length = LineLength(X_coordinates[0], Y_coordinates[0])
        if first_line_length == "Error" or first_line_length == 0:
            print("Error in ScoreImage4.py, ScoreImage4()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        second_line_length = LineLength(X_coordinates[1], Y_coordinates[1])
        if second_line_length == "Error" or second_line_length == 0:
            print("Error in ScoreImage4.py, ScoreImage4()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        third_line_length = LineLength(X_coordinates[2], Y_coordinates[2])
        if third_line_length == "Error" or third_line_length == 0:
            print("Error in ScoreImage4.py, ScoreImage4()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        lengths_of_lines.append(first_line_length)
        lengths_of_lines.append(second_line_length)
        lengths_of_lines.append(third_line_length)
        average_line_length = (lengths_of_lines[0] + lengths_of_lines[1] + lengths_of_lines[2]) / 3

        # Distances between lines
        # Find the Top line
        line_vertical_position = [np.nanmean(Y_coordinates[0]), np.nanmean(Y_coordinates[1]), np.nanmean(Y_coordinates[2])]
        top_line_index = np.argmax(line_vertical_position)

        # Find the Middle line
        line_vertical_position[top_line_index] = -float('Inf')
        mid_line_index = np.argmax(line_vertical_position)

        # Find the Bottom line
        line_vertical_position[mid_line_index] = -float('Inf')
        bottom_line_index = np.argmax(line_vertical_position)

        top_middle_gap = abs(np.nanmean(np.asarray(Y_coordinates[mid_line_index])) - np.nanmean(np.asarray(Y_coordinates[top_line_index])))
        bottom_middle_gap = abs(np.nanmean(np.asarray(Y_coordinates[bottom_line_index])) - np.nanmean(np.asarray(Y_coordinates[mid_line_index])))
        average_gap = (top_middle_gap + bottom_middle_gap) / 2

        # <><><><> Analysis of the ability to copy the shape <><><><>
        # Calculate the Straightness Score
        straightness_score = calculateStraightness(X_coordinates, Y_coordinates)
        if straightness_score == "Error":
            print("Error in ScoreImage4.py, ScoreImage4()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Average of the deviation from straight lines
        average_line_deviation = 1 / straightness_score

        # Calculate the Alignment and Alignment Score
        raw_alignment, alignment_score = calculateAlignment(4, X_coordinates[0], Y_coordinates[0], X_coordinates[1], Y_coordinates[1], X_coordinates[2], Y_coordinates[2])
        if raw_alignment == "Error" and alignment_score == "Error":
            print("Error in ScoreImage4.py, ScoreImage4()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Calculate the Line Ratio Score
        line_ratio_score = max((1 - abs(1/3 - (lengths_of_lines[mid_line_index] / lengths_of_lines[top_line_index]) )), 0)

        # Calculate the Equilaterality Score
        equilaterality_score = calculateEquilaterality([X_coordinates[top_line_index],X_coordinates[bottom_line_index]], [Y_coordinates[top_line_index],Y_coordinates[bottom_line_index]])
        if equilaterality_score == "Error":
            print("Error in ScoreImage4.py, ScoreImage4()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Calculate the Spacing Score
        spacing_score = min(top_middle_gap, bottom_middle_gap) / max(top_middle_gap, bottom_middle_gap)

        return (round(straightness_score, 4), round(equilaterality_score, 4), round(alignment_score, 4), 
                round(spacing_score, 4), round(line_ratio_score, 4), round(average_line_length, 4), 
                round(average_line_deviation, 4), round(average_gap, 4), round(raw_alignment, 4),
                round(top_middle_gap, 4), round(bottom_middle_gap, 4))
    
    except Exception as e:
        print("Error in ScoreImage4.py, ScoreImage4(): " + str(e))
        return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
        