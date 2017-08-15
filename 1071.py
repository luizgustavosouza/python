x = int(input())
y = int(input())
soma = []*0
if x == y:
    total = 0
for i in range(x,y) or range(y+1,x):
    if i % 2 != 0:
        soma.append(i)
total = sum(soma)
print(total)







