from tkinter import *
import Model



def main():
    Model.create_database()
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None
    


class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x490')
        self.root.title('tkinter flashcards')
        Button(self.root, text = "Create Set").grid(row = 0, column = 1)
        Button(self.root, text = "Edit Set").grid(row = 0, column = 2)
#-----------------------------------------------------
  
    def createset(self):
        pass
    
    def editset(self):
        pass
        