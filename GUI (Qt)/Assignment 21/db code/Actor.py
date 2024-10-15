class Actor:
    def __init__(self, n, a, i, h):
        self.name = n
        self.age = a
        self.nationality = i
        self.height = h

    def add(self):
        n=input("please give me the name of actor/actress: ")
        a=input("please give me the age of actor/actress: ")
        i=input("please give me the nationality of actor/actress: ")
        h=input("please give me the height of actor/actress: ")
        self(n,a,i,h)
        return self