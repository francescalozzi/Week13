import flet as ft


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Flight Delays", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txtNumCompagnieMinimo = ft.TextField(
            label="Num compagnie minimo",
            width=250,
            hint_text="Insert a your name"
        )

        # button for the "hello" reply
        self.btnAnalizzaAereoporti = ft.ElevatedButton(text="Analizza Aereoporti",
                                                       on_click=self._controller.handle_analizzaAereoporti)
        row1 = ft.Row([self.txtNumCompagnieMinimo, self.btnAnalizzaAereoporti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.ddAereoportoPartenza = ft.Dropdown(label= 'Aereoporto partenza', width=250)
        self.ddAereoportoArrivo = ft.Dropdown(label='Aereoporto arrivo', width=250)
        self.btnAereoportiConnessi = ft.ElevatedButton(text="Aereoporti Connessi",
                                                       on_click=self._controller.handle_aereoportiConnessi)

        row2 = ft.Row([self.ddAereoportoPartenza, self.ddAereoportoArrivo, self.btnAereoportiConnessi],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        self.txtNumTratteMassimo = ft.TextField(label ='Numero tratte massimo', width=250,)
        self.btnCercaItinerario = ft.ElevatedButton(text="Cerca Itinerario",
                                                       on_click=self._controller.handle_cercaItinerario)

        row3 = ft.Row([self.txtNumTratteMassimo, self.btnCercaItinerario],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row3)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

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
