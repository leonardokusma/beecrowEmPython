print("MUITO OBRIGADO")
alcool = 0
gas = 0
diesel = 0
num = 0
while(num !=4):
    num = int(input())
    if(num == 1):
        alcool+=1
    elif(num == 2):
        gas+=1
    elif(num == 3):
        diesel+=1
print("Alcool: %i"%alcool)
print("Gasolina: %i"%gas)
print("Diesel: %i"%diesel)
