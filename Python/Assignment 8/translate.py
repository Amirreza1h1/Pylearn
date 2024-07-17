import os
import gtts
# import tts


def read_from_file():
    global words_bank
    if os.path.exists("translate.txt"):
        with open("translate.txt", "r") as f:
            temp = f.read().split("\n")
            words_bank = []
            try:
                for i in range(0, len(temp), 2):
                    my_dict = {"en": temp[i], "fa": temp[i+1]}
                    words_bank.append(my_dict)
            except:
                print("database is empty!")

    else:
        print("there is a problem to read database!")


def write_to_file():
    with open("translate.txt", "w") as file:
        for word in words_bank:
            file.write(word["en"]+"\n")
            file.write(word["fa"]+"\n")


def show_menu():
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word to database")
    print("4- exit")


def translate_english_to_persian():
    user_text = input("enter your english text: ")
    user_words = user_text.split(" ")
    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"]+" "
                break
        else:
            output = output + user_word+" "
    print(output)


def translate_persian_to_english():
    user_text = input("enter your persian text: ")
    user_words = user_text.split(" ")
    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"]+" "
                break
        else:
            output = output + user_word+" "
    print(output)
    x = gtts.gTTS(output, lang="en", slow=False)
    x.save("voice.mp3")
    print(x)


def add_a_new_word():
    new_word = input("your new english word: ")
    for word in words_bank:
        if word["en"] == new_word:
            print("there is a meaning for this word in the database!")
            break
    else:
        new_word_fa = input("persian meaning: ")
        for word in words_bank:
            if word["fa"] == new_word_fa:
                print("there is a meaning for this word in the database!")
                break
        else:
            new_dict = {"en": new_word, "fa": new_word_fa}
            words_bank.append(new_dict)
            print("it appends successfully!")


read_from_file()
print("welcome to my tranlate")

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        add_a_new_word()
    elif choice == 4:
        write_to_file()
        exit(0)
