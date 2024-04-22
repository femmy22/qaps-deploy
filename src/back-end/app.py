from flask import Flask, request, Response
#from flask_login import LoginManager, UserMixin, jwt_required, login_user, logout_user
from flask_cors import CORS
import serviceBroker
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from datetime import timedelta, timezone, datetime


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=4)
jwt = JWTManager(app)

# Buffer used to store values collected. Sent to DB once a test completes 
buffer = {"raw":[], "test":[], "measurements":[]}

# Login route endpoint -> request object containing json object
@app.route('/login', methods=['POST'])
def login():

    # First: refresh the mySQL connection before sending to the DB
    service_json = {"service_id":99, "parameters":"nothing"}
    serviceBroker.main(service_json)

    username = request.json['username']
    password = request.json['password']
 
    # SB call to retrieve all user and password information
    #users = getUsers()
    users = {"admin":"prewriting2023"}

    # If valid credentials found: generate access token and add to JWT manager
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return {'token': access_token}, 200   
     
    else:
        return 'Bad login', 401

# --------------------------------------------------
# TO DO : Session logout    
# @app.route('/logout', methods=['POST'])
# @jwt_required
# def logout():
#     # Remove the JWT from local storage.
#     localStorage.removeItem('token');
#     return 'Logged out', 200
# --------------------------------------------------

# Get-data route endpoint: one route for all entered shapes 
# Format: {"shape":circle, "session": session..."json":{"x_cord":x,"y_cord":y...}}
@app.route('/new-data', methods=['POST', 'GET'], endpoint='new-data')
@jwt_required()
def serviceBrokerSet():

    # First: refresh the mySQL connection before sending to the DB
    service_json = {"service_id":99, "parameters":"nothing"}
    serviceBroker.main(service_json)

    sessionID = request.json['session']
    shape = request.json['shape']
    x_cords = request.json['json']['x_cords']
    y_cords = request.json['json']['y_cords']
    time_stamps = request.json['json']['time_stamps']
    canvasDimensionX = request.json['json']['canvasDimensionX']
    canvasDimensionY = request.json['json']['canvasDimensionY']
    
    # Format json for setting new data
    raw_data = {
        "shape": shape,
        "sessionID": sessionID,
        "x_cords": x_cords,
        "y_cords": y_cords,
        "time_stamps": time_stamps,
        "x_canvas_dimension": canvasDimensionX,
        "y_canvas_dimension": canvasDimensionY
    }

    # Append new raw data to the buffer
    buffer['raw'].append(raw_data)

    serviceBrokerJson = {"service_id":2,"parameters":raw_data}
    processed_data = serviceBroker.main(serviceBrokerJson)

    # If error when calculating shape (-1 is returned from process data if error occurred)
    if processed_data == -1:
        print(f"ERROR: failed to calculate scores for {shape}")
        return {"err":"err"}

    # Append new processed data to the buffer
    for data in processed_data["dimensions"]:
        buffer['test'].append(data)

    for data in processed_data["measurements"]:
        buffer['measurements'].append(data)

    return {"success":"success"}

# Calculate route endpoint (should only be hit once the last shape is evaluated)
@app.route('/calculate', methods=['POST', 'GET'], endpoint='calculate')
@jwt_required()
def calculate():

    # Insert raw data from the buffer to its corresponding rawData table in the database
    serviceBrokerJson = {
        "service_id":4,
        "parameters":{"table":"rawData", "data":buffer['raw']}
    }
    serviceBroker.main(serviceBrokerJson)

    # Insert test data from the buffer to its corresponding test table in the database
    serviceBrokerJson = {
        "service_id":4,
        "parameters":{"table":"test", "data":buffer['test']}
    }
    serviceBroker.main(serviceBrokerJson)

    # Insert measurements data from the buffer to its corresponding measurement table in the database
    serviceBrokerJson = {
        "service_id":4,
        "parameters":{"table":"measurement", "data":buffer['measurements']}
    }
    serviceBroker.main(serviceBrokerJson)

    # Clear buffer
    buffer['raw'] = []
    buffer['test'] = []
    buffer['measurements'] = []

    # Calculate.py: retrieve sessionID and calculate scores
    sessionID = request.json['session']
    serviceBrokerCalc = {
        "service_id": 10,
        "parameters": {
            "procedure": "\'calculate_scores\'",
            "inputs":sessionID
        }
    }
    serviceBroker.main(serviceBrokerCalc)

    return request.json
    
# Get-data route endpoint: accessed when retreiving any data from the DB, SELECT from DB
@app.route('/get-data', methods=['POST', 'GET'], endpoint='get-data')
@jwt_required()
def serviceBrokerGet():
    table = request.json['table']
    shape = request.json['shape']
    sessionID = request.json['session']
    #####dimension = request.json['dimension']

    # Minimum information needed to query the DB
    serviceBrokerGet = {
        "service_id": 3,
        "parameters" : {
            "table": table,
            "columns": "*",
            "data":{}
        }
    }
    
    # Extra detailed search if specified
    if shape != 'Any':
        serviceBrokerGet["parameters"]["data"]["shape"] = shape
    ##### if dimension != 'Any':
    #####     serviceBrokerGet["parameters"]["data"]["dimension"] = dimension
    if sessionID != '':
        serviceBrokerGet["parameters"]["data"]["sessionID"] = sessionID

    # Call Service Broker to grab test data from DB
    return serviceBroker.main(serviceBrokerGet)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # HELPER FUNCTIONS# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Retrieve all users/passwords and store in dict (used for authentication)
def getUsers():
    getUserSB = {"service_id":3, "parameters":{"table":"user","data":{},"columns":["*"]}}
    users = serviceBroker.main(getUserSB)
    users = {user[0]:user[1] for user in users}
    return users

# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original response
#         return response
