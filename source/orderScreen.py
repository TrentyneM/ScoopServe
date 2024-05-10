"""
Module: ScoopServe (orderScreen.py)
Author: Trentyne Morgan
This module controls the ordering options, total calculation
of the order, and a function to destroy the orderWindow and the
total window that pops up when placing an order.
"""

from tkinter import *                  # Tkinter GUI Library
from tkinter import messagebox         # Using MessageBoxes for Errors       
from PIL import Image, ImageTk         # Python Imaging Library
from idlelib.tooltip import Hovertip   # Used for alternate text on images.

# Function to destroy both child and parent windows.
def destroyAll(parentWindow, childWindow):
    parentWindow.destroy()
    childWindow.destroy()

# Function to calculate the total of the order. 
def calculateTotal(size, conetype, toppList):
    
    total = 0.00                # The total that will be returned
    selectedToppings = []       # The list of toppings that the user selected

    # List of topping options
    toppings = ['Nuts', 
                'Chocolate', 
                'Strawberry', 
                'Pineapple Syrup', 
                'Whipped Cream', 
                'Sprinkles', 
                'Sugar Cookies', 
                'Bananas', 
                'Cherries']
    
    # enumerate() takes an iterable list and turns an iterator that generates
    # a tuple containing both the index and value of each item in the list. i
    # is the index of the current item in the iteration, while val is the value
    # of the current item in the iteration
    for i, val in enumerate(toppList):

        if val.get():

            # Add an element to total that corresponds to the current index i
            total += [0.50, 0.90, 0.90, 1.00, 0.50, 0.30, 1.00, 0.50, 0.50][i]
            
            # Add the topping text to the selected toppings list
            selectedToppings.append(toppings[i])

    # Check and add total for scoopSize
    if size == "One Scoop":
        total += 1.50
    elif size == "Two Scoop":
        total += 2.50
    elif size == "Three Scoop":
        total += 3.50

    # Check and add total for coneType
    if conetype == "Sugar Cone":
        total += 1.00
    elif conetype == "Sundae Bowl":
        total += 1.50

    # Return the total and the list of selected toppings
    return total, selectedToppings

def orderThankYou(parentWindow, name, size, conetype, checkInput):

    if size != "" and conetype != "":

        totalAmount, toppText = calculateTotal(size, conetype, checkInput)  # Get total and toppings selected from calculatetotal.
        thankYouWindow = Toplevel(parentWindow)                             # Creating a new window, with the parent passed in from the function.
        thankYouWindow.title("Thank you for your order!")                   # Our window title for our thank you window
        thankYouWindow.iconbitmap("appIcon.ico")                            # Setting Our Window Icon

        # Label that thanks the user for their order, concatenating the customer name that was passed in as a
        # parameter to orderThankYou()
        thankYouLabel = Label(thankYouWindow, text = "Thank you for your order, " + name + "!", font = "Arial 16 bold")
        orderLabel = Label(thankYouWindow, text = "Your order: ", font = "Arial 9 bold")
        orderScoops = Label(thankYouWindow, text = "* " + size)
        orderConeType = Label(thankYouWindow, text = "* " + conetype)
        toppingsLabel = Label(thankYouWindow, text = "Toppings:", font = "Arial 9 bold")
        userToppings = Label(thankYouWindow, text = f"Selected Toppings: {', '.join(toppText)}")

        totalAmount = Label(thankYouWindow, text = f"Order Total: ${totalAmount:.2f}", font = "Arial 16 bold")

        # Button to close our window.
        thankYouButton = Button(thankYouWindow, text = "Close Window")

        # Placing our objects for the thank you window
        thankYouWidgets = [thankYouLabel, orderLabel, orderScoops, orderConeType, toppingsLabel,
            userToppings, totalAmount, thankYouButton]
        for thankYouWidget in thankYouWidgets:
            thankYouWidget.pack()

        # Command to destroy both windows when order finished
        thankYouButton.configure(command=lambda: destroyAll(parentWindow, thankYouWindow))
    
    else:

        messagebox.showerror('ScoopServe', 'You must select a Scoop Size and Cone Type!')

