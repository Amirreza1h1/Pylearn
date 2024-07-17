def pascal(a: int):
    for i in range(1, a+1):
        # first element is always 1
        C = 1
        for j in range(1, i+1):

            # first value in a line is always 1
            print(C, sep='', end=' ')

            # using Binomial Coefficient
            C = C * (i - j) // j
        print()


a = int(input("pascal's row: "))
pascal(a)
