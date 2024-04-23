a=int(input("first number:"))
A_a=[] # array of a
b=int(input("second number:"))
A_b=[] # array of b
A_c=[] # array of common

for i in range(1,a+1):
    if a%i == 0:
        A_a.append(i)

for i in range(1,b+1):
    if b%i == 0:
        A_b.append(i)

for i in A_a:
    if i in A_b:
        A_c.append(i)
print(A_c[-1])