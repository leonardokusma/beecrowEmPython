notas = 0
media = 0
while(notas != 2):
    nota = float(input())
    if(nota <0 or nota>10):
        print("nota invalida")
    else:
        media+=nota
        notas+=1

media /= 2.0
print("media = %.2f"%media)