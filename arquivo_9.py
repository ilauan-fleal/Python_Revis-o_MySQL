#Ordenando uma lista numérica de três elementos.s
ListaDeValores = []

a = int(input("Digite um primeiro valor inteiro:\n"))

b = int(input("Digite um segundo  valor inteiro:\n"))

c = int(input("Digite um terceiro valor inteiro:\n"))

def AgregaValoresNaLista(Lista):
    #Agregando itens na lista
    Lista.append(a)
    Lista.append(b)
    Lista.append(c)
    return Lista

def RecebeEordenaLista(Lista):
    AgregaValoresNaLista(Lista)
    Lista.sort()
    print("Exibição Ordenada:\n")
    for z in Lista:
       
        print(z)
    

v = RecebeEordenaLista(ListaDeValores)
print(v)