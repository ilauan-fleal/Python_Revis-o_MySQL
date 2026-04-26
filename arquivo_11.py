nota1 = 5
nota2 = 7

# Qual a media?

def CalculaMedia(x,y):
    media = (x + y)/2
    return media

resultado = CalculaMedia(nota1, nota2)

print(f"A media calculada entre os dois valores digitados é igual a %.1f" % resultado)


