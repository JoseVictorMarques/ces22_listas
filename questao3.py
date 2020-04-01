import sys

def  sum_to(n):
    "Sum to all integers numbers up to n (including n)"
    sum=0
    for i in range(n+1):
        sum= sum+ i
    return sum


def test( passou):
    "Print the result of the test"
    linenum= sys._getframe(1).f_lineno
    if passou :
        msg= "Test at line {0} ok". format(linenum)
    else:
        msg= "Test at line {0} Failed". format(linenum)
    print(msg)

# Caso de teste
test(sum_to(10) == 55)