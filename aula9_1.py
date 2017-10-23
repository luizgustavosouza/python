#Arquivos
#dados = open("exemplo.txt")
#linha = dados.readline()
#print(linha, end="")
#dados.close()

#Lendo um arquivo dinamicamente
nomeArq=input("Digite o nome do arquivo que deseja visualizar: ")
dados=open(nomeArq, "r")
linha=dados.readline()

while linha !="":
    print(linha, end="")
    linha=dados.readline()

dados.close()


outroArq=input("Digite o nome de outro arquivo: ")
outroDado=open(outroArq, "r")
outraLinha=outroDado.readline()

for i in outroDado:
    print(outraLinha, end="")
outroDado.close()

print(end="")

maisumArq=input("Digite o nome de mais um maldito arquivo: ")
maisumDado=open(maisumArq, "r")
maisumaLinha=maisumDado.readlines()

for i in maisumaLinha:
    print(maisumaLinha, end="")
maisumDado.close()


