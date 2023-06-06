import os
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        #returns version number
        print(sqlite3.version)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# creates a db file in specified directory once
def create_database():
    directory = r"/Users/everettmiller/sqlite.db"

    if os.path.isfile(directory) == False:
        create_connection(directory)