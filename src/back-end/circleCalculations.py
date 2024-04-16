from multiprocessing.managers import ValueProxy
import numpy as np
import matplotlib.pyplot as plt

two_pi = 2 * np.pi
rng = np.random.default_rng() # Construct a random number generator 


# Generate the Plot
title = 'Plotted circles'
plt.title(title, loc='center')


def makeTriangle():
    A,B,C = (0,0),(0,10),(10,0)
    valX = []
    valY = []
    
    for value in np.arange(A[0],C[0],0.04):
        valX.append(value)
        valY.append(0)
    
    for value in np.arange(A[1],B[1],0.04):
        valX.append(0)
        valY.append(value)
    
    slope = ((C[1] - B[1]) / (C[0] - B[0]))

    for value in np.arange(A[0],C[0],0.04):
        valX.append(value)
        valY.append((slope*value)+B[1])

    return valX, valY


def makeSquare():
    A,B,C,D = (0,0),(0,10),(10,0),(10,10)
    valX = []
    valY = []
    
    for value in np.arange(A[0],C[0],0.04):
        valX.append(value)
        valY.append(0)
    
    for value in np.arange(A[1],B[1],0.04):
        valX.append(0)
        valY.append(value)
    
    for value in np.arange(C[1],D[1],0.04):
        valX.append(10)
        valY.append(value)
    
    for value in np.arange(B[0],D[0],0.04):
        valX.append(value)
        valY.append(10)

    return valX, valY


def cart2pol(X, Y):
    phi = []
    rho = []

    for index in range(len(X)):
        x = X[index]
        # print("X Cart: " + str(x) +"\n")
        y = Y[index]
        # print("Y Cart: " + str(y) +"\n")
        phi.append(np.arctan2(y, x))
        rho.append(np.sqrt((x**2) + (y**2)))

    return(phi, rho)


def plotcircleRandom(x_center,y_center,user_color):
    x_trueCircle = []
    y_trueCircle = []
    radius = 10

    for ang in np.arange(0,two_pi,0.01):
        x_trueCircle.append((radius*np.cos(ang))+ x_center)
        y_trueCircle.append((radius*np.sin(ang))+ y_center)
        # radius -= 0.005
        
    # Plot the curve found through machine learning
    plt.scatter(x_trueCircle,y_trueCircle, color=user_color)

    return [x_trueCircle, y_trueCircle]


def plotcircle(x_center,y_center,radius,user_color):
    x_trueCircle = []
    y_trueCircle = []

    for ang in np.arange(0,two_pi,0.01):
        x_trueCircle.append((radius*np.cos(ang))+ x_center)
        y_trueCircle.append((radius*np.sin(ang))+ y_center)
        
    # Plot the curve found through machine learning
    plt.scatter(x_trueCircle,y_trueCircle, color=user_color)

    return [x_trueCircle, y_trueCircle]
        

def minMaxCircle(X, Y):

    # Estimate circle center
    # Find the center point in the x and y direction by finding the average value in each direction skipping NaN (undefined) values
    X0 = np.mean([np.nanmax(X), np.nanmin(X)])
    Y0 = np.mean([np.nanmax(Y), np.nanmin(Y)])

    print("\nEstimated Center Point: " + str(X0) + ", " + str(Y0))

    # Convert list of x and list of y values into polar coordinates at centered around X0 and Y0
    # Gives a list if Theta values in radians and a list of Radius values

    Th, Ra = cart2pol([num-X0 for num in X], [num-Y0 for num in Y])     


    # Creates three lists filled with zeros
    R = np.zeros((len(X),))
    Xc = np.zeros((len(X),))
    Yc = np.zeros((len(X),))


    for k in range(0,len(X)):
        # find opposite side of each point [Original Comment by Dr. Chu]
        oppside = Th[k] - np.pi
        
        if ( oppside > np.pi ):
            oppside = oppside - two_pi
        elif ( oppside < (-np.pi) ):
            oppside = oppside + two_pi

        oppk = np.argmin([np.abs(num-oppside) for num in Th])

        # caluclate radius and center of the circle that fits current [Original Comment by Dr. Chu]
        # point and opposite point [Original Comment by Dr. Chu]
        R[k] = (np.sqrt(((X[k] - X[oppk])**2) + ((Y[k] - Y[oppk])**2))) / 2
        Xc[k] = np.mean([X[k], X[oppk]])
        Yc[k] = np.mean([Y[k], Y[oppk]])


    # Find the minimum and maximum values of R calculated skipping Nan (Undefined) values
    minR = np.nanmin(R)
    maxR = np.nanmax(R)

    # Find the index of the minimum and maximum values of R calculated in their respective lists
    minRk = np.argmin(R)
    maxRk = np.argmax(R)

    # Create tuple of the center point for the minimum circumscribed circle
    CenterMin = (Xc[minRk], Yc[minRk])

    # Create tuple of the center point for the maximum inscribed circle
    CenterMax = (Xc[maxRk], Yc[maxRk])

    # Show the circles to the plot
    plotcircle(Xc[minRk], Yc[minRk], minR, 'red');
    plotcircle(Xc[maxRk], Yc[maxRk], maxR, 'blue');

    # Return the respective radii and center points of the minimum circumscribed circle and maximum inscribed circle
    return [minR, maxR, CenterMin, CenterMax]





