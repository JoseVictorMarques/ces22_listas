import sys

def count_words ( lista) :
    "Count how many words appear in the list"
    contador= 0
    for i in range(len(lista)):
        #Verificar se o elemento é do tipo string
        if type(lista[i]) == str:
            #Verificar se ocorre repetição
            repete = False
            for j in range(0,i):
                if lista[j]==lista[i]:
                    repete= True
                    break
            #Contar as palavras nao repetidas
            if repete == False:
                contador= contador +1
            #Verificar se a palavra é sam
            if lista[i]== "sam":
                break
    return contador


def test( passou):
    "Print the result of the test"
    linenum= sys._getframe(1).f_lineno
    if passou :
        msg= "Test at line {0} ok". format(linenum)
    else:
        msg= "Test at line {0} Failed". format(linenum)
    print(msg)


#Casos de testes

test(count_words(["cr7","messi", "neymar"]) == 3)
test(count_words(["sam", "edu","sam"]) == 1)
test(count_words(["sam"]) == 1)
test(count_words(["eu", "tu", "sam"]) == 3)
test(count_words(["arroz", 2, 4.2,"sam",10]) == 2)
test(count_words(["arroz", "sam","sam",10]) == 2)
test(count_words(["cr7","messi", "neymar","messi"]) == 3)
