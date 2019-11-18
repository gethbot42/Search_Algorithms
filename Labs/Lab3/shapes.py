#!/usr/bin/python3 -tt

# Todd Qualiano
# Lab 3
# CS 520
# Fall 2018

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY

# This line says 'Square inherits from 'Shape'
class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        # Must make an explicit call to the __init__ method of 'Shape'
        Shape.__init__(self, x, y)
        self.side = side

    def area(self):
        return self.side * self.side

# This line says 'Circle' inherits from 'Shape'
class Circle(Shape):
    allCircles = []
    pi = 3.14159
    def __init__(self, r=1, x=0, y=0):
        # Must make an explicit call to the __init__ method of 'Shape'
        Shape.__init__(self, x, y)
        self.radius = r # original code had self.radius = r
        self.__class__.allCircles.append(self)

    def area(self):
        return self.radius * self.radius * self.pi
        
    def area_all_circles():
        area_list = []
        for circ in Circle.allCircles:
            area_list.append(circ.area())
        return area_list

# Adding the Rectangle Class
class Rectangle(Shape):
    def __init__(self, side_a=1, side_b=2, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b
