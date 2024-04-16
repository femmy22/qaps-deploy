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
from ScoreImage9 import ScoreImage9
from Find4Sides import find4SidesOfSquare
from Find4Sides import identifyPossibleCorners

# <><><><> TESTING OF SCORE IMAGE 9 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

# Test 1
x_coordinates = []
y_coordinates = []
t_coordinates = []

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_X_6.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_Y_6.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_T_6.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(t) for t in intermediate]
        t_coordinates.append(intermediate)

output = ScoreImage9(x_coordinates, y_coordinates, t_coordinates)

# Expected Values: (0.8610862523503139, 0.7080561328144389, 1.0)
print("Square Chu: ",output)


# Test 2
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Squares/4LS_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Squares/4LS_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage9(x_coordinates, y_coordinates, t_coordinates)

# Square draw_file_linesn in 4 "pen" strokes
# MatLab Values: (0.9763, 0.7084, 0.9775)
# Expected Values:(0.9769689513162386, 0.7084033082154603, 0.9774654660679006)
print("4LS: ",output)


# Test 3
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Squares/OLS_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Squares/OLS_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage9(x_coordinates, y_coordinates, t_coordinates)

# Square draw_file_linesn in 1 "pen" stroke
# MatLab Values: (0,9542, 0.8316, 0.9706)
# Expected Values: (0.9798731955135402, 0.7692761640437807, 1.0)
print("OLS: ",output)

# # Test 4
# x_coordinates = []
# y_coordinates = []
# t_coordinates = []

# with open(testingFolderPath + '/Squares/X_squareHelp.txt') as file:
#     raw_file_lines = file.readlines()
#     for item in raw_file_lines:
#         intermediate = item.split(' ')
#         intermediate = [float(x) for x in intermediate]
#         x_coordinates.append(intermediate)

# with open(testingFolderPath + '/Squares/Y_squareHelp.txt') as file:
#     raw_file_lines = file.readlines()
#     for item in raw_file_lines:
#         intermediate = item.split(' ')
#         intermediate = [float(y) for y in intermediate]
#         y_coordinates.append(intermediate)

# # Determine the condition of data read from the files
# print("Number of draw_file_linesn lines: ",len(x_coordinates))
# for index in range(len(x_coordinates)):
#     print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
# print()

# plt.plot(x_coordinates[0], y_coordinates[0], 'k.')
# plt.plot(x_coordinates[1], y_coordinates[1], 'b.')

# corners, cornerIndexes = identifyPossibleCorners(x_coordinates, y_coordinates)
# print(cornerIndexes)
# x_coordinates, y_coordinates = find4SidesOfSquare(x_coordinates, y_coordinates, corners, cornerIndexes)

# plt.plot(x_coordinates[0], y_coordinates[0],'lime', label="Found Side 1")
# plt.plot(x_coordinates[1], y_coordinates[1],'r-', label="Found Side 2")
# plt.plot(x_coordinates[2], y_coordinates[2],'darkorange', label="Found Side 3")
# plt.plot(x_coordinates[3], y_coordinates[3],'magenta', label="Found Side 4")

# plt.xlabel('x coordinates')
# plt.ylabel('y coordinates')
# plt.title("Results of \"Find4SquareSides\" recursive function")
# plt.legend()
# plt.show()

# # Determine the condition of the data after being recursively split
# print("Number of draw_file_linesn lines: ",len(x_coordinates))
# for index in range(len(x_coordinates)):
#     print("Line " + str(index) + " has length: " + str(len(x_coordinates[index])))
# print()

# output = ScoreImage9(x_coordinates, y_coordinates, t_coordinates)
# print("Help: ",output)