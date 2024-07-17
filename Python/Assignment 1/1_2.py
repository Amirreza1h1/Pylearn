a=int(input("insert a:"))
b=int(input("insert b:"))
c=int(input("insert c:"))

if (a+b>c and a+c>b and b+c>a):
    print("you can create this triangle")
else:
    print("Warning you can't create such a triangle!!")