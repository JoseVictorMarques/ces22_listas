import sys
import time
import random

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    deltay = abs(y1 - y0)        # Calc the absolute y distance
    deltax = abs(x1 - x0)        # CXalc the absolute x distance
    return deltax == deltay          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
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


def checks_time(value):
    """ Checks the biggest vector what runs on 'tempo' s"""
    #Inicializar variaveis
    vet= []
    found_n = False
    n= 1000
    #Enquanto não achar n
    while(found_n == False):
        #Criar um vetor crescente de tamanho n
        for i in range(0,n):
            vet.append(i)
        #Verificar o tempo de teste
        t0= time.time()
        test(has_clashes(vet))
        t1= time.time()
        #Se o tempo superar o desejado termina o loop e retorna n
        if((t1-t0)>=value):
            found_n= True
            #Retornar o valor inferior
            return n-1
        #Incrementar n uma unidade
        else:
            n= n+1

    return n-1


## Testes disponiblizados pelo livro texto
test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two

## Tabuleiro 4 x4
test(has_clashes([0,1,2,3]))             # Try small 4x4 board
#Teste tempo 
#t0= time.time()
test(not has_clashes([2,0,3,1]))         # Solution to 4x4 
#t1= time.time()
#print(t1-t0)

## Tabuleiro 12 x 12
vet12= [0,1,2,3,4,5,6,7,8,9,10,11]
test(has_clashes([0,1,2,3,4,5,6,7,8,9,10,11]))
#Gerar ordem aleatoria
random.shuffle(vet12)
#t0= time.time()
test(has_clashes(vet12))
#t1= time.time()
#print(t1-t0)

#Tabuleiro 16 x 16
vet16= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
test(has_clashes([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#Gerar ordem aleatoria
random.shuffle(vet16)
#t0= time.time()
test(has_clashes(vet16))
#t1= time.time()
#print(t1-t0)

#Vericar o maior vetor que é executado em menos de 1 min
#Esse tempo eh da ordem de 10^4
#Esse é um teste lento portanto recomenda-se verificar apenas a soluçção pdf
#print(checks_time(60))


