#Funções Listas Lisp Like

def listaN(elementos,qtd,min,max):
    from random import randint #importando módulo para gerar valores aleatórios
    for i in range(qtd):
        elementos.append(randint(min,max)) #gerando uma lista com valores aleatórios usando a função randint e append
    return None

def car(dados): #é a operação seletora que retorna o primeiro elemento de uma lista dados;
    print(dados[0])

def cdr(dados): #é a operação seletora que retorna o resto da lista dados, isto é, retorna uma lista com todos os elementos da lista dados, exceto pelo primeiro;
    print (dados[1:len(dados)])

def cons(item,dados): #é a operação construtora que retorna uma lista que contém o item como primeiro elemento, seguido pela lista dados.
    print([item]+dados)


#Programa Principal
elementos = []
qtd=int(input('Informe a quantidade de elementos na lista: '))
mini=int(input('Informe o menor valor da faixa: '))
maxi=int(input('Informe o maior valor da faixa: '))
inception = int(input('Informe o novo valor  ser inserido no inicio da lista: '))
listaN(elementos,qtd,mini,maxi)

print("Lista completa: ", elementos)
print("Primeiro elemento:")
car(elementos)
print("Excluindo o Primeiro elemento:")
cdr(elementos)
print("Inserindo o elemento informado:")
cons(inception,elementos)