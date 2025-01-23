import random

def mariage(boys,girls):
    marry=[]

    while True:
        if len(boys)>0 and len(girls)>0:
            boy=boys.pop(random.randint(0,len(boys)-1))
            girl=girls.pop(random.randint(0,len(girls)-1))
            m=f"({boy},{girl})"
            marry.append(m)
        else:
            break

    return marry

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

print(mariage(boys,girls))