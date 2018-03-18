#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

import re
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class messageDialogWin(Gtk.Window):
  """docstring for messageDialogWin."""
  def __init__(self, tipo=None, tituloDialog='', textDialog='' ):
    super().__init__(title='titulo')
    self.respuesta = False
    dTipo = None
    dButton = None
    if (tipo == 'info'):
      dTipo = Gtk.MessageType.INFO
      dButton = Gtk.ButtonsType.OK
    elif (tipo == 'error'):
      dTipo = Gtk.MessageType.ERROR
      dButton = Gtk.ButtonsType.CANCEL
    elif (tipo == 'warning'):
      dTipo = Gtk.MessageType.WARNING
      dButton = Gtk.ButtonsType.OK_CANCEL
    elif (tipo == 'question'):
      dTipo = Gtk.MessageType.QUESTION
      dButton = Gtk.ButtonsType.YES_NO
    else:
      return
    dialog = Gtk.MessageDialog(self, 0, dTipo, dButton, tituloDialog)
    dialog.format_secondary_text(textDialog)
    response = dialog.run()
    if (tipo == 'warning'):
      if response == Gtk.ResponseType.OK:
        self.respuesta = True
    elif (tipo == 'question'):
      if response == Gtk.ResponseType.YES:
        self.respuesta = True
    dialog.destroy()


class widgetsUse(object):
  """Clase encargada de darle caracteristicas a los widgets asi como diferentes manejos"""
  def __init__(self, **arg):
    # Conexión a archivo galde
    self.builder = Gtk.Builder()
    self.builder.add_from_file(arg["gld"])

  def inicioApp(self):
    Gtk.main()
  
  def finApp(self, button, widgets):
    Gtk.main_quit()

  def windows(self, **args):
    try:
      window = self.builder.get_object(args["nombre"])
      window.connect("delete-event", Gtk.main_quit)
    except Exception as e:
      print(e)
      window = None
    return window


  """
  Isidro Rivera Monjaras
   Funcion para invocar botón e utilizara un diccionario con esta estructura
   dic {"nombre": 'nombre',
        "evento": {"tipo": 'clicked',
                   "funcion": fun, <---funcion creada
                   "widgets" : dic_wid } <------- Es necesario utilizar un diccionario para su llenado
   }
  """
  def button(self, **args):
    try:
      button = args["boton"] if 'boton' in args else self.builder.get_object(args["nombre"])
      for key, value in args.items():
        if (key == 'evento'):
          value["widgets"] = value["widgets"] if 'widgets' in value else None
          button.connect(value["tipo"], value["funcion"], value["widgets"])
    except Exception as e:
      print(e)
      button = None
    return button


  """
  Isidro Rivera Monjaras
  Funcion para realiazar la Conexión con los entrys necesarios
  por el momento utiliza un diccionario igual que los botones
  """
  def on_insert_text(self, entry, new_text, new_text_length, positionX, data):
    '''called when text is inserted on an entry'''
    try:
      if (data == 'numerico'): 
        ONLY_NUMBERS = re.compile('[\.0-9]')
        if '.' in list(entry.get_text()):
          ONLY_NUMBERS = re.compile('[0-9]')
      else:
        ONLY_NUMBERS = re.compile('[0-9]')
      if ONLY_NUMBERS.match(new_text) is None:
        entry.stop_emission('insert-text')
      #  editable.set_text(new_text + '.00')
    except Exception as e:
      entry.stop_emission('insert-text')

  def on_key_release(self, widget, ev, data):
    try:
      #if (widget.get_text().replace(' ', '') == ''):
      if (data == 'numerico'):
        widget.set_text(format(float(widget.get_text() if widget.get_text().replace(' ', '') != '' else '0.00'), '.2f'))
      else:
        widget.set_text(str(int(widget.get_text() if widget.get_text().replace(' ', '') != '' else '0')))
    except Exception as e:
      print(e)
    

  def entry(self, **args):
    try:
      entry = args["entry"] if 'entry' in args else self.builder.get_object(args["nombre"])
      for key, value in args.items():
        if (key == 'evento'):
          value["widgets"] = value["widgets"] if 'widgets' in value else None
          entry.connect(value["tipo"], value["funcion"], value["widgets"])
        elif (key == 'foco_ini'):
          entry.has_focus()
        elif (key == 'sensitive'):
          entry.set_sensitive(value)
        elif (key == 'set'):
          entry.set_text(value)
        elif (key == 'tipo'):
          entry.connect('key-release-event', self.on_key_release, value)
          entry.connect('insert-text', self.on_insert_text, value)
    except Exception as e:
      print(e)
      entry = None
    return entry


  """
  Funcion para cuadros de dialogo encargados de mensajes de aviso o antes de operaciones importantes
  dic = {"titulo"       : 'pruebas',
         "tipo"         : 'info',
         "tituloDialog" :'titulo',
         "textDialog"   : 'mensaje'
  }
  """
  def dialogoBox(self, **args):
    try:
      win = c = messageDialogWin(args["tipo"].lower(), args["tituloDialog"], args["textDialog"])
      return c.respuesta
    except Exception as e:
      print(e)
      return False


  def comboBox(self, **args):
    try:
      cb = args["cb"] if 'cb' in args else self.builder.get_object(args["nombre"])
      if (args["tipo"] == 'cbox'):
        dblist = Gtk.ListStore(str)
        for data in args["lista"]:
          dblist.append([data])
      else:
        dblist = Gtk.ListStore(*args["num_el"])
        dblist.append(*args["lista"])
      cb.set_model(dblist)
      render = Gtk.CellRendererText()
      cb.pack_start(render, True)
      cb.add_attribute(render, 'text', 0)
      for key,value in args.items():
        if (key == 'evento'):
          value["widgets"] = value["widgets"] if 'widgets' in value else None
          cb.connect(value["tipo"], value["funcion"], value["widgets"])
    except Exception as e:
      print(e)
      cb = None
    return cb


  def getDataCombo(self, combo):
    data = None
    try:
      tree_iter = combo.get_active_iter()
      if tree_iter is not None:
        model = combo.get_model()
        data = model[tree_iter]
    except Exception as e:
      print(e)
    return data
