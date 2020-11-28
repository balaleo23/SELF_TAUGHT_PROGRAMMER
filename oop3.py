def same(obj1, obj2):
    return obj1 is obj2
    

class Square:
    def __init__(self):
        pass

s1 = Square()
s2 = Square()



print(same(s1,s2))