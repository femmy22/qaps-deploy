#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np

def EndptDist(X=None, Y=None):
    try:
        # X and Y are same length 1-D vectors

        # using displacement between first and last point
        # Find the first NaN Point, Return the index of the point, MOVE LEFT ONE POSISITION
            # Do this for x and y

        nan_index_x = np.isnan(X)
        nan_index_y = np.isnan(Y)

        # If no x points were NaN, the last viable point is the last X point
        if not (True in nan_index_x):
            last_index_x = len(X) - 1
        else:
            last_index_x = np.asarray(X).argmax() - 1
            if (last_index_x == -1):
                last_index_x = 0

        # If no y points were NaN, the last viable point is the last Y point
        if not (True in nan_index_y):
            last_index_y = len(Y) - 1 
        else:
            last_index_y = np.asarray(Y).argmax() - 1
            if(last_index_y == -1):
                last_index_y = 0

        # Find the last useable point in the continuous list of points 
        last_index = min(last_index_x, last_index_y)

        # Only get the length of the points from the start to the last useable point
        L = np.sqrt((X[last_index] - X[0]) ** 2 + (Y[last_index] - Y[0]) ** 2)

        return L

    except Exception as e:
        print("Error in EndptDist.py, EndptDist(): " + str(e))
        return "Error"
        