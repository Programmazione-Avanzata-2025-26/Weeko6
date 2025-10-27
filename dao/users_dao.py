import mysql.connector
from dao.user_dto import UserDTO

# Classe che si occupa di rendere "trasparente" l'accesso al database

class UsersDAO:
    def __init__(self): # Eventualmente apertura e chiusura della connessione in una altra classe ancora
        self._cnx = mysql.connector.connect(user='root',
                                password='',
                                host='127.0.0.1',
                                database='pa')

    # Metodo DAO per aggiungere una riga alla tabella User

    def addUser(self, u): #id, name, phone
        cursor = self._cnx.cursor()
        query = """INSERT INTO User 
                   (id, name, phone) 
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (u.id, u.name, u.phone))
        self._cnx.commit()

    # Metodo DAO per ottenere tutte le righe della tabella User

    def getUsers(self):
        cursor = self._cnx.cursor()
        query = """SELECT * FROM User"""
        cursor.execute(query)
        result = []
        for row in cursor:
            uTemp = UserDTO(row[0], row[1], row[2])
            result.append(uTemp)
        return result
        cursor.close()