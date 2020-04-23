import sys
from random import *
import abc 

class Veiculo(object):
    """ Describes information of a vehicle"""
    __metaclass__=abc.ABCMeta

    def __init__(self):
        """Initialize some parameters"""
        self.valor = 0

    #Metodo abstrato
    @abc.abstractmethod
    def get_valor(self,preco):
        """Method that should do something"""
        pass

    #Definir a subclasse que estende a principal
class Carro(Veiculo):
    """ Describes information of a car"""
    def get_valor(self,preco):
        self.valor= self.valor + preco
        return self.valor



#############################################################

class Pessoa:
    """Describes information of a person"""
    def __init__(self, nome, idade ): 
        self.nome= nome
        self.idade= idade

    #Metodo de classe
    @classmethod
    def get_idade(cls,nome):
        """Chooses a random age to the person"""
        idade= 2020 - randint(1960,2002)
        return cls(nome,idade)

    #Metodo estático
    @staticmethod
    def get_ID():
        """Chooses a random number to represent the CPF"""
        return randint(100000,999999)




##TESTES
#Abstrato
Ferrari= Carro()
print(Ferrari.get_valor(500000))
#Classe
p= Pessoa.get_idade("Joao")
print(p.idade)
#Estático
print(p.get_ID())
