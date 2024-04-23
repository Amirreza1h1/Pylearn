import random

computer_number=random.randint(0,100)
x=0#the number of your guess

while True:
    user_number=int(input("your guess: "))

    if computer_number == user_number:
        print("you win👏🎉")
        print("the number of your guess is: ",x)
        break
    elif computer_number > user_number:
        print("go up⬆")
        x=x+1
    elif computer_number < user_number:
        print("go down⬇")
        x=x+1
    