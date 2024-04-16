#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

from Straightness import calculateStraightness, LineLength

# <><><><><><><><><><><> Image 5: One Vertical Line <><><><><><><><><><><> 

def ScoreImage5(X_coordinates, Y_coordinates, Time_coordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 5: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0)

        # <><><><> Calculate Error Measures <><><><>
        # Length of the Line
        line_length = LineLength(X_coordinates[0], Y_coordinates[0])
        if line_length == "Error" or line_length == 0:
            print("Error in ScoreImage5.py, ScoreImage5()")
            return (-1.0, -1.0, -1.0)

        # <><><><> Analysis of the ability to copy the shape <><><><>
        # Calculate the Straightness Score
        straightness_score = calculateStraightness(X_coordinates, Y_coordinates)
        if straightness_score == "Error":
            print("Error in ScoreImage5.py, ScoreImage5()")
            return (-1.0, -1.0, -1.0)

        # Average of the deviation from straight lines
        line_deviation = 1 / straightness_score

        return round(straightness_score, 4), round(line_length, 4), round(line_deviation, 4)
    
    except Exception as e:
        print("Error in ScoreImage5.py, ScoreImage5(): " + str(e))
        return (-1.0, -1.0, -1.0)
