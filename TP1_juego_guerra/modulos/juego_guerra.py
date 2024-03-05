# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:32:57 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""

from mazo import Mazo, DequeEmptyError
from carta import Carta
import random

N_TURNOS = 10000


class JuegoGuerra:
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
    palos = ['♠', '♥', '♦', '♣']
    
    def __init__(self, random_seed = 0):
        
        self._mazo_inicial = Mazo()
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._guerra = False
        self._ganador = ''
        self.empate = False
        self._turno = 0
        self._cartas_en_la_mesa = []
        self._seed = random_seed
    
    @property
    def mazo_1(self):
        return self._mazo_1
    
    @mazo_1.setter
    def mazo_1(self, valor):
        self._mazo_1 = valor
    
    @property
    def mazo_2(self):
        return self._mazo_2
    
    @mazo_2.setter
    def mazo_2(self, valor):
        self._mazo_2 = valor
        
    @property
    def empate(self):
        return self._empate
    
    @empate.setter
    def empate(self, valor):
        self._empate = valor
        
    @property
    def turnos_jugados(self):
        if self.empate:
            return N_TURNOS
        return self._turno + 1
           
    @property
    def ganador(self):
        return self._ganador
        
    def armar_mazo_inicial(self):
        """representa el mazo inicial, este mazo se crea al inicio
        de cada partida mediante combinación de los números y palos 
        de la baraja para formar cartas
        """
        random.seed(self._seed)
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores
                  for palo in JuegoGuerra.palos]
        
        #cartas_shuffled = random.sample(cartas, len(cartas))
        random.shuffle(cartas)
        cartas_shuffled = cartas
        
        for carta in cartas_shuffled:
            self._mazo_inicial.poner_carta_arriba(carta)
        
        return self._mazo_inicial
    
    def repartir_cartas(self):
        """reparte el mazo inicial entre los dos jugadores"""
        while len(self._mazo_inicial):
            carta_1 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_1.poner_carta_arriba(carta_1)
            carta_2 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_2.poner_carta_arriba(carta_2) 
            
        return self.mazo_1, self.mazo_2
    
    def iniciar_juego(self, ver_partida=True):
        
        self.armar_mazo_inicial()
        self.repartir_cartas()
        
        self._cartas_en_la_mesa = []
        self._turno = 0
        
        while len(self.mazo_1) and len(self.mazo_2) and self._turno != N_TURNOS:            
            try:
                if self._guerra:
                    for _ in range(3):
                        self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba())
                        self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba())
                
                self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba(mostrar=True))
                self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba(mostrar=True))
            
            except DequeEmptyError:
                #un mazo se quedó sin cartas durante el turno
                #declaro ganador al jugador que tiene cartas
                #debido al orden, el jugador 1 se queda primero sin cartas
                if len(self.mazo_1):
                    self._ganador = 'jugador 1'
                else:
                    self._ganador = 'jugador 2'
                self._guerra = False
                if ver_partida:
                    print(f'             ***** {self._ganador} gana la partida*****                           ')  
                
            else:
                if ver_partida:
                    self.mostrar_juego()
               
                if  self._cartas_en_la_mesa[-2] >  self._cartas_en_la_mesa[-1]:
                    for carta in self._cartas_en_la_mesa:
                        self.mazo_1.poner_carta_abajo(carta)
                    self._cartas_en_la_mesa = []
                    self._guerra = False
                    if len(self.mazo_2):
                        #si el mazo del oponente se queda sin cartas
                        #el juego debe terminar sin incrementar
                        #el número de turnos
                        self._turno += 1
                elif  self._cartas_en_la_mesa[-1] > self._cartas_en_la_mesa[-2]:
                    for carta in self._cartas_en_la_mesa:
                        self.mazo_2.poner_carta_abajo(carta)
                    self._cartas_en_la_mesa = []
                    self._guerra = False
                    if len(self.mazo_1):                        
                        #si el mazo del oponente se queda sin cartas
                        #el juego debe terminar sin incrementar
                        #el número de turnos
                        self._turno += 1
                else:
                    self._guerra = True
                    if ver_partida:
                        print('                      **** Guerra!! ****                       ')
            
            finally:                       
                if self._turno == N_TURNOS:
                    self.empate = True
                    if ver_partida:
                        print('                       ***** Empate *****                           ')  
                    
        if self._turno != N_TURNOS and not self._ganador: 
            if len(self.mazo_1):
                self._ganador = 'jugador 1'
            else:
                self._ganador = 'jugador 2'              
            if ver_partida:
                print(f'           ***** {self._ganador} gana la partida*****                           ')  
                      
        
        
    def mostrar_juego(self):
        # diferenciar las cartas del mazo y las 
        # cartas en la mesa
        print(f"Turno: {self._turno+1}")
        print('jugador 1:')        
        print(self.mazo_1)
        print()
        print('              ', end='')
        for carta in self._cartas_en_la_mesa:
            print(carta, end=' ')
        print('\n')
        print('jugador 2:')
        print(self.mazo_2)            
        print()
        print('------------------------------------')
        if self._ganador:
             print(f'         ***** 3){self._ganador} gana la partida*****                           ')  


if __name__ == "__main__":

    n = random.randint(0, 1000)
    juego = JuegoGuerra(random_seed=n)
    juego.iniciar_juego()
    
    print(n)
