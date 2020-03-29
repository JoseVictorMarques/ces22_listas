import sys

def is_prime(n):
    "Check  if the number n is prime or not"
    for i in range(2,n):
        #Verificar se eh 2
        if n==2:
         return True
        #Verificar se há algum divisor nesse intervalo
        elif n % i ==0:
            return False
    return True

def test( passou):
    "Print the result of the test"
    linenum= sys._getframe(1).f_lineno
    if passou :
        msg= "Test at line {0} ok". format(linenum)
    else:
        msg= "Test at line {0} Failed". format(linenum)
    print(msg)

#Casos de Teste
test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))
test(is_prime(19981013))
test(is_prime(19881112))