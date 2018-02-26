#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

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
            win = c = messageDialogWin(args["tipo"], args["tituloDialog"], args["textDialog"])
            return c.respuesta
        except Exception as e:
            print(e)
            return False
