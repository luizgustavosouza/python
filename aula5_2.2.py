#Subprogramas

def ler(valores):
    for i in range(len(valores)):
        valores[i] = int(input("insira um valor: "))
    return None

def ordenar(valores):
    valores.sort()
    return None

def escrever(valores):
    for i in valores:
        print(i,end=" ")
    print()
    return None

#Programa Principal

TAM=10
numeros=[0]*TAM

ler(numeros)
ordenar(numeros)
escrever(numeros)



