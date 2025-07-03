INVENTORY = { #THIS IS A DICTIONARY, WHICH REPRESENTS THE STORE'S INVENTORY
    "BAG BLUE": (80.000, 50),
    "BAG WHITE": (90.000, 50),
    "BAG RED": (70.000, 50),
    "BAG GREEN": (80.000, 50),
    "BAG YELLOW": (70.000, 50),
    "BAG BROWM": (70.000, 50),
    "BAG BLACK": (90.000, 50),
}
def add_inventory(): #THIS IS THE SECTION TO ADD A PRODUCT, IT ASK FOR THE PRODUCT NAME, PRICE AND QUANTITY AND IT IS SAVED IN THE INVENTORY
    product = input("Enter the product you want to add: ")
    price = float (input ("Enter the price of the product: "))
    quantity = int (input ("Enter the quantity: "))
    INVENTORY[product] = (price, quantity)

def search_product(): #SEARCH FOR THE PRODUCT HERE, AS LONG AS THE PRODUCT IS IN THE INVENTORY, OTHERWISE, IT WILL NOT APPEAR
    product = input ("Enter the name of the product you want to search for: ")
    if product in INVENTORY:
        price, quantity = INVENTORY[product]
        print (f"The {product} it is in inventory with a price of {price} and with a quantity of {quantity}.")
    else: 
        print ("Product not found.")
def uptade_prices(): # HERE IS THE PRICE UPDATE SECTION, THE USER MUST SET A POSITIVE PRICE, OTHERWISE IT WILL NOT BE SAVED
    product = input("Enter the name of the product: ")
    if product in INVENTORY:
        while True:
            try:
                new_price = float(input("Enter the new price: "))
                quantity = INVENTORY[product][1]
                INVENTORY[product] = (new_price, quantity)
                print (f"The product {product} has been updated with a price of {new_price}.")
                if new_price > 0: 
                    return new_price
                else: 
                    print ("the new price must be positive. ")
            except ValueError:
                print ("Invalid entry, please enter a number. ")
    else:
        print ("Product no found.")
def delete_product(): # HERE PRODUCTS WITH A DEL ARE ELIMINATED
    product = input("Enter the name of the product you want to delete: ")
    if product in INVENTORY:
        del INVENTORY[product]
        print (f"The product {product} has been removed from inventory.")
    else:
        print("Product no found.")
    
def calculate_total(): #HERE THE TOTAL IS CALCULATED, WITH THE LAMBDA FUNCTION
    # total = 0
    # for tupla in INVENTORY.values():
    #     total = total + (tupla[0]*tupla[1]) #Sin lamda
    total = lambda: sum([(tupla[0]*tupla[1]) for tupla in INVENTORY.values()])
    print (f"The total inventory is ${total():,.2f}.")

print (" Welcome to the Totta store inventory.")

while True: # HERE I USE A CYCLE, SO THAT THE PROGRAM CONTINUES UNTIL THE SAME USER DECIDES TO EXIT THE PROGRAM
    print ("Menu options.")

    print ("1. Add inventory.")
    print ("2. Search product.")
    print ("3. Uptade prices.")
    print ("4. Delete product.")
    print ("5. Calcule total.")
    print ("6. Exit.")

    options = input ("Select one option (1-6): ")
    if options == "1":
        add_inventory()
    elif options == "2":
        search_product()
    elif options == "3":
        uptade_prices()
    elif options == "4":
        delete_product()
    elif options == "5":
        calculate_total()
    elif options == "6":
        print ("Bye, see you later!! ")
        break
    else: 
        print ("Just a number from 1 to 6! ")