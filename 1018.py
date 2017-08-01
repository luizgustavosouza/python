N = int(input())

if 0 < N < 1000000:
    C1=N//100
    R=N%100
    C2=R//50
    R=R%50
    C3=R//20
    R=R%20
    C4=R//10
    R=R%10
    C5=R//5
    R=R%5
    C6=R//2
    R=R%2
    C7=R//1
    R=R%1
else:
    exit()

print(N, end="\n")
print(C1, 'nota(s) de R$ 100,00', end="\n")
print(C2, 'nota(s) de R$ 50,00', end="\n")
print(C3, 'nota(s) de R$ 20,00', end="\n")
print(C4, 'nota(s) de R$ 10,00', end="\n")
print(C5, 'nota(s) de R$ 5,00', end="\n")
print(C6, 'nota(s) de R$ 2,00', end="\n")
print(C7, 'nota(s) de R$ 1,00', end="\n")


