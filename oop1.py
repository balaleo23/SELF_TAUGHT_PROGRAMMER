class Square:
    square_list = []
    def __init__(self,numb):
        self.n = numb
        self.square_list.append(self.n)
        
sq1 = Square(10)    
sq2 = Square(15)
print(sq2.square_list)