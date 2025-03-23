import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpando o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("__")

    #obtendo texto

    texto = input("digite sua mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagens na lista

    mensagens.append({
        "nome": nome,
        "texto": texto,
    })