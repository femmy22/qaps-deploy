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
from ScoreImage1 import ScoreImage1

# <><><><> TESTING OF SCORE IMAGE 1 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

x_coordinates = []
y_coordinates = []
t_coordinates = []

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_X_1.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_Y_1.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_T_1.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(t) for t in intermediate]
        t_coordinates.append(intermediate)

output = ScoreImage1(x_coordinates, y_coordinates, t_coordinates)

# Straightness, Line_Length, Line_Deviation
# Expected Values: (0.9325, 1150.5564, 1.0724)
print(output)
