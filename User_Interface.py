import View 
import Inner_Workings
from Inner_Workings import *
from tkinter import *
from View import *





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
        Inner_Workings.create_table(name)

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
        Inner_Workings.create_table(name)

    # Create Button    
    Button(creategui, text = "Select", command = Inpt).grid(row = 0, column = 2)
