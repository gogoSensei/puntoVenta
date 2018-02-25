#!/usr/bin/python3

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

from src.widgets import widgetsUse

class main(widgetsUse):
    """docstring for logIn."""
    def __init__(self):
        super().__init__(gld="./gld/login.glade")
        window = self.windows(nombre="window1")
        window.show_all()
        bt_data = {"nombre":'bt_entrar',
                   "evento" : {"tipo": 'clicked',
                               "funcion": self.onButtonPressed}
                   }
        boton_entrar = self.button(**bt_data)
        bt_data["nombre"] = 'bt_cancel'
        bt_data["evento"]["funcion"] = self.onButtonPressed2
        boton_cancelar = self.button(**bt_data)
        entry_contrasena = self.entry(nombre='e_contrasena',foco_ini=True)
        e_data = {"nombre": 'e_usuario',
                  "evento": {"tipo": 'activate',
                             "funcion": self.onEntryValue,
                             "widgets": {"entry1": entry_contrasena}}
                  }
        entry_user = self.entry(**e_data)
        self.inicioApp()

    def onButtonPressed(self, button, widgets):
        print("Hello World!")

    def onButtonPressed2(self, button, widgets):
        print("Hello cancel!")

    def onEntryValue(self, entry, entry2):
        entry_contrasena = entry2["entry1"]
        entry_contrasena.set_active(True)
        print("Hello entry")
