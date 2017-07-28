#Funçao

def ler(valores):
    for i in range(len(valores)):
        valores[i]=int(input("Digite logo a droga de um numero: "))
    return None

def ordena(valores):
    valores.sort()
    return None

def escreve(valores):
    for i in valores:
        print(i, end=" ")
    print()


def maiornumero(valores):
    for i in valores:
        maior=max(valores)
    print(maior)

# Programa Principal

tam=int(input("Digite o tamanho do vetor: "))
numeros=[None]*tam
ler(numeros)
escreve(numeros)
ordena(numeros)
escreve(numeros)
maiornumero(numeros)
