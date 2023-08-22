# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:23:53 2022

@author: je_su
"""


from modulos.juego_guerra import JuegoGuerra
import unittest


class TestMazo(unittest.TestCase):
    def setUp(self):
        self.mazo= Mazo()

# Chequeo de repartir/poner arriba, sacar arriba/principio y poner abajo/final
    def test_poner_sacar_arriba(self):            #Poner arriba al momento de repartir las cartas, sacar arriba al momento de jugar el turno
        carta1=Carta('5','trebol')
        self.mazo.poner_arriba(carta1)
        self.assertIs(carta1, self.mazo.mazo.items[0])
        carta2=self.mazo.sacar_arriba()
        self.assertIs(carta1, carta2)

# def test_poner_abajo(self):                     #Poner abajo al momento de ganar el turno
        
        
        
if __name__ == '__main__':
    unittest.main()
