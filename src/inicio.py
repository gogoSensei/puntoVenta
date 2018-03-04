#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

from src.widgets import widgetsUse
from src.cajas import modCajas

class ventanaInicio(widgetsUse):
  """docstring for ventanaInicio."""
  def __init__(self, db):
    super().__init__(gld="./gld/menu_principal.glade")
    self.db = db
    # Pruebas de base de datos ----> print(self.db.rawQuery("SELECT * FROM prueba_base"))
    window = self.windows(nombre="window1")
    window.show_all()
    btData = {"nombre" : 'bt_ventas',
              "evento" : {"tipo"   : 'clicked',
                          "funcion": self.inicioCaja,
                          "widgets": {"window": window}}
             }
    botonCaja = self.button(**btData)
    btData["nombre"] = 'bt_salir'
    btData["evento"]["funcion"] = self.finApp
    botonSalir = self.button(**btData)

  def inicioCaja(self, button, widgets):
    widgets["window"].hide()
    modCajas(self.db, widgets["window"])
