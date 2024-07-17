a = []
while True:
    x = input("number'no for break': ")
    if x == "no":
        print(a)
        break
    else:
        int(x)
        a.append(x)
a.reverse()
print(a)