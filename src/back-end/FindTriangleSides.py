#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 29, 2023               #
#############################################

import numpy as np
# import matplotlib.pyplot as plt
from LineLength import LineLength

def identifyPossibleCorners(x_coordinates, y_coordinates):
    try: 
        farthest_left, farthest_right, lowest, highest = float('inf'), float('-inf'), float('inf'), float('-inf')

        for line in x_coordinates:
            for coord in line:
                if coord < farthest_left: farthest_left = coord
                if coord > farthest_right: farthest_right = coord

        for line in y_coordinates:
            for coord in line:
                if coord < lowest: lowest = coord
                if coord > highest: highest = coord

        # Expand out slightly the X and Y values used to create the six points of interest
        lowest -= 5
        highest += 5
        farthest_left -= 5
        farthest_right += 5
        midX = (farthest_left+farthest_right) / 2

        # plt.plot(farthest_left, lowest, 'r*')
        # plt.plot(farthest_right, lowest, 'r*')
        # plt.plot(midX, lowest, 'r*')
        # plt.plot(farthest_left, highest, 'r*')
        # plt.plot(farthest_right, highest, 'r*')
        # plt.plot(midX, highest, 'r*')

        closest_lowest_left_distance, index_closest_lowest_left = float('inf'), [0,0]
        closest_lowest_right_distance, index_closest_lowest_right = float('inf'), [0,0]
        closest_highest_left_distance, index_closest_highest_left = float('inf'), [0,0]
        closest_highest_right_distance, index_closest_highest_right = float('inf'), [0,0]
        closest_middle_top_distance, index_closest_middle_top = float('inf'), [0,0]
        closest_middle_bottom_distance, index_closest_middle_bottom = float('inf'), [0,0]

        for index in range(len(x_coordinates)):                       # For the number of pen strokes
            for coordinate_index in range(len(x_coordinates[index])):       # For the number of coordinates in each pen stroke

                # Check Lowest Left
                calculatedDistToLL = np.sqrt(( (farthest_left-(x_coordinates[index][coordinate_index]))**2 ) + ( (lowest-(y_coordinates[index][coordinate_index]))**2) )
                # If this actual drawn point is close to LL than the previous actual drawn point
                if calculatedDistToLL < closest_lowest_left_distance:
                    # Update the closest found distance to point LL
                    closest_lowest_left_distance = calculatedDistToLL
                    # Update the pen stroke to reflect this current point
                    index_closest_lowest_left[0] = index
                    # Update the coordinate of the stroke to reflect this current point
                    index_closest_lowest_left[1] = coordinate_index

                # Do the same process as above but for each of the other five points of interest
                # Check Lowest Right
                calculatedDistToLR = np.sqrt(( (farthest_right-(x_coordinates[index][coordinate_index]))**2 ) + ( (lowest-(y_coordinates[index][coordinate_index]))**2) )
                if calculatedDistToLR < closest_lowest_right_distance:
                    closest_lowest_right_distance = calculatedDistToLR
                    index_closest_lowest_right[0] = index
                    index_closest_lowest_right[1] = coordinate_index

                # Check Highest Left
                calculatedDistToHL = np.sqrt(( (farthest_left-(x_coordinates[index][coordinate_index]))**2 ) + ( (highest-(y_coordinates[index][coordinate_index]))**2) )
                if calculatedDistToHL < closest_highest_left_distance:
                    closest_highest_left_distance = calculatedDistToHL
                    index_closest_highest_left[0] = index
                    index_closest_highest_left[1] = coordinate_index

                # Check Highest Right
                calculatedDistToHR = np.sqrt(( (farthest_right-(x_coordinates[index][coordinate_index]))**2 ) + ( (highest-(y_coordinates[index][coordinate_index]))**2) )
                if calculatedDistToHR < closest_highest_right_distance:
                    closest_highest_right_distance = calculatedDistToHR
                    index_closest_highest_right[0] = index
                    index_closest_highest_right[1] = coordinate_index

                # Check Mid Top 
                #calculatedDistToMidTop = np.sqrt(( (midX-(x_coordinates[index][coordinate_index]))**2 ) + ( (0-(y_coordinates[index][coordinate_index]))**2) )
                calculatedDistToMidTop = np.sqrt(( (midX-(x_coordinates[index][coordinate_index]))**2 ) + ( ((lowest)-(y_coordinates[index][coordinate_index]))**2) )
                if calculatedDistToMidTop < closest_middle_top_distance:
                    closest_middle_top_distance = calculatedDistToMidTop
                    index_closest_middle_top[0] = index
                    index_closest_middle_top[1] = coordinate_index

                # Check Mid Bottom
                calculatedDistToMidBottom = np.sqrt(( (midX-(x_coordinates[index][coordinate_index]))**2 ) + ( ((highest)-(y_coordinates[index][coordinate_index]))**2) )
                if calculatedDistToMidBottom < closest_middle_bottom_distance:
                    closest_middle_bottom_distance = calculatedDistToMidBottom
                    index_closest_middle_bottom[0] = index
                    index_closest_middle_bottom[1] = coordinate_index
            

        # Save the six found points of interest from the various pen strokes as coordiante pairs: (X,Y)
        lowest_left = (x_coordinates[index_closest_lowest_left[0]][index_closest_lowest_left[1]], y_coordinates[index_closest_lowest_left[0]][index_closest_lowest_left[1]])
        lowest_right = (x_coordinates[index_closest_lowest_right[0]][index_closest_lowest_right[1]], y_coordinates[index_closest_lowest_right[0]][index_closest_lowest_right[1]])
        highest_left = (x_coordinates[index_closest_highest_left[0]][index_closest_highest_left[1]], y_coordinates[index_closest_highest_left[0]][index_closest_highest_left[1]])
        highest_right = (x_coordinates[index_closest_highest_right[0]][index_closest_highest_right[1]], y_coordinates[index_closest_highest_right[0]][index_closest_highest_right[1]])
        middle_top = (x_coordinates[index_closest_middle_top[0]][index_closest_middle_top[1]], y_coordinates[index_closest_middle_top[0]][index_closest_middle_top[1]])
        middle_bottom = (x_coordinates[index_closest_middle_bottom[0]][index_closest_middle_bottom[1]], y_coordinates[index_closest_middle_bottom[0]][index_closest_middle_bottom[1]])

        possible_corners = [lowest_left, lowest_right, highest_left, highest_right, middle_top, middle_bottom]
        possible_corners_indexes = [index_closest_lowest_left, index_closest_lowest_right,index_closest_highest_left, index_closest_highest_right, index_closest_middle_top, index_closest_middle_bottom]

        # plt.plot(LL[0], LL[1],'g*')
        # plt.plot(LR[0], LR[1],'g*')
        # plt.plot(HL[0], HL[1],'g*')
        # plt.plot(HR[0], HR[1],'g*')
        # plt.plot(MT[0], MT[1],'y*')
        # plt.plot(MB[0], MB[1],'y*')
        
        return possible_corners, possible_corners_indexes
    
    except Exception as e:
        print("Error in FindTriangleSides.py, identifyPossibleCorners(): " + str(e))
        return "Error", "Error"


