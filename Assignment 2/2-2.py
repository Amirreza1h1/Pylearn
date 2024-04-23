import random

computer_choice=0
computer_score=0
user_score=0
y=int(input("turn of wins: "))

while computer_score != y or user_score != y:

    x=random.randint(1,3) #1=rock 2=paper 3=scissors

    if x==1:
        computer_choice="rock"
    elif x==2:
        computer_choice="paper"
    else:
        computer_choice="scissors"

    user_choice=input("rock, paper, scissors: ")

    print("💻: ",computer_choice)
    print("🧠: ",user_choice)

    if (computer_choice == user_choice):
        print("draw")
    elif computer_choice == "rock" and user_choice == "paper":
        user_score=user_score+1
    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score=computer_score+1
    elif  computer_choice == "paper" and user_choice == "rock":
        computer_score=computer_score+1
    elif  computer_choice == "paper" and user_choice == "scissors":
        user_score=user_score+1
    elif  computer_choice == "scissors" and user_choice == "rock":
        user_score=user_score+1
    elif  computer_choice == "scissors" and user_choice == "paper":
        computer_score=computer_score+1
    if  computer_score == y:
        print("computer 💻 win")
        break
    if user_score == y:
        print("user 🧠 win")
        break