#Aula 3 | Exemplo 2

salario=float(input("Diga seu salario atual: "))
tempo=int(input("Diga quantos anos completos tem se serviço: "))

if tempo <1:
    print("Seu salário se mantém o mesmo: ", salario,". Tenha uma boa vida!")
else:
    if tempo<10:
        salario=salario*1.10
    else:
        salario=salario*1.25
    print("Seu novo salário, com abono é: ", salario,"Tenha uma boa vida!")