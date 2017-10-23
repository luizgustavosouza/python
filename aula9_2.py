#Escrevendo em arquivos de texto

dados=open("escreva.txt", "w")

dados.write("Glorioso Professor...\nIsso é realmente necessário?!!?\nSeu grandioso babaca!!! ")

dados.close()

#Lendo o maldito arquivo que acabei de escrever

dadosLer=open("escreva.txt", "r")
linha=dadosLer.readline()

while linha !="":
    print(linha,end="")
    linha=dadosLer.readline()

dadosLer.close()