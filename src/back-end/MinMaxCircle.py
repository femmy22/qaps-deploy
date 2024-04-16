#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np

two_pi = 2 * np.pi

def cart2pol(X, Y):
    try:
        phi = []
        rho = []

        for index in range(len(X)):
            x = X[index]
            # print("X Cart: " + str(x) +"\n")
            y = Y[index]
            # print("Y Cart: " + str(y) +"\n")
            phi.append(np.arctan2(y, x))
            rho.append(np.sqrt((x**2) + (y**2)))

        return (phi, rho)
    
    except Exception as e:
        print("Error in MinMaxCircle.py, cart2Pol(): " + str(e))
        return "Error", "Error"


def minMaxCircle(X, Y):
    try:

        # Estimate circle center
        # Find the center point in the x and y direction by finding the average value in each direction skipping NaN (undefined) values
        X0 = np.mean([np.nanmax(X), np.nanmin(X)])
        Y0 = np.mean([np.nanmax(Y), np.nanmin(Y)])

        # Convert list of x and list of y values into polar coordinates at centered around X0 and Y0
        # Gives a list if Theta values in radians and a list of Radius values

        Th, Ra = cart2pol([num-X0 for num in X], [num-Y0 for num in Y])  
        if Th == "Error":
            print("Error in MinMaxCircle.py, minMaxCircle()")
            return "Error", "Error", "Error", "Error"  

        # Creates three lists filled with zeros
        R = np.zeros((len(X),))
        Xc = np.zeros((len(X),))
        Yc = np.zeros((len(X),))

        for k in range(0,len(X)):
            # find opposite side of each point [Original Comment by Dr. Chu]
            opposite_side = Th[k] - np.pi
            
            if ( opposite_side > np.pi ):
                opposite_side = opposite_side - two_pi
            elif ( opposite_side < (-np.pi) ):
                opposite_side = opposite_side + two_pi

            opposite_k = np.argmin([np.abs(num-opposite_side) for num in Th])

            # caluclate radius and center of the circle that fits current [Original Comment by Dr. Chu]
            # point and opposite point [Original Comment by Dr. Chu]
            R[k] = (np.sqrt(((X[k] - X[opposite_k])**2) + ((Y[k] - Y[opposite_k])**2))) / 2
            Xc[k] = np.mean([X[k], X[opposite_k]])
            Yc[k] = np.mean([Y[k], Y[opposite_k]])

        # Find the minimum and maximum values of R calculated skipping Nan (Undefined) values
        min_r = np.nanmin(R)
        max_r = np.nanmax(R)

        # Find the index of the minimum and maximum values of R calculated in their respective lists
        min_r_k = np.argmin(R)
        max_r_k = np.argmax(R)

        # Create tuple of the center point for the minimum circumscribed circle
        CenterMin = (Xc[min_r_k], Yc[min_r_k])

        # Create tuple of the center point for the maximum inscribed circle
        CenterMax = (Xc[max_r_k], Yc[max_r_k])
        # Return the respective radii and center points of the minimum circumscribed circle and maximum inscribed circle
        return [min_r, max_r, CenterMin, CenterMax]

    except Exception as e:
        print("Error in MinMaxCircle.py, minMaxCircle(): " + str(e))
        return "Error", "Error", "Error", "Error"
