a = []
b=[]
while True:
    x = input("number'no for break': ")
    if x == "no":
        print(a)
        break
    else:
        a.append(int(x))

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])

print(b)