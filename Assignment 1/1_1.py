import math

result,a,b = 0,0,0

print("welcome to calculator")

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")
print("log")
print("sqrt")
print("please enter your choice: ")
op = input()

if op in ("sin","cos","tan","cot"):
    a = float(input("degree: "))
    a = a*math.pi/180
else:
    a = float(input("first number for factorial and sqrt: "))
    b = float(input("second number: "))

if op == "+":
    result=a+b

elif op =="-":
    result=a-b

elif op=="*":
    result=a*b

elif op=="/":
    if b==0:
        print("division to zero!!")
    else:
        result=a/b

elif op=="sin":
    result=math.sin(a)

elif op=="cos":
    result=math.cos(a)


elif op=="tan":
    result=math.tan(a)


elif op=="cot":
    result=1 / math.tan(a)

elif op=="factorial":
    result=math.factorial(int(a))

elif op=="log":
    result=math.log(a)

elif op=="sqrt":
    result=math.sqrt(a)

print(result)
