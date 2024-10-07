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

        # Se colocan las cartas arriba
        self.mazo.poner_carta_arriba(carta1)
        self.mazo.poner_carta_arriba(carta2)

        # Se sacan las cartas arriba
        carta_control = self.mazo.sacar_carta_arriba()
        self.assertIs(carta2, carta_control)

        #Se verifica que la carta que queda en el mazo se la que se coloco primero
        carta_control = self.mazo.sacar_carta_arriba()
        self.assertIs(carta1, carta_control)


    def test_poner_abajo(self):                     #Poner abajo al momento de ganar el turno
        carta1=Carta('5','trebol')
        carta2=Carta('3','corazones')

        # Se colocan las cartas abajo
        self.mazo.poner_carta_abajo(carta1)
        self.mazo.poner_carta_abajo(carta2)

        # Sacamos la carta superior (que debería ser la primera que pusimos en la parte de arriba)
        carta_control = self.mazo.sacar_carta_arriba()
        self.assertIs(carta1, carta_control)  # La carta que sacamos debe ser carta1, ya que fue la primera en ponerse abajo

        # Sacamos la siguiente carta, que debería ser la carta que pusimos al final (carta2)
        carta_control = self.mazo.sacar_carta_arriba()
        self.assertIs(carta2, carta_control)  # La siguiente carta debe ser carta2
        
        
if __name__ == '__main__':
    unittest.main()
