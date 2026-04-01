from database.DB_connect import get_connection
from model.corso import Corso

class Corso_DAO:

    @staticmethod
    def getallCorsi():
        cnx=get_connection()
        cursor=cnx.cursor(dictionary=True)

        query='''select * from corso'''

        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def cercacorst(matricola:int):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = '''select c.codins, c.nome, c.crediti, c.pd 
                    from iscrizione i, corso c, studente s
                    where i.codins=c.codins and s.matricola=i.matricola and i.matricola=%s
                    order by c.nome'''

        cursor.execute(query, (matricola,))
        res = []
        for row in cursor:
            res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def iscrivi(matricola: int, codins:str):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query_controllo = '''select * 
                        from iscrizione i
                        where i.matricola=%s and i.codins=%s'''

        query_iscrivi='''INSERT INTO iscrizione (matricola, codins) 
                         VALUES (%s, %s)'''

        cursor.execute(query_controllo, (matricola, codins))
        if cursor.fetchone() is None:
            cursor.execute(query_iscrivi, (matricola, codins))
            cnx.commit()
            cursor.close()
            cnx.close()
            return 1
        else:
            cursor.close()
            cnx.close()
            return 0

