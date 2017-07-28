#Programa Principal

TAM=10
numeros=[0]*TAM

for i in range(len(numeros)):
    n=int(input("insira um valor: "))
    numeros[i]=n
print(numeros)
print("O vetor ordenado fica assim: ", sorted(numeros))