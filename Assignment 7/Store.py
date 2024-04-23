import qrcode
import os

os.system("cls")

PRODUCTS = []


def read_from_database():
    file = open("database.txt", "r")

    for line in file:
        split_file = line.split(",")
        dict_file = {"code": split_file[0], "name": split_file[1],
                     "price": split_file[2], "count": split_file[3]}
        PRODUCTS.append(dict_file)

    file.close()


def write_to_database():
    file = open("database.txt", "w")
    for product in PRODUCTS:
        file.write(product+"\n")
    file.close()


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3-remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- save with QR code")
    print("8- Exit")


def add():
    code = input("enter code:")
    name = input("enter name:")
    price = input("enter price:")
    count = input("enter count:")
    new_product = {"code": code, "name": name, "price": price, "count": count}
    PRODUCTS.append(new_product)


def edit():
    status_code = True
    while status_code:
        product_code = input("enter code of product: ")
        for product in PRODUCTS:
            if product["code"] == product_code:
                print(product["name"], "\t\t", product["price"],
                      "\t\t", product["count"])
                product_name = product["name"]
                product_price = product["price"]
                product_count = product["count"]
                status_code = False
                break
        else:
            print("not found to commit change!!")
    while True:
        print("1- Name")
        print("2- Price")
        print("3- Count")
        product_change = int(input("which one should change(1,2,3): "))
        if product_change == 1 or product_change == 2 or product_change == 3:
            break
        else:
            print("please enter correct number!!")
    if product_change == 1:
        print(product_name)
        new_change = input("new name: ")
        for product in PRODUCTS:
            if product["code"] == product_code:
                product["name"] = new_change
                print("information updated succesfully")
    elif product_change == 2:
        print(product_price)
        new_change = input("new price: ")
        for product in PRODUCTS:
            if product["code"] == product_code:
                product["price"] = new_change
                print("information updated succesfully")
    elif product_change == 3:
        print(product_count)
        new_change = input("new count: ")
        for product in PRODUCTS:
            if product["code"] == product_code:
                product["count"] = new_change
                print("information updated succesfully")


def remove():
    product_code = input("code of product that you want to remove: ")
    for product in PRODUCTS:
        if product["code"] == product_code:
            PRODUCTS.remove(product)
            print("product remove succesfully")
            break
    else:
        print("there is not such a product in the list")


def search():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"],
                  "\t\t", product["price"])
            break
    else:
        print("not found!")


def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"],
              "\t\t", product["price"])


def buy():
    Product_to_buy = []
    status_to_buy = True
    while status_to_buy:
        product_code = input("enter code of product: ")
        for product in PRODUCTS:
            if product["code"] == product_code:
                product_count = input("please enter the quantity you want: ")
                if product_count <= product["count"]:
                    Product_to_buy.append(product)
                    Product_to_buy[product["count":product_count]]
                    product["count"] = product["count"]-product_count
                    print("do you have more things to buy?")
                    print("1- Yes")
                    print("2- No")
                    continue_to_buy = int(input(""))
                    if continue_to_buy == 2:
                        status_to_buy = False
                else:
                    print("Store does not have a quantity you want!")
                    print("Sorry!")
                    print("do you have other things to buy?")
                    print("1- Yes")
                    print("2- No")
                    continue_to_buy = int(input(""))
                    if continue_to_buy == 2:
                        status_to_buy = False
                # product_name = product["name"]
                # product_price = product["price"]
                break
        else:
            print("product not found!!")
            print("do you have other things to buy?")
            print("1- Yes")
            print("2- No")
            continue_to_buy = int(input(""))
            if continue_to_buy == 2:
                status_to_buy = False
    sum = 0
    for product in Product_to_buy:
        sum = product["count"]*product["price"]
        print(product["code"], "\t\t", product["name"], "\t\t",
              product["price"], "\t\t", product["count"])
    print("\t\t\t\ttotally "+sum+" Rials")


def save_with_QRcode(product_code_for_save):
    for product in PRODUCTS:
        if product["code"] == product_code_for_save:
            file_name = product["name"]+"\n" + \
                product["price"]+"\n"+product["count"]
            qr_code = qrcode.make(file_name)
            qr_code.save(file_name+".png")
            break
    else:
        print("product not found!")


print("Welcome to Store")
read_from_database()
print("Loading...")
print("Data loaded.")

while True:
    show_menu()

    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        selected_code = input("please enter your code: ")
        save_with_QRcode(selected_code)
    elif choice == 8:
        print("Are you sure?")
        print("1- Yes")
        print("2- No")
        exit_choice = int(input(""))
        if exit_choice == 1:
            write_to_database()
            exit(0)
    else:
        print("your input is not correct!!")
