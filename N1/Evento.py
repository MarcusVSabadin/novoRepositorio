# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:11:52 2022

@author: user_lc4_59
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:33:03 2022

@author: user_lc4_57
"""

class Evento:
    
    #construtor
    def __init__(self):
        self.Eventos = []
        
    def insereEvento(self, evento):
        self.Eventos.append(evento)
        
    def retornaEventos(self):
        return self.Eventos
    