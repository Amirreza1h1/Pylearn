class Complex_number:
    def __init__(self, real, imagine):
        self.real = real
        self.imaginary = imagine
        # self.show()

    def sum(self, n_2):
        sum_real = self.real+n_2.real
        sum_img = self.imaginary+n_2.imaginary
        x = Complex_number(sum_real, sum_img)
        return (x)

    def minus(self, n_2):
        min_real = self.real-n_2.real
        min_img = self.imaginary-n_2.imaginary
        x = Complex_number(min_real, min_img)
        return (x)

    def multiple(self, n_2):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        mul_real = (self.real*n_2.real)-(self.imaginary*n_2.imaginary)
        mul_img = (self.real*n_2.imaginary)+(self.imaginary*n_2.real)
        x = Complex_number(mul_real, mul_img)
        return (x)

    def show(self):
        if self.imaginary > 0:
            print(self.real, "+", self.imaginary, "i")
        elif self.imaginary < 0:
            print(self.real, self.imaginary, "i")
        else:
            print(self.real)


# Create two complex numbers
c1 = Complex_number(3, 4)  # 3 + 4i
c2 = Complex_number(2, -5)  # 2 - 5i

# Test addition
sum_result = c1.sum(c2)
print("Sum:", end=" ")
sum_result.show()  # Expected output: 5 - 1i

# Test subtraction
minus_result = c1.minus(c2)
print("Difference:", end=" ")
minus_result.show()  # Expected output: 1 + 9i

# Test multiplication
mul_result = c1.multiple(c2)
print("Product:", end=" ")
mul_result.show()  # Expected output: 26 - 7i