def selectCorrectCorners(x_coordinates, y_coordinates, possible_corners, possible_corners_indexes):
    try:
        first_point = (x_coordinates[0][0], y_coordinates[0][0])

        index_to_replace = 0
        minimum_distance_found = 999999

        # Replace the nearest Green Corner with the starting point
        for index in range(len(possible_corners)-2):
        # for index in range(len(possible_corners)):
            dist = np.sqrt(( (first_point[0]-(possible_corners[index][0]))**2 ) + ( (first_point[1]-(possible_corners[index][1]))**2) )
            if dist < minimum_distance_found:
                minimum_distance_found = dist
                index_to_replace = index
        possible_corners[index_to_replace] = first_point
        possible_corners_indexes[index_to_replace] = [0,0]
        LL, LR, HL, HR, MT, MB = possible_corners

        # A mapping of corner "Names" to their corrsponding corner set
        corner_name_to_index = {
            "LL" :[1,5],
            "LR" :[0,5],
            "HL": [3,4],
            "HR": [2,4],
            "MT": [2,3],
            "MB": [0,1]
        }
        # A mapping for coordinate tuples to corner "Names"
        coordinate_to_corner_name = {
            LL : "LL",
            LR : "LR",
            HL : "HL",
            HR : "HR",
            MT : "MT",
            MB : "MB"
        }

        # Get the index values for the corrsponding corner set that maps to the "Name" of the corner we just identifed.
        # These index values were possible corners which are now confirmed to be the found corners
        corner_buddies = corner_name_to_index[coordinate_to_corner_name[first_point]]

        # Convert the index values of the now found corners into their actual coordinate tuples
        final_corners = [ possible_corners[corner_buddies[0]], possible_corners[corner_buddies[1]] ]
        final_corner_indexes = [ possible_corners_indexes[corner_buddies[0]], possible_corners_indexes[corner_buddies[1]] ]

        return final_corners, final_corner_indexes

    except Exception as e:
        print("Error in FindTriangleSides.py, selectCorrectCorners(): " + str(e))
        return "Error", "Error"


