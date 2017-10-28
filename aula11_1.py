#Criando Dicionários chave:valor

time=dict()  #também pode ser feito time={}
qtdIntegrantes=int(input("Digite a quantidade de integrantes no time:  "))
for i in range(qtdIntegrantes):
    nome=input("Digite o nome do intgrante: ")
    especialidade=input("Digite a especialidade do "+nome+": " )
    time[nome]=especialidade
#print(time)
for chave,valor in time.items():
    print(chave,":",valor)
print()
#Com valores em ordem alfabética
for chave in sorted(time):
    print(chave,":",time[chave])
