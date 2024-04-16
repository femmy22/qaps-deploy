#############################################
#  VCU Engineering Capstone Team CS-23-321  #
#                                           #
#       Developed by Charles Cutler         #
#     for our Senior Capstone Project.      #
#                                           #
#              March 30, 2023               #
#############################################

import numpy as np

import matplotlib.pyplot as plt

def identifyPossibleCorners(x_coordinates, y_coordinates):
    try:
        # Find our "Bounding Box" coordinate values
        farthest_left, farthest_right, lowest, highest = float('inf'), float('-inf'), float('inf'), float('-inf')

        for line in x_coordinates:
            for coord in line:
                if coord < farthest_left: farthest_left = coord
                if coord > farthest_right: farthest_right = coord

        for line in y_coordinates:
            for coord in line:
                if coord < lowest: lowest = coord
                if coord > highest: highest = coord

        # Expand our "Bounding Box" by a small amount
        lowest -= 5
        highest += 5
        farthest_left -= 5
        farthest_right += 5

        plt.plot(farthest_left, lowest, 'r*')
        plt.plot(farthest_right, lowest, 'r*')
        plt.plot(farthest_left, highest, 'r*')
        plt.plot(farthest_right, highest, 'r*')

        closest_lowest_left_distance, index_closest_lowest_left = float('inf'), [0,0]
        closest_lowest_right_distance, index_closest_lowest_right = float('inf'), [0,0]
        closest_highest_left_distance, index_closest_highest_left = float('inf'), [0,0]
        closest_highest_right_distance, index_closest_highest_right = float('inf'), [0,0]

        for index in range(len(x_coordinates)):                 # For the number of pen strokes
            for coordinate_index in range(len(x_coordinates[index])):     # For the number of coordinates in each pen stroke
            # Find the points on our drawn line that are closest to 
            # each of the corners of our "Bounding Box"

                # Check Lowest Left
                calculatedDistToLL = np.sqrt(( (farthest_left-(x_coordinates[index][coordinate_index]))**2 ) + ( (lowest-(y_coordinates[index][coordinate_index]))**2) )
                if calculatedDistToLL < closest_lowest_left_distance:
                    closest_lowest_left_distance = calculatedDistToLL
                    index_closest_lowest_left[0] = index
                    index_closest_lowest_left[1] = coordinate_index

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
            
        lowest_left = (x_coordinates[index_closest_lowest_left[0]][index_closest_lowest_left[1]], y_coordinates[index_closest_lowest_left[0]][index_closest_lowest_left[1]])
        lowest_right = (x_coordinates[index_closest_lowest_right[0]][index_closest_lowest_right[1]], y_coordinates[index_closest_lowest_right[0]][index_closest_lowest_right[1]])
        highest_left = (x_coordinates[index_closest_highest_left[0]][index_closest_highest_left[1]], y_coordinates[index_closest_highest_left[0]][index_closest_highest_left[1]])
        highest_right = (x_coordinates[index_closest_highest_right[0]][index_closest_highest_right[1]], y_coordinates[index_closest_highest_right[0]][index_closest_highest_right[1]])

        possible_corners = [lowest_left, lowest_right, highest_left, highest_right]
        possible_corners_indexes = [index_closest_lowest_left, index_closest_lowest_right, index_closest_highest_left, index_closest_highest_right]

        plt.plot(lowest_left[0], lowest_left[1], 'g*')
        plt.plot(lowest_right[0], lowest_right[1], 'g*')
        plt.plot(highest_left[0], highest_left[1], 'g*')
        plt.plot(highest_right[0], highest_right[1], 'g*')

        return possible_corners, possible_corners_indexes

    except Exception as e:
        print("Error in Find4Sides.py, identifyPossibleCorners(): " + str(e))
        return "Error", "Error"


