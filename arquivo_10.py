#Implementando um simples programa de calculadora em python!

x = float(input("Digite um primeiro número:\n"))
y = float(input("Digite um segundo  número:\n"))

sinal = input("Agora digite um sinal correspondente a uma operação(+, -, *, /, **):.\n")



def Calculadora(x,y,sinal):
    while(sinal != ' '):

        if(sinal == '+'):
            return x + y
        elif(sinal == '-'):
            return x - y
        elif(sinal == '*'):

            return x * y
        elif(sinal == '/'):

            return x // y
        elif(sinal == '**'):
            return x ** y
        else:

            print("Parâmetro inválido digite novamente:\n")
            sinal = input()
    

resultado = Calculadora(x,y,sinal)
print(resultado)