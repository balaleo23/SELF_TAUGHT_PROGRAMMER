class Shape(): 
    def what_am_i(self): 
        print("I am a shape.") 


class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
    def calculate_perimeter(self):
        return 2*(self.width+self.length)


class Square(Shape):
    def __init__(self,side):
        self.side = side

    def calculate_perimeter(self):
        return self.side*4    