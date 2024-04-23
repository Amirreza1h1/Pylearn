name=input("your name: ")
family=input("your family: ")
l1=int(input("grade 1:"))#l1 = lesson one
l2=int(input("grade 2:"))
l3=int(input("grade 3:"))

if (0<=l1<=20) and (0<=l2<=20) and (0<=l3<=20):
    avg=(l1+l2+l3)/3
    if avg>=17:
        print("Great")
    elif avg>=12 and avg<17:
        print("Normal")
    else:
        print("Fail")
else:
    print("your input value is not valid( it should be between 0 to 20)")
