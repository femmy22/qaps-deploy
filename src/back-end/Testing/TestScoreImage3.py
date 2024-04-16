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
from ScoreImage3 import ScoreImage3

# <><><><> TESTING OF SCORE IMAGE 3 <><><><>

testingFolderPath = "/Users/charlescutler/Desktop/Image Testing Data"

# Test 1
x_coordinates = []
y_coordinates = []
t_coordinates = []

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_X_5.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(x) for x in intermediate]
        x_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_Y_5.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(y) for y in intermediate]
        y_coordinates.append(intermediate)

with open(testingFolderPath + '/Chu Archive Data/SPD_S09_T_5.txt') as file:
    raw_file_lines = file.readlines()
    for item in raw_file_lines:
        intermediate = item.split('\t')
        intermediate = [float(t) for t in intermediate]
        t_coordinates.append(intermediate)

output = ScoreImage3(x_coordinates, y_coordinates, t_coordinates)

# Roundness, Closure, Gap, Radius_Best_Fit, Min_Radius, Max_Radius
# Expected Values: (0.6645, 0.7113, 207.5076, 359.3531, 276.4623, 416.0684)
print(output)

# Test 2
x_coordinates = [[556, 556, 554, 553, 552, 551, 550, 548], [546, 545, 544, 538, 536, 535, 533, 532, 531, 528, 527, 526, 524, 524, 523, 521, 520, 520, 519, 517, 516, 515, 511, 509, 507, 505, 503, 501, 500, 499, 498, 
496, 496, 496, 494, 493, 492, 491, 490, 489, 488, 486, 486, 486, 485, 484, 484, 484, 484, 483, 483, 482, 481, 481, 481, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 480, 481, 482, 483, 483, 484, 486, 488, 488, 491, 492, 492, 493, 494, 496, 496, 498, 500, 501, 504, 505, 508, 508, 509, 513, 516, 517, 520, 524, 528, 532, 534, 538, 540, 543, 546, 548, 555, 561, 566, 570, 573, 577, 580, 583, 586, 589, 592, 597, 600, 603, 607, 610, 614, 616, 619, 622, 625, 629, 633, 636, 639, 642, 645, 647, 648, 650, 653, 655, 656, 658, 660, 661, 664, 665, 667, 668, 668, 671, 672, 673, 674, 676, 677, 678, 680, 680, 681, 684, 685, 686, 687, 688, 688, 689, 690, 690, 690, 690, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 691, 690, 689, 688, 688, 687, 686, 685, 684, 684, 684, 683, 682, 682, 681, 680, 678, 676, 675, 674, 673, 672, 671, 670, 669, 668, 667, 666, 664, 664, 663, 661, 660, 659, 658, 657, 656, 655, 653, 652, 650, 648, 647, 645, 644, 643, 643, 642, 641, 640, 640, 639, 637, 637, 636, 635, 634, 633, 632, 630, 
629, 628, 627, 625, 624, 622, 621, 620, 618, 617, 616, 616, 613, 612, 611, 609, 608, 608, 607, 606, 604, 604, 602, 601, 600, 600, 599, 597, 596, 596, 595, 593, 592, 590, 588, 588, 586, 585, 584, 583, 582, 580, 580, 579, 578, 577, 576, 575, 573, 572, 572, 571, 569, 569, 568, 568, 567, 566, 564, 564, 563, 562, 561, 560, 560, 559, 557, 556, 556, 555, 554, 553, 552]]

y_coordinates = [[426, 426, 426, 426, 426, 426, 426, 426], [425, 425, 425, 423, 422, 421, 421, 420, 419, 418, 417, 417, 417, 417, 416, 415, 414, 413, 413, 411, 410, 409, 406, 404, 401, 399, 397, 395, 394, 393, 392, 389, 388, 386, 385, 383, 381, 379, 377, 376, 374, 373, 372, 370, 369, 367, 365, 365, 362, 361, 361, 358, 357, 357, 353, 353, 352, 350, 349, 347, 346, 345, 344, 341, 340, 337, 332, 330, 329, 327, 325, 323, 321, 320, 317, 314, 312, 309, 306, 304, 302, 301, 300, 298, 297, 296, 294, 293, 292, 290, 288, 288, 287, 286, 285, 283, 282, 281, 281, 279, 278, 277, 276, 274, 273, 273, 273, 272, 272, 270, 270, 269, 269, 269, 269, 269, 269, 269, 269, 269, 269, 270, 270, 272, 272, 273, 273, 273, 274, 275, 276, 276, 277, 277, 279, 281, 281, 282, 284, 285, 286, 288, 290, 291, 293, 294, 296, 297, 298, 300, 301, 303, 304, 306, 308, 309, 311, 313, 315, 321, 322, 325, 327, 330, 332, 333, 335, 337, 339, 341, 342, 
345, 347, 349, 351, 353, 353, 356, 357, 359, 361, 363, 364, 365, 367, 369, 370, 373, 374, 376, 377, 379, 380, 381, 382, 384, 384, 385, 386, 387, 389, 391, 393, 393, 395, 396, 397, 397, 398, 398, 399, 401, 402, 402, 404, 405, 405, 406, 407, 408, 409, 409, 409, 410, 412, 413, 413, 414, 415, 416, 417, 417, 417, 417, 417, 417, 417, 418, 418, 418, 418, 418, 418, 418, 418, 419, 419, 419, 419, 419, 419, 419, 419, 419, 419, 419, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 421, 422, 422, 422, 423, 423, 423, 423, 423, 424, 424]]

output = ScoreImage3(x_coordinates, y_coordinates, [[],[]])

# Roundness, Closure, Gap, Radius_Best_Fit, Min_Radius, Max_Radius
# Expected Values: (0.7031, 0.9762, 4.4721, 93.9916, 75.5, 107.379)
print(output)
