x=int(input("fibonachi number: "))
a,b,c=0,1,0

for i in range(x):
    print(b)
    c=b
    b=a+b
    a=c