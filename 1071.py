x = int(input())
y = int(input())
soma = []
if x == y:
    print('0')
for i in range(x,y,1) or range(y,x,1):
    if i % 2 != 0:
        print(i)
        #soma[i]=i
print(soma)


