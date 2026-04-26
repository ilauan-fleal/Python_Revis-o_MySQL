#Exercício -> Escrevendo um programa , que compara se duas sequências digitadas pelo usuário são iguais!

Lista1 = []

Lista2 = []

#Função que irá receber as duas listas e permitir que o usuário insira dados nelas!!!

def AgregaValorNaLista(lista1, lista2):
    print("Quantos elementos irá digitar na primeira lista?:\n")
    n = int(input())
    i = 1
    while(i < n + 1):
        print(f"Ok, valor registrado! Digite o elemento %d" % i)
        elemento = input()
        lista1.append(elemento)
        i = i + 1
    print("Excelente, agora, digite o total de elementos que irá inserir na segunda lista\n")
    x = int(input())
    y = 1
    while(y < x + 1):
        print(f"Ok, valor registrado! Digite o elemento %d" % y)
        valor = input()
        lista2.append(valor)
        y = y + 1

#Função que irá verificar as sequências de valores digitadas!!

def VerificaSequenciaDeValores(lista1, lista2):
    for z in range(len(lista1)):
        for k in range(len(lista2)):
            if(lista1[z] == lista2[k]):
                print("Sequências digitadas foram idênticas!\n")
                exit(1)
            else:
                print("As sequências divergem entre si!\n")
                exit(1)

#Chamada das funções


AgregaValorNaLista(Lista1, Lista2)

VerificaSequenciaDeValores(Lista1, Lista2)