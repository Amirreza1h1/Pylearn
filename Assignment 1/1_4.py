w,h=0,0
w=float(input("your weight(kg): "))
h=float(input("your height(m): "))
BMI=w/h**2

if 35<=BMI<40:
    print("extreme obesity")
elif 30<=BMI<35:
    print("obesity")
elif 25<=BMI<30:
    print("overweight")
elif 18.5<=BMI<25:
    print("normal weight")
elif BMI<18.5:
    print("underweight")
print(BMI)