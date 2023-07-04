import os
import sqlite3
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
def create_database():
    global directory
    directory = r"/Users/everettmiller/database.db"

    if os.path.isfile(directory) == False:
        create_connection(directory)
        if conn:
            conn.close()
# creates a table for each set in SINGLE database file
def create_table():
    '''
    create table for new set
    --> create a primary key column
    --> create a value that corresponds with each ID
------------------------------------------------------
     create a database connection to the SQLite database
     specified by db_file
    :param db_file: database file
    :return: Connection object or None
    '''
    Inpt = "relish"
    name = " "+Inpt+" "

    sql_create_table = """CREATE TABLE IF NOT EXISTS"""+name+"""(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text);"""


    conn = create_connection(directory)

    if conn is not None:
         # create projects table
        try:
            c = conn.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)
         
    else:
        print("Error! cannot create the database connection.")

