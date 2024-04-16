#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import sys
# Set path
sys.path.append('src/back-end')

# Import
from ScoreImage8 import ScoreImage8

# <><><><> TESTING OF SCORE IMAGE 8 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

# Test 1
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_X_15.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_Y_15.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage8(x_coordinates, y_coordinates, [[]])

# Straightness, Bisection_Ratio, Bisection_Angle, Average_Line_Deviation, Gap, 
#   Angle_Of_Line_1, Angle_Of_Line_2, Vertical_Line_Length, Horizontal_Line_Length
# Expected Values: (0.8901, 0.4695, 1.0, 1.1234, 0, -84.5868, 5.0282, 818.7942, 1110.2229)
print("\n2LPH Chu: ", output)

# Test 2: Two Line Plus
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Plus/twoLinePlusX.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Plus/twoLinePlusY.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage8(x_coordinates, y_coordinates, [[]])

# Straightness, Bisection_Ratio, Bisection_Angle, Average_Line_Deviation, Gap, 
#   Angle_Of_Line_1, Angle_Of_Line_2, Vertical_Line_Length, Horizontal_Line_Length
# Expected Values: (0.9943, 0.9047, 0.9999, 1.0058, 0, 89.1266, -0.0088, 277.4374, 233.6)
print("\n2LP: ",output)


# Test 3: Three Line Plus Horizontal
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Plus/3LPH_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Plus/3LPH_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage8(x_coordinates, y_coordinates, [[]])

# Straightness, Bisection_Ratio, Bisection_Angle, Average_Line_Deviation, Gap, 
#   Angle_Of_Line_1, Angle_Of_Line_2, Vertical_Line_Length, Horizontal_Line_Length
# Expected Values: (0.9792, 0.8169, 0.9999, 1.0212, 2.5298, -1.0602, 88.1084, 208.8569, 228.3829)
print("\n3LPH: ",output)

# Test 4: Three Line Plus Vertical
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Plus/3LPV_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Plus/3LPV_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage8(x_coordinates, y_coordinates, [[]])

# Straightness, Bisection_Ratio, Bisection_Angle, Average_Line_Deviation, Gap, 
#   Angle_Of_Line_1, Angle_Of_Line_2, Vertical_Line_Length, Horizontal_Line_Length
# Expected Values: (0.9768, 1.0, 0.9999, 1.0237, 2.5299, 89.2174, -0.1508, 205.3202, 146.4569)
print("\n3LPV: ",output)


# Test 5: Four Line Plus
x_coordinates = []
y_coordinates = []

with open(testingFolderPath + '/Plus/4LP_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Plus/4LP_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage8(x_coordinates, y_coordinates, [[]])

# Straightness, Bisection_Ratio, Bisection_Angle, Average_Line_Deviation, Gap, 
#   Angle_Of_Line_1, Angle_Of_Line_2, Vertical_Line_Length, Horizontal_Line_Length
# Expected Values: (0.985, 0.9478, 0.9984, 1.0152, 3.4818, -1.4598, -88.2492, 304.5039, 307.0667)
print("\n4LP: ",output)
