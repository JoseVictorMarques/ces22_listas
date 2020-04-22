import sys

def is_palindrome(word):
    "Check if the word is palindrome or not"
    l= list(word)
    # Usar lista auxiliar
    aux=l[:]
    # Inverter
    aux.reverse()
    #Veriicar
    if aux == l:
        return True
    return False
    


def test( passou):
    "Print the result of the test"
    linenum= sys._getframe(1).f_lineno
    if passou :
        msg= "Test at line {0} ok". format(linenum)
    else:
        msg= "Test at line {0} Failed". format(linenum)
    print(msg)

# Casos de teste
test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))