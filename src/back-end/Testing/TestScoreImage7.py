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
from ScoreImage7 import ScoreImage7
from process_data import padInputs

# <><><><> TESTING OF SCORE IMAGE 7 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

x_coordinates = []
y_coordinates = []
t_coordinates = []

with open(testingFolderPath + '/Mini Vertical Lines/TLL_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Mini Vertical Lines/TLL_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)


x_coordinates = padInputs(x_coordinates)
y_coordinate = padInputs(y_coordinates)

output = ScoreImage7(x_coordinates, y_coordinates, t_coordinates)

# Straightness, Equilaterality, Alignment, Average_Line_Length, Average_Line_Deviation, Gap, Raw_Alignment
# Expected Values: (0.988, 0.9438, 0.8688, 143.0452, 1.0122, 288.263, 19.3159)
print(output)
