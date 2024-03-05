# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:23:53 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""


from modulos.juegoGuerra import JuegoGuerra
import unittest


class TestJuegoGuerra(unittest.TestCase):
    
    def test_resulta_gana_jugador1(self):
        """
        Compruebo el número de turnos de 3 partidas con
        el jugador 1 como ganador
        """

        # jugador 1 gana la partida en el turno 137
        self.juego_1 = JuegoGuerra(random_seed=314)
        # jugador 1 gana la partida en el turno 638
        self.juego_2 = JuegoGuerra(random_seed=59)
        # jugador 1 gana la partida en el turno 1383
        self.juego_3 = JuegoGuerra(random_seed=883)

        self.juego_1.iniciar_juego(ver_partida=False)
        self.juego_2.iniciar_juego(ver_partida=False)
        self.juego_3.iniciar_juego(ver_partida=False)
        
        self.assertEqual(self.juego_1.turnos_jugados, 137)
        self.assertEqual(self.juego_1.ganador, 'jugador 1')
        
        self.assertEqual(self.juego_2.turnos_jugados, 638)
        self.assertEqual(self.juego_2.ganador, 'jugador 1')
        
        self.assertEqual(self.juego_3.turnos_jugados, 1383)
        self.assertEqual(self.juego_3.ganador, 'jugador 1')
        
    
    def test_resulta_gana_jugador2(self):
        """
        compruebo el número de turnos de 3 partidas con
        el jugador 2 como ganador
        """

        # jugador 2 gana la partida en el turno 145
        self.juego_4 = JuegoGuerra(random_seed=167)
        # jugador 2 gana la partida en el turno 1112
        self.juego_5 = JuegoGuerra(random_seed=190)
        # jugador 2 gana la partida en el turno 1373 por Guerra
        self.juego_6 = JuegoGuerra(random_seed=735)

        self.juego_4.iniciar_juego(ver_partida=False)
        self.juego_5.iniciar_juego(ver_partida=False)
        self.juego_6.iniciar_juego(ver_partida=False)
        
        self.assertEqual(self.juego_4.turnos_jugados, 145)
        self.assertEqual(self.juego_4.ganador, 'jugador 2')
        
        self.assertEqual(self.juego_5.turnos_jugados, 1112)
        self.assertEqual(self.juego_5.ganador, 'jugador 2')
        
        self.assertEqual(self.juego_6.turnos_jugados, 1373)
        self.assertEqual(self.juego_6.ganador, 'jugador 2')
    
    def test_resulta_empate(self):
        """
        compruebo el resultado de 2 partidas con empate
        """

        # juego empate
        self.juego_7 = JuegoGuerra(random_seed=547)
        self.juego_8 = JuegoGuerra(random_seed=296)

        self.juego_7.iniciar_juego(ver_partida=False)
        self.juego_8.iniciar_juego(ver_partida=False)
        
        self.assertTrue(self.juego_7.empate)
        self.assertTrue(self.juego_8.empate)
    
    
if __name__ == '__main__':
    unittest.main()
