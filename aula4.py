#Funções

def fatorial(num):
    if num==0:
        return 1
    else:
        return num*fatorial(num-1)

def fib(num):
    if 1<=num<=2:
        return 1
    else:
        return fib(num-1)+fib(num-2)

def soma(f,n):
    parcial=0

    for i in range(1,n+1):
        parcial=parcial+f(i)
    return parcial

#Programa Principal

numero=int(input('Informe um valor para calcular o fatorial: '))
x=fatorial(numero)

sequencia=int(input('Informe um valor para calcular a sequencia de fibbonaci: '))
y=fib(sequencia)

progressao=int(input('Informe uma valor para calcular uma progressão: '))
z=soma(fatorial, progressao)

print(x,y,z)
