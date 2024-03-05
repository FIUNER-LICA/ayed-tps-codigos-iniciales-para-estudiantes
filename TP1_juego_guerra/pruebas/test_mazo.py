# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:23:53 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""


from modulos.carta import Carta
from modulos.mazo import Mazo
import unittest


class TestMazo(unittest.TestCase):
    def setUp(self):
        self.mazo= Mazo()

    def test_poner_sacar_arriba(self):            #Poner arriba al momento de repartir las cartas, sacar arriba al momento de jugar el turno
        carta1=Carta('5','trebol')
        carta2=Carta('3','corazones')
        self.mazo.poner_carta_arriba(carta1)
        self.mazo.poner_carta_arriba(carta2)
        self.assertIs(carta2, self.mazo.mazo.cabeza.dato)
        carta_control=self.mazo.sacar_carta_arriba()
        self.assertIs(carta2, carta_control)

    def test_poner_abajo(self):                     #Poner abajo al momento de ganar el turno
        carta1=Carta('5','trebol')
        carta2=Carta('3','corazones')
        self.mazo.poner_carta_abajo(carta1)
        self.mazo.poner_carta_abajo(carta2)
        self.assertIs(carta2, self.mazo.mazo.cola.dato)
        
        
if __name__ == '__main__':
    unittest.main()
