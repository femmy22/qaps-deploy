#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

from CircFit import circfit
from EndptDist import EndptDist
from MinMaxCircle import minMaxCircle

# <><><><><><><><><><><> Image 3: Circle <><><><><><><><><><><> 

def ScoreImage3(X_coordinates, Y_coordinates, Time_coordinates):
    try:
        # <><><><> Error Handling <><><><>
        if (len(X_coordinates) < 1) or (len(Y_coordinates) < 1):
            print("\nSCORE IMAGE 3: X or Y coordinates not provided")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # <><><><> Reformat Input <><><><>
        # If they drew the circle in one line, change nothing
        if (len(X_coordinates) == 1) or (len(Y_coordinates) == 1):
            Xcoordinates = X_coordinates[0]
            Ycoordinates = Y_coordinates[0]
            TimeCoordinates = Time_coordinates[0]
        # Else, concatenate all drawn line segments into one continous line of data points
        else:
            Xcoordinates = []
            Ycoordinates = []
            TimeCoordinates = []
            for row in range(len(X_coordinates)):
                [Xcoordinates.append(x) for x in X_coordinates[row]]
                [Ycoordinates.append(y) for y in Y_coordinates[row]]
                [TimeCoordinates.append(time) for time in Time_coordinates[row]]

        # <><><><> Calculate Error Measures <><><><>     
        # Roundness: ratio between the max inscribed circle and min circumscribed circle
        # http://www.measurement.sk/M2009/proceedings/352_Vetrik.pdf
        # Minimum Circle zone: uses difference between the 2 circles
        min_rad, max_rad, center_min_V, center_max_V = minMaxCircle(Xcoordinates, Ycoordinates)
        if min_rad == "Error" and max_rad == "Error":
            print("Error in ScoreImage3.py, ScoreImage3()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Size: radius of least square circle
        # (X-Xc)^2+(Y-Yc)^2=R^2 is rewritten as 2XcX+2YcY+R^2-Xc^2-Yc^2=X^2+Y^2, then AX+BY+C=X^2+Y^2
        # http://www.mathworks.com/matlabcentral/fileexchange/5557-circle-fit
        # This circle fit was first published by P.Delogne and I.Kasa in the 1970s and is known as "Kasa method" in statistics. 
        # It works well when points cover a large part of the circle but is heavily biased when points are restricted to a small arc. 
        # Better fits were proposed by Pratt and Taubin.
        # This code minimises sum((x.^2 + y.^2 - R^2).^2)
        x_center_best_fit, y_center_best_fit,  radius_best_fit, equation_best_fit = circfit(Xcoordinates,Ycoordinates)
        if str(radius_best_fit) == "Error":
            print("Error in ScoreImage3.py, ScoreImage3()")
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)

        # Closure: distance between end points
        gap = EndptDist(Xcoordinates, Ycoordinates)
        if gap == "Error":
            print("Error in ScoreImage3.py, ScoreImage3()")   
            return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0) 

        # <><><><> Analysis of the ability to copy the shape <><><><>
        Roundness = ( min_rad * 2 ) / ( max_rad * 2 )
        Closure = max((1 - gap / ( 2 * radius_best_fit[0])), 0)

        return round(Roundness, 4), round(Closure, 4), round(gap, 4), round(radius_best_fit[0], 4), round(min_rad, 4), round(max_rad, 4)

    except Exception as e:
        print("Error in ScoreImage3.py, ScoreImage3(): " + str(e))
        return (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0) 