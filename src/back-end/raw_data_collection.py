
# # A procedure is currently used to calculate all scores. This file is saved for later
# def main(data):

#     # Importing here to avoid import mapping error
#     import serviceBroker

#     raw_data = data["json"]
#     raw_data["shape"] = data["shape"]
#     # insert
#     # passing db_set a json which contains the table name (rawData) and the data being inseted into the rawData table... also store the Id of this raw_data
#     service_json = {"service_id":4, "parameters":{"table":"rawData", "data":raw_data}}
#     serviceBroker.main(service_json = service_json)

#     # pass raw data to process_data and get a score
#     # if there is an error, return appropriate error code
#     ##### if(status == 200):
#     service_json = {"service_id":2, "parameters":data}
#     serviceBroker.main(service_json = service_json)

    #####     if(status == 200):
    #####         return 200
    #####     else: return status

    ##### else:
    #####     return status

    ### THIS RESPONSILBITY SHOULD BE MOVED TO PROCESS DATA
    # #store the fields of the test to be passed into the test table
    # test_data = {"sessionID": sessionID, "score":score, "shape":shape}
    # print(test_data)#debugging
    # print("test data created, now passing to db_set to go into test table...")#debugging

    # #db_set the test into the test table, and store the test id for future use
    # service_json = {"service_id":4, "parameters":{"table":"test", "data":test_data}}
    # test_data_id = serviceBroker.main(service_json = service_json)
    # return test_data_id

def main(data):
    #Process the data to get a score
    score = process_data(data)
    return score

def process_data(data):
    #Dummy implementation
    #You should replace this with your actual data processing logic
    score = len(data["json"])   #for example, the score is based on the length of the data
    return score

#Example usage:
data_sample ={
    "json": {"name": "John", "age": 25},
    "shape": "rectangle"
}
print(main(data_sample)) #Outputs the score(in this case, length of the json data)