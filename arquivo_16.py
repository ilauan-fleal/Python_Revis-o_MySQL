#Esse programa irá exibir um arquivo digitado pelo usuário!

x = open("arquivo_2.txt", "r")


y = x.readlines()

for z in y:
    print(z)


d = input("Agora, escreva um novo conteúdo para o arquivo:")

y = open("arquivo_2.txt", "w")

y.write(d)

y.close()


