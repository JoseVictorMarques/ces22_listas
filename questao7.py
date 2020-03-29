import sys

def sum_of_squares(xs):
    "Return the sum of the squares of list's elements"
    soma=0
    for i in range(len(xs)):
        #Verificar o tipo de dado é valido
        if type(xs[i])==int or type(xs[i])==float:
            soma= soma+ xs[i]**2
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
test(sum_of_squares([2,3,4])==29)
test(sum_of_squares([])==0)
test(sum_of_squares([2,-3,4])==29)
test(sum_of_squares([2,"gil",4.5])==24.25)
test(sum_of_squares(["ed","sand"])==0)