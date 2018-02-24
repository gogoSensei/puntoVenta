#!/usr/bin/python3

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class main(object):
    """docstring for logIn."""
    def __init__(self):
        # Conexión a archivo galde
        builder = Gtk.Builder()
        builder.add_from_file("./gld/login.glade")
        # Obteniendo todos los widgets
        boton_entrar = builder.get_object("bt_entrar")
        boton_cancelar = builder.get_object("bt_cancel")
        entry_user = builder.get_object("e_usuario")
        entry_contrasena = builder.get_object("e_contrasena")
        window = builder.get_object("window1")
        # Activando las señales
        entry_user.has_focus()
        entry_user.connect("activate", self.onEntryValue, entry_contrasena)
        window.connect("delete-event", Gtk.main_quit)
        boton_entrar.connect("clicked", self.onButtonPressed)
        boton_cancelar.connect("clicked", self.onButtonPressed2)
        window.show_all()
        Gtk.main()

    def onButtonPressed(self, button):
        print("Hello World!")

    def onButtonPressed2(self, button):
        print("Hello cancel!")

    def onEntryValue(self, entry, entry2):
        entry_contrasena = entry2
        entry_contrasena.set_text("hello")
        print("Hello entry")
