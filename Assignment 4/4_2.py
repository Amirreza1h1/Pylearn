import math

user_number = int(input("enter number:"))
n=0
x=None
while True:
    x=math.factorial(n)
    if x == user_number:
        print("Yes!!")
        break
    elif x > user_number:
        print("No!!")
        break
    n+=1 
