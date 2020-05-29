from __future__ import annotations
from abc import ABC, abstractmethod

class Motorizacao(ABC):
    """ Definir a classe Creator """

    @abstractmethod
    def metodo_fabrica1(self):
        """Definir metodo de fabrica para automovel"""
        pass
    
    @abstractmethod
    def metodo_fabrica2(self):
        """Definir metodo de fabrica para caminhao"""
        pass

    def operacao_adicional(self, option: str)->str:
        """ Realizar operacao"""
        if option == 'Automovel':
            veiculo = self.metodo_fabrica1()
        else:
            veiculo = self.metodo_fabrica2()
        
        result = f"Motorização: Creator.  Essa classe define motorização {veiculo.imprimir()}"
        return result

class Eletrica(Motorizacao):
    """ Definir classe para um ConcrectCreator """

    def metodo_fabrica1(self) ->Automovel :
        return Automovel()
    def metodo_fabrica2(self) ->Caminhao :
        return Caminhao()

class Hibrida(Motorizacao):
    """ Definir classe para um ConcrectCreator """

    def metodo_fabrica1(self) ->Automovel :
        return Automovel()
    def metodo_fabrica2(self) ->Caminhao :
        return Caminhao()


class Combustao(Motorizacao):
    """ Definir classe para um ConcrectCreator """

    def metodo_fabrica1(self) ->Automovel :
        return Automovel()
    def metodo_fabrica2(self) ->Caminhao :
        return Caminhao()


class Veiculo(ABC):
    """ Definir classe Product """
    @abstractmethod
    def imprimir(self) -> str:
        pass

class Caminhao(Veiculo):
    """ Definir classe para um ConcrectProduct"""
    def imprimir(self) -> str:
        return "Caminhao: ConcrectProduct."

class Automovel(Veiculo):
    """ Definir classe para um ConcrectProduct"""
    def imprimir(self) -> str:
        return "Automovel: ConcrectProduct."

def cliente(creator: Motorizacao, option:str) -> None:
    """ Definir cliente para interagir com o Creator"""

    print(f"Solcilitação do cliente.\n"
          f"{creator.operacao_adicional(option)}", end="")


if __name__ == "__main__":
    
    print("\n")
    print("Usando a Motorização Eletrica")
    cliente(Eletrica(),'Automovel')
    print("\n")

    print("Usando a Motorização de Combustao")
    cliente(Combustao(),'Caminhao')