#valX, valY = makeTriangle()
#valX, valY = makeSquare()
# x = [str(num) + "\n" for num in valX]
# print(x)
# y = [str(num) + "\n" for num in valY]
# print(y)

# with open("x.txt", "w+") as file:
#     file.writelines(x)

# with open("y.txt", "w+") as file:
#     file.writelines(y)



valX, valY = plotcircleRandom(0,0,"g")

# valX = [556, 556, 554, 553, 552, 551, 550, 548, 546, 545, 544, 538, 536, 535, 533, 532, 531, 528, 527, 526, 524, 524, 523, 521, 520, 520, 519, 517, 516, 515, 511, 509, 507, 505, 503, 501, 500, 499, 498, 
# 496, 496, 496, 494, 493, 492, 491, 490, 489, 488, 486, 486, 486, 485, 484, 484, 484, 484, 483, 483, 482, 481, 481, 481, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 481, 482, 483, 483, 484, 486, 488, 488, 491, 492, 492, 493, 494, 496, 496, 498, 500, 501, 504, 505, 508, 508, 509, 513, 516, 517, 520, 524, 528, 532, 534, 538, 540, 543, 546, 548, 555, 561, 566, 570, 573, 577, 580, 583, 586, 589, 592, 597, 600, 603, 607, 610, 614, 616, 619, 622, 625, 629, 633, 636, 639, 642, 645, 647, 648, 650, 653, 655, 656, 658, 660, 661, 664, 665, 667, 668, 668, 671, 672, 673, 674, 676, 677, 678, 680, 680, 681, 684, 685, 686, 687, 688, 688, 689, 690, 690, 690, 690, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 690, 689, 688, 688, 687, 686, 685, 684, 684, 684, 683, 682, 682, 681, 680, 678, 676, 675, 674, 673, 672, 671, 670, 669, 668, 667, 666, 664, 664, 663, 661, 660, 659, 658, 657, 656, 655, 653, 652, 650, 648, 647, 645, 644, 643, 643, 642, 641, 640, 640, 639, 637, 637, 636, 635, 634, 633, 632, 630, 
# 629, 628, 627, 625, 624, 622, 621, 620, 618, 617, 616, 616, 613, 612, 611, 609, 608, 608, 607, 606, 604, 604, 602, 601, 600, 600, 599, 597, 596, 596, 595, 593, 592, 590, 588, 588, 586, 585, 584, 583, 582, 580, 580, 579, 578, 577, 576, 575, 573, 572, 572, 571, 569, 569, 568, 568, 567, 566, 564, 564, 563, 562, 561, 560, 560, 559, 557, 556, 556, 555, 554, 553, 552]

# valY = [426, 426, 426, 426, 426, 426, 426, 426, 425, 425, 425, 423, 422, 421, 421, 420, 419, 418, 417, 417, 417, 417, 416, 415, 414, 413, 413, 411, 410, 409, 406, 404, 401, 399, 397, 395, 394, 393, 392, 389, 388, 386, 385, 383, 381, 379, 377, 376, 374, 373, 372, 370, 369, 367, 365, 365, 362, 361, 361, 358, 357, 357, 353, 353, 352, 350, 349, 347, 346, 345, 344, 341, 340, 337, 332, 330, 329, 327, 325, 323, 321, 320, 317, 314, 312, 309, 306, 304, 302, 301, 300, 298, 297, 296, 294, 293, 292, 290, 288, 288, 287, 286, 285, 283, 282, 281, 281, 279, 278, 277, 276, 274, 273, 273, 273, 272, 272, 270, 270, 269, 269, 269, 269, 269, 269, 269, 269, 269, 269, 270, 270, 272, 272, 273, 273, 273, 274, 275, 276, 276, 277, 277, 279, 281, 281, 282, 284, 285, 286, 288, 290, 291, 293, 294, 296, 297, 298, 300, 301, 303, 304, 306, 308, 309, 311, 313, 315, 321, 322, 325, 327, 330, 332, 333, 335, 337, 339, 341, 342, 
# 345, 347, 349, 351, 353, 353, 356, 357, 359, 361, 363, 364, 365, 367, 369, 370, 373, 374, 376, 377, 379, 380, 381, 382, 384, 384, 385, 386, 387, 389, 391, 393, 393, 395, 396, 397, 397, 398, 398, 399, 401, 402, 402, 404, 405, 405, 406, 407, 408, 409, 409, 409, 410, 412, 413, 413, 414, 415, 416, 417, 417, 417, 417, 417, 417, 417, 418, 418, 418, 418, 418, 418, 418, 418, 419, 419, 419, 419, 419, 419, 419, 419, 419, 419, 419, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 422, 422, 422, 423, 423, 423, 423, 423, 424, 424]

plt.scatter(valX,valY, color="g")

output = minMaxCircle(valX, valY)
print (output)
score = ( output[0] * 2 ) / ( output[1] * 2 )

print(score)
# Show the scatter plot on the screen
plt.show()

















#valX = []
#valY = []
#    with open("/Users/charlescutler/Desktop/CMSC 451/Archive/SPD_S09_X_14.txt", "r") as f:
#        line = f.readline()
#        valX = line.split('\t')
#    f.close()

#    with open("/Users/charlescutler/Desktop/CMSC 451/Archive/SPD_S09_Y_14.txt", "r") as f:
#        line = f.readline()
#        valY = line.split('\t')
#    f.close()
