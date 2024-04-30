# ScoopServe Ordering Menu

from tkinter import *               # Tkinter GUI Library

def orderMenu(parentWindow, customerName, orderType):

    # Using Toplevel() to create a new window. The parent window
    # must be specified so we use the parameter passed in from
    # orderMenu, parentWindow.
    orderWindow = Toplevel(parentWindow)
    orderWindow.title("ScoopServe - Creating Order")
 
    # sets the geometry of toplevel
    orderWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(orderWindow, text ="This is a new window").pack()