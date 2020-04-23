import sys

class Point:
    """ Point Class represents and manipulates the x,y coords """
    
    def __init__(self,x=0,y=0):
        """ Creates a new point"""
        self.x=x
        self.y=y
    def get_line_to(self, other):
        """ Returns the line coefs """
        a= (self.y-other.y)/(self.x - other.x)
        b= ((other.x *self.y) -(self.x*other.y))/(other.x- self.x)
        return (a,b)
    

#Teste
print(Point(4,11).get_line_to(Point(6,15)))
    