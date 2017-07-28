#Função
def fib(num):
    if num==0:
        return 0
    if 1<=num<=2:
        return 1
    else:
        return fib(num-1)+fib(num-2)

def chamadas(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        





#Programa Principal
sequencia=int(input('Informe um valor para calcular a sequencia de fibbonaci: '))
x=fib(sequencia)
print(x)
