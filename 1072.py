n = int(input())
inside = 0
outside = 0
for i in range(n):
    if n < 10000:
        x = int(input())
        if (x>=10) and (x<=20):
            inside +=1
        else:
            outside +=1
print(inside, 'in')
print(outside, 'out')



