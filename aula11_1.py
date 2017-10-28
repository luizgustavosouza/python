#Criando Dicionários chave:valor

time=dict()  #também pode ser feito time={}
qtdIntegrantes=int(input("Digite a quantidade de integrantes no time:  "))
nomeTime="Infra Data Center"
gestorName=input("Informe o nome do Gestor: ")
for i in range(qtdIntegrantes):
    nome=input("Digite o nome do intgrante: ")
    especialidade=input("Digite a especialidade do "+nome+": " )
    time[nome]=especialidade
print()
print("O time "+nomeTime+ " gerenciado por "+gestorName+" é composto por: ")
for chave,valor in time.items():
    print(chave)
print()
print("Ordenando...")
#Com valores em ordem alfabética
for chave in sorted(time):
    print(chave)
print()
print("As especialidades do time "+nomeTime+" são:")
for valor in time.values():
    print(valor)
print()
print("Ordenando as especialidades do time "+nomeTime+" :")
for valor in sorted(time.values()):
    print(valor)
