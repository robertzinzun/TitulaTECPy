import os
import mysql.connector

class Conexion:
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DATABASE=os.environ.get('DATABASE')
    HOST=os.environ.get('HOST')
    def getDb(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='titulaciones'
        )
        return db