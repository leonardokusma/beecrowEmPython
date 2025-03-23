n1 = int(input())
n2 = int(input())
soma = 0
if (n2>n1):
    for n in range(n1,(n2+1)):
        if (n%13!=0):
            soma+=n
if (n1>n2):
    for n in range(n2,(n1+1)):
        if (n%13!=0):
            soma+=n

print(soma)