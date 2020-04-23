import sys
import math

class  Shape:
    geometric_type= 'Generic Shape'

    def area(self): # This acts as a pplaceholder for the interface
        raise NotImplementedError
    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot (self, ratio, topleft):
        #Imagine some nice plotting logic here

        print(' Plotting at {} . ratio {}.'. format(topleft,ratio))

class Polygon( Shape, Plotter): #base class for polygons
    geometric_type= 'Polygon'

class RegularPolygon(Polygon): #Is- A Poliygon
    geometric_type= 'Regular Polygon'

    def __init__(self, side):
        self.side= side

class RegularHexagon(RegularPolygon):
    geometric_type= 'Regular Hexagon'

    def area (self):
        return 1.5*(3**.5*self.side**2)
    
class Square(RegularPolygon):
    geometric_type='Square'

    def area(self):
        return self.side**2

#############################################
# CRIAR EXTENSOES 

class Rectangle(Polygon) :
    geometric_type= 'Retangle'

    def __init__(self, side1, side2):
        self.side1= side1
        self.side2= side2

    def area(self):
        return self.side1 * self.side2

class Circle(Shape, Plotter):
    geometric_type= 'Circle'

class Arc(Circle):
    geometric_type= 'Arc'

    def __init__(self, radius, angle):
        self.radius = radius
        self.angle= angle #radianos

    def area(self):
        return (self.angle/2) * self.radius**2


##############################################
# AVALIAR MRO

square= Square(12)
print(square.__class__.__mro__)
rectangle= Rectangle(8,6)
print(rectangle.__class__.__mro__)
arc= Arc(2,math.pi)
print(arc.__class__.__mro__)

