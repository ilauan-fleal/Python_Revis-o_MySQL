import math
print("Olá, bem-vindo ao programa resolucionador de equações do segundo grau:\n")
a = float(input("Digite o valor do coeficiente a:\n"))
b = float(input("Digite o valor do coeficiente b:\n"))
c = float(input("Digite o valor do coeficiente c:\n"))



def ResolveEquacao(a, b, c):
    delta = b**2 - 4 *a*c
    if(delta < 0):
        print("A equação não tem raíz real!\n")
        exit(0)
    elif(delta == 0):
        print("A equação apresenta duas raízes reais e iguais!\n")
        x = (-b + math.sqrt(delta))/(2*a)
        return x
    else:
        print("A equação apresenta duas raízes reais distintas!\n")
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"A primeira raíz é %.2f e a segunda é igual a %.2f.\n" % (x1,x2))
                

k = ResolveEquacao(a,b,c)
print(k)

