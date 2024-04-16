#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

# <><><><><><><><><><><> Square Closure <><><><><><><><><><><> 
def calculateClosure(image, x_line_one, y_line_one, x_line_two, y_line_two, x_line_three, y_line_three, x_line_four=None, y_line_four=None):
    try:
        if image == 6:
            x = [0,0,0,0,0,0]
            y = [0,0,0,0,0,0]

            # set of 6 points
            # First point of Line 1
            x[0] = x_line_one[0]
            y[0] = y_line_one[0]
            # Last point of Line 1
            x[1] = x_line_one[-1]
            y[1] = y_line_one[-1]

            # First point of Line 2
            x[2] = x_line_two[0]
            y[2] = y_line_two[0]
            # Last point of Line 2
            x[3] = x_line_two[-1]
            y[3] = y_line_two[-1]

            # First point of Line 3
            x[4] = x_line_three[0]
            y[4] = y_line_three[0]
            
            # Last point of Line 3
            x[5] = x_line_three[-1]
            y[5] = y_line_three[-1]

            # calculate distance
            dist = [[float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")]]
            p = 0
            Pair = [[float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")]]
            mindist = [[float("Nan")],
                    [float("Nan")],
                    [float("Nan")]]

            for k in range(0,6,1):
                for l in range(k+1,6,1):
                    dist[k][l] = np.sqrt( ( (x[k] - x[l] )**2) + ((y[k] - y[l])**2) )

                flag = True
                for row in Pair:
                    for element in row:
                        if element == k:
                            flag = False
                        else: 
                            continue

                if flag:
                    a, i = np.nanmin(dist[k]), dist[k].index(np.nanmin(dist[k]))
                    Pair[p] = [k, i]
                    mindist[p] = a
                    p = p + 1

            closure = max(mindist)

        elif image == 9:
            x = [0,0,0,0,0,0,0,0]
            y = [0,0,0,0,0,0,0,0]

            # Set of 8 points
            # First point of Line 1
            x[0] = x_line_one[0]
            y[0] = y_line_one[0]
            # Last point of Line 1
            x[1] = x_line_one[-1]
            y[1] = y_line_one[-1]

            # First point of Line 2
            x[2] = x_line_two[0]
            y[2] = y_line_two[0]
            # Last point of Line 2
            x[3] = x_line_two[-1]
            y[3] = y_line_two[-1]

            # First point of Line 3
            x[4] = x_line_three[0]
            y[4] = y_line_three[0]
            
            # Last point of Line 3
            x[5] = x_line_three[-1]
            y[5] = y_line_three[-1]

            # First point of Line 4
            x[6] = x_line_four[0]
            y[6] = y_line_four[0]
            # Last point of Line 4
            x[7] = x_line_four[-1]
            y[7] = y_line_four[-1]

            # calculate distance
            dist = [[float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"), float("Nan"),float("Nan"), float("Nan")]]
            p = 0
            Pair = [[float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")],
                    [float("Nan"), float("Nan")]]
            mindist = [[float("Nan")],
                    [float("Nan")],
                    [float("Nan")],
                    [float("Nan")]]

            for k in range(0,8,1):
                for l in range(k+1,8,1):
                    dist[k][l] = np.sqrt( ( (x[k] - x[l] )**2) + ((y[k] - y[l])**2) )

                flag = True
                for row in Pair:
                    for element in row:
                        if element == k:
                            flag = False
                        else: 
                            continue

                if flag:
                    a, i = np.nanmin(dist[k]), dist[k].index(np.nanmin(dist[k]))
                    Pair[p] = [k, i]
                    mindist[p] = a
                    p = p + 1

            closure = max(mindist)

        return closure

    except Exception as e:
        print("Error in Closure.py, calculateClosure(), Image " + str(image) +": " + str(e))
        return "Error"
