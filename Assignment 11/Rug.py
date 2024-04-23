class Rug:
    def __init__(self, size):
        if size % 2 == 0:
            raise ValueError("Rug size must be an odd number.")
        self.size = size
        self.matrix = self.generate_rug()

    def show(self):
        for row in self.matrix:
            print(row)

    def generate_rug(self):
        n = self.size
        mid = n // 2
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = max(abs(mid - i), abs(mid - j))
        return matrix


# Example usage:
rug_size = int(input("Enter the size of the rug (odd number): "))
rug = Rug(rug_size)
rug.show()
