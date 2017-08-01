#Para calcular sua idade em dias

a = int(input('informe sua idade: '))

print (a * 365 , 'dia(s)')

#Para calcular sua idade em anos
d = int(input('Informe quantos dias você viveu(valor informado anteriormente): '))

print(d // 365, 'ano(s)')
print((d % 365) // 30, 'mes(es)')
print((d % 365) % 30, 'dia(s)')