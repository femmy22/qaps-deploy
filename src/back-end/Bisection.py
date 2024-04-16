#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

def calculateBisection(X_bisection, Y_bisection, X_coordinates, Y_coordinates):
    try: 
        last_index = np.max(np.nonzero(Y_coordinates))
        line_1_segment_1_length = np.sqrt( (X_bisection - X_coordinates[0])**2 + (Y_bisection - Y_coordinates[0])**2 )
        line_2_segment_2_length = np.sqrt( (X_bisection - X_coordinates[last_index])**2 + (Y_bisection - Y_coordinates[last_index])**2 )
        bisection_score = min([line_1_segment_1_length, line_2_segment_2_length]) / max([line_1_segment_1_length, line_2_segment_2_length])

        return bisection_score
    
    except Exception as e:
        print("Error in Bisection.py, calculateBisection(): " + str(e))
        return "Error"