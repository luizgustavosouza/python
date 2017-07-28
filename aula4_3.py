#Funçoes

def imc(p,a):
    return p/(a*a)

def analyzer(p,a):
    analista=imc(p,a)

    if analista <=18.5:
        return 1
    elif analista <= 24.9:
        return 2
    elif analista <= 29.9:
        return 3
    else:
        return 4

#Progrmama Principal

print("Bem vindo mane!!")

dados=input("Informa ai pra mim teu peso(Kg) e tua altura(m)").split()

x=float(dados[0])
y=float(dados[1])

resultado=analyzer(x,y)

if y<1.65:
    print("So esqueceu de crescer ne? ")

if resultado==1:
    print("Voce esta magro D+")
elif resultado==2:
    print("Que isso hein fera, ta fitness!")
elif resultado==3:
    print("Ta na hora de começar a fechar a boca, ta ficando gordinho(a)")
else:
    print("Academia ja! Nutricionista ja!! ")
    