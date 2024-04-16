#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import sys
import matplotlib.pyplot as plt

# Set path
sys.path.append('src/back-end')

# Import
from Find4Sides import identifyPossibleCorners
from Find4Sides import selectCorrectCorners
from Find4Sides import sortCorners
from Find4Sides import find4SidesOfSquare

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

def find4SidesTester(title, file_path_X, file_path_Y):
    x_coordinates = []
    y_coordinates = []

    with open(testingFolderPath + file_path_X) as file:
        raw = file.readlines()
        for item in raw:
            intermediate = item.split(' ')
            intermediate = [float(x) for x in intermediate]
            x_coordinates.append(intermediate)

    with open(testingFolderPath + file_path_Y) as file:
        raw = file.readlines()
        for item in raw:
            intermediate = item.split(' ')
            intermediate = [float(y) for y in intermediate]
            y_coordinates.append(intermediate)

    # Determine the condition of data read from the files
    print("Number of drawn lines: ",len(x_coordinates))
    for index in range(len(x_coordinates)):
        print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
    print()

    for index in range(len(x_coordinates)):
        if index%2 == 0:
            plt.plot(x_coordinates[index], y_coordinates[index], 'k.')
        else:
            plt.plot(x_coordinates[index], y_coordinates[index], 'b.')

    corners, cornerIndexes = identifyPossibleCorners(x_coordinates, y_coordinates)
    print(cornerIndexes)
    sorted_corners_indexes = sortCorners(cornerIndexes) 
    print(sorted_corners_indexes)
    
    x_coordinates, y_coordinates = find4SidesOfSquare(x_coordinates, y_coordinates, sorted_corners_indexes)

    plt.plot(x_coordinates[0], y_coordinates[0],'lime', label="Found Side 1")
    plt.plot(x_coordinates[1], y_coordinates[1],'r-', label="Found Side 2")
    plt.plot(x_coordinates[2], y_coordinates[2],'darkorange', label="Found Side 3")
    plt.plot(x_coordinates[3], y_coordinates[3],'magenta', label="Found Side 4")

    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.title(title + ": Results of \"Find4SquareSides\" recursive function")
    plt.legend()
    plt.show()

    # Determine the condition of the data after being recursively split
    print("Number of drawn lines: ",len(x_coordinates))
    for index in range(len(x_coordinates)):
        print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
    print()

find4SidesTester("One Line Square", "/Squares/OLS_X.txt", "/Squares/OLS_Y.txt")
find4SidesTester("Two Line Square", "/Squares/2LS_X.txt", "/Squares/2LS_Y.txt")
find4SidesTester("Four Line Square", "/Squares/4LS_X.txt", "/Squares/4LS_Y.txt")