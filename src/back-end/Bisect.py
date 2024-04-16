#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

from LineIntersect import lineintersect

def bisect(X1, Y1, X2, Y2):
    try: 
        minimum_distance = 10000
        for i in range(len(X1)):
            for j in range(len(X2)):
                dist = np.sqrt((X1[i] - X2[j]) ** 2 + (Y1[i] - Y2[j]) ** 2)
                if dist < minimum_distance:
                    minimum_distance = dist
                    i1 = i
                    i2 = j

        # determine which is the vertical line
        X1_span = np.nanmax(X1) - np.nanmin(X1)
        X2_span = np.nanmax(X2) - np.nanmin(X2)

        # determine neighbouring points that borders the intersection
        if X1_span > X2_span: # (X1, Y1) is the horizontal line
            flag = 1 # flag gives whether line 1 or line 2 is the horizontal line   

            # horizontal line
            if (X1[i1] - X2[i2]) * (X1[i1-1] - X2[i2]) < 0:
                #I1 and I1-1 are on opposite sides of I2
                i1b = i1 - 1
            else: i1b = i1 + 1

            # vertical line
            if (Y2[i2] - Y1[i1]) * (Y2[i2-1] - Y1[i1]) < 0:
                #I2 and I2-1 are on opposite sides of I1
                i2b = i2 - 1
            else: i2b = i2 + 1
        else: # (X1, Y1) is the vertical line
            flag = 2

            # horizontal line
            if (X2[i2] - X1[i1]) * (X2[i2-1] - X1[i1]) < 0:
                #I2 and I2-1 are on opposite sides of I1
                i2b = i2 - 1
            else:
                i2b = i2 + 1

            # vertical line
            if (Y1[i1] - Y2[i2]) * (Y1[i1-1] - Y2[i2]) < 0:
                #I1 and I1-1 are on opposite sides of I2
                i1b = i1 - 1
            else:
                i1b = i1 + 1

        # two lines in the middle
        l1 = [X1[i1], Y1[i1], X1[i1b], Y1[i1b]]
        l2 = [X2[i2], Y2[i2], X2[i2b], Y2[i2b]]

        # print(i1)
        # print(i1b)
        # print(i2)
        # print(i2b)

        # determine intersection
        if X1[i1] == X1[i1b]: # if L1 is completely vertical
            x_intersect = X1[i1]
            y_intersect = (Y2[i2] - Y2[i2b]) / (X2[i2] - X2[i2b]) * (x_intersect - X2[i2]) + Y2[i2]
        elif X2[i2] == X2[i2b]: # if L2 is completely vertical
            x_intersect = X2[i2]
            y_intersect = (Y1[i1] - Y1[i1b]) / (X1[i1] - X1[i1b]) * (x_intersect - X1[i1]) + Y1[i1]
        else: # cannot use this function if one of the lines is completely vertical
            x_intersect, y_intersect = lineintersect(l1,l2)
            if x_intersect == "Error" and y_intersect == "Error":
                print("Error in Bisect.py, bisect()")
                return "Error", "Error"
        
        return x_intersect, y_intersect

    except Exception as e:
        print("Error in Bisect.py, bisect(): " + str(e))
        return "Error", "Error"
