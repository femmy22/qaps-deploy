##########################################################
#                SERVICE CODES                           #
# ------------------------------------------------------ #
#                                                        #
#       1  - raw_data_collection.py                      #      
#       2  - process_data.py                             #
#       3  - SELECT into the DB                          #
#       4  - INSERT from DB                              #
#       5  - DELETE from DB                              #
#       6  - UPDATE to DB                                #
#       7  - custom QUEREY to DB                         #
#       10 - calcuate scores                             #
#       99 - refresh DB connection                       #
#                                                        #
##########################################################

import traceback
import process_data
import raw_data_collection
from db import connection

#import calculate

# Create a connection to the database. This uses the DB.py subclass
# These are the credentials to access Amazon RDS mySQL database
# host = 'rds-prewriting-1.ck3kad0trtue.us-east-1.rds.amazonaws.com'
# database = 'rds-prewriting-1'
# user = 'admin'
# password = 'Prewriting$123'
# port = '3306'

# host = 'localhost'
# database = 'testdb'
# user = 'root'
# password = 'localdbbento'
# port = '3306'

# PHP myAdmin database credentials (testing)
# host = "cmsc508.com"
# database = "22FA_team32"
# user = "shieldsn"
# password = "V01000930"
# host = "127.0.0.1"
# database = "23fa_test"
# user = "tobq"
# password = "localdbbento"
host = "aws-test-1.c5wcy2ag81s4.us-east-2.rds.amazonaws.com"
database = "23fa_test"
user = "admin"
password = 'Capstone24'
port = "3306"



conn = connection(host = host, database = database, user = user, password = password, port = port)

# Short hands for .py main() functions
raw_data_collection = raw_data_collection.main
process_data = process_data.main

def main(service_json):
        global conn

        # Extract the service code and the parameters for the service
        service_id = service_json["service_id"]
        parameters = service_json["parameters"]

        try:

                # Raw data collection
                if service_id == 1:
                        raw_data_collection(parameters)
                        return
                
                # Process data
                elif service_id == 2:
                        processed_data = process_data(parameters)
                        return processed_data
                
                # SELECT statement DB
                elif service_id == 3:
                        return conn.select(parameters)
                
                # INSERT statement DB
                elif service_id == 4:
                        conn.insert(parameters)

                # DELETE statement DB
                elif service_id == 5:
                        conn.delete(parameters)
                
                # UPDATE statement DB
                elif service_id == 6:
                        conn.update(parameters)

                # Custom QUERY DB
                elif service_id == 7:
                        return -1

                # Calculate total score
                elif service_id == 10:
                        conn.procedure(parameters)
                # Calculate mean difference
                elif service_id == 11:
                        conn.meanproc(parameters)
                
                # Service code 99 used to refresh mySQL connection 
                elif service_id == 99:
                        conn = connection(host = host, database = database, user = user, password = password, port = port)

                else:
                        print("Whoops, i think you put in an invalid Service Code!")
        except:

                print("error in service broker")
                print("service id: ",service_id)
                print(traceback.print_exc())

        return -1
