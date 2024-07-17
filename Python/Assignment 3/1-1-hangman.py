import random

words_bank = [
    "tree","food","book","blue","train","fish","woman","life","freedom","iran","sky","cyrus","ford","ferrari","canada","image","voice"
]
user_mistakes=0
good_chars=[]
bad_chars=[]
x=random.randint(0,len(words_bank)-1)
word = words_bank[x]


while user_mistakes < 6:
    lw=len(word)
    for i in range(len(word)):
       if word[i] in good_chars:
            print(word[i], end=" ")
            lw -=1
       else:
            print("_ ", end="")

    if lw==0:
        print("You won 🎉🎊👏")
        break

    user_cahr=input("please write your guess: ").lower()

    if len(user_cahr)==1:
        if user_cahr in word:
            good_chars.append(user_cahr)
            print("✅")
        else:
            bad_chars.append(user_cahr)
            user_mistakes+=1
            print("❌")
    else:
        print("write one character!!!!")
if user_mistakes == 6:
    print("You lose ☠")


