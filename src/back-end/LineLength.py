#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np

# LineLength is a helper function for determining the length of a line segment given 
# a set of x and y coordinates that make up that line segement. 
def LineLength(X, Y):
    try:
        # X and Y are same length python lists
        # np.diff() returns a list where each element represents the numerical
        # distance between two neighboring values in the original list
        # Example: np.diff([1,2,4,7]) would return [1,2,3]
            # This is because the distance between 1 and 2 is 1
            #                 the distance between 2 and 4 is 2
            #             and the distance between 4 and 7 is 3
        X_diff = np.diff(X)
        Y_diff = np.diff(Y)

        # Calculate the "Under the square root portion" of the linear distance formula
        x_Diff_Squared = [(x**2) for x in X_diff] 
        y_Diff_Squared = [(y**2) for y in Y_diff]

        under_the_square_root = []
        for index in range(len(x_Diff_Squared)):
            under_the_square_root.append(x_Diff_Squared[index]+y_Diff_Squared[index])

        dist = np.sqrt(under_the_square_root)

        # Return the total length of the line by
        # taking the sum of the distances between all points on that line
        # Ignoring the NaN (Undefined) values
        L = np.nansum(dist)
        return L

    except Exception as e:
        print("Error In LineLength.py, LineLength(): " + str(e))
        return "Error"