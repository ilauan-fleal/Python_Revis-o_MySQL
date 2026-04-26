#Programa específico para processar um determinado arquivo Fasta
import os
nome = input("Digite o nome do arquivo:\n")

dicionario = {}

#Criando função Python, para verificar existência do arquivo!

def VerificaExistenciaDeArquivo(arquivo):
    if(os.path.exists(arquivo)):
        print("O arquivo existe.")
    else:
        print("O arquivo não existe, o programa deverá ser encerrado.")
        exit(1)


#Criando função , para processar determinado tipo de arquivo!


def ProcessaArquivo(nome):
    arquivo = open(nome, "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        if linha[0] == ">":
            AtualSeq = linha[1:].strip() #Remover espaços em branco!
            dicionario[AtualSeq] = " "
        else:
            dicionario[AtualSeq] = dicionario[AtualSeq] + linha.strip()

    print(dicionario)

#Chamada da função, para verificar a existência do arquivo!

VerificaExistenciaDeArquivo(nome)

#Chamada da função, para processar o arquivo!

ProcessaArquivo(nome)
