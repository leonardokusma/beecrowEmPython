lista = []

for a in range(10):
    num = int(input())
    lista.append(num)

posicoes = {}


for i, num in enumerate(lista):
    if num in posicoes:
        posicoes[num].append(i)
    else:
        posicoes[num] = [i]

repetidos = False
for num, b in posicoes.items():
    if len(b) > 1:
        repetidos = True
        print(f"O número {num} se repete nas posições: {b}")

if not repetidos:
    print("Não há números repetidos.")