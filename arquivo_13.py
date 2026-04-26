#Revisando manipulação de arquivos com Python!

file = open("arquivo_1.txt", "r")

#O método readlines() serve, para leitura do arquivo e em seguida armazená-lo em uma lista.

linhas = file.readlines()

for lines in linhas:
    print(lines)

#O método read() serve, para leitura de um arquivo inteiro.

FullText = file.read()



