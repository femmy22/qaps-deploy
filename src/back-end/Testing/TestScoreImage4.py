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
from ScoreImage4 import ScoreImage4

# <><><><> TESTING OF SCORE IMAGE 4 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

x_coordinates = []
y_coordinates = []
t_coordinates = []

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_X_7.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_Y_7.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data//SPD_S09_T_7.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(t) for t in intermediate]
        t_coordinates.append(intermediate)

output = ScoreImage4(x_coordinates, y_coordinates, t_coordinates)

# Straightness, Equilaterality, Alignment, Spacing, Line Ratio, Average_Line_Length, 
#   Average_Line_Deviation, Average_Gap, Raw_Alignment, Top_Middle_Gap, Bottom_Middle_Gap
# Expected Values: (0.9878, 0.997, 0.8739, 0.9421, 0.7796, 1114.4371, 1.0123, 195.2172, 165.3417, 201.0422, 189.3923)
print(output)
