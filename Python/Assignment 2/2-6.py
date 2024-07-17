import random

dice=random.randint(1,6)

while True:
    if dice in (1,2,3,4,5):
        print("dice= ",dice)
        break
    else:
        print(dice)
        print("you have reward!!😍")
        print("you can dice again")
        dice=random.randint(1,6)
