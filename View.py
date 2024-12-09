import database
import features
from tkinter import *
from database import *
from features import *
 


def main():
    database.create_database()
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None
    


class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x490')
        self.root.title('tkinter flashcards')
        Button(self.root,text = "Create Set",command = self.createset).grid(row = 0, column = 1)
        Button(self.root, text = "Edit Set",command = self.editset).grid(row = 0, column = 2)
#-----------------------------------------------------
    # When the user clicks on the createtable button a window is created 
    def createset(self):
        # Create set method will be put here
        features.create_textbox(self)
    

    def editset(self):
        features.edit_textbox(self)
    
        
