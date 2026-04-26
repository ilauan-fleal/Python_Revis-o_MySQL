import os

arquivo = input("Digite o nome ou caminho do arquivo:\n")

#Cria-se função para verificar a existência do arquivo.

def VerificaExistenciaDeArquivo(arquivo):
    if(os.path.exists(arquivo)):
        print("O arquivo existe.")
    else:
        print("O arquivo não existe, o programa deverá ser encerrado.\n")
        exit(1)

#Cria-se uma função para fazer a leitura do arquivo.

def LeituraDeArquivo(arquivo):
    x = open(arquivo, "r")
    y = x.readlines()
    for z in y:
        print(z)

#Cria-se uma função para introduzir dado no arquivo e em seguida exibir esse dado digitado.

def IntroduzirDadoNoArquivoComLeitura(arquivo):
    x = open(arquivo, "w")
    d = input("Escreva um dado no arquivo, para ser gravado e exibido:\n")
    x.write(d)
    print("Excelente, o dado gravado no arquivo foi:\n")
    print(d)


#Cria-se uma função de Menu


def Menu(arquivo):
    
    print("Atenção! Escolha uma dentre as opções abaixo disponíveis:")
    while(1):
        print("1-> O programa irá ler um arquivo de texto:\n")
        print("2-> O programa deverá exibir o conteúdo do arquivo lido:\n")
        print("3-> O programa deverá ser plenamente fechado.\n")
        escolha = int(input())
        if(escolha == 1):
            LeituraDeArquivo(arquivo)
            break
        elif(escolha == 2):
            IntroduzirDadoNoArquivoComLeitura(arquivo)
            break
        elif(escolha == 3):
            print("Programa encerrado!")
            exit(1)
        else:
            print("Valor inválido , dentre as opções disponíveis, escolha novamente.\n")
            escolha = int(input())        

#Chamada das funções


VerificaExistenciaDeArquivo(arquivo)
Menu(arquivo)


