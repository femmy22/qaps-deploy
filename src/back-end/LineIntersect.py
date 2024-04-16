#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

def lineintersect(l1,l2):
    try:
        # Default values for x and y
        x , y = float('NaN'), float('NaN')

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
                return "Error", "Error"

        x, y = Pint[1][0], Pint[0][0]

        # Find maximum and minimum values for the final test
        l1_min_X = np.min(np.array([l1[0], l1[2]]))
        l2_min_X = np.min(np.array([l2[0], l2[2]]))
        l1_min_Y = np.min(np.array([l1[1], l1[3]]))
        l2_min_Y = np.min(np.array([l2[1], l2[3]]))

        l1_max_X = np.max(np.array([l1[0], l1[2]]))
        l2_max_X = np.max(np.array([l2[0], l2[2]]))
        l1_max_Y = np.max(np.array([l1[1], l1[3]]))
        l2_max_Y = np.max(np.array([l2[1], l2[3]]))

        # Test if the intersection is a point from the two lines because 
        # all the performed calculations where for infinite lines 
        if ((x<l1_min_X) or (x>l1_max_X) or (y<l1_min_Y) or (y>l1_max_Y) |
            (x<l2_min_X) or (x>l2_max_X) or (y<l2_min_Y) or (y>l2_max_Y) ):
            x, y = float('NaN'), float('NaN')
            print('There''s no intersection between the two line segments')
            return "Error", "Error"

        return (x, y)
    
    except Exception as e:
        print("Error in LineIntersect.py, lineintersect(): " + str(e))
        return "Error", "Error"