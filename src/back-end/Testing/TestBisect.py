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
from Bisect import bisect

# <><><><> TESTING OF BISECT <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

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

output = bisect(x_coordinates[0], y_coordinates[0],x_coordinates[1], y_coordinates[1])

# Expected Values: 37
#                  36
#                  22
#                  23
#                  (652.898407457841, 524.2596052465406)
print(output)

