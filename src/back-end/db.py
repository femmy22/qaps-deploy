from mysql.connector import MySQLConnection
# super buddy

class connection(MySQLConnection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Param: a dictionary with three keys: table, columns, and data. data represents the WHERE 
    #        clause (dictionary), and columns represent the projection of the SELECT statement(list)
    # Returns: result feedback
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def select(self, parameters): 

        table = parameters["table"]
        data = parameters['data']
        columns = ','.join(parameters['columns'])
        condition = ''

        # String formatting for mySQL select
        for key, value in data.items():
            if isinstance(value, str) or isinstance(value, list):
                condition += f"{key} = \"{value}\"  AND "
            else:
                condition += f"{key} = {value}  AND "
        condition += " 1=1"

        query = ("SELECT %s FROM %s WHERE %s" % (columns, table, condition))

        # Execute query using a cursor
        cursor = self.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Param: a dictionary with two keys, data and table, data represents the WHERE clause in the SELECT
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def insert(self, parameters):
        allData = parameters['data']
        table = parameters["table"]

        # If we have multiple entries that need to be inserted
        if isinstance(allData, list):

            # This will be a string of the VALUES in the format "(),(),()"
            allValues = ''

            # Gets a comma separated string of keys (the table columns)
            columns = ','.join(allData[0].keys())

            # For each entry
            for entry in allData:
                values = ''

                # Parses and formats data to the structure of the mySQL query
                for item in entry.values():
                    if isinstance(item, str) or isinstance(item, list):
                        values += f"\"{item}\","
                    else:
                        values += str(item) + ','

                # Strip the last comma off
                values = values[:-1]

                # Append all of the 'values' together, allow for multiple queries
                allValues = f"{allValues}({values}),"

            # Strip the last comma off
            allValues = allValues[:-1]
            query = "INSERT INTO %s(%s) VALUES %s" % (table,columns,allValues,)
            
            # Execute the query
            cursor = self.cursor()
            cursor.execute(query)
            self.commit()

        else:
            data = allData
            values = ''

            # gets a comma separated string of keys (the table columns)
            columns = ','.join(data.keys())

            # Parses and formats data to the structure of the mySQL query
            for item in data.values():
                if isinstance(item, str) or isinstance(item, list):
                    values += f"\"{item}\","
                else:
                    values += str(item) + ','

            # Strip the last comma off, two ways to do this
            values = values[:-1]
            # vals = vals.rstrip(vals[-1])

            # Construct the query
            query = "INSERT INTO %s(%s) VALUES (%s)" % (table,columns,values,)
            print(query)

            # Commit new raw data to the rawData table
            cursor = self.cursor()
            cursor.execute(query)
            self.commit()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Param: a single dictionary, that has 3 elements, a dict of updates, a table, and a dictionary of 
    #        column-value pairs that constructs the WHERE clause 
    # Returns: result feedback
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def update(self, parameters): 
        data = parameters['data']
        updates = parameters['updates']  
        table = parameters["table"]
        adjustment = ''
        condition = ''

        # Puts key value pairs in a query-like string for the SET clause
        for key, value in updates.items():
            print(key, value)
            if isinstance(value, str):
                adjustment += f"{key} = \"{value}\","
            else:
                adjustment += f"{key} = {value},"
            
        adjustment = adjustment[:-1]

        # Format string for mySQL select WHERE clause
        for key, value in data.items():
            if isinstance(value, str):
                condition += f"{key} = \"{value}\"  AND "
            else:
                condition += f"{key} = {value}  AND "
        condition += " 1=1"

        query = ("UPDATE %s SET %s WHERE %s" % (table, adjustment, condition))
        print(query)

        # Execute query, commit, and return success
        cursor = self.cursor()
        cursor.execute(query)
        self.commit()
        result = "Success"

        return result

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Param: a dictionary with two keys, table and data. data represents the WHERE clause in the DELETE query
    # Returns: result feedback
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def delete(self, parameters):
        table = parameters['table']
        delete = parameters['data']
        condition = ''

        # Parses and formats data to the structure of the mySQL DELETE query
        for key, value in delete.items():
            if isinstance(value, str):
                condition += f"{key} = \"{value}\"  AND "
            else:
                condition += f"{key} = {value}  AND "
        condition += " 1=1"

        query = ("DELETE FROM %s WHERE %s" % (table, condition,))

        # Execute query, commit, and return success
        cursor = self.cursor()
        cursor.execute(query)
        self.commit()
        result = "Success"
        return result

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Resets all tables of the database
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def reset(self):
        query = ("CALL reset_all_tables()")

        # Execute query, commit, and return success
        cursor = self.cursor()
        cursor.execute(query)
        self.commit()
        result = "Database reset successful"

        return result
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Used for a general query, takes in a dict {"query":desired_query}
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def query(self, parameters):
        query = parameters["query"]
        cursor = self.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Param: receives a procedure and a list of inputs
    # Returns: executes a procedure on the given input parameter list
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def procedure(self, parameters):
        procedure = parameters["procedure"]
        inputs = parameters["inputs"]
        
        cursor = self.cursor()
        cursor.callproc('calculate_scores', [inputs])
        self.commit()
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Param: receives a procedure and a list of inputs
    # Returns: executes a procedure on the given input parameter list
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def meanproc(self, parameters):
        procedure = parameters["procedure"]
        inputs = parameters["inputs"]
        cursor = self.cursor()
        cursor.callproc('calculate_difference', [inputs])
        self.commit()



        


