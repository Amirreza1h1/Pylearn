def diamond(n: int):
    star_count = 1
    space_count = n-1
    # top of diamond
    for j in range(n-1):
        print(" "*space_count, end="")
        print("*"*star_count)
        space_count -= 1
        star_count += 2
    # bottom of diamond
    for j in range(n):
        print(" "*space_count, end="")
        print("*"*star_count)
        space_count += 1
        star_count -= 2


n = int(input("enter your number: "))
diamond(n)
