import sys

#Imprimir a linha de cabeçalho
lista=["     "," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12"]
espaco="  "
nova_lista=espaco.join(lista)
print(nova_lista)
linha_sep= "  "+ ":" + "-" *50
print(linha_sep)


#Imprimir as linhas da tabela
vec_lista=[]
for i in range(1,13):
    if i<10:
        vec_lista.append(" ")
    vec_lista.append(str(i))
    vec_lista.append("  ")
    for j in range(1,13):
        #Atribuir os espaços
        if i*j <10:
            vec_lista.append("   ")
        elif i*j<100:
            vec_lista.append("  ")
        else:
            vec_lista.append(" ")
        vec_lista.append(str(j*i))
    if i<10:
        vec_lista[2:2]=[":"]
    else :
        vec_lista[1:1]=[":"]
    #Juntar as strings
    separador=""
    s=separador.join(vec_lista)
    print(s)
    vec_lista=[]


