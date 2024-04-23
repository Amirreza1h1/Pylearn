import math

while True:
    print("ax*3+bx*2+cx+d=e")
    while True:
        a = float(input("please insert a: "))
        print(a if a != 0 else "it can not be zero")
        if a != 0:
            break

    b = float(input("please insert b: "))
    c = float(input("please insert c: "))
    d = float(input("please insert d: "))
    e = float(input("please insert e: "))
    b=b/a
    c=c/a
    d=(d-e)/a
    
    p = c - ((b**2)/3)
    q = (2*(b**3)/27) - (b*c/3) + d

    Delta = (q**2/4) + (p**3/27)

    if Delta > 0:
        x = (((-q/2)+(Delta**(1/2)))**(1/3)) + (((-q/2)-(Delta**(1/2)))**(1/3)) - (b/3)
        print("answer is: ",x)
    elif Delta == 0:
        x_1 = -2*((q/2)**(1/3)) - (b/3)
        x_23 = ((q/2)**(1/3)) - (b/3)
        print("answers are: ",x_1," and ",x_23,"(this one is calculated twice!!)")
    else:
        x = (q*3*3**(1/2))/(2*((-p)**(1/2))**3)
        x_1 = (2/(3**(1/2)))*((-p)**(1/2))*math.sin((1/3)*math.asin(x)) - (b/3)
        x_2 = (-2/(3**(1/2)))*((-p)**(1/2))*math.sin((1/3)*math.asin(x)+(math.pi/3)) - (b/3)
        x_3 = (2/(3**(1/2)))*((-p)**(1/2))*math.cos((1/3)*math.asin(x)+(math.pi/6)) - (b/3)
        print("answers are: ",x_1," , ",x_2," and ",x_3)

    ask = input("Do you want solve another one or no!!(yes or no)")
    if ask == "no":
        break