def selectCorrectCorners(x_coordinates, y_coordinates, possible_corners, possible_corners_indexes):
    try:
        first_point = (x_coordinates[0][0], y_coordinates[0][0])

        index_to_replace = 0
        minimum_distance_found = 999999

        # Replace the nearest Green Corner with the starting point
        for index in range(len(possible_corners)):
        # for index in range(len(possible_corners)):
            dist = np.sqrt(( (first_point[0]-(possible_corners[index][0]))**2 ) + ( (first_point[1]-(possible_corners[index][1]))**2) )
            if dist < minimum_distance_found:
                minimum_distance_found = dist
                index_to_replace = index
        possible_corners[index_to_replace] = first_point
        possible_corners_indexes[index_to_replace] = [0,0]
        LL, LR, HL, HR = possible_corners

        # A mapping of corner "Names" to their corrsponding corner set
        corner_name_to_index = {
            "LL" :[1,2,3],
            "LR" :[0,2,3],
            "HL": [0,1,3],
            "HR": [0,1,2]
        }
        # A mapping for coordinate tuples to corner "Names"
        coordinate_to_corner_name = {
            LL : "LL",
            LR : "LR",
            HL : "HL",
            HR : "HR"
        }

        # Get the index values for the corrsponding corner set that maps to the "Name" of the corner we just identifed.
        # These index values were possible corners which are now confirmed to be the found corners
        corner_buddies = corner_name_to_index[coordinate_to_corner_name[first_point]]

        # Convert the index values of the now found corners into their actual coordinate tuples
        final_corners = [ possible_corners[corner_buddies[0]], possible_corners[corner_buddies[1]], possible_corners[corner_buddies[2]] ]
        final_corner_indexes = [ possible_corners_indexes[corner_buddies[0]], possible_corners_indexes[corner_buddies[1]], possible_corners_indexes[corner_buddies[2]] ]

        return final_corners, final_corner_indexes

    except Exception as e:
        print("Error in Find4Sides.py, selectCorrectCorners(): " + str(e))
        return "Error", "Error"


def sortCorners(corners_to_sort):
    try:
        # Put the corners in order they are found when "walking" along the drawn triangle
        sorted_corner_indexes = []

        number_of_corners_to_sort = len(corners_to_sort)

        startIndex = 0
        while len(sorted_corner_indexes) < number_of_corners_to_sort:
            # Find the smallest index point on the first line
            minimum_value = float('inf')
            minimum_corner = []
            minimum_index = 0
            found = False

            # For the corners we need to search through
            for index in range(len(corners_to_sort)):
                if corners_to_sort[index][1] < minimum_value and corners_to_sort[index][0] == startIndex:
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
                startIndex += 1
            
        return sorted_corner_indexes

    except Exception as e:
        print("Error in Find4Sides.py, sortCorners(): " + str(e))
        return "Error"

