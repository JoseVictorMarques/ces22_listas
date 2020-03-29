import sys

def sum_list( lista):
    """Sum all numbers of the list but not inclunding the first even number"""
    p_par= False
    soma=0
    for i in range(len(lista)):
        #Verificar se o elemento é um numero
        if type(lista[i]) == int or type(lista[i])== float:
            #Verificar se é o primeiro par
            if lista[i]%2==0 and p_par==False :
                p_par=True
            else :
                soma= soma+lista[i]
    return soma


# Casos de teste
lista1= [1,2,3,4,5,6]
print("O valor da lista1 eh ", sum_list(lista1))
lista2= [1,3,5]
print("O valor da lista2 eh ", sum_list(lista2))
lista3=[2]
print("O valor da lista3 eh ", sum_list(lista3))
lista4=[1.2, 1.5,2.2,3]
print("O valor da lista4 eh ", sum_list(lista4))
lista5=["arroz", 2, 4.2, 7]
print("O valor da lista5 eh ", sum_list(lista5))