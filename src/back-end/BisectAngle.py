#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

def calculateBisectionAngle(X_coordinates, Y_coordinates):
    try:
        X_coordinates_transposed = np.transpose(np.array(X_coordinates))
        Y_coordinates_transposed = np.transpose(np.array(Y_coordinates))

        best_fit_line_values = np.polyfit(X_coordinates_transposed, Y_coordinates_transposed, deg=1)

        angle = np.arctan(best_fit_line_values[0]) / np.pi * 180

        return angle
    
    except Exception as e:
        print("Error in BisectAngle.py, calculateBisectionAngle(): " + str(e))
        return "Error"