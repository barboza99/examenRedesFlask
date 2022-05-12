import mysql.connector

args = {'host': 'localhost', 
        'user': 'root', 
        'password': 'gaspar12345', 
        'dbname': 'examen', 
        'tableName': 'usuarios'}

query1 = "SELECT * FROM usuarios;"

def connecion():
    try:
        connection = mysql.connector.connect(host = args['host'],
                                            database = args['dbname'],
                                            user = args['user'],
                                            password = args['password'])
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected: ", db_info)
            cursor = connection.cursor()
            cursor.execute(query1)
            records = cursor.fetchall()
            
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
            
            return records
    except OSError as e:
        print("Error while connecting to MySQL", e)
    # finally: 
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")