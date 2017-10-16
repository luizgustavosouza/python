def preencheVetor(qualquercoisa):
    for i in range(len(qualquercoisa)):
        qualquercoisa[i] = int(input("Digita ai os valores do vetor:"))
    return None


def buscaElemento(x,y):
    for j in range(len(x)):
        if x[j] == y:
            print("O valor ", y, "foi encontrado na posição: ",j)
        else:
            print("O valor ", y, "não foi encontrado. Lamento otário!")
        return
tam = int(input("Digite ai o tamanho do vetor: "))
vetor = [None] * tam
preencheVetor(vetor)
print(vetor)
oprocurado = int(input("Qual que tu quer achar? Digita ae: "))
buscaElemento(vetor,oprocurado)



