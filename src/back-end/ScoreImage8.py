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
from Bisect import bisect
from Bisection import calculateBisection
from BisectAngle import calculateBisectionAngle
from Intersection import intersection

# <><><><><><><><><><><> Image 8: Plus <><><><><><><><><><><> 

def ScoreImage8(X_coordinates, Y_coordinates, Time_coordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 8: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
        if (len(X_coordinates) > 4) or (len(Y_coordinates) > 4):
            print("\nSCORE IMAGE 8: Too many lists of X or Y coordinates provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        if len(X_coordinates) == 2:    
        # Plus shape was drawn in two "pen" strokes                 
            # <><><><> Calculate Error Measures <><><><>
            # Length of the Lines
            first_line_length = LineLength(X_coordinates[0], Y_coordinates[0])
            if first_line_length == "Error" or first_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            second_line_length = LineLength(X_coordinates[1], Y_coordinates[1])
            if second_line_length == "Error" or second_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            # Determine which line is vertical and which line is horizontal
            span_X = [max(x) - min(x) for x in X_coordinates]
            span_Y = [max(y) - min(y) for y in Y_coordinates]

            vertical_line, horizontal_line = [], []
            for index in range(len(span_X)):
                if span_Y[index]>span_X[index]:
                    vertical_line.append(index)
                if span_X[index]>span_Y[index]:
                    horizontal_line.append(index)

            if vertical_line[0] == 0 and horizontal_line[0] == 1:
                vertical_line_length = first_line_length
                horizontal_line_length = second_line_length
            elif vertical_line[0] == 1 and horizontal_line[0] == 0:
                vertical_line_length = second_line_length
                horizontal_line_length = first_line_length

            # Portion of line at bisection (from start to bisection)
            X_bisection, Y_bisection = bisect(X_coordinates[0], Y_coordinates[0], X_coordinates[1], Y_coordinates[1])
            if X_bisection == "Error" and Y_bisection == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
            
            bisect_line_1 = calculateBisection(X_bisection, Y_bisection, X_coordinates[0],Y_coordinates[0])
            if bisect_line_1 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            bisect_line_2 = calculateBisection(X_bisection, Y_bisection, X_coordinates[1],Y_coordinates[1])
            if bisect_line_2 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            gap = 0

            # Angle of each drawn line based on the slope of the best fit line to those coordinates
            angle_of_line_1 = calculateBisectionAngle(X_coordinates[0], Y_coordinates[0])
            if angle_of_line_1 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            angle_of_line_2 = calculateBisectionAngle(X_coordinates[1], Y_coordinates[1]) 
            if angle_of_line_2 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        elif len(X_coordinates) == 3:
        # Plus shape was drawn in three "pen" strokes
            # <><><><> Calculate error measures <><><><>
            # Length of the Lines
            first_line_length = LineLength(X_coordinates[0], Y_coordinates[0])
            if first_line_length == "Error" or first_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            second_line_length = LineLength(X_coordinates[1], Y_coordinates[1])
            if second_line_length == "Error" or second_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            third_line_length = LineLength(X_coordinates[2], Y_coordinates[2])
            if third_line_length == "Error" or third_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            lengths = [first_line_length, second_line_length, third_line_length]

            if first_line_length > second_line_length and first_line_length > third_line_length:
                long_line = 0
                indexes_of_legs = [1, 2]
            elif second_line_length > first_line_length and second_line_length > third_line_length:
                long_line = 1
                indexes_of_legs = [0, 2]
            else:
                long_line = 2
                indexes_of_legs = [0, 1]

            leg_1 = indexes_of_legs[0]
            leg_2 = indexes_of_legs[1]

            # Determine which line is vertical and which line is horizontal
            span_X = [max(x) - min(x) for x in X_coordinates]
            span_Y = [max(y) - min(y) for y in Y_coordinates]

            vertical_lines, horizontal_lines = [], []
            for index in range(len(span_X)):
                if span_Y[index]>span_X[index]:
                    vertical_lines.append(index)
                if span_X[index]>span_Y[index]:
                    horizontal_lines.append(index)

            vertical_line_length, horizontal_line_length = 0, 0
            for index_value in vertical_lines:
                if index_value == 0: vertical_line_length += first_line_length
                if index_value == 1: vertical_line_length += second_line_length
                if index_value == 2: vertical_line_length += third_line_length
            for index_value in horizontal_lines:
                if index_value == 0: horizontal_line_length += first_line_length
                if index_value == 1: horizontal_line_length += second_line_length
                if index_value == 2: horizontal_line_length += third_line_length

            # Estimate mean by assuming the intersection is meant to be at 
            # the cross between the first points of Line 2 and Line 3
            mean_X = np.nanmean([X_coordinates[leg_1][0], X_coordinates[leg_2][0]])
            mean_Y = np.nanmean([Y_coordinates[leg_1][0], Y_coordinates[leg_2][0]])

            bisect_line_1 = abs(mean_Y - Y_coordinates[long_line][0]) / abs(mean_Y - Y_coordinates[long_line][-1])  # bisection of L1 by intersection point
            bisect_line_2 = min([lengths[leg_1], lengths[leg_2]]) / max([lengths[leg_1], lengths[leg_2]])           # ratio of L2 vs L3

            gap = np.sqrt( ((X_coordinates[leg_1][0] - X_coordinates[leg_2][0])**2) + ((Y_coordinates[leg_1][0] - Y_coordinates[leg_2][0])**2) )

            # Angle of each drawn line based on the slope of the best fit line to those coordinates
            angle_of_line_1 = calculateBisectionAngle(X_coordinates[long_line], Y_coordinates[long_line])
            if angle_of_line_1 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            X_legs, Y_legs = [], []
            for index in range(len(X_coordinates[leg_1])):
                X_legs.append(X_coordinates[leg_1][index])
                Y_legs.append(Y_coordinates[leg_1][index])

            for index in range(len(X_coordinates[leg_2])):
                X_legs.append(X_coordinates[leg_2][index])
                Y_legs.append(Y_coordinates[leg_2][index])   
            
            angle_of_line_2 = calculateBisectionAngle(X_legs, Y_legs)
            if angle_of_line_2 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)    

        else:
            # Plus shape was drawn in four or more "pen" strokes ( we ignore the strokes after 4 )
            # <><><><> Calculate error measures <><><><>
            # Length of the Lines
            first_line_length = LineLength(X_coordinates[0], Y_coordinates[0])
            if first_line_length == "Error" or first_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            second_line_length = LineLength(X_coordinates[1], Y_coordinates[1])
            if second_line_length == "Error" or second_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            third_line_length = LineLength(X_coordinates[2], Y_coordinates[2])
            if third_line_length == "Error" or third_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            fourth_line_length = LineLength(X_coordinates[3], Y_coordinates[3])
            if fourth_line_length == "Error" or fourth_line_length == 0:
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            lengths = [first_line_length, second_line_length, third_line_length, fourth_line_length]

            # Determine which lines are vertical and which lines are horizontal
            span_X = [max(x) - min(x) for x in X_coordinates]
            span_Y = [max(y) - min(y) for y in Y_coordinates]

            vertical_lines, horizontal_lines = [], []
            for index in range(len(span_X)):
                if span_Y[index]>span_X[index]:
                    vertical_lines.append(index)
                if span_X[index]>span_Y[index]:
                    horizontal_lines.append(index)
            
            vertical_line_length, horizontal_line_length = 0, 0
            for index_value in vertical_lines:
                if index_value == 0: vertical_line_length += first_line_length
                if index_value == 1: vertical_line_length += second_line_length
                if index_value == 2: vertical_line_length += third_line_length
                if index_value == 3: vertical_line_length += fourth_line_length
            for index_value in horizontal_lines:
                if index_value == 0: horizontal_line_length += first_line_length
                if index_value == 1: horizontal_line_length += second_line_length
                if index_value == 2: horizontal_line_length += third_line_length
                if index_value == 3: horizontal_line_length += fourth_line_length

            # Find the mathematical estimated intersection point 
            temp_line_1 = [X_coordinates[horizontal_lines[0]][0], Y_coordinates[horizontal_lines[0]][0], X_coordinates[horizontal_lines[1]][0], Y_coordinates[horizontal_lines[1]][0]]
            temp_line_2 = [X_coordinates[vertical_lines[0]][0], Y_coordinates[vertical_lines[0]][0], X_coordinates[vertical_lines[1]][0], Y_coordinates[vertical_lines[1]][0]]
            Xo, Yo = intersection(temp_line_1, temp_line_2)
            if Xo == "Error" and Yo == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            # Find the minimum and maximum values for the x and y directions
            X_min = np.nanmin( [np.nanmin(X_coordinates[horizontal_lines[0]]), np.nanmin(X_coordinates[horizontal_lines[1]])] )
            X_max = np.nanmax( [np.nanmax(X_coordinates[horizontal_lines[0]]), np.nanmax(X_coordinates[horizontal_lines[1]])] )
            Y_min = np.nanmin( [np.nanmin(Y_coordinates[vertical_lines[0]]), np.nanmin(Y_coordinates[vertical_lines[1]])] )
            Y_max = np.nanmax( [np.nanmax(Y_coordinates[vertical_lines[0]]), np.nanmax(Y_coordinates[vertical_lines[1]])] )

            line_1_length = abs(Yo - Y_min)
            line_2_length = abs(Y_max - Yo)
            bisect_line_1 = min([line_1_length, line_2_length]) / max([line_1_length, line_2_length])     # vertical line

            line_1_length = abs(Xo - X_min)
            line_2_length = abs(X_max - Xo)
            bisect_line_2 = min([line_1_length, line_2_length]) / max([line_1_length, line_2_length])     # horizontal 

            gap_vertical = np.sqrt( ((X_coordinates[vertical_lines[0]][0] - X_coordinates[vertical_lines[1]][0])**2) + ((Y_coordinates[vertical_lines[0]][0] - Y_coordinates[vertical_lines[1]][0])**2) )
            gap_horizontal = np.sqrt( ((X_coordinates[horizontal_lines[0]][0] - X_coordinates[horizontal_lines[1]][0])**2) + ((Y_coordinates[horizontal_lines[0]][0] - Y_coordinates[horizontal_lines[1]][0])**2) )
            gap = (gap_vertical + gap_horizontal) / 2

            # Angle for Horizontal Line
            X_horizontal = []
            Y_horizontal = []
            for index in range(len(X_coordinates[horizontal_lines[0]])):
                X_horizontal.append(X_coordinates[horizontal_lines[0]][index])
                Y_horizontal.append(Y_coordinates[horizontal_lines[0]][index])

            for index in range(len(X_coordinates[horizontal_lines[1]])):
                X_horizontal.append(X_coordinates[horizontal_lines[1]][index])
                Y_horizontal.append(Y_coordinates[horizontal_lines[1]][index])   
            
            angle_of_line_1 = calculateBisectionAngle(X_horizontal, Y_horizontal) 
            if angle_of_line_1 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

            # Angle for Vertical Line
            X_vertical = []
            Y_vertical = []
            for index in range(len(X_coordinates[vertical_lines[0]])):
                X_vertical.append(X_coordinates[vertical_lines[0]][index])
                Y_vertical.append(Y_coordinates[vertical_lines[0]][index])

            for index in range(len(X_coordinates[vertical_lines[1]])):
                X_vertical.append(X_coordinates[vertical_lines[1]][index])
                Y_vertical.append(Y_coordinates[vertical_lines[1]][index])   
            
            angle_of_line_2 = calculateBisectionAngle(X_vertical, Y_vertical) 
            if angle_of_line_2 == "Error":
                print("Error in ScoreImage8.py, ScoreImage8()")
                return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # <><><><> Analysis of the ability to copy the shape <><><><>
        # Calculate the Straightness Score
        straightness_score = calculateStraightness(X_coordinates, Y_coordinates)
        if straightness_score == "Error":
            print("Error in ScoreImage8.py, ScoreImage8()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Average of the deviation from straight lines
        average_line_deviation = 1 / straightness_score

        # Calculate the Bisection Score
        bisection_score = ((bisect_line_1 + bisect_line_2) / 2)

        # Calculate the Bisection Angle Score
        bisection_angle_score = np.sin(abs(angle_of_line_2 - angle_of_line_1) / 180 * np.pi)

        return (round(straightness_score, 4), round(bisection_score, 4), round(bisection_angle_score, 4),
                round(average_line_deviation, 4), round(gap, 4), round(angle_of_line_1, 4), round(angle_of_line_2, 4),
                round(vertical_line_length, 4), round(horizontal_line_length, 4))
    
    except Exception as e:
        print("Error in ScoreImage8.py, ScoreImage8(): " + str(e))
        return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
