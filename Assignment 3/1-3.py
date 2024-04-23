a = []
f = False  # f -> flag

while True:
    x = input("write a number: ")
    if x == "exit":
        break
    if int(x) in a:    
        print("duplicated number!! not allow")
    else:
        a.append(int(x))

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] < a[i]:
            print("unorder list")
            print(a)
            f=True
            break
    if i==len(a)-1:
        print("order list")
        print(a)
        break
    if f:
        break