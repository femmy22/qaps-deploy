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
from ScoreImage10 import ScoreImage10
from process_data import padInputs

# <><><><> TESTING OF SCORE IMAGE 10 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

x_coordinates = []
y_coordinates = []
tcoords = []

with open(testingFolderPath + '/Unsymmetrical Lines/TDLL_X.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Unsymmetrical Lines/TDLL_Y.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split(' ')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

x_coordinates = padInputs(x_coordinates)
y_coordinate = padInputs(y_coordinates)

output = ScoreImage10(x_coordinates, y_coordinates, tcoords)

# Straightness, Alignment, Line_Ratio, Average_Line_Length, Average_Line_Deviation, Gap, Raw_Alignment
# Expected Values: (0.9919, 0.9814, 0.9703, 223.9971, 1.0081, 128.1037, 6.4)
print(output)