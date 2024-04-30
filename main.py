# ScoopServe Program Prototype

from tkinter import *               # Tkinter GUI Library
from tkinter import messagebox      # Using MessageBoxes for Errors
from PIL import Image, ImageTk      # Python Imaging Library
import orderScreen                  # ScoopServe Ordering Screen Module

# If the program is running as the main module,
# execute.
if __name__ == "__main__":

    mainWindow = Tk()                            # Declaring our Main Application Window 
    mainWindow.title('ScoopServe - Welcome!')    # Title of the Welcome Screen
    mainWindow.geometry("443x480")               # Main Application Window Width and Height
    mainWindow.resizable(False, False)           # Width and Height of the Window are not resizable.

    # Tkinter Variables
    customerName = StringVar(value = '')         # Holds the Customer's name
    customerOrderType = StringVar(value = '')    # The order type of the customer

    # Creating a new Canvas() widget inside of our mainWindow that needs to be
    # 440 pixels wide, and 298 pixels tall. Canvas widgets are used for complex
    # layouts as well as images and text. Pack and place the splashImage Canvas
    # object
    splashImage = Canvas(mainWindow, width = 440, height = 298)

    # Loading our splash screen image onto the splashImage Canvas 
    # Widget and convert it to a photImage object using ImageTk.PhotoImage()
    windowImg = ImageTk.PhotoImage(Image.open("scoopsplash.jpg"))

    # Place our canvas widget in the main window at 0, 0 coordinates,
    # use the (anchor = ) arugment to anchor the element to the top 
    # left corner, and use our image file inside of windowImg.
    splashImage.create_image(0, 0, anchor = NW, image = windowImg)

    # Creating a new Frame to Hold our Entry Box and Label
    entryFrame = Frame(mainWindow)

    # Our application title as a label. The text displays ScoopServe in Arial font, 16 pt
    # and bold weight.
    applicationTitle = Label(mainWindow, text = "ScoopServe", font = ('Arial 16 bold'))

    # Label for Customer Name Input
    customerNameInputLabel = Label(mainWindow, text = "Customer Name: ")
    
    # Our customer name input entry box. It belongs to mainWindow
    # the input stored from the Entry box is in customerName.
    nameInput = Entry(mainWindow, textvariable = customerName)

    # Our Pick-Up and Dine In Buttons
    dineInButton = Button(mainWindow, text = "Dine-In")
    carryOutButton = Button(mainWindow, text = "Carry-Out Order")

    # Function for Dine-In Button
    def dineIn():

        nameEmpty = customerName.get()

        if nameEmpty == "":

            messagebox.showerror('ScoopServe', 'You must enter a customer name!')

        else:

            # Set the Order Type 
            customerOrderType.set("Dine-In")

            # Opening a new window when the dineInButton is clicked
            orderScreen.orderMenu(mainWindow, customerName, customerOrderType)

    # Function for Order Out Button
    def orderOut():

        nameEmpty = customerName.get()

        if nameEmpty == "":

            messagebox.showerror('ScoopServe', 'You must enter a customer name!')

        else:

            # Set the Order Type 
            customerOrderType.set("Order Out")

            # Opening a new window when the dineInButton is clicked
            orderScreen.orderMenu(mainWindow, customerName, customerOrderType)
        
    # Placing our Objects
    splashImage.pack()                                            # Splash Screen for Main Window
    applicationTitle.pack(pady= 10)                               # Application Title
    customerNameInputLabel.pack(anchor = W)                       # Input label for Customer Name Textbox
    nameInput.pack(fill = X)                                      # Input box for the user to enter their name
    dineInButton.pack(side = LEFT, fill = X, expand = True)       # Dine-In Order Button
    carryOutButton.pack(side = LEFT, fill = X, expand = True)     # Carry Out Order Button

    dineInButton.configure(command = dineIn)
    carryOutButton.configure(command = orderOut)

    # Our mainWindow Loop
    mainWindow.mainloop()
    