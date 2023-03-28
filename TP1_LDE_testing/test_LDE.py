# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:00:21 2022
@author: Catedra de Algoritmos y Estructura de Datos
"""

from modulos import ListaDobleEnlazada
import unittest
import random


class Test_LDE(unittest.TestCase):
    """Test de la clase ListaDobleEnlazada"""

    def setUp(self):
        self.n_elementos = 200
        """ LDE vacía """
        self.lde_1 = ListaDobleEnlazada()

        """ LDE con elementos repetidos con lista auxiliar"""
        self.lde_2 = ListaDobleEnlazada()
        self.lista_aux_2 = random.choices(range(-self.n_elementos // 2, self.n_elementos // 2), k=self.n_elementos)
        for item in self.lista_aux_2:
            self.lde_2.agregar_al_final(item)

        """LDE de elementos no repetidos con lista auxiliar"""
        self.lde_3 = ListaDobleEnlazada()
        self.lista_aux_3 = random.sample(range(-self.n_elementos, self.n_elementos), self.n_elementos)
        for item in self.lista_aux_3:
            self.lde_3.agregar_al_final(item)

        # self.posicion = random.randint(1, self.n_elementos - 1)  # randint incluye el extremo

    def test_iteracion(self):
        """
        Verificamos que tenga sobrecargado los métodos necesarios para ser
        iterado en un bucle for.
        En cada iteración debe devolver el dato siguiente, no el nodo.
        """

        nodo = self.lde_2.cabeza
        for dato in self.lde_2:
            self.assertEqual(nodo.dato, dato,
                             "Los datos arrojados en el for no coinciden con los datos "
                             "obtenidos por recorrido manual de la LDE desde la cabeza")
            nodo = nodo.siguiente

    def test_agregar_al_inicio(self):
        """
        pruebo que al agregar elementos al inicio de la lista
        la misma tiene tamaño correcto y se llena correctamente
        """
        valorNuevo = 25

        # Agregar al inicio de lista no vacia
        lde2_copia = self.lde_2.copiar()
        lde2_copia.agregar_al_inicio(valorNuevo)

        self.recorrer_lista(lde2_copia)
        self.assertEqual(len(self.lde_2), len(lde2_copia) - 1,
                         "El tamaño de la lista luego de agregar debe incrementarse en uno")

        nodo_copia = lde2_copia.cabeza
        self.assertEqual(nodo_copia.dato, valorNuevo,
                         "El primer nodo no contiene el valor que se solicito agregar")

        nodo_copia = nodo_copia.siguiente
        nodo_original = self.lde_2.cabeza
        while nodo_original.siguiente is not None:
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Se modificaron los datos de la lista luego de agregar el nuevo elemento")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente

        # Anexar en lista vacia (self.lde_1)
        lde1_copia = self.lde_1.copiar()
        lde1_copia.agregar_al_inicio(valorNuevo)

        self.recorrer_lista(lde1_copia)
        self.assertEqual(len(lde1_copia), 1,
                         "Al agregar un elemento al inicio de una lista vacia, su nuevo tamaño debe ser uno")

        self.assertEqual(lde1_copia.cabeza.dato, valorNuevo,
                         "El nodo agregado a la lista vacia no contiene el valor que se solicito agregar")
        self.assertIs(lde1_copia.cabeza, lde1_copia.cola,
                      "En una lista de un elemento, la cabeza es la misma que la cola")

    def test_agregar_al_final(self):
        """
        pruebo que al anexar elementos al final de la lista
        la misma tiene tamaño correcto y se llena correctamente
        """

        valorNuevo = 25

        # Anexar en lista no vacia
        lde2_copia = self.lde_2.copiar()
        lde2_copia.agregar_al_final(valorNuevo)

        self.recorrer_lista(lde2_copia)
        self.assertEqual(len(self.lde_2), len(lde2_copia) - 1,
                         "El tamaño de la lista luego de anexar debe incrementarse en uno")

        nodo_original = self.lde_2.cabeza
        nodo_copia = lde2_copia.cabeza
        while nodo_original.siguiente is not None:
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Se modificaron los datos de la lista luego de anexar el nuevo elemento")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente

        nodo_copia = nodo_copia.siguiente
        self.assertEqual(nodo_copia.dato, valorNuevo,
                         "El ultimo nodo no contiene el valor que se solicito agregar")
        self.assertIs(nodo_copia, lde2_copia.cola,
                      "El ultimo nodo no coincide con la refencia a la cola de la lista")

        # Anexar en lista vacia (self.lde_1)
        lde1_copia = self.lde_1.copiar()
        lde1_copia.agregar_al_final(valorNuevo)

        self.recorrer_lista(lde1_copia)
        self.assertEqual(len(lde1_copia), 1,
                         "Al anexar un elemento en una lista vacia, su nuevo tamaño debe ser uno")

        self.assertEqual(lde1_copia.cabeza.dato, valorNuevo,
                         "El nodo anexado a la lista vacia no contiene el valor que se solicito agregar")
        self.assertIs(lde1_copia.cabeza, lde1_copia.cola,
                      "En una lista de un elemento, la cabeza es la misma que la cola")

    def test_insertar_extremos(self):
        """
        inserto ítems en los extremos de la LDE, compruebo
        tamaño correcto y su valor.
        """

        """inserto 1er item al inicio"""
        self.lde_2.insertar(120, 0)
        self.n_elementos += 1
        self.assertEqual(len(self.lde_2), self.n_elementos)
        self.assertEqual(self.lde_2.cabeza.dato, 120)

        """inserto 2do item en la última posición"""
        self.lde_2.insertar(180, len(self.lde_2) - 1)
        self.n_elementos += 1
        self.assertEqual(len(self.lde_2), self.n_elementos)
        nodo_actual = self.lde_2.cabeza
        nodo_anterior = None
        valor = None
        while nodo_actual.siguiente:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            valor = nodo_anterior.dato
        self.assertEqual(valor, 180)

    def test_insertar_interior(self):
        """
        pruebo insertar un ítem en una posición aleatoria
        de la LDE y compruebo que el elemento es insertado
        """
        # print(f"\nPosición aleatoria donde se inserta: {self.posicion}")
        posicion = random.randint(1, self.n_elementos - 1)

        self.lde_2.insertar(250, posicion)
        self.n_elementos += 1
        self.assertEqual(self.lde_2.tamanio, self.n_elementos)

        contador = 0
        nodo_actual = self.lde_2.cabeza
        valor = None
        while nodo_actual and contador != posicion:
            contador += 1
            nodo_actual = nodo_actual.siguiente
            valor = nodo_actual.dato

        self.assertEqual(valor, 250)

    def test_excepciones_insertar(self):
        """
        intento insertar en posiciones incorrectas o no existentes de
        la LDE y compruebo que se lanzan las excepciones correspondientes
        """
        self.assertRaises(Exception, self.lde_2.insertar, 210, -10,
                          "La LDE debe arrojar excepcion al intentar insertar en posición negativa")
        self.assertRaises(Exception, self.lde_2.insertar, 210, self.n_elementos + 10,
                          "La LDE debe arrojar excepcion al intentar insertar en posición mayor al tamaño")

    def test_extraer_extremos(self):
        """
        pruebo extraer ítems al inicio y al final de la LDE
        con/sin parámetro, verifico el valor extraído y el tamaño
        resultante de la LDE
        """
        # Extraer al inicio
        self.assertEqual(self.lde_3.extraer(0), self.lista_aux_3.pop(0),
                         "No se extrajo correctamente los elementos de la lista")
        self.assertEqual(len(self.lde_3), self.n_elementos - 1,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        # Extraer al final sin parámetro
        self.assertEqual(self.lde_3.extraer(), self.lista_aux_3.pop(),
                         "Cuando no se pasa argumento, se debe extraer el ultimo elemento de la lista")
        self.assertEqual(len(self.lde_3), self.n_elementos - 2,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        # Extraer al final usando parámetro
        self.assertEqual(self.lde_3.extraer(len(self.lde_3) - 1), self.lista_aux_3.pop(),
                         "No se extrajo correctamente los elementos de la lista")
        self.assertEqual(self.lde_3.tamanio, self.n_elementos - 3,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        # Extraer al final parámetro -1
        self.assertEqual(self.lde_3.extraer(-1), self.lista_aux_3.pop(),
                         "No se extrajo correctamente los elementos de la lista")
        self.assertEqual(self.lde_3.tamanio, self.n_elementos - 4,
                         "No se actualizo debidamente el tamaño de la lista luego de extraer")
        # Verificamos que la lista este correctamente enlazada
        self.recorrer_lista(self.lde_3)

    def test_extraer_interior(self):
        """
        extraigo un elemento de una posición aleatoria de la lista
        con elementos no repetidos y compruebo que el mismo no permanece
        en la lista
        """
        posicion = random.randint(1, self.n_elementos - 1)
        lde3_copia = self.lde_3.copiar()

        item = lde3_copia.extraer(posicion)

        # Verifico tamaño
        self.assertEqual(len(lde3_copia), len(self.lde_3) - 1,
                         "No se modifico correctamente el tamaño de la lista luego de la extracción")

        # Verifico que este correctamente enlazada
        self.recorrer_lista(lde3_copia)

        nodo_original = self.lde_3.cabeza
        nodo_copia = lde3_copia.cabeza
        contador_pos = 0
        while nodo_original is not None:
            if contador_pos == posicion:
                self.assertEqual(nodo_original.dato, item,
                                 "El elemento extraido no coincide con el elemento originariamente en la posicion solicitada")
                nodo_original = nodo_original.siguiente
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Luego de la extracción los demás elementos de la lista se vieron alterados")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente
            contador_pos += 1

    def test_excepciones_extraer(self):
        """
        pruebo extraer en una lista vacía y en posiciones fuera
        de los límites de la LDE. Compruebo las excepciones
        """
        # LDE vacía
        self.assertRaises(Exception, self.lde_1.extraer,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer, 0,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer, -1,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer, self.n_elementos - 1,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer, self.n_elementos + 10,
                          "Extraer de una lista vacia deberia arrojar un error")
        self.assertRaises(Exception, self.lde_1.extraer, -(self.n_elementos + 10),
                          "Extraer de una lista vacia deberia arrojar un error")

        # LDE no vacia
        self.assertRaises(Exception, self.lde_2.extraer, -50,
                          "Extraer de una posicion negativa dede arrojar error")
        self.assertRaises(Exception, self.lde_2.extraer, self.n_elementos + 50,
                          "Extraer de una posicion mayor al tamaño de la lista menos uno dede arrojar error")

    def test_operador_len(self):
        """
        Prueba que este sobrecargado el operador len() para la LDE
        """
        self.assertEqual(len(self.lde_1), 0, "No funciona el operador len() en la LDE")
        self.assertEqual(len(self.lde_2), self.n_elementos, "No funciona el operador len() en la LDE")

    def test_copiar(self):
        """
        hago una copia de una LDE con elementos y sin elementos
        y comparo nodo a nodo para verificar la copia.
        """
        lde_3_copia = self.lde_3.copiar()

        # Compruebo la integridad fisica de la lista original
        self.recorrer_lista(self.lde_3)
        # Compruebo que la lista copiada este correctamente enlazada
        self.recorrer_lista(lde_3_copia)

        nodo_original = self.lde_3.cabeza
        nodo_copia = lde_3_copia.cabeza

        # Compruebo longitud de las listas
        self.assertEqual(len(lde_3_copia), len(self.lde_3),
                         "Los tamaños de las listas copiadas nos son las mismas.")
        # Compruebo que las listas sean instancias diferentes
        self.assertIsNot(lde_3_copia, self.lde_3.copiar,
                         "Las listas copiadas son referencias al mismo espacio de memoria.")

        while nodo_original or nodo_copia:
            # Compruebo igualdad del contenido de ambas listas
            self.assertEqual(nodo_original.dato, nodo_copia.dato,
                             "Los datos de la lista copiada no son iguales a los de la lista original")
            # Compruebo que los nodos de ambas listas sean instancias diferentes
            self.assertIsNot(nodo_original, nodo_copia,
                             "Los nodos de las lista copiada son compartidos con los de la lista original")
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente

    def test_invertir(self):

        """
        Creo una LDE con elementos aleatorios, realizo una copia de la misma,
        e invierto la original.
        Recorro las listas, una desde el inicio y la otra desde el final y
        verifico que el contenido de los nodos sea el mismo.

        """

        for _ in range(0, self.n_elementos):
            item = random.randint(-self.n_elementos, self.n_elementos)
            self.lde_1.agregar_al_inicio(item)

        lista_copia = self.lde_1.copiar()
        self.lde_1.invertir()

        # Verifico que sus elementos esten correctamente enlazados
        self.recorrer_lista(self.lde_1)

        nodo_invertido = lista_copia.cabeza
        nodo_original = self.lde_1.cola

        for _ in range(self.n_elementos):
            self.assertEqual(nodo_invertido.dato, nodo_original.dato)
            # Avanzo al siguiente nodo de lista invertida
            nodo_invertido = nodo_invertido.siguiente
            # Avanzo al siguiente nodo de lista original
            nodo_original = nodo_original.anterior

    def test_ordenar(self):
        """
        Ordeno dos listas con los mismos elementos: una lista de Python con
        el método sort() y una LDE con el método ordenar().
        Comparo los resultados nodo a nodo y verifico que sean iguales.

        """
        self.lista_aux_3.sort()
        self.lde_3.ordenar()

        # Verifico que la lista ordenada este correctamente enlazada
        self.recorrer_lista(self.lde_3)

        for i, dato in enumerate(self.lde_3):
            self.assertEqual(self.lista_aux_3[i], dato,
                             "Los datos en la lista no se ordenaron correctamente")

    def recorrer_lista(self, lista):
        """
        Metodo auxiliar para usar en tests de métodos complejos
        de la clase lista doblemente enlazada. Verifica que los nodos de la lista
        esten bien enlazados entre sí (forward y backward).
        """

        # Recorro de adelante para atras
        nodo = lista.cabeza
        counter = 0
        elementos = []

        self.assertIsNone(nodo.anterior,
                          "El elemento anterior a la cabeza de la lista debe ser None")

        while nodo is not None:
            counter += 1
            elementos.append(nodo.dato)
            nodo = nodo.siguiente

        self.assertEqual(len(lista), counter,
                         "Tamaño informado por la lista no coincide con la cantidad de nodos en la misma.")

        # Recorro de atras para adelante
        nodo = lista.cola

        self.assertIsNone(nodo.siguiente,
                          "El elemento siguiente a la cola de la lista debe ser None")

        while nodo is not None:
            counter -= 1
            self.assertEqual(elementos[counter], nodo.dato,
                             "Los elementos en la lista recorrida de atras para adelante son diferentes "
                             "a que si la recorremos de adelante para atrás.")
            nodo = nodo.anterior

    def test_metodo_concatenar(self):
        """
        Verifico que funcione bien la concatenacion de listas mediante el metodo
        concatenar. El metodo modifica la instancia que realiza la invocacion.
        """
        lista_concatenada1 = self.lde_3.copiar()
        lista_concatenada1.concatenar(self.lde_2)

        # Compruebo que las listas originales esten intactas
        self.recorrer_lista(self.lde_3)
        self.recorrer_lista(self.lde_2)

        # Compruebo que la lista concatenada este bien enlazada
        self.recorrer_lista(lista_concatenada1)

        # Verifico que los elementos resulten efectivamente de la concatenacion
        # en orden de la lista lde_3 con lde_2
        nodo_original = self.lde_3.cabeza
        nodo_concat = lista_concatenada1.cabeza
        while nodo_original is not None:
            self.assertEqual(nodo_original.dato, nodo_concat.dato,
                             "No coinciden los nodos de la lista 1 con la lista concatenada")
            nodo_original = nodo_original.siguiente
            nodo_concat = nodo_concat.siguiente
        nodo_original = self.lde_2.cabeza
        while nodo_original is not None:
            self.assertEqual(nodo_original.dato, nodo_concat.dato,
                             "No coinciden los nodos de la lista 2 con la lista concatenada")
            nodo_original = nodo_original.siguiente
            nodo_concat = nodo_concat.siguiente

    def test_operador_add(self):
        """
        Verifico que funcione la concatenacion de listas mediante
        el uso del operador +
        Este operador devuelve una LDE que reuslta de la concatenación de las
        dos LDE que recibe como operandos. Internamente no modifica ninguno
        de sus dos operandos.
        """
        # lista_concatenada1 = self.lista_aux_3 + self.lista_aux_2
        lista_concatenada1 = self.lde_3 + self.lde_2

        # Compruebo que las listas originales esten intactas
        self.recorrer_lista(self.lde_3)
        self.recorrer_lista(self.lde_2)

        # Compruebo que la lista concatenada este bien enlazada
        self.recorrer_lista(lista_concatenada1)

        # Verifico que los elementos resulten efectivamente de la concatenacion
        # en orden de la lista lde_3 con lde_2
        nodo_original = self.lde_3.cabeza
        nodo_concat = lista_concatenada1.cabeza
        while nodo_original is not None:
            self.assertEqual(nodo_original.dato, nodo_concat.dato,
                             "No coinciden los nodos de la lista 1 con la lista concatenada")
            nodo_original = nodo_original.siguiente
            nodo_concat = nodo_concat.siguiente
        nodo_original = self.lde_2.cabeza
        while nodo_original is not None:
            self.assertEqual(nodo_original.dato, nodo_concat.dato,
                             "No coinciden los nodos de la lista 2 con la lista concatenada")
            nodo_original = nodo_original.siguiente
            nodo_concat = nodo_concat.siguiente


if __name__ == "__main__":
    unittest.main()
