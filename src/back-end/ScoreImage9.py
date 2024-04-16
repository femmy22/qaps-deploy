#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

from Straightness import calculateStraightness, LineLength
from Equilaterality import calculateEquilaterality
from Find4Sides import find4SidesOfSquare
from Find4Sides import identifyPossibleCorners
from Find4Sides import selectCorrectCorners
from Find4Sides import sortCorners
from Closure import calculateClosure

# <><><><><><><><><><><> Image 9: Square<><><><><><><><><><><> 

def ScoreImage9(X_coordinates, Y_coordinates, Time_coordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 9: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        if (len(X_coordinates) > 4) or (len(Y_coordinates) > 4):
            print("\nSCORE IMAGE 10: Too many lists of X or Y coordinates provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        possible_corners, possible_corner_indexes = identifyPossibleCorners(X_coordinates, Y_coordinates)
        if possible_corners == "Error" and possible_corner_indexes == "Error":
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        sorted_corners_indexes = sortCorners(possible_corner_indexes)
        if sorted_corners_indexes == "Error":
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        X_sides, Y_sides = find4SidesOfSquare(X_coordinates, Y_coordinates, sorted_corners_indexes)
        if X_sides == "Error" and Y_sides == "Error":
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        if (len(X_sides) < 4) or (len(Y_sides) < 4):
            print("Error in ScoreImage9.py, ScoreImage9(): Could not find four sides")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # <><><><> Calculate error measures <><><><>
        # Length of the Lines
        first_line_length = LineLength(X_sides[0], Y_sides[0])
        if first_line_length == "Error" or first_line_length == 0:
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        second_line_length = LineLength(X_sides[1], Y_sides[1])
        if second_line_length == "Error" or second_line_length == 0:
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        third_line_length = LineLength(X_sides[2], Y_sides[2])
        if third_line_length == "Error" or third_line_length == 0:
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        fourth_line_length = LineLength(X_sides[3], Y_sides[3])
        if fourth_line_length == "Error" or fourth_line_length == 0:
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        average_line_length = ((first_line_length + second_line_length + third_line_length + fourth_line_length) / 4)

        average_gap = calculateClosure(9, X_sides[0], Y_sides[0], X_sides[1], Y_sides[1], X_sides[2], Y_sides[2], X_sides[3], Y_sides[3])
        if average_gap == "Error":
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
        
        # <><><><> Analysis of the ability to copy the shape <><><><>
        # Calculate the Straightness Score
        straightness_score = calculateStraightness(X_sides, Y_sides)
        if straightness_score == "Error":
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Calculate the Equilaterality Score
        equilaterality_score = calculateEquilaterality(X_sides, Y_sides)
        if equilaterality_score == "Error":
            print("Error in ScoreImage9.py, ScoreImage9()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Average of the deviation from straight lines
        average_line_deviation = 1 / straightness_score

        # Calculate the Closure Score
        closure_score = max([ (1- (average_gap / average_line_length)), 0])

        return (round(straightness_score, 4), round(equilaterality_score, 4), round(closure_score, 4), 
                round(average_line_length, 4), round(average_line_deviation, 4), round(average_gap , 4))

    except Exception as e:
        print("Error in ScoreImage9.py, ScoreImage9(): " + str(e))
        return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)