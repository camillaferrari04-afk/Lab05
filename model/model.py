from Lab05.database.corso_DAO import Corso_DAO
from Lab05.database.studente_DAO import Studente_DAO


class Model:
    def __init__(self):
        pass

    def getallCorsi(self):
        return Corso_DAO.getallCorsi()

    def cercaisc(self, corso):
        return Studente_DAO.cercaisc(corso)

    def cercast(self, matricola):
        return Studente_DAO.cercast(matricola)

    def cercacor(self, matricola):
        return Corso_DAO.cercacorst(matricola)

    def iscrivi(self, matricola, codins):
        return Corso_DAO.iscrivi(matricola, codins)

