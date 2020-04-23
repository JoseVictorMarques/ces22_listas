import sys

def cleanword(str):
    """ Clean the simbols, except letters"""
    xstr= list(str)
    mylist= []
    for x in xstr:
        if x.isalpha() == True:
            mylist.append(x)
    separador= ""
    s= separador.join(mylist)
    return s

def has_dashdash(str):
    """ Checks if there are two dashs"""
    achou1= False
    xstr= list(str)
    for x in xstr:
        if achou1 == False:
            if x == '-':
                achou1= True
        else:
            if x == '-':
                return True
            else:
                achou1= False

    return False

def extract_words(str):
    """ Extract only words, transform to lower case if necessary """
    str= str.lower()
    wds= str.split()
    mylist=[]
    print(wds)
    for x in wds:
        aux= x.split()
        for y in aux:
            if y.isalpha() == True:
                mylist.append(y)
            else:
                lista= list(y)
                for z in lista:
                    if z.isalpha() == False:
                        lista.remove(z)
                separador=""
                new_str = separador.join(lista)
                if new_str.isalpha() == False:
                    lista_aux= list(new_str)
                    for z in lista_aux:
                        if z.isalpha() == False:
                            lista_aux.remove(z)
                    new_str=separador.join(lista_aux)
                    #Verificar se a string nao é nula
                    if new_str.isalpha()==True:
                        mylist.append(new_str)
                else:
                    mylist.append(new_str)

    return mylist


def word_count(str, lista):
    """Count how many words have on the text"""
    contador = 0
    for x in lista:
        if x == str:
            contador= contador+1
    
    return contador


def wordset(lista):
    """ Checks what words were used """
    my_list=[]
    for x in lista:
        achou = False
        for y in my_list:
            if x == y:
                achou = True
        if achou == False:
            my_list.append(x)
    
    my_list.sort()
    return my_list
            

def longestword(lista):
    """Return the longest word of the list"""
    if lista != []:
        max= lista[0]
        for x in lista:
            if len(x)>len(max):
                max=x
    
        return len(max)
    else:
        return 0


