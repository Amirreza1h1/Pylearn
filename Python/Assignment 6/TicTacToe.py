import pyfiglet
import os
from colorama import Fore, init, Style
import time
import random
os.system("cls")

start = time.time()

fonts = pyfiglet.Figlet().getFonts()
title = "Tic Tac Toe"
pyfiglet.print_figlet(title, font=fonts[36], colors="GREEN")


def show():
    for row in game_board:
        for cell in row:
            init()
            if cell == "X":
                print(Fore.RED, cell, end=" ")
            elif cell == "O":
                print(Fore.BLUE, cell, end=" ")
            elif cell == "-":
                print(Style.RESET_ALL, cell, end=" ")
        print()
    print(Style.RESET_ALL)


def check_winer():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        return True

    elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][1] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][1] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        return True

    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("Player 2 wins!")
        return True

    count = 0
    for row in game_board:
        for cell in row:
            if cell != "-":
                count += 1
    if count == 9:
        print(Fore.YELLOW, "Draw!")
        return True


game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
show()

def PLAYER():
    while True:
        while True:
            print("Player 1")
            row = int(input("row[1-3]: "))-1
            col = int(input("col[1-3]: "))-1

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("Wrong insert :/")
            else:
                print("Wrong input :/")
        show()
        if check_winer() == True:
            break
        while True:
            print("Player 2")
            row = int(input("row[1-3]: "))-1
            col = int(input("col[1-3]: "))-1

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    break
                else:
                    print("Wrong insert :/")
            else:
                print("Wrong input :/")
        show()
        if check_winer() == True:
            break

def CPU():
    while True:
        while True:
            print("Player")
            row = int(input("row[1-3]: "))-1
            col = int(input("col[1-3]: "))-1

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("Wrong insert :/")
            else:
                print("Wrong input :/")
        show()
        if check_winer() == True:
            break
        print("CPU")
        while True:
            row = random.randint(1,3)
            col = random.randint(1,3)

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    break
        show()
        if check_winer() == True:
            break


print("menu")
print("1-play with PLAYER")
print("2-play with CPU")

while True:
    choose = int(input("-> "))
    print(choose if choose == 1 or choose == 2 else "choose again!")
    if choose == 1 or choose == 2:
        break
if choose==1:
    PLAYER()
else:
    CPU()

print("Time spend: "+str(time.time()-start)+" seconds")
