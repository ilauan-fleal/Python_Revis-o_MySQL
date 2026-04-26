
lista = [4, 3, 2, 1, 0]

#Construindo algoritmo de ordenação em Python!

def SelecionaValores(listagem):
    for z in range(len(listagem)):
        menor = z
        for k in range(z + 1,len(listagem)):
            if(listagem[k] < listagem[menor]):
                menor = k
        if(listagem[z] != listagem[menor]):

            auxiliar = listagem[z]
            listagem[z] = listagem[menor]
            listagem[menor] = auxiliar
    print(listagem)


resultado = SelecionaValores(lista)
print(resultado)