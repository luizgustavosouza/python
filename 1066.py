par=0
impar=0
positivo=0
negativo=0

for i in range(5):
    num = int(input())

    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

    if num > 0:
        positivo = positivo + 1

    #if num == 0:
     #   negativo = negativo - 1
    else:
        negativo = negativo + 1

print(par, "valor(es) par(es)", end="\n")
print(impar, "valor(es) impar(es)", end="\n")
print(positivo, "valor(es) positivo(s)", end="\n")
print(negativo, "valor(es) negativo(s)", end="\n")


