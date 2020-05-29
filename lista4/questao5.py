from __future__ import annotations
from abc import ABC, abstractmethod


class Document(ABC):
    """
    Definir a classe para o Context
    """

    _state = None
    """
    Referência para o estado atual do contexto
    """

    def __init__(self, state: State) -> None:
        self.change_state(state)

    def change_state(self, state: State):
        """
        Mudar o estado do objeto
        """

        print(f"Documento: Mudança de estado para {type(state).__name__}")
        self._state = state
        self._state.document = self

    """
    O comportamento do Documento depende do estado em que ele se encontra
    """

    def request1(self):
        self._state.doThis()

    def request2(self):
        self._state.doThat()


class State(ABC):
    """
    Definir a classe dos estados
    """

    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, document: Document) -> None:
        self._document = document

    @abstractmethod
    def doThis(self) -> None:
        pass

    @abstractmethod
    def doThat(self) -> None:
        pass


"""
Acionar os Concrect States para especificar o estado
"""

class Draft(State):
    """ Definir Concrect State """
    def doThis(self) -> None:
        print("Draft -> Published by user.")
        self.document.change_state(Moderation())

    def doThat(self) -> None:
        print("Draft -> Published by admin.")
        self.document.change_state(Published())


class Moderation(State):
    """ Definir Concrect State """
    def doThis(self) -> None:
        print("Moderation-> Approved by admin")
        self.document.change_state(Published())

    def doThat(self) -> None:
        print("Moderation-> Review failed")
        self.document.change_state(Draft())

class Published(State):
    """ Definir Concrect State """
    def doThis(self) -> None:
        print("Published-> Published expired")
        self.document.change_state(Draft())

    def doThat(self) -> None:
        print("Published ")

        

if __name__ == "__main__":
    #Solicitação do cliente

    document = Document(Draft())
    document.request1()
    document.request1()