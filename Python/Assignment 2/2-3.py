sum,n=0,0,
grade=input("grade: ")

while grade != "exit":
    sum=sum+float(grade)
    n=n+1
    grade=input("grade: ")

print("your average: ",sum/n)