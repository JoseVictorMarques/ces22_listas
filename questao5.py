import sys

def count_words ( lista) :
    "Count how many words appear in the list"
    p_sam= False
    contador= 0
    for i in range(len(lista)):
        #Verificar se o elemento é do tipo string
        if type(lista[i]) == str:
            #Verificar se a palavra é sam
            if lista[i]== "sam" and p_sam== False:
                p_sam = True
            else :
                contador= contador +1
    return contador



#Casos de testes
lista1= ["cr7","messi", "neymar"]
print("O valor da lista1 eh ", count_words(lista1))
lista2= ["sam", "edu","sam"]
print("O valor da lista2 eh ", count_words(lista2))
lista3=["sam"]
print("O valor da lista3 eh ", count_words(lista3))
lista4=["eu", "tu", "sam"]
print("O valor da lista4 eh ", count_words(lista4))
lista5=["arroz", 2, 4.2,"sam",10]
print("O valor da lista5 eh ", count_words(lista5))
