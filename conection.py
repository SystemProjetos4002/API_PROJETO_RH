import mysql.connector
from mysql.connector import errorcode

def conecta(host,user,password,database):
    try:
        db_connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
        print("Database connection made!")
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)
    else:
        db_connection.close()
    