# -*- coding: utf-8 -*-


import unittest
from modulos.abb import ABB
import numpy as np


class Testabb(unittest.TestCase):
    
    def setUp(self):
        self.abb = ABB()
    
    def agregar_claves(self, *args):
        for value in args:
            self.abb.agregar(clave=value, valor=2*value)
    
    def tearDown(self):
        pass
    
    def test_busqueda(self):
        claves = [45, 100, 20, 80, 55, 25, 18]
        self.agregar_claves(*claves)
        for clave in claves:
            self.assertEqual( self.abb.obtener(clave), 2*clave )        
    
    def test_insercion(self):
        """
        Verifica la insercion binaria tradicional
        """
        self.agregar_claves(45, 100, 20, 80, 10, 110, 50)
        # verifico posicion relativa desde la raiz
        self.assertEqual(self.abb.raiz.clave, 45,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.cargaUtil, 90,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoDerecho.clave, 100,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoDerecho.cargaUtil, 200,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoIzquierdo.clave, 20,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoIzquierdo.cargaUtil, 40,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoDerecho.hijoIzquierdo.clave, 80,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoDerecho.hijoIzquierdo.cargaUtil, 160,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoIzquierdo.hijoIzquierdo.clave, 10,
                         "Nodo insertado incorrectamente")
        self.assertEqual(self.abb.raiz.hijoIzquierdo.hijoIzquierdo.cargaUtil, 20,
                         "Nodo insertado incorrectamente")
        # verifico nodos hojas
        self.assertTrue(self.abb.raiz.hijoIzquierdo.hijoIzquierdo.esHoja(), 
                        "Nodo 10 debe ser un nodo hoja")
        self.assertTrue(self.abb.raiz.hijoDerecho.hijoIzquierdo.hijoIzquierdo.esHoja(), 
                        "Nodo 50 debe ser un nodo hoja")
        self.assertTrue(self.abb.raiz.hijoDerecho.hijoDerecho.esHoja(), 
                        "Nodo 110 debe ser un nodo hoja")
        # verifico nodos internos
        self.assertFalse(self.abb.raiz.esHoja(), 
                         "Nodo 45 debe ser nodo interno, no un nodo hoja")
        self.assertFalse(self.abb.raiz.hijoIzquierdo.esHoja(), 
                         "Nodo 20 debe ser nodo interno, no un nodo hoja")
        self.assertFalse(self.abb.raiz.hijoDerecho.esHoja(), 
                         "Nodo 100 debe ser un nodo interno, no un nodo hoja")
        self.assertFalse(self.abb.raiz.hijoDerecho.hijoIzquierdo.esHoja(), 
                         "Nodo 80 debe ser un nodo interno, no un nodo hoja")
    
    def test_operador_contains(self):
        """
        Verifica la sobrecarga del operador 'in', que corrobora si
        un elemento está o no en el ABB
        """
        self.agregar_claves(45, 100, 20, 80, 10)
        self.assertTrue( 100 in self.abb )
        self.assertTrue( 10 in self.abb )
        self.assertFalse( 1 in self.abb )
    
    def test_recorrido(self):
        """
        Para evaluar el recorrido, los elementos del árbol deben 
        recorrerse in-orden al iterar sobre él en un ciclo for
        """
        # tratamos de evitar tener claves repetidas
        claves = list(set(np.random.randint(0,1000, (100,))))
        np.random.shuffle(claves)
        self.agregar_claves(*claves)
        # comparo recorrido del árbol con lista ordenada
        claves = np.sort(claves)
        for n, item in enumerate(self.abb):
            self.assertEqual(claves[n], item[0])
    
    def test_eliminacion(self):
        """
        Verifica los distintos casos de eliminacion en un arbol
        """
        self.agregar_claves(100, 50, 20, 35, 75, 110, 105, 137, 150, 
                 145, 25, 170, 80, 120, 22, 125, 108, 79, 115, 130, 60)
        # elimino nodo hoja izquierdo
        self.abb.eliminar(clave=115)
        self.assertFalse( 115 in self.abb,
                         msg="Elemento sigue figurando en el arbol")
        self.assertIs( self.abb.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.hijoIzquierdo, None, 
                         msg="Procedimiento erroneo de eliminacion de nodo hoja" )
        # elimino nodo hoja derecho
        self.abb.eliminar(clave=130)
        self.assertFalse( 130 in self.abb,
                         msg="Elemento sigue figurando en el arbol")
        self.assertIs( self.abb.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.hijoDerecho.hijoDerecho, None, 
                         msg="Procedimiento erroneo de eliminacion de nodo hoja" )
        # elimino nodo con un hijo izquierdo
        self.abb.eliminar(clave=35)
        self.assertFalse( 35 in self.abb,
                         msg="Elemento sigue figurando en el arbol")
        self.assertEqual( self.abb.raiz.hijoIzquierdo.hijoIzquierdo.hijoDerecho.clave, 25, 
                         msg="Procedimiento erroneo de eliminacion de nodo con un hijo" )
        # elimino nodo con un hijo derecho
        self.abb.eliminar(clave=120)
        self.assertFalse( 120 in self.abb,
                         msg="Elemento sigue figurando en el arbol")
        self.assertEqual( self.abb.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.clave, 125, 
                         msg="Procedimiento erroneo de eliminacion de nodo con un hijo" )
        # elimino nodo con hijo derecho e izquierdo (reemplazo con sucesor)
        self.abb.eliminar(clave=110)
        self.assertFalse( 110 in self.abb,
                         msg="Elemento sigue figurando en el arbol")
        self.assertEqual( self.abb.raiz.hijoDerecho.clave, 125, 
                         msg="Procedimiento erroneo de eliminacion de nodo con dos hijos: " +
                             "debe ser con reemplazo con sucesor" )
        self.assertIs( self.abb.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo, None,
                         msg="No se elimino el nodo sucesor de su posicion original" )
        # elimino nodo raiz (reemplazo con sucesor)
        self.abb.eliminar(clave=100)
        self.assertFalse( 100 in self.abb,
                         msg="Elemento sigue figurando en el arbol")
        self.assertEqual( self.abb.raiz.clave, 105, 
                         msg="Procedimiento erroneo de eliminacion de nodo con dos hijos: " +
                             "debe ser con reemplazo con sucesor" )
        self.assertIs( self.abb.raiz.hijoDerecho.hijoIzquierdo.clave, 108,
                         msg="No se elimino correctamente el nodo " +
                         "sucesor de su posicion original" )
    
    def test_tamano(self):
        # insercion
        claves = [5, 7, 3, 4, 9, 1, 6, 8]
        self.assertEqual(self.abb.tamano, 0, "Al instanciar el ABB, su tamaño debe ser cero")
        for n, i in enumerate(claves):
            self.abb.agregar(clave=i, valor=2*i)
            self.assertEqual(self.abb.tamano, n+1, f"ABB deberia tener {n+1} elementos")
        self.assertEqual(len(self.abb), len(claves), "El operador len() debería estar correctamente sobrecargado")
        # eliminacion
        size = len(self.abb)
        for n, i in enumerate(claves):
            self.abb.eliminar(clave=i)
            self.assertEqual(self.abb.tamano, size-1-n, f"ABB deberia tener {size-1-n} elementos")
        # (re)agregado
        np.random.shuffle(claves)
        for n, i in enumerate(claves):
            self.abb.agregar(clave=i, valor=2*i)
            self.assertEqual(self.abb.tamano, n+1, f"ABB deberia tener {n+1} elementos")
    
    def test_excepciones(self):
        """
        Asegura que se lancen debidamente las excepciones al realizar 
        operaciones inválidas
        """
        claves = [45, 100, 20, 80, 55, 25, 18]
        self.agregar_claves(*claves)
        # eliminacion de elemento que no esta en el arbol
        with self.assertRaises(Exception, msg='Debe arrojar error si se elimina elemento que no esta en el arbol') as _:
            self.abb.eliminar(clave=120)
        # acceso a clave que no existe en el arbol
        with self.assertRaises(Exception, msg='Debe arrojar error si se pide el valor de una clave inexistente') as _:
            self.abb.obtener(clave=50)
        # Por el momento se permite que se agreguen claves repetidas,
        # se deja libertad al programador si permite agregarlo mas de
        # una vez o sobrescribe el valor previo.
        
    def test_sobrecarga_indexacion(self):
        """
        Verifica que el ABB tenga sobrecargado los métodos necesarios
        para poder asignar, acceder y eliminar elementos mediante 
        indexación (es decir, con los corchetes)
        """
        claves = [45, 100, 20, 80, 55, 25, 18]
        # asignacion por indexado
        # por el momento no se verifica sobrescritura de carga util
        for i in claves:
            self.abb[i] = 2*i
        self.assertEqual(len(self.abb), len(claves))
        # acceso por indexado
        for i in claves:
            self.assertEqual(self.abb[i], 2*i)
        # eliminacion por indexado
        for i in claves:
            del self.abb[i]
        self.assertEqual(len(self.abb), 0)
        
    
if __name__ == '__main__':
    unittest.main()
