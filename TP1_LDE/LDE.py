# Lista Doble Enlazada utilizando nodos y referencias

class Nodo:
    def __init__(self, dato):
        pass

    # getter y setters para los atributos del nodo

class ListaDobleEnlazada:
    def __init__(self):
        pass

   # getters y setters para los atributos de la LDE

    def agregar_al_inicio(self, dato):
        pass

    def agregar_al_final(self, dato):
        pass

    def insertar(self, dato, posicion):
        pass

    def extraer(self, posicion=None):
        pass

    def copiar(self):
        pass

    def invertir(self):
        pass

    def concatenar(self, otra_lista):
        pass        

    def esta_vacia(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __add__(self, otra_lista):
        pass
    
    def __str__(self):
        pass

if __name__ == "__main__":
    #prueba de metodos
    lista = ListaDobleEnlazada()

    lista.agregar_al_inicio(1)
    lista.agregar_al_inicio(2)
    lista.agregar_al_inicio(3)
    lista.agregar_al_final(4)
    lista.agregar_al_final(5)
    lista.agregar_al_final(6)
    
    print(lista)
