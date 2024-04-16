#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import sys
# Set path
sys.path.append('src/back-end')

# Import
from ScoreImage6 import ScoreImage6

# <><><><> TESTING OF SCORE IMAGE 6 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

# Test 1
x_coordinates, y_coordinates = [], []

with open(testingFolderPath + '/Triangles/X_chrisThreeLineTri.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Triangles/Y_chrisThreeLineTri.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)


output = ScoreImage6(x_coordinates,y_coordinates,[])

# Straightness, Equilaterality, Closure, Average_Line_Length, Average_Line_Deviation,
#   Average_Gap, Short_Long_Side_Ratio
# Expected Values (0.9872, 0.6911, 0.9809, 186.8941, 1.0129, 3.5778, 0.6911)
print(output)


# Test 2
x_coordinates, y_coordinates = [], []

with open(testingFolderPath + '/Triangles/J_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Triangles/J_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

output = ScoreImage6(x_coordinates,y_coordinates,[])

# Straightness, Equilaterality, Closure, Average_Line_Length, Average_Line_Deviation,
#   Average_Gap, Short_Long_Side_Ratio
# Expected Values (0.9803, 0.7949, 0.8978, 258.908, 1.0201, 26.4484, 0.7949)
print(output)
