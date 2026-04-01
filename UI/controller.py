import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def filldpdcorso(self):
        for c in self._model.getallCorsi():
            self._view._dpdcorso.options.append(ft.dropdown.Option(
                key=c.codins,
                data=c,
                text=str(c),
                on_click=self._memorizzacorso
            ))

    def handlecercaisc(self, e):
        if not self._view._dpdcorso.value:
            self._view.create_alert("Devi selezionare un corso")
            return
        corso=self._view._dpdcorso.value
        self._view._txtOut.controls.clear()

        self._view._txtOut.controls.append(
            ft.Text(value=f"Studenti del corso {self._dpdcorsoscelto.nome}", color="lightblue", size=18))
        for c in self._model.cercaisc(corso):
            self._view._txtOut.controls.append(ft.Text(f"{str(c)}"))

        self._view.update_page()

    def handlecercast(self, e):
        if self._view._txtmatr.value=="":
            self._view.create_alert("Devi inserire una matricola")
        else:
            studente=self._model.cercast(self._view._txtmatr.value)
            if not studente:
                self._view.create_alert("Studente non trovato")

            else:
                self._view._txtOut.controls.clear()
                self._view._txtnome.value=studente.nome
                self._view._txtcognome.value=studente.cognome

                self._view.update_page()


    def handlecercacor(self, e):
        if self._view._txtmatr.value == "":
            self._view.create_alert("Devi inserire una matricola")
        else:
            studente = self._model.cercast(self._view._txtmatr.value)
            if not studente:
                self._view.create_alert("Studente non trovato")

            else:
                self._view._txtOut.controls.clear()
                self._view._txtnome.value = studente.nome
                self._view._txtcognome.value = studente.cognome
                self._view._txtOut.controls.append(
                    ft.Text(value=f"Corsi dello studente {studente.nome} {studente.cognome}", color="lightblue", size=18))
                for c in self._model.cercacor(studente.matricola):
                    self._view._txtOut.controls.append(ft.Text(f"{str(c)}"))

                self._view.update_page()

    def handleiscrivi(self, e):
        if self._view._txtmatr.value == "":
            self._view.create_alert("Devi inserire una matricola")
            return
        if not self._view._dpdcorso.value:
            self._view.create_alert("Devi selezionare un corso")
            return

        studente = self._model.cercast(self._view._txtmatr.value)
        if not studente:
            self._view.create_alert("Studente non trovato")
            return

        self._view._txtOut.controls.clear()
        self._view._txtnome.value = studente.nome
        self._view._txtcognome.value = studente.cognome

        if self._model.iscrivi(studente.matricola, self._dpdcorsoscelto.codins ):
            self._view._txtOut.controls.append(
                ft.Text(value=f"Studente {studente.nome} {studente.cognome} iscritto a {self._dpdcorsoscelto.nome}",
                        color="lightblue",
                        size=18))
        else:
            self._view._txtOut.controls.append(
                ft.Text(value=f"Studente {studente.nome} {studente.cognome} già iscritto a {self._dpdcorsoscelto.nome}",
                        color="red",
                        size=18))

        self._view.update_page()

    def _memorizzacorso(self,e):
        self._dpdcorsoscelto=e.control.data