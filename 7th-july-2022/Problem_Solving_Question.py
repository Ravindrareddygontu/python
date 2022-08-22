'''1.Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.'''
class Shape:
    area = 0
   
    class Square:
        def __init__(self,length):
            self.length = length

        def Area(self):
           b = Shape()
           b.Area()
           
    def Area(self):
        print(self.area)
            
obj = Shape.Square(23)
obj.Area()
