#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

from Straightness import calculateStraightness, LineLength
from Equilaterality import calculateEquilaterality
from Closure import calculateClosure
from FindTriangleSides import identifyPossibleCorners
from FindTriangleSides import bestTriangleEdgeFinder
from FindTriangleSides import selectCorrectCorners
from FindTriangleSides import sortCorners

# <><><><><><><><><><><> Image 6: Triangle <><><><><><><><><><><> 

def ScoreImage6(X_coordinates, Y_coordinates, TimeCoordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 6: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        possible_corners, possible_corner_indexes = identifyPossibleCorners(X_coordinates, Y_coordinates)
        if possible_corners == "Error" and possible_corner_indexes == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        selected_corners, selected_corners_indexes = selectCorrectCorners(X_coordinates, Y_coordinates, possible_corners, possible_corner_indexes) 
        if selected_corners_indexes == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        sorted_corners_indexes = sortCorners(selected_corners_indexes)
        if sorted_corners_indexes == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
       
        X_sides, Y_sides = bestTriangleEdgeFinder(X_coordinates,Y_coordinates, sorted_corners_indexes)
        if X_sides == "Error" and Y_sides == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
        
        if len(X_sides) < 3 or len(Y_sides) < 3:
            print("\nSCORE IMAGE 6: Could not find 3 distinct sides")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # <><><><> Calculate error measures <><><><>     
        # Length of lines
        length_of_lines = []
        first_line_length = LineLength(X_sides[0], Y_sides[0])
        if first_line_length == "Error" or first_line_length == 0:
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        second_line_length = LineLength(X_sides[1], Y_sides[1])
        if second_line_length == 'Error' or second_line_length == 0:
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)   

        third_line_length = LineLength(X_sides[2], Y_sides[2])
        if third_line_length == "Error" or third_line_length == 0:
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        length_of_lines.append(first_line_length)
        length_of_lines.append(second_line_length)
        length_of_lines.append(third_line_length)
        average_line_length = (length_of_lines[0] + length_of_lines[1] + length_of_lines[2]) / 3

        min_length = min(length_of_lines)
        max_length = max(length_of_lines)
        short_long_side_ratio = min_length / max_length

        # <><><><> Analysis of the ability to copy the shape <><><><>
        # Calculate the Straightness Score
        straightness_score = calculateStraightness(X_sides, Y_sides)
        if straightness_score == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Average of the deviation from straight lines
        average_line_deviation = 1 / straightness_score

        # Calculate the Equilaterality Score
        equilaterality_score = calculateEquilaterality(X_sides,Y_sides)
        if equilaterality_score == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Calculate the Spacing Score
        average_gap = calculateClosure(6, X_sides[0], Y_sides[0], X_sides[1], Y_sides[1], X_sides[2], Y_sides[2])
        if average_gap == "Error":
            print("Error in ScoreImage6.py, ScoreImage6()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
    
        closure_score = max([ (1- (average_gap / average_line_length)), 0])

        return (round(straightness_score, 4), round(equilaterality_score, 4), round(closure_score, 4),
                round(average_line_length, 4), round(average_line_deviation, 4), round(average_gap, 4),
                round(short_long_side_ratio, 4))
    
    except Exception as e:
        print("Error in ScoreImage6.py, ScoreImage6(): " + str(e))
        return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
