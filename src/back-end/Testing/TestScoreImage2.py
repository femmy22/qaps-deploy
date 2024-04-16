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
from ScoreImage2 import ScoreImage2

# <><><><> TESTING OF SCORE IMAGE 2 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

x_coordinates = []
y_coordinates = []
t_coordinates = []

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_X_4.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_Y_4.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_T_4.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(t) for t in intermediate]
        t_coordinates.append(intermediate)

output = ScoreImage2(x_coordinates, y_coordinates, t_coordinates)

# Straightness, Equilaterality, Alignment, Average_Line_Length, Average_Line_Deviation, Gap, Raw_Alignment
# Expected Values: (0.9482, 0.4274, 0.3662, 911.3407, 1.0547, 105.9783, 809.3603)
print(output)
