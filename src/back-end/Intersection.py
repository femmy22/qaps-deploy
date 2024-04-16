#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

def intersection(l1,l2):
    try: 
        # Default values for x and y
        x = float('NaN')
        y = float('NaN')

        ml1 = (l1[3] - l1[1]) / (l1[2] - l1[0])
        ml2 = (l2[3] - l2[1]) / (l2[2] - l2[0])
        bl1 = l1[1] - ml1 * l1[0]
        bl2 = l2[1] - ml2 * l2[0]

        a = np.array([[1, -ml1], [1, -ml2]])
        b = np.array([[bl1],[bl2]])
        Pint = np.linalg.solve(a, b)

        # When the lines are parallel there's x or y will be Inf
        for value in Pint:
            if np.isinf(value):
                print('No solution found, probably the lines are parallel')
                "Error", "Error"

        x,y = Pint[1][0], Pint[0][0]

        return (x,y)
    
    except Exception as e:
        print("Error in Intersection.py, intersection(): " + str(e))
        return "Error", "Error"