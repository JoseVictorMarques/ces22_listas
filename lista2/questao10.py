import sys

#Definir a função tags
def tags(nome_aluno):
    def tags_decorador(func):
        def new_function(p1, p2, exame):
            return "<" + nome_aluno + ">" + func(p1,p2,exame)
        return new_function
    return tags_decorador

@tags("Jose Victor")
def media(p1,p2,exame):
    media= (p1+p2+exame)/3
    return " media :  %g " %media


##Teste
print(media(7,8,9))
print(media(7.5,8.6,6.9))