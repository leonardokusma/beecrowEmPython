
numeros = []
maior = 0
posi = 0
for i in range(100):
    numeros.append(int(input()))
    if(i == 0):
        maior = numeros[i]
    elif(numeros[i] > maior):
        maior = numeros[i]
        posi = i+1
print(maior)
print(posi)
