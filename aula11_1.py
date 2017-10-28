#Criando Dicionários chave:valor

time=dict()  #também pode ser feito time={}
qtdIntegrantes=int(input())
for i in range(4):
    nome=input("Digite o nome do intgrante: ")
    especialidade=input("Digite a especialidade do integrante: ")
    time[nome]=especialidade

#print(time)

for chave,valor in time.items():
    print(chave,":",valor)

print()
#Com valores aleatórios
for chave in sorted(time):
    print(chave,":",time[chave])