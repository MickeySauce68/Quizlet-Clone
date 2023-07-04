from tkinter import *
import Model
import Controller


def main():
    Model.create_database()
    Model.create_table()
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None
    


class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x490')
        self.root.title('tkinter flashcards')
        Button(self.root,text = "Create Set",command = self.createset()).grid(row = 0, column = 1)
        Button(self.root, text = "Edit Set").grid(row = 0, column = 2)
#-----------------------------------------------------
  
    def createset(self):
        '''
        creategui = Tk()
        .geometry('560x50')
        filecontents = self.textspace.get(0.0, END)
        '''
        Controller.createtable_press()
    def editset(self):
        pass
        