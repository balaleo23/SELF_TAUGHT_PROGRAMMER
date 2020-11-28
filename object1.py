

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
    def calculate_perimeter(self):
        return 2*(self.width+self.length)


class Square:
    def __init__(self,side):
        self.side = side

    def calculate_perimeter(self):
        return self.side*4    


rec = Rectangle(10,20)
print(rec.length)
print(rec.calculate_perimeter())

sq1 = Square(2)
print(sq1.side)
print(sq1.calculate_perimeter())
















# Rectangle.calculate_perimeter()
# print(Rectangle.calculate_perimeter(self))

# class Square:
#     def _init_(self,side)
#         self.side = side
    
        
    
#     def calculate_perimeter():
#         return 4*side