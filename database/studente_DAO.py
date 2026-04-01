from database.DB_connect import get_connection
from model.studente import Studente

class Studente_DAO:

    @staticmethod
    def cercaisc(codins: str):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = '''select s.matricola, s.nome, s.cognome, s.CDS 
                    from iscrizione i, corso c, studente s
                    where i.codins=c.codins and s.matricola=i.matricola and c.codins=%s
                    order by s.cognome'''

        cursor.execute(query, (codins,))
        res = []
        for row in cursor:
            res.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def cercast(matricola: int):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = '''select *
                    from studente s
                    where s.matricola=%s'''

        cursor.execute(query, (matricola,))
        res=None
        row=cursor.fetchone()
        if row is not None:
            res= Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"])

        cursor.close()
        cnx.close()
        return res
