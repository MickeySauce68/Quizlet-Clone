import view 
import database
from database import *
from tkinter import *
from view import *





def create_textbox(self):
    # Creates window
    creategui = Tk()
    creategui.geometry('560x50')


    # label and text box
    Label(creategui, text = "Set Name").grid(row = 0, column = 0)
    text = Entry(creategui, width = 40)
    text.grid(row = 0, column = 1)
    

    def Inpt():
        name=text.get()
        database.create_table(name)

    # Create Button    
    Button(creategui, text = "Create", command = Inpt).grid(row = 0, column = 2)

def edit_textbox(self):
     # Creates window
    creategui = Tk()
    creategui.geometry('560x50')


    # label and text box
    Label(creategui, text = "Set Name").grid(row = 0, column = 0)
    text = Entry(creategui, width = 40)
    text.grid(row = 0, column = 1)
    

    def Inpt():
        name=text.get()
        database.create_table(name)

    # Create Button    
    Button(creategui, text = "Select", command = Inpt).grid(row = 0, column = 2)


def name_table(self):
    pass

##################################################################################################LAST START OFF