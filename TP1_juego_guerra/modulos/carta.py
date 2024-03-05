# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:51:54 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""

class Carta:
    
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible:bool = False
        
    @property
    def visible(self):
        return self._visible
        
    @visible.setter
    def visible(self, visible):
        self._visible = visible
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
        
    @property
    def palo(self):
        return self._palo
    
    @palo.setter
    def palo(self, palo):
        self._palo = palo  
    
    def _valor_numerico(self):
        valores = ['J','Q','K','A']
        if self.valor in valores:
            idx = valores.index(self.valor)
            return (11 + idx)
        return int(self.valor)            
            
        
    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()
        
    def __str__(self):
        if self.visible == False:
            return "-X"
        else:
            return self.valor + self.palo
    
    def __repr__(self):
        return str(self)
    
    
if __name__ == "__main__":
    carta = Carta("♣", "3")
    print(carta)
    carta.visible = True
    print(carta)
    