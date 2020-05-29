from __future__ import annotations
from abc import ABC, abstractmethod

class Veiculo:
    """ Define a classe abstrata """

    def __init__(self, motorizacao):
        self.motorizacao= motorizacao

    def imprimir(self) -> str:
        return (f"Veiculo: classe base\n"
                f"{self.motorizacao.definir_motorizacao()}")

class Automovel(Veiculo):
    """ Extende a classe abstrata"""

    def imprimir(self) -> str:
        return (f"Automovel: classe extendida\n"
                f"{self.motorizacao.definir_motorizacao()}")

class Caminhao(Veiculo):
    """ Extende a classe abstrata"""

    def imprimir(self) -> str:
        return (f"Caminhao: classe extendida\n"
                f"{self.motorizacao.definir_motorizacao()}")

class Motorizacao(ABC):
    """ Define a classe implementação"""

    @abstractmethod
    def definir_motorizacao(self) -> str:
        pass

class Eletrica(Motorizacao):
    """ Define uma implementação concreta """

    def definir_motorizacao(self) -> str:
        return "Motorização elétrica: implementação concreta"

class Hibrida(Motorizacao):
    """ Define uma implementação concreta """

    def definir_motorizacao(self) -> str:
        return "Motorização híbrida: implementação concreta"


class Combustao(Motorizacao):
    """ Define uma implementação concreta """

    def definir_motorizacao(self) -> str:
        return "Motorização de combustão: implementação concreta"


def cliente(abstraction: Veiculo) -> None:
    """ Define o cliente """

    print(abstraction.imprimir(), end="")


if __name__ == "__main__":

    motorizacao = Eletrica()
    cliente (Veiculo(motorizacao))
    print("\n")

    motorizacao = Hibrida()
    cliente (Caminhao(motorizacao))
    print("\n")

    motorizacao = Combustao()
    cliente (Automovel(motorizacao))
    print("\n")