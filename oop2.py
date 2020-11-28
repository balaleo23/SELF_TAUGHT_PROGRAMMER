class Square:
    def __init__(self, s1):
        self.s1 = s1
        
    def calculate_perimeter(self):
        return self.s1 * 4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)



sq2 = Square(5)
print(sq2)