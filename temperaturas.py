lista =  [23.6, 37.9, 25.1, 19.0, 29.8]
maior = 0
menor = 100

for a in lista:
    if(maior < a):
        maior = a
    if(menor > a):
        menor = a
soma = sum(lista)
qtd = len(lista)
media = soma/qtd
print(maior)
print(menor)
print("%.2f"%media)
