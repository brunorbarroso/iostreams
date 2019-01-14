import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class Database:

    def __init__(self, databaseUser, databasePassword, databaseHost, databaseName):
        self.user       = databaseUser
        self.password   = databasePassword
        self.host       = databaseHost
        self.database   = databaseName
    
    def connector(self):
        self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database, charset="utf8")
        self.cursor = self.connection.cursor(prepared=True)

    def execute(self, query, params):
        try:
            self.connector()
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Record successfully into table")
            return self.cursor.lastrowid
        except mysql.connector.Error as error :
            self.connection.rollback() #rollback if any exception occured
            print("Failed record into table {}".format(error))
        finally:
            #closing database connection.
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")