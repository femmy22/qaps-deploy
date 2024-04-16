from db import connection
import serviceBroker

def main(parameters):
    sessionID = parameters["sessionID"]
    dims = ["straightness", "equilaterality", "alignment", "roundness", "closure", "spacing", "lineRatio", "bisection", "bisectionAngle", "score"]
    columns = ["score"]
    insertDict = {}

    # Iterate through all dimensions
    for dim in dims:
        total = 0
        count = 0
        average = 0

        print("Calculating:",dim)
        # Select query made, grabbing all the scores from some sessionID that are associated with dimension "dim"
        select_data = {"table":"test","columns":columns,"data":{"dimension": dim, "sessionID": sessionID}}
        service_json = service_json = {"service_id":3, "parameters":select_data}
        results = serviceBroker.main(service_json = service_json)

        # Iterate though the scores, find the average of them all
        for score in results:
            if score[0] is None:
                continue
            total += score[0]
            count += 1
        if count == 0:
            break
        average = total/count

        # Insert the dim and the average score into insert dict. 
        insertDict[dim] = average

    # Calculate final score by taking the sum of all scores and dividing by the number of scores
    insertDict["score"] = sum(insertDict.values())

    # Add session ID
    insertDict["sessionID"] = sessionID

    # Insert data into score table
    insert_data = {"table":"score", "data":insertDict}
    service_json = service_json = {"service_id":4, "parameters":insert_data}
    status = serviceBroker.main(service_json = service_json)


