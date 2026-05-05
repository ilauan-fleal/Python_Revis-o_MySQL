
#Programa para integrar Python com MySQL
import MySQLdb

host = "localhost"

user = "root"

password = "***************"

db = "---------------"

port = 3306

con = MySQLdb.connect(host, user, password, db, port)


c = con.cursor(MySQLdb.cursors.DictCursor)



def Seleciona(field, table, Where=None):
    global c #Fazendo Referência a variável global
    query = " SELECT " + field + " FROM " + table
    if(Where):
        query = query + " WHERE " + Where
    c.execute(query)
    return c.fetchall()




#Criando função para inserir dados, no banco!

def Inserir(values, table, fields=None):
    global c, con
    query = " INSERT INTO " + table
    if(fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])
    c.execute(query)
    con.commit()





values = [
    "DEFAULT, 'Marcotti', '2000-08-09', 'Av. AAAAAAAAAA, BBBBB', 'Estado AAAA', 'AA', '444444'",
    

]

#Criando função, para update:

def Atualizar(sets, table, where=None):
    global c, con
    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " =' " + value + " ' " for field, value in sets.items()])
    if(where):
        query = query + " WHERE " + where
    print(query)
    c.execute(query)
    con.commit()


def Deletar(table, where):
    global c, con
    query = "DELETE FROM " + table + " WHERE " + where
    c.execute(query)
    con.commit()

