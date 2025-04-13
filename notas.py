def arrendondarNotas(notas):
    notasCertas = []

    for nota in notas:
        if(nota >= 38 ):
            multiplo = ((nota//5)+1)*5

            if((multiplo - nota) < 3):
                notasCertas.append(multiplo)
            else:
                notasCertas.append(nota)
        else:
            notasCertas.append(nota)
    return notasCertas