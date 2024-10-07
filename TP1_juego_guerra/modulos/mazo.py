# mazo.py

from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.__mazo = ListaDobleEnlazada()  # Inicializa el mazo como una lista doblemente enlazada
        
    def poner_carta_arriba(self, carta):
        self.__mazo.agregar_al_inicio(carta)  # Agrega una carta al inicio del mazo (arriba)
        
    def poner_carta_abajo(self, carta):
        self.__mazo.agregar_al_final(carta)  # Agrega una carta al final del mazo (abajo)
        
    def sacar_carta_arriba(self, mostrar=False):
        if len(self.__mazo) == 0:
            raise DequeEmptyError('El mazo está vacío')  # Lanza una excepción si el mazo está vacío
        carta = self.__mazo.extraer(0)  # Extrae la carta del inicio del mazo
        if mostrar:
            carta.visible = True  # Hace la carta visible si se solicita
        return carta  # Devuelve la carta extraída
    
    def __len__(self):
        return len(self.__mazo)  # Devuelve el número de cartas en el mazo
    
    def __iter__(self):
        return iter(self.__mazo)  # Hace que el mazo sea iterable
    
    def __str__(self):
        salida = ''
        for idx, carta in enumerate(self.__mazo):
            salida += str(carta) + ' '  # Agrega cada carta a la cadena de salida
            if idx % 10 == 9:
                salida += '\n'  # Agrega un salto de línea cada 10 cartas
        return salida  # Devuelve la representación en cadena del mazo}
    

