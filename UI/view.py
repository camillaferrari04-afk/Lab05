import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._controller = None

    def load_interface(self):
        self._title = ft.Text("Segreteria studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self._dpdcorso = ft.Dropdown(label="corso", hint_text="Selezionare un corso", width=500)
        self._controller.filldpdcorso()
        self._btncercaisc= ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handlecercaisc)

        self._txtmatr=ft.TextField(label='matricola', width=150)
        self._txtnome=ft.TextField(label='nome', read_only=True, width=250)
        self._txtcognome = ft.TextField(label='cognome', read_only=True, width=250)

        self._btncercast= ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handlecercast)
        self._btncercacor= ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handlecercacor)
        self._btniscrivi= ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleiscrivi)

        row1= ft.Row(controls=[self._dpdcorso, self._btncercaisc], alignment=ft.MainAxisAlignment.CENTER)
        row2= ft.Row(controls=[self._txtmatr, self._txtnome, self._txtcognome], alignment=ft.MainAxisAlignment.CENTER)
        row3= ft.Row(controls=[self._btncercast, self._btncercacor, self._btniscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._txtOut=ft.ListView(expand=True)

        self._page.controls.extend([row1, row2, row3, self._txtOut])
        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
