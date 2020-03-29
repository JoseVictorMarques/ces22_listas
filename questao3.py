import sys

def  sum_to(n):
    "Sum to all integers numbers up to n (including n)"
    sum=0
    for i in range(n+1):
        sum= sum+ i
    return sum


#TEST
#valor= sum_to(10)
#print(valor)