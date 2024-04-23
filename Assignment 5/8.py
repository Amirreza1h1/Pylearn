# status=True means "*" and status=False means "#"
def generate_text(b: int, status: bool):
    text = ""
    switch = None  # switch=True means "*" and switch=False means "#"
    for i in range(b):
        if not status and i == 0:  # start with #
            text += "#"
            switch = True
        elif status and i == 0:  # start with *
            text += "*"
            switch = False
        else:
            # if switch:
            #     text += "*"
            # else:
            #     text += "#"
            text += "*" if switch else "#"
            switch = not switch
    return text


def main():
    a = int(input("please enter rows: "))
    b = int(input("please enter columns: "))
    status = False
    for i in range(a):
        text = generate_text(b, status)
        print(text)
        status = not status


main()
