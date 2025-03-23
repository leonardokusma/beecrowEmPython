n1 = int(input())
n2 = int(input())

if (n2>n1):
    for n in range(n1+1,(n2)):
        if (n%5==2 or n%5==3):
            print(n)
if (n1>n2):
    for n in range(n2+1,(n1)):
        if (n % 5 == 2 or n % 5 == 3):
            print(n)