from tkinter import *
from functools import partial

# To-do:
# Fix labels not clearing after adding new label
# Learn to allign everything to be centered and/or pretty

def Main():

    root = Tk()
    root.geometry("400x400")
   
    class myEntry:
        
        def __init__(self, width = 30, row = 0, column = 0):
            self.entryWidth = width
            self.entryRow = row
            self.entryColumn = column

            self.entry = Entry(root, width = self.entryWidth)
            self.entry.grid(row = self.entryRow, column = self.entryColumn, padx = 50, pady = 10)

        def setLabel(self):
            self.myLabel = Label(root, text=self.entry.get())
            self.myLabel.grid(row = self.entryRow, column = self.entryColumn + 1)
        
        def setwidth(self, num = int):
            self.entry.configure(width = num)
        
        def setheight(self, num = int):
            self.entry.configure(width = num)

        def get(self):
            return self.entry.get()
        

    class myButton:

        def __init__(self, text, command, row = 0, column = 0):
            self.text = text
            self.command = command
            self.row = row
            self.column = column

            self.button = Button(root, text = self.text, command = self.command)
            self.button.grid(row = self.row, column = self.column)


    username = myEntry(30, 0, 0)
    userbutton = myButton("Enter Username", username.setLabel, 1)
    
    password = myEntry(30, 2, 0)
    passbutton = myButton("Enter Password", password.setLabel, 3)

    



    root.mainloop()




if __name__ == '__main__':
    Main()
