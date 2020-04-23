import sys
from random import randint

def flight(passageiro, companhia, destino):
    """Defines flight parameters """
    print("--How can I help you?")
    print("--Hi, my name is", passageiro,". I want to buy a air ticket.")
    print("--What is your destiny, Sr.", passageiro, "?")
    print("--I have no idea. I am looking for a tourists places!")
    print("--On this case we have the options:")
    keys = destino.keys()

    for k in keys:
        print(k, ":" , destino[k])
     
    escolha1=randint(0,len(keys)-1)
    print("--I want to go to", destino[escolha1])
    
    print("--What the flight company?")
    escolha2= randint(0,len(companhia)-1)
    print("--",companhia[escolha2])


#Teste
destino={1:"Fortaleza", 2:"Sao Paulo",3: "Rio de Janeiro",4: "Salvador", 5:"Porto Alegre"}
companhia= ["Latam", "Gol", "Azul"]
passageiro= "Jose Victor"
flight(passageiro, companhia, destino)