def orderMenu(parentWindow, customerName, orderType):

    scoopSizeVar = StringVar(value = '')                 # Scoop Size Variable
    coneTypeVar = StringVar(value = '')                  # Cone Type Variable
    customerNameVar = StringVar(value = customerName)    # Customer Name Variable (passed from orderMenu())
    orderTypeVar = StringVar(value = orderType)          # Order Type Variable
    toppingSelection = [BooleanVar() for _ in range(9)]  # Topping Selection List (we use 9 tkinter boolean vars to store the choices.
    orderWindow = Toplevel(parentWindow)                 # Using Toplevel() to create a new window. toplevel(orignalParentWindow)
    orderWindow.title("ScoopServe - Creating Order")     # Setting our window title
    orderWindow.geometry("640x300")                      # Sets the geometry of our orderWindow to 640x300
    orderWindow.iconbitmap("appIcon.ico")                # We can use iconbitmap(icoFile) to change the icon of our window. 
    orderWindow.resizable(False, False)                  # Window width and height is not resizable
 
    # Frame for Scoop Sizes, it belongs to the second window "orderWindow"
    # with a border width of 1, and relief is our styling of the border.
    # in this case, we want a ridge.
    scoopSizes = Frame(orderWindow, borderwidth = 1, relief='ridge')
    scoopSizeLabel = Label(scoopSizes, text ='Scoop Size', font = "Arial")
    scoopSizeImage = ImageTk.PhotoImage(Image.open("coneSmall.png"))
    scoopPhotoLabel = Label(scoopSizes, image = scoopSizeImage)
    scoopPhotoHover = Hovertip(scoopPhotoLabel, 'An ice cream cone.')
    scoopPhotoLabel.image = scoopSizeImage

    # Our radio buttons to pick between one, two or three scoops.
    oneScoopSizeRadioButton = Radiobutton(scoopSizes, text = 'One Scoop - $1.50', value = "One Scoop", variable = scoopSizeVar)
    twoScoopSizeRadioButton = Radiobutton(scoopSizes, text = 'Two Scoop - $2.50', value = "Two Scoop", variable = scoopSizeVar)
    threeScoopSizeRadioButton = Radiobutton(scoopSizes, text = 'Three Scoop - $3.50', value = "Three Scoop", variable = scoopSizeVar)

    # Frame for our Cone Types, and we have a label, and 2 radiobuttons
    # for a sundae type cone and a regular sugar cone.
    coneType = Frame(orderWindow, borderwidth = 1, relief = 'ridge') 
    coneTypeLabel = Label(coneType, text ='Cone Type', font = "Arial")
    coneTypeSundae = Radiobutton(coneType, text = "Sugar Cone - $1.00", value = "Sugar Cone", variable = coneTypeVar) 
    coneTypeCone = Radiobutton(coneType, text = "Sundae Bowl - $1.50", value = "Sundae Bowl", variable = coneTypeVar)
    coneTypeImage = ImageTk.PhotoImage(Image.open("sundaeBowl.png"))
    conePhotoLabel = Label(coneType, image = coneTypeImage)
    conePhotoHover = Hovertip(conePhotoLabel, 'An ice cream sundae.')
    conePhotoLabel.image = coneTypeImage

    # Frame for Our Toppings Menu, and Check Buttons for each of the toppings
    toppingsMenu = Frame(orderWindow, borderwidth = 1, relief = 'ridge')
    toppingsLabel = Label(toppingsMenu, text = 'Toppings', font = 'Arial')
    toppingSelection = [BooleanVar() for _ in range(9)]
    toppNuts = Checkbutton(toppingsMenu, text = 'Nuts - $0.50', variable = toppingSelection[0])
    toppChoc = Checkbutton(toppingsMenu, text = 'Chocolate - $0.90', variable = toppingSelection[1])
    toppStraw = Checkbutton(toppingsMenu, text = 'Strawberry - $0.90', variable = toppingSelection[2])
    toppPSyrup = Checkbutton(toppingsMenu, text = 'Pineapple Syrup - $1.00', variable = toppingSelection[3])
    toppWCream = Checkbutton(toppingsMenu, text = 'Whipped Cream - $0.50', variable = toppingSelection[4])
    toppSprink = Checkbutton(toppingsMenu, text = 'Sprinkles - $0.30', variable = toppingSelection[5])
    toppSCookie = Checkbutton(toppingsMenu, text = 'Sugar Cookies - $1.00', variable = toppingSelection[6])
    toppBananas = Checkbutton(toppingsMenu, text = 'Bananas - $0.50', variable = toppingSelection[7])
    toppCherries = Checkbutton(toppingsMenu, text = 'Cherries - $0.50', variable = toppingSelection[8])

    # Frame for our Order Summary
    orderSummary = Frame(orderWindow, borderwidth = 1, relief = 'ridge')
    customerLabelTitle = Label(orderSummary, text = "Customer Name:")
    customerNameLabel = Label(orderSummary, text = customerNameVar.get())
    orderTypeTitle = Label(orderSummary, text = "Order Type:")
    orderTypeLabel = Label(orderSummary, text = orderTypeVar.get())
    placeOrderButton = Button(orderSummary, text = "Place Order")

    # Configure row and column weights to make the layout evenly spaced
    orderWindow.grid_columnconfigure(0, weight=1)
    orderWindow.grid_columnconfigure(1, weight=1)
    orderWindow.grid_columnconfigure(2, weight=1)
    orderWindow.grid_rowconfigure(0, weight=1)

    # Drawing the grid, frame, and our three radio buttons for one, two
    # or three scoop sizes. For the scoopSizes grid; we give it 20 pixels
    # of padding on the left and right, and 20 pixels of padding on the top
    # and bottom. We also draw the rest of our Frames on the window this way.
    gridLayout = [scoopSizes, coneType, toppingsMenu, orderSummary]
    for index, item in enumerate(gridLayout):
        gridLayout[index].grid(row = 0, column = index, sticky = "nsew", padx = 10, pady = 10)

    # Widgets for Scoop Size Frame 
    scoopSizeLabel.grid(row=0, column=0)
    oneScoopSizeRadioButton.grid(row = 1, column = 0)
    twoScoopSizeRadioButton.grid(row = 2, column = 0)
    threeScoopSizeRadioButton.grid(row = 3, column = 0)
    scoopPhotoLabel.grid(row = 7, column = 0, pady = (60))

    # Widgets for Cone Type Frame
    coneTypeLabel.grid(row = 0, column=0)             
    coneTypeSundae.grid(row=1, column=0, sticky=W)  
    coneTypeCone.grid(row=2, column=0, sticky=W)    
    conePhotoLabel.grid(row=7, column = 0, pady = (60))
    
    # Render all widgets for toppings Frame (using item breaks the window.)
    toppingsSection = [toppingsLabel, toppNuts, toppChoc, toppStraw, toppStraw,
        toppPSyrup, toppWCream, toppSprink, toppSCookie, toppBananas, toppCherries]
    for index, item in enumerate(toppingsSection):
        toppingsSection[index].grid(row = index, column = 0)
    
    # Widgets for Order Summary Frame
    orderSummarySection = [customerLabelTitle, customerNameLabel, orderTypeTitle,
        orderTypeLabel, placeOrderButton]
    for index, item in enumerate(orderSummarySection):
        orderSummarySection[index].grid()

    placeOrderButton.configure(command=lambda: orderThankYou(orderWindow, customerName, 
    scoopSizeVar.get(), coneTypeVar.get(), toppingSelection))