import os
import sqlite3
import Inner_Workings
import User_Interface
from Inner_Workings import *
from User_Interface import *
from sqlite3 import Error

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
def create_database(name):
    global directory
    directory = r"C:\\Users\\rettm\Desktop\\Quizlet-Clone-main (1)\\Quizlet-Clone-main\\"+str(name)

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


    conn = Inner_Workings.create_connection(directory)

    if conn is not None:
        # creates table for terms
        try:
            c = conn.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)
        
    else:
        print("Error! cannot create the database connection.")

        
        


