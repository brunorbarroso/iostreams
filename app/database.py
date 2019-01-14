import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from app import helper as h
from app import config

class Database:

    def __init__(self):
        self.user       = config.database_user
        self.password   = config.database_password
        self.host       = config.database_host
        self.database   = config.database_name
    
    def connector(self):
        self.connection = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database, charset="utf8")
        self.cursor = self.connection.cursor(prepared=True)

    def execute(self, query, params):
        try:
            self.connector()
            self.cursor.execute(query, params)
            self.connection.commit()
            h.logger(f"Record successfully into table. ID: {self.cursor.lastrowid}")
            return self.cursor.lastrowid
        except mysql.connector.Error as error :
            self.connection.rollback() #rollback if any exception occured
            h.logger(f"Failed record into table {format(error)}")
        finally:
            #closing database connection.
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                h.logger("MySQL connection is closed")