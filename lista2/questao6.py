import sys

class Point:
    """ Point Class represents and manipulates the x,y coords """
    
    def __init__(self,x=0,y=0):
        """ Creates a new point"""
        self.x=x
        self.y=y
    def slope_from_origin(self):
        """ Checks the slope from origin """
        return self.y/self.x
    


##Teste
print(Point(4,10).slope_from_origin())
#Se o valor da coordenada x for nulo haverá erro no retorno, tendo em vista
#que a divisão por zero não é permitida