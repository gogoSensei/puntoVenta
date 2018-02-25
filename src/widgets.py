#!/usr/bin/python3

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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
