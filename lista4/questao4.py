from __future__ import annotations
from abc import ABC, abstractmethod
import random
import tkinter as tk

class Solicitacao(ABC):
    """
    Definir a classe para a solicitação (Command)
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class VerificaSaldo(Solicitacao):
    """
    Definir a classe para verificar o saldo (Command2)
    """

    def __init__(self ) -> None:
        self.saldo= random.randrange(1000,10000)

    def execute(self) -> None:
        print(f"\nO saldo " f" é dado por " f"{self.saldo}")

class VerificaExtrato(Solicitacao):
    """
    Definir a classe para verificar o extrato (Command2)
    """

    def __init__(self) -> None:

        self.extrato= random.randrange(1000,10000)

    def execute(self) -> None:
        print(f"\nO extrato " f" é dado por " f"{self.extrato}")

class RealizaTransferencia(Solicitacao):
    """
    Definir a classe para realizar transferencias (Command1)
    """

    def __init__(self, receiver: Receiver, valor: float) -> None:
        """
        Definir a função de inicialização
        """

        self.receiver = receiver
        self.valor = valor

    def execute(self) -> None:
        """
        Realizar a solicitacao de transferencia
        """

        print("Realizar uma transferencia ao Receiver", end="")
        self.receiver.do_something(self.valor)
    


class Receiver:
    """
    Define a classe do receptor (Receiver)
    """

    def do_something(self, valor: float) -> None:
        print(f"\nReceiver recebe {valor} ", end="")


class Invoker:
    """
    Define a classe para requisitar os comandos
    """
    invocacao = None
   

    def set_invocacao(self, command: Solicitacao):
        self.invocacao = command
        self.invocacao.execute()


#Definir variaveis globais
invoker = Invoker()
receiver = Receiver()

class Aplicacao_Cliente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.criar_solicitacao()

    def criar_solicitacao(self):
        self.solicitacao = tk.Button(self)
        self.solicitacao["text"] = "Solicite à aplicação\n (Clique aqui)"
        self.solicitacao["command"] = self.verifica_solicitacoes
        self.solicitacao.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def verifica_solicitacoes(self):
        invoker.set_invocacao(VerificaSaldo())
        invoker.set_invocacao(RealizaTransferencia(receiver, random.randrange(100,1000) ))

root = tk.Tk()
app = Aplicacao_Cliente(master=root)
app.mainloop()





