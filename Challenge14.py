class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self)
        print("Created a square!")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)
        
    def is_same(self, another):
        if self == another:
            return True
        else:
            return False

squ1 = Square(10)
print(squ1)
squ2 = Square(20)
print(squ1.is_same(squ2))
squ3 = squ1
print(squ1.is_same(squ3))
