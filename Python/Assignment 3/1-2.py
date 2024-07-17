a=[]
f=0 # f -> flag for duplicate number

while True:
    x=int(input("write a number: "))
    for i in range(len(a)):
        if a[i] == x:
            print("duplicated number!!")
            f=1
            break
    
    if f != 1:
        a.append(x)
    else:
        break
print(a)