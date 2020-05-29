# Exemplo do uso de decoradores na Pizza
# Os preços são meramentes a efeito de exemplo

class PizzaComponent:

    def __init__(self):
        self.cost=0.0
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.cost
    
class Bandeja(PizzaComponent):
    cost=0.0

class Decorator(PizzaComponent):
    def __init__(self,pizzaComponent):
        self.component =  pizzaComponent
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)

class Tomate(Decorator):
    cost= 0.80
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Cebola( Decorator):
    cost = 1.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Mussarela( Decorator):
    cost = 3.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Presunto( Decorator):
    cost = 4.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Ovo( Decorator):
    cost = 0.30
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


#Exemplos
mussarela= Mussarela(Tomate(Bandeja()))
print( mussarela.getDescription()+ ": $ " + str(mussarela.getTotalCost()))

portuguesa= Presunto(Ovo(Mussarela(Tomate(Bandeja()))))
print( portuguesa.getDescription()+ ": $ " + str(portuguesa.getTotalCost()))
