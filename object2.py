class Square:
    def __init__(self,s1):
        self.s1 = s1

    def change_size(self,num):
        self.s1 += num
        return self.s1

sq1 =Square(25)
print(sq1.s1)


print(sq1.change_size(10))
