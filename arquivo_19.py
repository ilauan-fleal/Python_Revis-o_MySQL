#Programa , para ler arquivo multifasta no Python




import os

arquivo = input("Digite o nome ou caminho do arquivo:\n")

#Cria-se função para verificar a existência do arquivo.

dicionario = {}


def VerificaExistenciaDeArquivo(arquivo):
    if(os.path.exists(arquivo)):
        print("O arquivo existe.")
    else:
        print("O arquivo não existe, o programa deverá ser encerrado.")
        exit(1)

def LeituraDeArquivo(arquivo):
    s = open(arquivo, "r+")
    x = s.readlines()
    d = input("Escreva um dado de cabeçalho:\n")
    dicionario[d] = x
    print(dicionario)

def EscritaDeArquivo(arquivo):
    s = open(arquivo, "w")
    d = input("Escreva um dado , para ser gravado no arquivo:\n")
    s.write(d)


#Chamada da primeira função para verificar existência do arquivo

VerificaExistenciaDeArquivo(arquivo)

#Em seguida, chama-se a segunda função para introduzir um dado no arquivo(escrita)

EscritaDeArquivo(arquivo)


#Por fim, chama-se a última função para realizar a leitura do arquivo

LeituraDeArquivo(arquivo)

