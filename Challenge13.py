class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)


class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4
    
    def change_size(self, l):
        self.len += l

class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r

class Rider:
    def __init__(self, n):
        self.name = n

rec1 = Rectangle(12, 24)
rec1.what_am_i()
squ1 = Square(36)
squ1.what_am_i()

rider1 = Rider("Cal")
horse1 = Horse("Cara", rider1.name)

print(horse1.rider)


    
