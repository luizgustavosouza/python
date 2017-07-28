#Funçoes

#Funçao para ler valores do teclado e armazenar em um vetor
def ler(valores):
    for i in range(len(valores)):
        valores[i]=int(input("Digite logo a droga de um numero: "))

    return None

#Funçao para ordenar os valores do vetor(ordem crescente)
def ordenar(valores):
    valores.sort()

    return None

#Funçao para imprimir os valores
def escrever(valores):
    for i in valores:
        print(i, end=" ")
    print()
    return None



#A droga do Programa Principal
tam=3
numeros=[None]*tam
ler(numeros)
escrever(numeros)
ordenar(numeros)
escrever(numeros)