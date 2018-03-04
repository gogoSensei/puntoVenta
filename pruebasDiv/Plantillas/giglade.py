#!/usr/bin/env python
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def __init__(self, obgs):
      self.entry2 = obgs.get_object("entry2")
      self.window = obgs.get_object("window1")
      self.window.show_all()
      print(dir(self.window))
    
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")
    
    def on_button2_pressed(self, button):
        print("Pressed button 2")
    
    def on_entry1_key_press_event(self, entry, valor):
        #dato = entry.get_text()
        # 36 Enter
        # 23 tabulador
        if (valor.get_keycode()[1] in (36,23)):
            self.entry2.set_text("Hola mundo")
            self.window.set_focus(self.entry2)
            print("Hola mundo")
        
builder = Gtk.Builder()
builder.add_from_file("/home/isidro/Projects/puntoVenta/pruebasDiv/Plantillas/example.glade")
builder.connect_signals(Handler(builder))

Gtk.main()
