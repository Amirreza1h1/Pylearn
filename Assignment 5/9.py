def multiple_grid(a: int, b: int):
    print("x", end="  ")
    for i in range(1, b+1):
        print(i, end="  ")
    print("")

    for i in range(1, a+1):
        print(i, end="  ")
        for j in range(1, b+1):
            print(i*j, end="  ")
        print("")


a = int(input("please enter rows: "))
b = int(input("please enter columns: "))
multiple_grid(a, b)
