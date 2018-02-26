#!/usr/bin/python3
# -*- coding: utf-8 -*-

############# Isidro Rivera Monjaras ############
#############       19/02/2018       ############

from src.widgets import widgetsUse

class ventanaInicio(widgetsUse):
    """docstring for ventanaInicio."""
    def __init__(self):
        super().__init__(gld="./gld/inicio.glade")
        window = self.windows(nombre="window1")
        window.show_all()
