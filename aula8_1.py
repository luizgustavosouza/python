#Funções

def listaN(elementos,qtd,min,max):
    #importando módulo para gerar valores aleatórios
    from random import randint
    for i in range(qtd):
        elementos.append(randint(min,max))
    return None

# Programa Principal

#Obtendo valores
qtdNumeros = int(input("Qauantos valores devem conter na lista ? "))
minimo = int(input("Informe o menor valor da faixa: "))
maximo = int(input("Informe o maior valor da faixa: "))

numeros = []

listaN(numeros,qtdNumeros,minimo,maximo)
print(numeros)