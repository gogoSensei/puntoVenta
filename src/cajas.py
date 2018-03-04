#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       28/02/2018       ############

from src.widgets import widgetsUse
#from src.inicio import ventanaInicio

class modCajas(widgetsUse):
  """docstring for cajas"""
  def __init__(self, db, widgetWinIni):
    super().__init__(gld="./gld/ventas.glade")
    self.db = db
    self.windowIni = widgetWinIni
    self.window = self.windows(nombre="window1")
    self.window.show_all()
    btSalirDat = {"nombre" : 'bt_salir',
                  "evento" : {"tipo" : 'clicked', "funcion" : self.salirCaja}}
    self.botonSalir = self.button(**btSalirDat)
    dicEntry = {"nombre":'e_precio', "tipo"  :'numerico', "set"   :'0.00'}
    dicEntry["nombre"] = 'e_precio'
    self.precio        = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_total'
    self.total         = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_pago'
    self.total         = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_cambio'
    self.total         = self.entry(**dicEntry)
    dicEntry = {"nombre":'e_cantidad', "tipo"  :'integer', "set"   :'0'}
    self.cantidad      = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_producto'
    self.idproducto    = self.entry(**dicEntry)
    self.window.set_focus(self.idproducto)

  def salirCaja(self, button, widgets):
    self.windowIni.show_now()
    self.window.destroy()