n = int(input())
coelhos = 0
ratos = 0
sapos = 0
total = 0
for i in range(n):
    teste, tipo = input().split(" ")
    teste = int(teste)
    if(tipo == 'C'):
        coelhos +=teste
        total += teste
    elif(tipo == 'R'):
        ratos += teste
        total += teste
    elif(tipo == 'S'):
        sapos += teste
        total += teste

percoelho = (coelhos*100.00)/float(total)
perrato = (ratos*100.00)/float(total)
persapos = (sapos*100.00)/float(total)
print("Total:", total,"cobaias")
print("Total de coelhos:", coelhos)
print("Total de ratos:",ratos)
print("Total de sapos:", sapos)
print("Percentual de coelhos: %.2f %%"%percoelho)
print("Percentual de ratos: %.2f %%"%perrato)
print("Percentual de sapos: %.2f %%"%persapos)