tam = int(input())#recebe o tamanho do vetor
qualquercoisa = [None]*tam
while 1>0:
    for i in range(len(qualquercoisa)):
        qualquercoisa[i] = int(input())
    oprocurado = int(input("Qual que tu quer achar? Digita ae: "))
    for j in range(len(qualquercoisa)):
        if qualquercoisa[j] == oprocurado:
            print("O valor ", oprocurado, "foi encontrado na posição: ",j)
            exit()
    else:
        print("O valor ", oprocurado, "não foi encontrado. Lamento otário!")