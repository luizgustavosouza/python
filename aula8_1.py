#Subprogramas
def listaN(elementos,qtd,min,max):
    from random import randint #importando módulo para gerar valores aleatórios
    for i in range(qtd):
        elementos.append(randint(min,max)) #gerando uma lista com valores aleatórios usando a função randint e append
    return None

def ordenaL(elementos):
    ordenada = elementos.sort() #ordenando a lista em ordem crescente
    return None

#Removendo os elementos repetidos
def repetidosL(elementos):
    i = 0
    while i<len(elementos):
        if elementos.count(elementos[i])==1: #Se o elemento só aparecer uma vez contador é incrementado passando para o proximo elemento da lista
            i+=1
        else:
            elementos.remove(elementos[i]) #Se o elemento aparecer mais de uma vez a primeira ocorrencia da esq para a dir do elemento é removida
    return None

#Programa Principal
#Obtendo os valores
qtd=int(input('Informe a quantidade de elementos na lista: '))
mini=int(input('Informe o menor valor da faixa: '))
maxi=int(input('Informe o maior valor da faixa: '))
elementos=[] #criando uma lista vazia

listaN(elementos,qtd,mini,maxi) #chamada para a função/módulo/subprograma

print(elementos) #imprimindo a lista

print("Ordenando a lista...")
ordenaL(elementos) #chamada para a função/módulo/subprograma
print(elementos)

print("Removendo elementos repetidos...")
repetidosL(elementos) #chamada para a função/módulo/subprograma
print(elementos)