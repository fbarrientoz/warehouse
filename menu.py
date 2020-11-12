import os
"""
fUNCTIONALITY:
-Register products
    -id(auto)
    -title
    -category
    -stock
    -price
    
COMMENT MULTIPLE LINES

 def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("clear")
"""


def print_product_info(prod):
    print(
        str(prod.id) + " | " +
        prod.title + " | " +
        prod.category + " | " +
        str(prod.stock) + " | " +
        str(prod.price) + " | "
    )


def clear2():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system("clear")

    # return os.system('cls' if os.name== 'nt' else 'clear;)


def print_menu():
    print('*'*50)
    print('Welcome - WareHouse')
    print('*'*50)

    print('[1] Add product to Catalog')
    print('[2] Display Catalog')
    print('[3] Display Products out of stock')
    print('[4] Total stock value')
    print('[5] Cheapest products')
    print('[6] Delete product')

    print('[7] Update product')
    print('[8] Update stock')

    print('[x] Exit')

    print('-'*20)  # repeat the char


def print_header(text):
    clear2()
    print('*'*50)
    print(text)
    print('*'*50)
