#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

import os
from src.widgets  import widgetsUse
from src.inicio   import ventanaInicio
from src.db       import dbase
from yaml         import load, dump

class main(widgetsUse):
  """docstring for logIn."""
  def __init__(self):
    super().__init__(gld="./gld/login.glade")
    self.conn = None
    window = self.windows(nombre="window1")
    window.show_all()
    entry_contrasena = self.entry(nombre='e_contrasena',foco_ini=True)
    e_data = {"nombre": 'e_usuario',
              "evento": {"tipo": 'key-press-event',
                         "funcion": self.onEntryUser,
                         "widgets": {"window"   : window,
                                     "entry_con": entry_contrasena}}
              }
    entry_user = self.entry(**e_data)
    cb_data = {"nombre" : 'cbbases',
               "tipo"   : 'bcbox',
               "num_el" : (str, str), # Solo hace falta al acumular mas de un elemento dentro del combo
               "lista"  : self.listBases(),
               "evento" : {"tipo"   :'changed',
                           "funcion":self.onCbBase,
                           "widgets":{"window"      : window,
                                      "e_usuario"   : entry_user}
                           }
               }
    cb_base = self.comboBox(**cb_data)
    bt_data = {"nombre":'bt_entrar',
               "evento" : {"tipo": 'clicked',
                          "funcion": self.onButtonEntrar,
                          "widgets": {"window"      : window,
                                      "e_usuario"   : entry_user,
                                      "e_contrasena": entry_contrasena,
                                      "cb_base"     : cb_base}
                          }
              }
    boton_entrar = self.button(**bt_data)
    bt_data["nombre"] = 'bt_cancel'
    bt_data["evento"]["funcion"] = self.onButtonCancel
    boton_cancelar = self.button(**bt_data)
    self.inicioApp()

  def onButtonEntrar(self, button, widgets):
    dic_err = {"tipo"         : 'error',
               "tituloDialog" : 'ERROR',
               "textDialog"   : 'Es necesario agregar todos los datos una base de datos'
              }
    datosDb = self.getDataCombo(widgets["cb_base"])
    if (datosDb is None or widgets["e_usuario"].get_text()  == '' or widgets["e_contrasena"].get_text() == ''):
      self.dialogoBox(**dic_err)
      return
    try:
      c = dbase(datosDb[1])
    except Exception as e:
      dic_err["textDialog"] = 'Es necesario revisar su conexión con la base de datos o llamar a su personal de soporte'
      self.dialogoBox(**dic_err)
      return
    _res = c.rawQueryOne("SELECT valida_user('{}', '{}')".format(widgets["e_usuario"].get_text(), widgets["e_contrasena"].get_text()))
    if (_res[0]):
      ventanaInicio(c)
      widgets["window"].destroy()
    else:
      dic_err["textDialog"] = 'El usuari o contraseña es incorrecto'
      self.dialogoBox(**dic_err)

  def onButtonCancel(self, button, widgets):
    widgets["e_usuario"].set_text("") 
    widgets["e_contrasena"].set_text("") 
    widgets["window"].set_focus(widgets["e_usuario"])

  def onEntryUser(self, entry, val ,widgets):
    if (val.get_keycode()[1] in (36,23)):
      entry_contrasena = widgets["entry_con"]
      widgets["window"].set_focus(entry_contrasena)

  def onCbBase(self, cb, widgets):
    try:
      widgets["window"].set_focus(widgets["e_usuario"])
    except Exception as e:
      print(e)

  def listBases(self):
      res = []
      try:
        if (os.path.isfile('.base.yaml')):
          with open(r'.base.yaml') as file:
            data = load(file)
        else:
          data = {"baseProduccion" : { "url"    : 'localhost',
                                       "nombre" : 'Base Produccion'}
                 }
          with open('.base.yaml','w') as file:
            file.write(dump(data))
        for key, value in data.items():
          res.append([value["nombre"], key])
      except Exception as e:
        print(e)
      return res

