# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:00:21 2022

@author: Belén
"""

from modulos.LDE import Nodo, ListaDobleEnlazada
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
        self.lista_aux_2 = random.choices(range(-self.n_elementos//2, self.n_elementos//2), k=self.n_elementos)
        for item in self.lista_aux_2:
            self.lde_2.agregar_al_final(item)
            
        """LDE de elementos no repetidos con lista auxiliar"""
        self.lde_3 = ListaDobleEnlazada()
        self.lista_aux_3 = random.sample(range(-self.n_elementos, self.n_elementos), self.n_elementos)
        for item in self.lista_aux_3:
            self.lde_3.agregar_al_final(item)
        
       
        self.posicion = random.randint(1, self.n_elementos-1) #randint incluye el extremo
        
    def test_iteracion(self):
        """
        Verificamos que tenga sobrecargado los métodos necesarios para ser
        iterado en un bucle for.
        En cada iteración debe devolver el dato siguiente, no el nodo.
        """

        nodo = self.lde_2.cabeza
        for dato in self.lde_2:
            self.assertEqual(nodo.dato, dato,
                             "La lista no arroja los datos de sus nodos correctamente al ser iterado en un for")
            nodo = nodo.siguiente
    
    def test_agregar_al_inicio(self):
        """
        pruebo que al agregar elementos al inicio de la lista
        la misma tiene tamaño correcto y se llena correctamente      
        """
        lista_aux = []
        for _ in range(self.n_elementos):
            item = random.randint(-self.n_elementos//2, self.n_elementos//2)
            lista_aux.insert(item, 0)
            self.lde_1.agregar_al_inicio(item)
        
        self.assertEqual(self.lde_1.tamanio, self.n_elementos)
        
        for ind, dato in enumerate(self.lde_1):
            self.assertEqual(dato, lista_aux[ind])
    
    def test_agregar_al_final(self):
        """
        pruebo que al anexar elementos al final de la lista
        la misma tiene tamaño correcto y se llena correctamente
        """
        lista_aux = []
        for _ in range(self.n_elementos):
            item = random.randint(-self.n_elementos//2, self.n_elementos//2)
            lista_aux.append(item)
            self.lde_1.agregar_al_final(item)
            
        self.assertEqual(self.lde_1.tamanio, self.n_elementos)
        
        for ind, dato in enumerate(self.lde_1):
            self.assertEqual(dato, lista_aux[ind])
            
    def test_insertar_extremos(self):
        """
        inserto ítems en los extremos de la LDE, compruebo 
        tamaño correcto y su valor.
        """

        """inserto 1er item al inicio"""
        self.lde_2.insertar(120, 0)
        self.n_elementos += 1
        self.assertEqual(self.lde_2.tamanio, self.n_elementos)
        self.assertEqual(self.lde_2.cabeza.dato, 120)
        
        """inserto 2do item en la última posición"""
        self.lde_2.insertar(180, self.lde_2.tamanio-1)
        self.n_elementos += 1
        self.assertEqual(self.lde_2.tamanio, self.n_elementos)
        nodo_anterior = None
        nodo_actual = self.lde_2.cabeza
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
        print(f"\nPosición aleatoria donde se inserta: {self.posicion}")
        
        self.lde_2.insertar(250, self.posicion)
        self.n_elementos += 1
        self.assertEqual(self.lde_2.tamanio, self.n_elementos)
        
        contador = 0
        nodo_actual = self.lde_2.cabeza
        while nodo_actual and contador != self.posicion:            
            contador += 1
            nodo_actual = nodo_actual.siguiente 
            valor = nodo_actual.dato 
            
        self.assertEqual(valor, 250)
    
    def test_excepciones_insertar(self):
        """
        intento insertar en posiciones incorrectas o no existentes de
        la LDE y compruebo que se lanzan las excepciones correspondientes
        """               
        self.assertRaises(Exception, self.lde_2.insertar, 210, -10)
        self.assertRaises(Exception, self.lde_2.insertar, 234, -(self.n_elementos + 10))
        self.assertRaises(Exception, self.lde_2.insertar, 220, self.n_elementos + 10)


    def test_extraer_extremos(self):
        """
        pruebo extraer ítems al inicio y al final de la LDE
        con/sin parámetro, verifico el valor extraído y el tamaño
        resultante de la LDE
        """
        """al inicio"""
        self.assertEqual(self.lde_3.extraer(0).dato, self.lista_aux_3[0])
        self.assertEqual(self.lde_3.tamanio, self.n_elementos-1)
        """al final sin parámetro"""
        self.assertEqual(self.lde_3.extraer().dato, self.lista_aux_3[-1])
        self.assertEqual(self.lde_3.tamanio, self.n_elementos-2)
        """al final usando parámetro"""
        self.assertEqual(self.lde_3.extraer(self.lde_3.tamanio-1).dato, self.lista_aux_3[-2])
        self.assertEqual(self.lde_3.tamanio, self.n_elementos-3)
        """al final parámetro -1"""
        self.assertEqual(self.lde_3.extraer(-1).dato, self.lista_aux_3[-3])
        self.assertEqual(self.lde_3.tamanio, self.n_elementos-4)
        
    def test_extraer_interior(self):
        """
        extraigo un elemento de una posición aleatoria de la lista
        con elementos no repetidos y compruebo que el mismo no permanece
        en la lista
        """
        print(f"\nPosición aleatoria donde se extrae: {self.posicion}")
        item = self.lde_3.extraer(self.posicion)
        print(f"ítem extraído: {item}")
        nodo_actual = self.lde_3.cabeza
        
        while nodo_actual:            
            self.assertNotEqual(item, nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente 
        
        self.assertEqual(self.lde_3.tamanio, self.n_elementos-1)    
        
    def test_excepciones_extraer(self):
        """
        pruebo extraer en una lista vacía y en posiciones fuera
        de los límites de la LDE. Compruebo las excepciones
        """ 
        """LDE vacía"""             
        self.assertRaises(Exception, self.lde_1.extraer)
        self.assertRaises(Exception, self.lde_1.extraer, 0)
        self.assertRaises(Exception, self.lde_1.extraer, -1)
        self.assertRaises(Exception, self.lde_1.extraer, self.n_elementos-1)
        self.assertRaises(Exception, self.lde_1.extraer, self.n_elementos + 10)
        self.assertRaises(Exception, self.lde_1.extraer, -(self.n_elementos + 10))
        """LDE con elementos entre -100 y 100"""
        self.assertRaises(Exception, self.lde_2.extraer, -(self.n_elementos + self.n_elementos/4))
        self.assertRaises(Exception, self.lde_2.extraer, (self.n_elementos + self.n_elementos/4))
        """LDE co elementos entre -200 y 200"""
        self.assertRaises(Exception, self.lde_3.extraer, (self.n_elementos + self.n_elementos/2))
        self.assertRaises(Exception, self.lde_3.extraer, -(self.n_elementos + self.n_elementos/2))
     
    
    def test_mostrar_por_consola(self):
        """
        compruebo que la LSE se muestre por consola como una lista de
        elementos, donde cada elemento muestra el atributo "dato" del nodo
        correspondiente en la LSE
        """
        self.assertEqual(str(self.lista_aux_3), str(self.lde_3))
    
            
    def auxiliar_copiar(self, lista_original, lista_copia):
        """
        función auxiliar para el test del método copiar
        """
        nodo_original = lista_original.cabeza
        nodo_copia = lista_copia.cabeza
        
        self.assertEqual(lista_original.tamanio, lista_copia.tamanio)
        
        while nodo_original or nodo_copia: #termina si ambos son None
            self.assertEqual(nodo_original.dato, nodo_copia.dato)
            nodo_original = nodo_original.siguiente
            nodo_copia = nodo_copia.siguiente
        
    
    def test_copiar(self):
        """
        hago una copia de una LDE con elementos y sin elementos
        y comparo nodo a nodo para verificar la copia.
        compruebo que se hace la copia del contenido de cada nodo
        remuevo un nodo de la copia en una posición aleatoria, modifico
        el contenido del nodo y verifico que el contenido del nodo en la 
        misma posición en la lista original no se modificó.        
        """
        lde_3_copia = self.lde_3.copiar()
        self.auxiliar_copiar(self.lde_3, lde_3_copia)
        
        lde_1_copia = self.lde_1.copiar()
        self.auxiliar_copiar(self.lde_1, lde_1_copia)
    
        self.posicion = 5
        #extraigo de la copia un nodo         
        nodo_extraido = lde_3_copia.extraer(self.posicion)        
        dato_original = nodo_extraido.dato
       
        #modifico el nodo extraído
        nodo_extraido.dato =  3*self.n_elementos #valor fuera del rango
  
        #compruebo que el contenido en la lista original
        #en la posición del nodo extraído no se modifica
        contador = 0
        nodo_actual = self.lde_3.cabeza        
        for _ in range(self.posicion):
            nodo_actual = nodo_actual.siguiente 
            contador += 1             
            
        self.assertEqual(dato_original, nodo_actual.dato)
       
    
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
   
        nodo_inicio = lista_copia.cabeza
        nodo_fin = self.lde_1.cola 
        
        for _ in range(self.n_elementos):
            
            self.assertEqual(nodo_inicio.dato, nodo_fin.dato)
            
            nodo_inicio = nodo_inicio.siguiente
            nodo_fin = nodo_fin.anterior       
            
    
    def test_ordenar(self):
        """
        Ordeno dos listas con los mismos elementos: una lista de Python con
        el método sort() y una LDE con el método ordenar().
        Comparo los resultados nodo a nodo y verifico que sean iguales.
        
        """
        self.lde_3.ordenar()
        self.lista_aux_3.sort()
        
        for i,nodo in enumerate(self.lde_3):
            
            self.assertEqual(self.lista_aux_3[i], nodo.dato)
            
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
        while nodo is not None:
            counter += 1
            elementos.append(nodo.dato)
            nodo = nodo.siguiente
        self.assertEqual(len(lista), counter,
                         "Tamaño informado por la lista no coincide con cantidad de nodos en la misma.")

        # Recorro de atras para adelante
        nodo = lista.cola
        while nodo is not None:
            counter -= 1
            nodo = nodo.anterior
            self.assertEqual(elementos[counter], nodo.dato,
                             "Los elementos en la lista recorrida de atras para adelante son diferentes "
                             "a que si la recorremos de adelante para atrás.")


    def test_metodo_concatenar(self):
        """
        Verifico que funcione bien la concatenacion de listas mediante el metodo
        concatenar.
        """        
        # lista_concatenada1 = self.lista_aux_3 + self.lista_aux_2
        lista_concatenada1 = self.lde_3.concatenar(self.lde_2)

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
       
           