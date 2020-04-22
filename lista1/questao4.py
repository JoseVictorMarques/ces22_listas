import sys

def sum_list( lista):
    """Sum all numbers of the list but not inclunding the first even number"""
    soma=0
    for i in range(len(lista)):
        #Verificar se o elemento é um numero
        if type(lista[i]) == int or type(lista[i])== float:
            #Verificar se é o primeiro par
            if lista[i]%2==0 :
                break
            else :
                soma= soma+lista[i]
    return soma

def test( passou):
    "Print the result of the test"
    linenum= sys._getframe(1).f_lineno
    if passou :
        msg= "Test at line {0} ok". format(linenum)
    else:
        msg= "Test at line {0} Failed". format(linenum)
    print(msg)

# Casos de teste
test(sum_list([1,2,3,4,5,6])==1)
test( sum_list([1,3,5]) == 9)
test( sum_list([2]) == 0)
test(sum_list([1.2, 1.5,2.2,3])== 7.9)
test( sum_list(["arroz", 2, 4.2, 7]) ==0 )