# IF there are two line segemnts not one to start remove the start of both from the corners list OR turn two lines into one and then do one line version???
def find4SidesOfSquare(x_coordinates, y_coordinates, sorted_corner_indexes):
    try: 
        if (len(x_coordinates) > 4) or (len(y_coordinates) > 4):
            print("Error in Find4Sides.py, find4SidesOfSquare(): " +
                  "Square drawn in more than 4 line segments.")
            return "Error", "Error"

        if (len(x_coordinates) == 4) and (len(y_coordinates) == 4):
        # Square was drawn in 4 "pen" strokes
            return x_coordinates, y_coordinates
        
        # Square was drawn in 3 "pen" strokes
        elif (len(x_coordinates) == 3) and (len(y_coordinates) == 3):
            new_X_coordinates = []
            new_Y_coordinates = []

            # Identify the longest line and the original index of it
            longestLineX = []
            longestLineY = []
            longestLineOriginalIndex = -1
            longestFoundLength = 0
            for index in range(len(x_coordinates)):
                if len(x_coordinates[index]) > longestFoundLength:
                    longestLineOriginalIndex = index
                    longestLineX = x_coordinates[index]
                    longestLineY = y_coordinates[index]
                
            # Get the corresponding corners for that longest line
            longestLineCorners = [ci for ci in sorted_corner_indexes if ci[0] == longestLineOriginalIndex]
            
            # Sort the corresponding corners
            sortedCornersIndexes = sortCorners(longestLineCorners)

            # Walk along and split that long line
            # Add segemnts from line 0
            temp_X = []
            temp_Y = []
            cornerIndex = 0
            for index in range(len(x_coordinates[longestLineOriginalIndex])):
                if index == sortedCornersIndexes[cornerIndex][1]:
                    # Grab the corner as the end of the current line segement
                    temp_X.append(x_coordinates[longestLineOriginalIndex][index])
                    temp_Y.append(y_coordinates[longestLineOriginalIndex][index])
                    # Add this set of coordinates as a "found line segment"
                    new_X_coordinates.append(temp_X)
                    new_Y_coordinates.append(temp_Y)

                    # Reset the temp lists
                    temp_X = []
                    temp_Y = []
                    # Grab the corner as the beginning of the next line segement
                    temp_X.append(x_coordinates[longestLineOriginalIndex][index])
                    temp_Y.append(y_coordinates[longestLineOriginalIndex][index])
    
                    # If there is another corner to split at
                    if cornerIndex < (len(sorted_corners_indexes_0)-1):
                        # Move to the next corner
                        cornerIndex += 1
                else:
                    temp_X.append(x_coordinates[longestLineOriginalIndex][index])
                    temp_Y.append(y_coordinates[longestLineOriginalIndex][index])

            # Handle any "extra segments"
            # Remove extraneous segments such as:
            # Lists of one element to handle the case where the starting point and a corner are the same
            for index in range(len(new_X_coordinates)):
                if len(new_X_coordinates[index]) <= 1:
                    new_X_coordinates.pop(index)
                    new_Y_coordinates.pop(index)

            # Handle Any overflow ( in this case this will be the second segment )
            if len(temp_X) > 1 and len(temp_Y) > 1:
                overflow1_X = temp_X
                overflow1_Y = temp_Y

            # Add in the overflow as the second line segment
            new_X_coordinates.append(overflow1_X)
            new_Y_coordinates.append(overflow1_Y)

            # Put the new pieces with the other two "shorter" lines 
            if longestLineOriginalIndex == 0:
                new_X_coordinates.append(x_coordinates[1])
                new_Y_coordinates.append(y_coordinates[1])
                new_X_coordinates.append(x_coordinates[2])
                new_Y_coordinates.append(y_coordinates[2])
            elif longestLineOriginalIndex == 1:
                new_X_coordinates.append(x_coordinates[0])
                new_Y_coordinates.append(y_coordinates[0])
                new_X_coordinates.append(x_coordinates[2])
                new_Y_coordinates.append(y_coordinates[2])
            else:
                new_X_coordinates.append(x_coordinates[1])
                new_Y_coordinates.append(y_coordinates[1])
                new_X_coordinates.append(x_coordinates[0])
                new_Y_coordinates.append(y_coordinates[0])

            return new_X_coordinates, new_Y_coordinates

        # Square was drawn in 2 "pen" strokes
        elif (len(x_coordinates) == 2) and (len(y_coordinates) == 2):
            new_X_coordinates, new_Y_coordinates = [], []

            # Seperate the corner based on the line segments they appear on
            sorted_corners_indexes_0, sorted_corners_indexes_1 = [], []
            for corner in sorted_corner_indexes:
                if corner[0] == 0:
                    sorted_corners_indexes_0.append(corner)
                if corner[0] == 1:
                    sorted_corners_indexes_1.append(corner)

            overflow1_X, overflow1_Y = [], []
            overflow2_X, overflow2_Y = [], []
            if len(sorted_corners_indexes_0) > 0:
                # Add segments from line 0
                temp_X, temp_Y = [], []
                cornerIndex = 0

                for index in range(len(x_coordinates[0])):
                    if index == sorted_corners_indexes_0[cornerIndex][1]:
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
                        if cornerIndex < (len(sorted_corners_indexes_0)-1):
                            # Move to the next corner
                            cornerIndex += 1
                    else:
                        temp_X.append(x_coordinates[0][index])
                        temp_Y.append(y_coordinates[0][index])

                # If the started at the corner AND the starting point was picked as the corner 
                #   As opposed to the end, we need to add the remaining points as a side
                if (len(temp_X) > 1) and (len(temp_Y) > 1) and (sorted_corners_indexes_0[0] == [0,0]):
                    new_X_coordinates.append(temp_X)
                    new_Y_coordinates.append(temp_Y)

                # If they started in the middle of a side, we might have hangover that needs to be
                #   added in front of the current "side 4"
                elif (len(temp_X) > 1) and (len(temp_Y) > 1) and (sorted_corners_indexes_0[0] != [0,0]):
                    overflow1_X = temp_X
                    overflow1_Y = temp_Y
        
            if len(sorted_corners_indexes_1)>0:
                # Add segments from line 1
                temp_X, temp_Y = [], []
                cornerIndex = 0
                for index in range(len(x_coordinates[1])):
                    if index == sorted_corners_indexes_1[cornerIndex][1]:
                        # Grab the corner as the end of the current line segement
                        temp_X.append(x_coordinates[1][index])
                        temp_Y.append(y_coordinates[1][index])
                        # Add this set of coordinates as a "found line segment"
                        new_X_coordinates.append(temp_X)
                        new_Y_coordinates.append(temp_Y)

                        # Reset the temp lists
                        temp_X = []
                        temp_Y = []
                        # Grab the corner as the beginning of the next line segement
                        temp_X.append(x_coordinates[1][index])
                        temp_Y.append(y_coordinates[1][index])
        
                        # If there is another corner to split at
                        if cornerIndex < (len(sorted_corners_indexes_1)-1):
                            # Move to the next corner
                            cornerIndex += 1
                    else:
                        temp_X.append(x_coordinates[1][index])
                        temp_Y.append(y_coordinates[1][index])

                if len(temp_X) > 1 and len(temp_Y) > 1:
                    overflow2_X = temp_X
                    overflow2_Y = temp_Y

                # If the started at the corner AND the starting point was picked as the corner 
                #   As opposed to the end, we need to add the remaining points as a side
                if (len(temp_X) > 1) and (len(temp_Y) > 1) and (sorted_corners_indexes_1[0] == [0,0]):
                    new_X_coordinates.append(temp_X)
                    new_Y_coordinates.append(temp_Y)

                # If they started in the middle of a side, we might have hangover that needs to be
                #   added in front of the current "side 4"
                elif (len(temp_X) > 1) and (len(temp_Y) > 1) and (sorted_corners_indexes_1[0] != [0,0]):
                    overflow2_X = temp_X
                    overflow2_Y = temp_Y

            # Remove extraneous segments such as:
            # Lists of one element to handle the case where the starting point and a corner are the same
            correctSegmentsX, correctSegmentsY = [],[]
            for index in range(len(new_X_coordinates)):
                if len(new_X_coordinates[index]) > 1:
                    correctSegmentsX.append(new_X_coordinates[index])
                    correctSegmentsY.append(new_Y_coordinates[index])

            new_X_coordinates = correctSegmentsX
            new_Y_coordinates = correctSegmentsY
            
            if len(new_X_coordinates) == 4:
                # Handle the overflow
                remainingCoordsX = []
                remainingCoordsY = []
                if len(overflow1_X) > 0 and len(overflow1_Y) > 0:
                    remainingCoordsX = overflow1_X + new_X_coordinates[2]
                    remainingCoordsY = overflow1_Y +new_Y_coordinates[2]

                # Remove the old partial line segment
                new_X_coordinates.pop(2)
                new_Y_coordinates.pop(2)
                # Insert the new complete line segment
                new_X_coordinates.insert(2, remainingCoordsX)
                new_Y_coordinates.insert(2, remainingCoordsY)

                remainingCoordsX = []
                remainingCoordsY = []
                if len(overflow2_X) > 0 and len(overflow2_Y) > 0:
                    remainingCoordsX = overflow2_X + new_X_coordinates[0]
                    remainingCoordsY = overflow2_Y +new_Y_coordinates[0]

                # Remove the old partial line segment
                new_X_coordinates.pop(0)
                new_Y_coordinates.pop(0)
                # Insert the new complete line segment
                new_X_coordinates.insert(0, remainingCoordsX)
                new_Y_coordinates.insert(0, remainingCoordsY)

            elif len(overflow1_X) > 0 and len(overflow1_Y) > 0:
                new_X_coordinates.append(overflow1_X)
                new_Y_coordinates.append(overflow1_Y)

            return new_X_coordinates, new_Y_coordinates

        elif (len(x_coordinates) == 1) and (len(y_coordinates) == 1):
            # Square was drawn in 1 "pen" stroke
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
                    if corner_index < 3:
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
            
            # If the started at the corner AND the starting point was picked as the corner 
            #   As opposed to the end, we need to add the remaining points as a side
            if (len(temp_X) > 1) and (len(temp_Y) > 1) and (sorted_corner_indexes[0] == [0,0]):
                new_X_coordinates.append(temp_X)
                new_Y_coordinates.append(temp_Y)

            # If they started in the middle of a side, we might have hangover that needs to be
            #   added in front of the current "side 1"
            elif (len(temp_X) > 1) and (len(temp_Y) > 1) and (sorted_corner_indexes[0] != [0,0]):
                new_X_coordinates[0] = temp_X + new_X_coordinates[0] 
                new_Y_coordinates[0] = temp_Y + new_Y_coordinates[0]

            return new_X_coordinates, new_Y_coordinates
    
    except Exception as e:
        print("Error in FindTriangleSides.py, sortCorners(): " + str(e))
        return "Error", "Error"