def sortCorners(corners_to_sort):
    try:
        # Put the corners in order they are found when "walking" along the drawn triangle
        sorted_corner_indexes = []

        start_index = 0
        while len(sorted_corner_indexes) < 2:
            # Find the smallest index point on the first line
            minimum_value = float('inf')
            minimum_corner = []
            minimum_index = 0
            found = False

            # For the corners we need to search through
            for index in range(len(corners_to_sort)):
                if corners_to_sort[index][1] < minimum_value and corners_to_sort[index][0] == start_index:
                    minimum_index = index
                    minimum_value = corners_to_sort[index][1]
                    minimum_corner = corners_to_sort[index]
                    found = True

            if found:
                # Insert it at the beginning of the list
                sorted_corner_indexes.append(minimum_corner)
                # Remove from the original list
                corners_to_sort.pop(minimum_index)
            else:
                start_index += 1
            
        return sorted_corner_indexes

    except Exception as e:
        print("Error in FindTriangleSides.py, sortCorners(): " + str(e))
        return "Error"


# IF there are two line segemnts not one to start remove the start of both from the corners list OR turn two lines into one and then do one line version???
def bestTriangleEdgeFinder(x_coordinates, y_coordinates, sorted_corner_indexes):
    try: 
        if (len(x_coordinates) > 3) or (len(y_coordinates) > 3):
            print("Error in FindTriangleSides.py, bestTriangleEdgeFinder(): " +
                  "Triangle drawn in more than 3 line segments.")
            return "Error", "Error"

        if (len(x_coordinates) == 3) and (len(y_coordinates) == 3):
            return x_coordinates, y_coordinates

        elif (len(x_coordinates) == 2) and (len(y_coordinates) == 2):
            # Triangle was drawn in 2 "pen" strokes
            line_0_length = LineLength(x_coordinates[0], y_coordinates[0])
            if line_0_length == "Error":
                print("Error in FindTriangleSides.py, bestTriangleEdgeFinder()")
                return "Error", "Error"

            line_1_length = LineLength(x_coordinates[1], y_coordinates[1])
            if line_1_length == "Error":
                print("Error in FindTriangleSides.py, bestTriangleEdgeFinder()")
                return "Error", "Error"

            if line_0_length > line_1_length:
                longest_line_index = 0
                short_line_index = 1
            else:
                short_line_index = 0
                longest_line_index = 1

            #plt.plot(x_coordinates[longest_line_index], y_coordinates[longest_line_index], 'k.', label="Longest Line")
            #plt.plot(x_coordinates[short_line_index], y_coordinates[short_line_index], 'b.', label="Shortest Line")

            # Get the corners associated with the longest line
            longest_line_corners = []
            for corner in sorted_corner_indexes:
                if corner[0] == longest_line_index:
                    longest_line_corners.append(corner)
            if len(longest_line_corners) == 0:
                print("Error in FindTriangleSides.py, bestTriangleEdgeFinder(): " + 
                      "2 Line Triangle had no found corners on the longest drawn line.")
                return "Error", "Error"

            new_X_coordinates, new_Y_coordinates, temp_X, temp_Y = [], [], [], []
            corner_index = 0

            for index in range(len(x_coordinates[longest_line_index])):
                if index == longest_line_corners[corner_index][1]:
                    # Grab the corner as the end of the current line segement
                    temp_X.append(x_coordinates[longest_line_index][index])
                    temp_Y.append(y_coordinates[longest_line_index][index])
                    # Add this set of coordinates as a "found line segment"
                    new_X_coordinates.append(temp_X)
                    new_Y_coordinates.append(temp_Y)

                    # Reset the temp lists
                    temp_X = []
                    temp_Y = []
                    # Grab the corner as the beginning of the next line segement
                    temp_X.append(x_coordinates[longest_line_index][index])
                    temp_Y.append(y_coordinates[longest_line_index][index])

                    # If there is another corner to split at
                    if corner_index < (len(longest_line_corners)-1):
                        # Move to the next corner
                        corner_index += 1
                else:
                    temp_X.append(x_coordinates[longest_line_index][index])
                    temp_Y.append(y_coordinates[longest_line_index][index])

            #  Remove lists of one element to handle the case where the starting point and first corner are the same
            correct_segments_X, correct_segments_Y = [], []
            for index in range(len(new_X_coordinates)):
                if len(new_X_coordinates[index]) > 1:
                    correct_segments_X.append(new_X_coordinates[index])
                    correct_segments_Y.append(new_Y_coordinates[index])

            new_X_coordinates = correct_segments_X
            new_Y_coordinates = correct_segments_Y
            
            if len(temp_X) > 1:
                new_X_coordinates.append(temp_X)
                new_Y_coordinates.append(temp_Y)

            new_X_coordinates.append(x_coordinates[short_line_index])
            new_Y_coordinates.append(y_coordinates[short_line_index])

            return new_X_coordinates, new_Y_coordinates
        
        # Otherwise we need to split the one line segment into the three sides of a triangle
        else:
            # Triangle was drawn in 1 "pen" stroke
            new_X_coordinates, new_Y_coordinates, temp_X, temp_Y = [], [], [], []
            corner_index = 0

            for index in range(len(x_coordinates[0])):
                if index == sorted_corner_indexes[corner_index][1]:
                    # Grab the corner as the end of the current line segement
                    temp_X.append(x_coordinates[0][index])
                    temp_Y.append(y_coordinates[0][index])
                    # Add this set of coordinates as a "found line segment"
                    new_X_coordinates.append(temp_X)
                    new_Y_coordinates.append(temp_Y)

                    # Reset the temp lists
                    temp_X = []
                    temp_Y = []
                    # Grab the corner as the beginning of the next line segement
                    temp_X.append(x_coordinates[0][index])
                    temp_Y.append(y_coordinates[0][index])

                    # If there is another corner to split at
                    if corner_index < 1:
                        # Move to the next corner
                        corner_index += 1
                else:
                    temp_X.append(x_coordinates[0][index])
                    temp_Y.append(y_coordinates[0][index])

            #  Remove lists of one element to handle the case where the starting point and first corner are the same
            correct_segments_X, correct_segments_Y = [], []
            for index in range(len(new_X_coordinates)):
                if len(new_X_coordinates[index]) > 1:
                    correct_segments_X.append(new_X_coordinates[index])
                    correct_segments_Y.append(new_Y_coordinates[index])

            new_X_coordinates = correct_segments_X
            new_Y_coordinates = correct_segments_Y
            
            if len(temp_X) > 1:
                new_X_coordinates.append(temp_X)
                new_Y_coordinates.append(temp_Y)

            return new_X_coordinates, new_Y_coordinates

    except Exception as e:
        print("Error in FindTriangleSides.py, bestTriangleEdgeFinder(): " + str(e))
        return "Error", "Error"