# ScoopServe Ordering Menu

from tkinter import *               # Tkinter GUI Library
from tkinter import messagebox      # Using MessageBoxes for Errors
from PIL import Image, ImageTk      # Python Imaging Library

def windowDestroy(parent, current):

    parent.destroy()
    current.destroy()

def orderThankYou(parent):

    thankYouWindow = Toplevel(parent)
    thankYouWindow.title("Thank you for your order!")
    thankYouLabel = Label(thankYouWindow, text = "Thank you for your order!", font = "Arial")
    thankYouButton = Button(thankYouWindow, text = "Close Window")
    thankYouButton.pack()

def orderMenu(parentWindow, customerName, orderType):

    scoopSizeVar = StringVar()                           # Scoop Size Variable
    coneTypeVar = StringVar()                            # Cone Type Variable
    customerNameVar = StringVar(value = customerName)    # Customer Name Variable (passed from orderMenu())
    orderTypeVar = StringVar(value = orderType)          # Order Type Variable

    # Using Toplevel() to create a new window. The parent window
    # must be specified so we use the parameter passed in from
    # orderMenu, parentWindow.
    orderWindow = Toplevel(parentWindow)
    orderWindow.title("ScoopServe - Creating Order")
 
    # Sets the geometry of our orderWindow to 300x300
    orderWindow.geometry("640x300")
 
    # Frame for Scoop Sizes, it belongs to the second window "orderWindow"
    # with a border width of 1, and relief is our styling of the border.
    # in this case, we want a ridge.
    scoopSizes = Frame(orderWindow, borderwidth = 1, relief='ridge')
    scoopSizeLabel = Label(scoopSizes, text ='Scoop Size', font = "Arial")
    scoopSizeImage = ImageTk.PhotoImage(Image.open("coneSmall.png"))
    scoopPhotoLabel = Label(scoopSizes, image = scoopSizeImage)
    scoopPhotoLabel.image = scoopSizeImage

    # Our radio buttons to pick between one, two or three scoops.
    oneScoopSizeRadioButton = Radiobutton(scoopSizes, text = 'One Scoop', value = "One", variable = scoopSizeVar)
    twoScoopSizeRadioButton = Radiobutton(scoopSizes, text = 'Two Scoop', value = "Two", variable = scoopSizeVar)
    threeScoopSizeRadioButton = Radiobutton(scoopSizes, text = 'Three Scoop', value = "Three", variable = scoopSizeVar)

    # Frame for our Cone Types, and we have a label, and 2 radiobuttons
    # for a sundae type cone and a regular sugar cone.
    coneType = Frame(orderWindow, borderwidth = 1, relief = 'ridge') 
    coneTypeLabel = Label(coneType, text ='Cone Type', font = "Arial")
    coneTypeSundae = Radiobutton(coneType, text = "Sundae Bowl", value = "Sundae", variable = coneTypeVar) 
    coneTypeCone = Radiobutton(coneType, text = "Sugar Cone", value = "Cone", variable = coneTypeVar)
    coneTypeImage = ImageTk.PhotoImage(Image.open("sundaeBowl.png"))
    conePhotoLabel = Label(coneType, image = coneTypeImage)
    conePhotoLabel.image = coneTypeImage

    # Frame for Our Toppings Menu, and Check Buttons for each of the toppings
    toppingsMenu = Frame(orderWindow, borderwidth = 1, relief = 'ridge')
    toppingsLabel = Label(toppingsMenu, text = 'Toppings', font = 'Arial')
    toppNuts = Checkbutton(toppingsMenu, text = 'Nuts - $0.50')
    toppChoc = Checkbutton(toppingsMenu, text = 'Chocolate - $0.90')
    toppStraw = Checkbutton(toppingsMenu, text = 'Strawberry - $0.90')
    toppPSyrup = Checkbutton(toppingsMenu, text = 'Pineapple Syrup - $1.00')
    toppWCream = Checkbutton(toppingsMenu, text = 'Whipped Cream - $0.50')
    toppSprink = Checkbutton(toppingsMenu, text = 'Sprinkles - $0.30')
    toppSCookie = Checkbutton(toppingsMenu, text = 'Sugar Cookies - $1.00')
    toppBananas = Checkbutton(toppingsMenu, text = 'Bananas - $0.50')
    toppCherries = Checkbutton(toppingsMenu, text = 'Cherries - $0.50')

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
    scoopSizes.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    coneType.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    toppingsMenu.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
    orderSummary.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

    # Widgets for Scoop Size Frame 
    scoopSizeLabel.grid(row=0, column=0)
    oneScoopSizeRadioButton.grid(row = 1, column = 0)
    twoScoopSizeRadioButton.grid(row = 2, column = 0)
    threeScoopSizeRadioButton.grid(row = 3, column = 0)
    scoopPhotoLabel.grid(row = 7, column = 0, pady = (60))

    # Widgets for Cone Type Frame
    coneTypeLabel.grid(row=0, column=0)             # Grid the label
    coneTypeSundae.grid(row=1, column=0, sticky=W)  # Grid the first radio button
    coneTypeCone.grid(row=2, column=0, sticky=W)    # Grid the second radio button
    conePhotoLabel.grid(row=7, column = 0, pady = (60))
    
    # Widgets for Toppings Frame
    toppingsLabel.grid(row = 0, column = 0)
    toppNuts.grid(row = 1, column = 0)
    toppChoc.grid(row = 2, column = 0)
    toppStraw.grid(row = 3, column = 0)
    toppPSyrup.grid(row = 4, column = 0)
    toppWCream.grid(row = 5, column = 0)
    toppSprink.grid(row = 6, column = 0)
    toppSCookie.grid(row = 7, column = 0)
    toppBananas.grid(row = 8, column = 0)
    toppCherries.grid(row = 9, column = 0)

    # Widgets for Order Summary Frame
    customerLabelTitle.grid(row = 0, column = 0)
    customerNameLabel.grid(row = 1, column = 0)
    orderTypeTitle.grid(row = 2, column = 0)
    orderTypeLabel.grid(row = 3, column = 0)
    placeOrderButton.grid(row = 4, column = 0)

    placeOrderButton.configure(command=lambda: orderThankYou(orderWindow, ))