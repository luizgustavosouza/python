#Subprogramas Lisp Like
def car(dados):
    print(dados[0])

def cdr(dados):
    print(dados[1:len(dados)])

def cons(item,dados): #é a operação construtora que retorna uma lista que contém o item como primeiro elemento, seguido pela lista dados.
    print([item]+dados)


def soma(dados):
    if dados == []:
        return 0
    else:
        return car(dados) + soma(cdr(dados))

#Programa Princiapal

elementos=[1,2,3,4,5,6,7,8,9]
