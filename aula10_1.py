qtdInfraDC=int(input("Digite a quantidade de pessoas no time de Infra DataCenter: "))
qtdInfraDBA=int(input("Digite a quantidade de pessoas no time de Infra DBA: "))
qtdInfraNTW=int(input("Digite a quantidade de pessoas no time de Infra Network: "))
qtdInfraMGM=int(input("Digite a quantidade de pessoas no time de Infra Management: "))

infraDC=set()
infraDBA=set()
infraNTW=set()
infraMGM=set()

gestor=input("Digite o nome do Gestor")

for i in range(qtdInfraDC):
    nome=input("Digite o nome do analista de data center: ")
    infraDC.add(nome)


for j in range(qtdInfraDBA):
    nome=input("Digite o nome do analista de banco de dados: ")
    infraDBA.add(nome)


for k in range(qtdInfraNTW):
    nome=input("Digite o nome do analista de Redes: ")
    infraNTW.add(nome)

for l in range(qtdInfraMGM):
    nome=input("Digite o nome do analista de Gestão: ")
    infraMGM.add(nome)

print("O time de Infra Data Center é composto por: ", infraDC)
print()
print("O time de Infra Data Base é composto por: ", infraDBA)
print()
print("O time de Infra Data Base é composto por: ", infraNTW)
print()
print("O time de Infra Data Base é composto por: ", infraMGM)
print()
operacao = infraDC.union(infraDBA).union(infraNTW).union(infraMGM)
print()
print("O time de Operação é composto por: ", operacao)