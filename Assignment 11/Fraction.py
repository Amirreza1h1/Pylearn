import math


class Fraction:
    def __init__(self, nume, deno):
        self.numenator = nume
        self.denominator = deno
        self.fix()
        self.simplize()

    def sum(self, n_2):
        sum_num = int(self.numenator*n_2.denominator +
                      n_2.numenator*self.denominator)
        sum_den = int(self.denominator*n_2.denominator)
        x = Fraction(sum_num, sum_den)
        return (x)

    def multiple(self, n_2):
        mul_num = int(self.numenator*n_2.numenator)
        mul_den = int(self.denominator*n_2.denominator)
        x = Fraction(mul_num, mul_den)
        return (x)

    def minus(self, n_2):
        min_num = int(self.numenator*n_2.denominator -
                      n_2.numenator*self.denominator)
        min_den = int(self.denominator*n_2.denominator)
        x = Fraction(min_num, min_den)
        return (x)

    def divide(self, n_2):
        div_num = int(self.numenator*n_2.denominator)
        div_den = int(self.denominator*n_2.numenator)
        x = Fraction(div_num, div_den)
        return (x)

    def simplize(self):
        gcd = int(math.gcd(self.numenator, self.denominator))
        self.numenator = int(self.numenator/gcd)
        self.denominator = int(self.denominator/gcd)

    def convert_to_number(self):
        result = self.numenator/self.denominator
        return (result)

    def fix(self):
        if self.denominator == 0:
            print("the denominator of a fraction can not be zero!!")

    def show(self):
        print(self.numenator, "/", self.denominator)


while True:
    print("Number 1:")
    n_1_num = int(input("the numenator: "))
    n_1_den = int(input("the denominator: "))
    n_1 = Fraction(n_1_num, n_1_den)
    n_1.show()

    print("Number 2:")
    n_2_num = int(input("the numenator: "))
    n_2_den = int(input("the denominator: "))
    n_2 = Fraction(n_2_num, n_2_den)
    n_2.show()

    sum = n_1.sum(n_2)
    mul = n_1.multiple(n_2)
    min = n_1.minus(n_2)
    div = n_1.divide(n_2)

    sum.show()
    mul.show()
    min.show()
    div.show()
    print(n_1.convert_to_number())
