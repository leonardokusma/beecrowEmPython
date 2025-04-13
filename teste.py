menor = int(input())
maior = int(input())
sum = 0
if(maior < menor):
    aux = menor
    menor = maior
    maior = aux

for a in range(menor,maior+1):
    sum += a
print(sum)

