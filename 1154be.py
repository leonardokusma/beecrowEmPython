count =0
idade =1
media = 0

while(idade >0):
    idade = int(input())
    if(idade>0):
        media +=idade
        count+=1


media = media / float(count)
print("%.2f"%media)
