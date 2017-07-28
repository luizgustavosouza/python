num=int(input("Digite um numero para calcularmos seu fatorial: "))
contador=1
fatorial=1

while contador<=num:
    fatorial*=contador
    contador+=1
print("O fatorial de", num, "e",fatorial)

fat=1
for i in range(1,num+1):
    fat*=i
print("Fatorial com for: ", fatorial)