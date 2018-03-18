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
    self.precio        = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_total'
    self.total         = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_pago'
    self.pago         = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_cambio'
    self.cambio         = self.entry(**dicEntry)
    dicEntry = {"nombre":'e_cantidad', "tipo"  :'integer', "set"   :'0'}
    self.cantidad      = self.entry(**dicEntry)
    dicEntry["nombre"] = 'e_producto'
    dicEntry["evento"] = {"tipo":'key-press-event', "funcion":self.addProducto}
    self.idproducto    = self.entry(**dicEntry)
    self.nombre        = self.entry(nombre='producto_nombre')
    self.window.set_focus(self.idproducto)

  def salirCaja(self, button, widgets):
    self.windowIni.show_now()
    self.window.destroy()

  def addProducto(self, entry, values, widgets=None):
    if (values.get_keycode()[1] in (36,23)):
      _res = self.db.rawQueryOne("SELECT * FROM get_val_producto({})".format(entry.get_text()))
      print(_res)
      if (_res[0] is None):
        dic_err = {"tipo"         : 'error',
                   "tituloDialog" : 'ERROR',
                   "textDialog"   : 'El Producto {} no existe'.format(entry.get_text())
                  }
        self.dialogoBox(**dic_err)
        entry.set_text('0')
        self.precio.set_text('0.00')
        self.nombre.set_text('')
        self.cantidad.set_text('0')
        return
      self.precio.set_text(_res[1])
      self.nombre.set_text(_res[0])
      self.window.set_focus(self.cantidad)
