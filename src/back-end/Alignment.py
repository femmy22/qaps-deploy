#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np

from LineLength import LineLength

# <><><><><><><><><><><> Alignment <><><><><><><><><><><> 
def calculateAlignment(image, x_line_one, y_line_one, x_line_two, y_line_two, x_line_three=None, y_line_three=None):
    try:
        line_one_length = LineLength(x_line_one, y_line_one)
        if line_one_length == "Error":
            print("Error in Alignment.py, calculateAlignment()")
            return "Error", "Error"

        line_two_length = LineLength(x_line_two, y_line_two)
        if line_two_length == "Error":
            print("Error in Alignment.py, calculateAlignment()")
            return "Error", "Error"

        if x_line_three != None and y_line_three != None:
            line_three_length = LineLength(x_line_three, y_line_three)
            if line_three_length == "Error":
                print("Error in Alignment.py, calculateAlignment()")
                return "Error", "Error"

        if image == 2:
            # Alignment: Aligning the Beginning of Each Line
            alignment = abs(np.nanmean(np.asarray(x_line_one)) - np.nanmean(np.asarray(x_line_two)))  
            longest_line_length = max(line_one_length, line_two_length)

            # if alignment is < 0 , put 0
            alignment_score = max((1 - (alignment / longest_line_length)), 0) 
        
        elif image == 4:
            # Alignment: Aligning the Beginning of Each Line, taking the largest offset between the lines 
            maximum = max(np.nanmean(np.asarray(x_line_one)), np.nanmean(np.asarray(x_line_two)), np.nanmean(np.asarray(x_line_three)))
            minimum = min(np.nanmean(np.asarray(x_line_one)), np.nanmean(np.asarray(x_line_two)), np.nanmean(np.asarray(x_line_three)))

            alignment = abs(maximum - minimum)
            longest_line_length = max(line_one_length, line_two_length, line_three_length)

            # if alignment is < 0 , put 0
            alignment_score  = max((1 - (alignment / longest_line_length )), 0)
        
        elif image == 7:
            # Alignment: Aligning the Beginning of Each Line ( these are vertical lines )
            alignment = abs(np.nanmean(np.asarray(y_line_one)) - np.nanmean(np.asarray(y_line_two)))  
            longest_line_length = max(line_one_length, line_two_length)

            # if alignment is < 0 , put 0
            alignment_score  = max((1 - (alignment / longest_line_length )), 0)
        
        elif image == 10:
            # Alignment: Aligning top of each line
            alignment = abs(np.nanmin(np.asarray(y_line_one)) - np.nanmin(np.asarray(y_line_two)))
            longest_line_length = max(line_one_length, line_two_length)

            # if alignment is < 0 , put 0
            alignment_score  = max((1 - (alignment / longest_line_length )), 0)
        
        return alignment, alignment_score

    except Exception as e:
        print("Error in Alignment.py, calculateAlignment(): " + str(e))
        return "Error", "Error"
