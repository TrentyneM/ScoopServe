"""
Program: ScoopServe (main.py)
Author: Trentyne Morgan
A program that allows users to enter their name and
order type, and then be brought to a menu where they can 
select a scoop size, cone or sundae and a list of toppings
they may add to their ice cream. After their options are selected,
they may place an order to get their total for purchase. 
"""

from tkinter import *                   # Tkinter GUI Library

from tkinter import messagebox          # Using MessageBoxes for Errors
from PIL import Image, ImageTk          # Python Imaging Library
from idlelib.tooltip import Hovertip    # Used for alternate text on images.
import tkinter as tk                    # Importing tkinter as tk.
import orderScreen                      # ScoopServe Ordering Screen Module

mainWindow = tk.Tk()                         # Declaring our Main Application Window 
mainWindow.title('ScoopServe - Welcome!')    # Title of the Welcome Screen
mainWindow.geometry("443x480")               # Main Application Window Width and Height
mainWindow.resizable(False, False)           # Width and Height of the Window are not resizable.
mainWindow.iconbitmap("appIcon.ico")         # ScoopServe Window Icon 

# Tkinter Variables
customerName = tk.StringVar(value = '')         # Holds the Customer's name
customerOrderType = tk.StringVar(value = '')    # The order type of the customer

# Creating a new Canvas() widget inside of our mainWindow that needs to be
# 440 pixels wide, and 298 pixels tall. Canvas widgets are used for complex
# layouts as well as images and text. Pack and place the splashImage Canvas
# object.
splashImage = tk.Canvas(mainWindow, width = 440, height = 298)

# Alternate text for the splash screen image
splashHover = Hovertip(splashImage, 'An assortment of colorful ice cream')

# Loading our splash screen image onto the splashImage Canvas 
# Widget and convert it to a photImage object using ImageTk.PhotoImage()
windowImg = ImageTk.PhotoImage(Image.open("scoopsplash.jpg"))

# Place our canvas widget in the          main window at 0, 0 coordinates,
# use the (anchor = ) arugment to anchor the element to the top 
# left corner, and use our image file inside of windowImg.
splashImage.create_image(0, 0, anchor = NW, image = windowImg)

# Creating a new Frame to Hold our Entry Box and Label
entryFrame = tk.Frame(mainWindow)

# Our application title as a label. The text displays ScoopServe in Arial font, 16 pt
# and bold weight.
applicationTitle = tk.Label(mainWindow, text = "ScoopServe", font = ('Arial 16 bold'))

# Label for Customer Name Input
customerNameInputLabel = tk.Label(mainWindow, text = "Customer Name: ")
    
# Our customer name input entry box. It belongs to mainWindow
# the input stored from the Entry box is in customerName.
nameInput = tk.Entry(mainWindow, textvariable = customerName)

# Our Pick-Up and Dine In Buttons
dineInButton = tk.Button(mainWindow, text = "Dine-In Order")
carryOutButton = tk.Button(mainWindow, text = "Carry-Out Order")

# Function for placing an order; 
def placeOrder(orderType):

    # This variable is for checking if the customerName is empty
    nameEmpty = customerName.get()

    # If nameEmpty is equal to an empty string..
    if nameEmpty == "":

        # Use an Error Message Box to inform the user that they must enter a 
        # customer name. messageBox.showError('errorWindowTitle', 'errorWindowText')
        messagebox.showerror('ScoopServe', 'You must enter a customer name!')

    # Otherwise...
    else:

        # Set the Order Type 
        customerOrderType = orderType
        name = customerName.get()

        # Opening a new window when the dineInButton is clicked
        orderScreen.orderMenu(mainWindow, name, customerOrderType)
        
# Placing our Objects
splashImage.pack()                                            # Splash Screen for Main Window
applicationTitle.pack(pady= 10)                               # Application Title
customerNameInputLabel.pack(anchor = W)                       # Input label for Customer Name Textbox
nameInput.pack(fill = X)                                      # Input box for the user to enter their name
dineInButton.pack(side = LEFT, fill = X, expand = True)       # Dine-In Order Button
carryOutButton.pack(side = LEFT, fill = X, expand = True)     # Carry Out Order Button

# Using lambda functions to ensure that the function only runs
# when the buttons are pushed on this window.
dineInButton.configure(command=lambda: placeOrder("Dine-In"))
carryOutButton.configure(command=lambda: placeOrder("Carry Out"))

# Our mainWindow Loop
mainWindow.mainloop()
