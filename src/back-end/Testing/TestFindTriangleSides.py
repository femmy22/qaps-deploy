#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import sys
import matplotlib.pyplot as plt

# Set path
sys.path.append('src/back-end')

# Import
from FindTriangleSides import identifyPossibleCorners
from FindTriangleSides import selectCorrectCorners
from FindTriangleSides import sortCorners
from FindTriangleSides import bestTriangleEdgeFinder

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
x_coordinates, y_coordinates = [], []

with open('/Users/charlescutler/Desktop/Image Testing Data/Triangles/newTriangleX.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open('/Users/charlescutler/Desktop/Image Testing Data/Triangles/newTriangleY.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

plt.plot(x_coordinates, y_coordinates, 'b.')
plt.plot(x_coordinates[0][0], y_coordinates[0][0],'rx', label="First \"Pen Down\"")

possible_corners, possible_corners_indexes = identifyPossibleCorners(x_coordinates,y_coordinates)
selected_corners, selected_corners_indexes = selectCorrectCorners(x_coordinates, y_coordinates, possible_corners, possible_corners_indexes)
    
plt.plot(selected_corners[0][0], selected_corners[0][1], 'g*')
plt.plot(selected_corners[1][0], selected_corners[1][1], 'g*')

sorted_corners_indexes = sortCorners(selected_corners_indexes)

# Determine the condition of data read from the files
print("Number of drawn lines: ",len(x_coordinates))
for index in range(len(x_coordinates)):
    print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
print()

x_coordinates, y_coordinates = bestTriangleEdgeFinder(x_coordinates,y_coordinates, sorted_corners_indexes)
plt.plot(x_coordinates[0], y_coordinates[0],'k-', label="Found Side 1")
plt.plot(x_coordinates[1], y_coordinates[1],'r-', label="Found Side 2")
plt.plot(x_coordinates[2], y_coordinates[2],'c-', label="Found Side 3")

# Determine the condition of the data after being recursively split
print("Number of drawn lines: ",len(x_coordinates))
for index in range(len(x_coordinates)):
    print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
print()

plt.xlabel('x coordinates')
plt.ylabel('y coordinates')
plt.title("Results of \"FindTriangleSides\" recursive function")
plt.legend()
plt.show()


def testTriangle(title, file_path_X, file_path_Y):
    x_coordinates, y_coordinates = [], []
    with open('/Users/charlescutler/Desktop/' + file_path_X) as file:
        raw_file_lines = file.readlines()
        for item in raw_file_lines:
            intermediate = item.split(' ')
            intermediate = [float(x) for x in intermediate]
            x_coordinates.append(intermediate)

    with open('/Users/charlescutler/Desktop/' + file_path_Y) as file:
        raw_file_lines = file.readlines()
        for item in raw_file_lines:
            intermediate = item.split(' ')
            intermediate = [float(y) for y in intermediate]
            y_coordinates.append(intermediate)

    # Plot the Pen Strokes
    for index in range(len(x_coordinates)):
        plt.plot(x_coordinates[index], y_coordinates[index], 'k.')
    
    # Mark the First Point
    plt.plot(x_coordinates[0][0], y_coordinates[0][0],'rx', label="First \"Pen Down\"")

    # Find the Six Possible Corners
    possible_corners, possible_corners_indexes = identifyPossibleCorners(x_coordinates=x_coordinates,y_coordinates=y_coordinates)
    
    # Select 3 corners and Plot them
    selected_corners, selected_corners_indexes = selectCorrectCorners(x_coordinates, y_coordinates, possible_corners, possible_corners_indexes) 
    print(selected_corners, selected_corners_indexes)
    plt.plot(selected_corners[0][0], selected_corners[0][1], 'g*')
    plt.plot(selected_corners[1][0], selected_corners[1][1], 'g*')

    sorted_corners_indexes = sortCorners(selected_corners_indexes)

    print(sorted_corners_indexes)

    # Determine the length of each pen stroke
    print("Number of drawn lines: ",len(x_coordinates))
    for index in range(len(x_coordinates)):
        print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
    print()

    x_coordinates, y_coordinates = bestTriangleEdgeFinder(x_coordinates,y_coordinates, sorted_corners_indexes)
    plt.plot(x_coordinates[0], y_coordinates[0],'magenta', label="Found Side 1")
    plt.plot(x_coordinates[1], y_coordinates[1],'lime', label="Found Side 2")
    try: 
        plt.plot(x_coordinates[2], y_coordinates[2],'c-', label="Found Side 3")
    except IndexError:
        pass

    # Determine the length of the now 3 line segements
    print("Number of drawn lines: ",len(x_coordinates))
    for index in range(len(x_coordinates)):
        print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
    print()

    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.title(title + ": Results of \"FindTriangleSides\" recursive function")
    plt.legend()
    plt.show()


# Older
# All three of these are correctly Identified
testTriangle("Perfect Three Line", "Image Testing Data/Triangles/x_perTri_threeLines.txt", "Image Testing Data/Triangles//y_perTri_threeLines.txt") # Correctly Identified
testTriangle("Chris One Line","Image Testing Data/Triangles/chrisOneLineTriangleX.txt", "Image Testing Data/Triangles/chrisOneLineTriangleY.txt") # Correctly Identified
testTriangle("Perfect One Line","Image Testing Data/Triangles/x_perTri_oneLine.txt","Image Testing Data/Triangles/y_perTri_oneLine.txt") # Correctly Identified

# HAVE FUN CHARLES!
testTriangle("A","Image Testing Data/Triangles/A_X.txt","Image Testing Data/Triangles/A_Y.txt") # Correctly Identified
testTriangle("B","Image Testing Data/Triangles/B_X.txt","Image Testing Data/Triangles/B_Y.txt") # Correctly Identified
testTriangle("C","Image Testing Data/Triangles/C_X.txt","Image Testing Data/Triangles/C_Y.txt") # Correctly Identified
testTriangle("D","Image Testing Data/Triangles/D_X.txt","Image Testing Data/Triangles/D_Y.txt") # Correctly Identified
testTriangle("E","Image Testing Data/Triangles/E_X.txt","Image Testing Data/Triangles/E_Y.txt") # WRONG CORNERS SELECTED
testTriangle("F","Image Testing Data/Triangles/F_X.txt","Image Testing Data/Triangles/F_Y.txt") # WRONG CORNERS SELECTED
testTriangle("G","Image Testing Data/Triangles/G_X.txt","Image Testing Data/Triangles/G_Y.txt") # Correctly Identified
testTriangle("H","Image Testing Data/Triangles/H_X.txt","Image Testing Data/Triangles/H_Y.txt") # Correctly Identified
testTriangle("I","Image Testing Data/Triangles/I_X.txt","Image Testing Data/Triangles/I_Y.txt") # Correctly Identified
testTriangle("J","Image Testing Data/Triangles/J_X.txt","Image Testing Data/Triangles/J_Y.txt") # Correctly Identified
testTriangle("K","Image Testing Data/Triangles/K_X.txt","Image Testing Data/Triangles/K_Y.txt") # Correctly Identified

# New 3/2/2023
testTriangle("3 Line Chris","Image Testing Data/Triangles/X_chrisThreeLineTri.txt","Image Testing Data/Triangles/Y_chrisThreeLineTri.txt") # Correctly Identified
testTriangle("Broke Tri",'Image Testing Data/Triangles/brTri_X.txt', 'Image Testing Data/Triangles/brTri_Y.txt') # Correctly Identified
