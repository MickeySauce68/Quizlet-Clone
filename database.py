import os
import sqlite3
import database
import features
from database import *
from features import *
from sqlite3 import Error

name = "John"

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    global conn
    conn = None 
    try:
        conn = sqlite3.connect(db_file)

        #returns version number
        print(sqlite3.version)

    except Error as e:
        print(e)

    return conn


    

# creates a db file in specified directory once
def create_database():
    global directory
    directory = r"/Users/everettmiller/Quizlet-Clone"+str(name)

    if os.path.isfile(directory) == False:
        create_connection(directory)
        if conn:
            conn.close()





# creates a table for each set in SINGLE database file
def create_table(name):
    '''
    input from the textbox will create the new table
    '''



    sql_create_table = """CREATE TABLE IF NOT EXISTS """+str(name)+""" (id term PRIMARY KEY,name text NOT NULL);"""


    conn = database.create_connection(directory)

    if conn is not None:
        # creates table for terms
        try:
            c = conn.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)
        
    else:
        print("Error! cannot create the database connection.")

        
        


