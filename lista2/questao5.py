import sys

class Point:
    """ Point Class represents and manipulates the x,y coords """

    def __init__(self, x=0, y=0):
        """Creates a new point"""
        self.x= x
        self.y= y
    
    def reflect_x(self):
        """ Reflect the point in relation to x-axis"""
        return(self.x, - self.y)




##Teste
print(Point(3, 5).reflect_x())

