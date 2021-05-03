import math

class Apple:
    def __init__(self, w, c, s, d):
        self.weight = w
        self.color = c
        self.size = s
        self.deli = d
        print("Created an apple!")

class Circle:
    def __init__(self, r):
        self.range = r
        print("Created a circle!")

    def area(self):
        return self.range ** 2 * math.pi

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
        print("Created a triangle!")

    def area(self):
        return self.bottom * self.height / 2

class Hexagon:
    def __init__(self, l):
        self.len = l
        print("Created a hexagon!")

    def calculate_perimeter(self):
        return self.len * 6

ap1 = Apple(200, "red", "norm", "good")
print(ap1.weight)
print(ap1.color)
print(ap1.size)
print(ap1.deli)

cir1 = Circle(5)
print(round(cir1.area(), 2))

tri1 = Triangle(10, 20)
print(tri1.area())

hex1 = Hexagon(10)
print(hex1.calculate_perimeter())



