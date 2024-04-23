a=[]
n=int(input("size of your snake:"))
f=True #f-> true == *

for i in range(n):
    if f:
        a.append("*")
        f=False
    else:
        a.append("#")
        f=True
snake="".join(a)
print(snake)