import Media
import Film
import Series
import Documentary
import Clip
import Actor
import Db


PRODUCTS = []
ACTORS = []

print("Welcome to Media Store")
print("Loading...")
Db.read()
print("Data loaded.")

while True:
    Media.show_menu()

    choice = int(input("enter your choice: "))

    if choice == 1:  # add
        print("what do you want to add?")
        print("1- Media")
        print("2- Actor")
        flag = input("")
        if int(flag) == 1 or flag == "Media":
            print("what kind of Media?!")
            print("1- Film")
            print("2- Series")
            print("3- Documentary")
            print("4- Clip")
            flag = int(input(""))
            if flag == 1:
                PRODUCTS.append(Film.add())
                print("Added succesfully")
            elif flag == 2:
                PRODUCTS.append(Series.add())
                print("Added succesfully")
            elif flag == 3:
                PRODUCTS.append(Documentary.add())
                print("Added succesfully")
            elif flag == 4:
                PRODUCTS.append(Clip.add())
                print("Added succesfully")
            else:
                print("your input is not correct!!")

        elif int(flag) == 2 or flag == "Actor":
            ACTORS.append(Actor.add())
            print("Added succesfully")
        else:
            print("your input is not correct!!")

    elif choice == 2:  # edit
        print("what do you want to edit?")
        print("1- Film")
        print("2- Series")
        print("3- Documentary")
        print("4- Clip")
        flag = int(input(""))
        video = input("what is the name of that?"+"\n")
        for product in PRODUCTS:
            if product.name == video:
                if flag == 1:
                    Film.edit()
                    break
                elif flag == 2:
                    Series.edit()
                    break
                elif flag == 3:
                    Documentary.edit()
                    break
                elif flag == 4:
                    Clip.edit()
                    break
        else:
            print("your input is not correct!!")
    elif choice == 3:  # remove
        print("what do you want to remove?")
        print("1- Actor")
        print("2- Media")
        flag = int(input(""))
        if flag == 1:
            name = input("what is the name of that?"+"\n")
            for index, n in ACTORS:
                if name == n.name:
                    del ACTORS[index]
                    break
            else:
                print("there is no such an actor in database!!")
            break

        if flag == 2:
            video = input("what is the name of that?"+"\n")
            for index, p in PRODUCTS:
                if p.name == video:
                    del PRODUCTS[index]
                    break
            else:
                print("there is no such a media in database!!")
        else:
            print("your input is not correct!!")
    elif choice == 4:  # search
        print('give me to time in minute for example 80 and 110' +
              '\n'+'to search among the Film type!')
        a = input("first time:")
        b = input("second time:")
        searched_array=[]
        for index, p in PRODUCTS:
                if p.type == 'Film':
                    searched_array.append(PRODUCTS[index])
        if not searched_array:
            print("there is no such a Film in database!!")

    elif choice == 5:  # show_list
        Media.showinfo(PRODUCTS)
    elif choice == 6:  # download
        Media.showinfo(PRODUCTS)
        video = input("please give me the name of the product:"+'\n')
        for index, p in PRODUCTS:
            if p.name == video:
                Media.download(p.url)
                break
        else:
            print("there is no such a media in database!!")

    elif choice == 7:  # Exit
        print("Are you sure?")
        print("1- Yes")
        print("2- No")
        exit_choice = int(input(""))
        if exit_choice == 1:
            Db.write()
            exit(0)
    else:
        print("your input is not correct!!")
