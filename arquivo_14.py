

file = open("arquivo_1.txt", "r")

#O método readline() serve, para leitura de uma linha de cada vez

linha = file.readline()

for z in linha:
    print(z)


#Agora, haverá a reescrita do arquivo!

n = open("arquivo_1.txt", "w")

n.write("Adicionando dado ao arquivo")


