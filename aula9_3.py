#Escrevendo em um arquivo divertido

nomeArq=input("Qual o nome do arquivo que deseja criar: ")
qtdLinhas=int(input("Qual a quantidade de linhas: "))
dados=open(nomeArq, "w")

for i in range(qtdLinhas):
    nova=input()
    dados.write(nova + "\n")
dados.close()

#Lendo o arquivo
print(end="")
print("Lendo o arquivo B): ")

dadosLer=open(nomeArq)
linha=dadosLer.readline()

while linha !="":
    print(linha, end="")
    linha=dadosLer.readline()

dadosLer.close()