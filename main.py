"""
Program: Warehouse control
Author: Fabiola Barrientos
Date: Nov. 3030
Functionality:
    - Register products
      - id (auto generated)
      - title
      - stock
      - price


"""
from menu import clear2, print_menu, print_header, print_product_info
from product import Product
import pickle


catalog = []
idNumber = 0

def disctinct_categories():
    print_header("Discticn categories")
    categories = []

    for prod in catalog:
        if prod.category not in categories:
            categories.append(prod.category)
    
    for cat in categories:
        print(cat)


def most_expensive_items():
    print_header("3 most expensive products prices")
    prices = []
    for prod in catalog:
        prices.append(prod.price)

    # sort the array
    prices.sort(reverse=True)

    # print
    print(prices[0])
    print(prices[1])
    print(prices[2])


def serialize_data():
    writer = open("warehouse.data", "wb")  # wb = wrute binary
    pickle.dump(catalog, writer)
    writer.close()
    print("**Data serialized!!")


def deserialize_data():
    global idNumber

    try:
        reader = open("warehouse.data", "rb")  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)
            idNumber = prod.id

        #last = catalog[-1]
        #idNumber = last.id + 1
        how_many = len(catalog)
        print("** Read: " + str(how_many) + " products")
    except:
        print("The file not exist!!!..")


def delete_product():
    print_header("Delete produc")

    display_products()

    print("***********************")
    idDeleted = int(input("Give me the ID to deleted:"))
    print("***********************")

    found = False
    for prod in catalog:
        if(prod.id == idDeleted):
            found = True
            catalog.remove(prod)
            print("Product ["+str(idDeleted)+"] as been removed!!!!..")

    if(not found):
        print("ID not founded!!!... try again")


def update_product():
    print_header("Update product")
    display_products()

    print("***********************")
    idUpdated = int(input("Give me the ID to update:"))
    print("***********************")

    found = False
    for prod in catalog:
        if(prod.id == idUpdated):
            found = True
            catalog.remove(prod)

            title = input("Give me a Title: ")
            category = input("Give me a Category: ")
            stock = int(input("Give me a stock: "))
            price = float(input("Give me a price: "))

            # Validations
            if(len(title) < 1):
                print("Error: Title should not be empty")
            if(len(category) < 1):
                print("Error: Category should not be empty")
            if(price < 1):
                print("Error: Price should not be less than 1")

            new_product = Product(idUpdated, title, category, stock, price)
            catalog.append(new_product)

            print("Product ["+str(idUpdated)+"] as been modified!!!!..")

    if(not found):
        print("ID not founded!!!... try again")


def update_product_stock():

    print_header("Update product stock")
    display_products()

    try:
        print("***********************")
        idUpdated = int(input("Give me the ID to update stock:"))
        print("***********************")

        found = False
        for prod in catalog:
            if(prod.id == idUpdated):
                found = True
                stock = int(input("Give me a new stock: "))
                prod.stock = stock
                print("Product ["+str(idUpdated) +
                      "] as been modified stock!!!!..")

        if(not found):
            print("ID not founded!!!... try again")
    except:
        print("Error on update stock!!!!!")


def update_product_price():

    print_header("Update product price")
    display_products()

    try:
        print("***********************")
        idUpdated = int(input("Give me the ID to update price:"))
        print("***********************")

        found = False
        for prod in catalog:
            if(prod.id == idUpdated):
                found = True
                price = int(input("Give me a new price: "))
                prod.price = price
                print("Product ["+str(idUpdated) +
                      "] as been modified price!!!!..")

        if(not found):
            print("ID not founded!!!... try again")
    except:
        print("Error on update price!!!!!")


def display_cheaper_products():
    print_header("Cheapest product is")

    cheapest = catalog[0]
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod
    print("Cheapest product is:")
    print_product_info(cheapest)


def display_products():
    print_header("Catalog")
    for prod in catalog:
        print_product_info(prod)


def display_products_equal_zero():
    print_header("Stock == 0")
    for prod in catalog:
        if(prod.stock == 0):
            print_product_info(prod)


def display_total_stock_value():
    print_header("Total stock Value")
    Total = 0

    for prod in catalog:

        Total += prod.stock * prod.price

    print("Total stock: " + str(Total))


"""
def display_cheaper_products():
    print_header("Creaper products")
    for prod in catalog.sort("price"):
        print_product_info(prod)
"""


def register_products():
    try:
        global idNumber

        print_header("Add products")
        title = input("Give me a Title: ")
        category = input("Give me a Category: ")
        stock = int(input("Give me a stock: "))
        price = float(input("Give me a price: "))

        # Validations
        if(len(title) < 1):
            print("Error: Title should not be empty")
        if(len(category) < 1):
            print("Error: Category should not be empty")
        if(price < 1):
            print("Error: Price should not be less than 1")

        idNumber += 1

        new_product = Product(idNumber, title, category, stock, price)
        catalog.append(new_product)
    except:
        print("Unexpected error!!!....")


# Main operations
opc = ''

deserialize_data()

input("Press enter to continue....")


while(opc != 'x'):
    clear2()
    print_menu()
    opc = input('Please select an option:')

    if(opc == '1'):
        register_products()
        serialize_data()
    elif(opc == '2'):
        display_products()
    elif(opc == '3'):
        display_products_equal_zero()
    elif(opc == '4'):
        display_total_stock_value()
    elif(opc == '5'):
        display_cheaper_products()
    elif(opc == '6'):
        delete_product()
        serialize_data()
    elif(opc == '7'):
        update_product()
        serialize_data()
    elif(opc == '8'):
        update_product_stock()
        serialize_data()
    elif(opc == '9'):
        update_product_price()
        serialize_data()
    elif(opc == '10'):
        most_expensive_items()
    elif(opc == '11'):
        disctinct_categories()

    input('Enter to continue....')