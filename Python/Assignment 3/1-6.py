a=int(input("first number:"))
A_a=[] # array of a
b=int(input("second number:"))
A_b=[] # array of b
A_c=[] # array of common

for i in range(1,50):
    A_a.append(a*i)

for i in range(1,50):
    A_b.append(b*i)

for i in A_a:
    if i in A_b:
        A_c.append(i)
print(A_c[0])