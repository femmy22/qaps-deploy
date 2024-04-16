import copy
import ScoreImage1
import ScoreImage2
import ScoreImage3
import ScoreImage4
import ScoreImage5
import ScoreImage6
import ScoreImage7
import ScoreImage8
import ScoreImage9
import ScoreImage10

# Shapes list not requiring padding
NO_PADS = {"Circle", "Single Line", "Vertical Line", "Plus Sign", "Square", "Triangle"}

def padInputs(inputList):
    
    # Find the Length of the longest list of coordinates
    longestLength = 0
    for row in inputList:
        if len(row) > longestLength:
            longestLength = len(row)

    # For every list of coordinates that is NOT the longest list of coordinates
    # Pad the list of coordinates with NaN values
    for row in inputList:
        rowDifference = 0

        if len(row) < longestLength:
            rowDifference = longestLength - len(row)

        for item in range(rowDifference):
            row.append(float('Nan'))
    
    return inputList

# This will use Charle's Python maps to return a score
def main(data):

    # * importing here to avoid an import mapping error *
    import serviceBroker

    # Extract variables from data[]
    shape = data["shape"]
    sessionID = data['sessionID']
    xcoords = copy.deepcopy(data["x_cords"])
    ycoords = copy.deepcopy(data["y_cords"])
    tcoords = copy.deepcopy(data["time_stamps"])
    
    # Initialize python dictionary with empty lists for dims and measurements
    processed_data = {"dimensions":[],"measurements":[]}

    # If shape is not Circle || if needs padding: add value padding
    if shape not in NO_PADS:
        xcoords = padInputs(xcoords)
        ycoords = padInputs(ycoords)
        tcoords = padInputs(tcoords)
        
        # if less than 2 coordinates, void them
        if len(xcoords) < 2:
            return -1

    # # # # # # # # # # LOGIC SEPARATING THE DIFFERENT SHAPES # # # # # # # # # # #
    # For each shape, we run the appropriate script, get the cooresponding scores #
    # for each dimension and store each score (one for each dimentsion).          #
    # They will later be evaulated to calculate the final scores                  #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Circle dimension evaluation
    if shape == "Circle":

        scores = ScoreImage3.ScoreImage3(xcoords, ycoords, tcoords)
        roundness, closure, gap, radius_best_fit, min_rad, max_rad = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"roundness","score":roundness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"closure","score":closure})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"gap","score":gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"radius_best_fit","score":radius_best_fit})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"min_rad","score":min_rad})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"max_rad","score":max_rad})

    # Double line dimension evaluation
    elif shape == "Double Line":
        
        scores = ScoreImage2.ScoreImage2(xcoords, ycoords, tcoords)
        straightness, equilaterality, alignment, average_line_length, average_line_deviation, gap, raw_alignment = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"equilaterality","score":equilaterality})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"alignment","score":alignment})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_length","score":average_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"gap","score":gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"raw_alignment","score":raw_alignment})

    # Triple line dimension evaluation
    elif shape == "Triple Line":

        scores = ScoreImage4.ScoreImage4(xcoords, ycoords, tcoords)
        straightness, equilaterality, alignment, spacing, lineRatio, average_line_length, average_line_deviation, average_gap, raw_alignment, top_middle_gap, bottom_middle_gap = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6], scores[7], scores[8], scores[9], scores[10]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"equilaterality","score":equilaterality})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"alignment","score":alignment})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"spacing","score":spacing})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"lineRatio","score":lineRatio})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_length","score":average_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_gap","score":average_gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"raw_alignment","score":raw_alignment})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"top_middle_gap","score":top_middle_gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"bottom_middle_gap","score":bottom_middle_gap})

    # Square dimension evaluation
    elif shape == "Square":

        scores = ScoreImage9.ScoreImage9(xcoords, ycoords, tcoords)
        straightness, equilaterality, closure, average_line_length, average_line_deviation, average_gap = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"equilaterality","score":equilaterality})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"closure","score":closure})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_length","score":average_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_gap","score":average_gap})
        # processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"bottom_middle_gap","score":bottom_middle_gap})
        # processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"bottom_middle_gap","score":bottom_middle_gap})
        # processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"bottom_middle_gap","score":bottom_middle_gap})

    # Single line dimension evaluation
    elif shape == "Single Line":
        
        scores = ScoreImage1.ScoreImage1(xcoords, ycoords, tcoords)
        straightness, line_length, line_deviation = scores[0],scores[1],scores[2]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"line_length","score":line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"line_deviation","score":line_deviation})

    # Verticle dimension evaluation
    elif shape == "Vertical Line":

        scores = ScoreImage5.ScoreImage5(xcoords, ycoords, tcoords)
        straightness, line_length, line_deviation = scores[0],scores[1],scores[2]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"line_length","score":line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"line_deviation","score":line_deviation})

    # Mini verticle dimension evaluation
    elif shape == "Mini Vertical Lines":

        scores = ScoreImage7.ScoreImage7(xcoords, ycoords, tcoords)
        straightness, equilaterality, alignment, average_line_length, average_line_deviation, gap, raw_alignment = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"equilaterality","score":equilaterality})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"alignment","score":alignment})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_length","score":average_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"gap","score":gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"raw_alignment","score":raw_alignment})

    # Unsymmetrical dimension evaluation
    elif shape == "Unsymmetrical Lines":

        scores = ScoreImage10.ScoreImage10(xcoords, ycoords, tcoords)
        straightness, alignment, lineRatio, average_line_length, average_line_deviation, gap, raw_alignment = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"alignment","score":alignment})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"lineRatio","score":lineRatio})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_length","score":average_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"gap","score":gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"raw_alignment","score":raw_alignment})

    # Plus sign dimension evaluation
    elif shape == "Plus Sign":

        scores = ScoreImage8.ScoreImage8(xcoords, ycoords, tcoords)
        straightness, bisection, bisectionAngle, average_line_deviation, gap, angle_of_line, angle_of_line2, verticle_line_length, horizontal_line_length = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6], scores[7], scores[8]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"bisection","score":bisection})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"bisectionAngle","score":bisectionAngle})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"gap","score":gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"angle_of_line","score":angle_of_line})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"angle_of_line2","score":angle_of_line2})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"verticle_line_length","score":verticle_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"horizontal_line_length","score":horizontal_line_length})
     
     # Triangle dimension evaluation
    elif shape == "Triangle":

        scores = ScoreImage6.ScoreImage6(xcoords, ycoords, tcoords)
        straightness, equilaterality, closure, average_line_length, average_line_deviation, average_gap, short_long_side_ratio = scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6]

        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"straightness","score":straightness})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"equilaterality","score":equilaterality})
        processed_data["dimensions"].append({"sessionID":sessionID,"shape":shape,"dimension":"closure","score":closure})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_length","score":average_line_length})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_line_deviation","score":average_line_deviation})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"average_gap","score":average_gap})
        processed_data["measurements"].append({"sessionID":sessionID,"shape":shape,"dimension":"short_long_side_ratio","score":short_long_side_ratio})

    # Return -1 if process_data fails 
    if processed_data["dimensions"][0] == -1:
        return -1
    
    return processed_data
