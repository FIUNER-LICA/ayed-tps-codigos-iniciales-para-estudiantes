import math
import random
import unittest

from ayedfiuner.estructuras.arbolAVL import ArbolAVL


class TestArbolAVL(unittest.TestCase):
    """Suite de pruebas unitarias exhaustivas para la estructura de datos Árbol AVL.

    A diferencia de un árbol binario de búsqueda (BST) convencional, un árbol
    AVL debe mantener cuatro propiedades o 'invariantes' en todo momento:
        1. Orden BST: Para todo nodo, hijo_izq < nodo < hijo_der.
        2. Factor de Equilibrio: FE en {-1, 0, 1} en cada nodo.
        3. Cota Logarítmica de Altura: Altura <= 1.44 * log2(N + 2).
        4. Consistencia del Tamaño: El atributo 'tamaño' coincide con la
        cantidad real de nodos.

    Esta suite combina pruebas de casos borde, pruebas estructurales de
    rotaciones y pruebas de volumen/estrés.
    """

    def setUp(self):
        """Se ejecuta automáticamente antes de cada método de prueba.

        Garantiza un entorno limpio y reproducible al fijar la semilla
        aleatoria.
        """
        self.arbol = ArbolAVL()
        random.seed(42)  # Permite reproducir exactamente cualquier fallo aleatorio

    # -------------------------------------------------------------------------
    # Método Auxiliar (Oráculo de Invariantes)
    # -------------------------------------------------------------------------
    def _validar_invariantes_avl(self, arbol):
        """Método 'oráculo' que verifica simultáneamente todas las reglas matemáticas

        que un árbol AVL válido debe cumplir obligatoriamente.

        Args:
            arbol (ArbolAVL): Árbol que se someterá a inspección.
        """
        # Obtenemos el recorrido inorden. En un BST correcto, el inorden
        # SIEMPRE devuelve las claves de forma estrictamente ascendente.
        recorrido = list(arbol.inorden())
        claves = [item.clave for item in recorrido]

        # 1. Validación de Propiedad de Orden BST (claves ordenadas)
        self.assertEqual(
            claves,
            sorted(claves),
            "Fallo de orden BST: Las claves en inorden no están estrictamente ordenadas.",
        )

        # 2. Validación de Claves Únicas (evita nodos duplicados silenciosos)
        self.assertEqual(
            len(set(claves)),
            len(claves),
            "Fallo de integridad: Existen claves duplicadas en la estructura.",
        )

        # 3. Validación de Consistencia de Tamaño
        self.assertEqual(
            len(claves),
            arbol.tamaño,
            f"Fallo de contabilidad: El tamaño reportado ({arbol.tamaño}) "
            f"no coincide con la cantidad real de nodos ({len(claves)}).",
        )

        # 4. Validación del Factor de Equilibrio en CADA NODO
        # FE = Altura(Subárbol Derecho) - Altura(Subárbol Izquierdo)
        for item in recorrido:
            self.assertIn(
                item.factor_de_equilibrio,
                (-1, 0, 1),
                msg=f"Fallo de balanceo AVL: El nodo con clave {item.clave} "
                f"posee un Factor de Equilibrio inválido ({item.factor_de_equilibrio}).",
            )

        # 5. Validación Teórica de la Cota de Altura Máxima
        # La altura de un árbol AVL de N nodos jamás supera h <= 1.44 * log2(N + 2)
        if arbol.tamaño > 0:
            altura_maxima = math.ceil(1.44 * math.log2(arbol.tamaño + 2))
            self.assertLessEqual(
                arbol.altura,
                altura_maxima,
                f"Fallo de altura: La altura actual ({arbol.altura}) excede "
                f"el límite teórico máximo ({altura_maxima}) para N={arbol.tamaño}.",
            )

    # -------------------------------------------------------------------------
    # 1. Casos Borde y Estado Inicial
    # -------------------------------------------------------------------------
    def test_arbol_vacio_inicial(self):
        """Verifica que un árbol recién creado responda correctamente a consultas

        básicas sin lanzar errores inesperados y levante excepciones ante
        búsquedas inválidas.
        """
        self.assertEqual(self.arbol.tamaño, 0, "Un árbol nuevo debe tener tamaño 0.")
        self.assertEqual(
            list(self.arbol.inorden()),
            [],
            "El inorden de un árbol vacío debe ser una lista vacía.",
        )

        # Consultar una clave inexistente debe lanzar KeyError o ValueError
        with self.assertRaises((KeyError, ValueError)):
            _ = self.arbol[99]

    # -------------------------------------------------------------------------
    # 2. Pruebas Explícitas de las 4 Rotaciones AVL
    # -------------------------------------------------------------------------
    def test_rotacion_simple_derecha_LL(self):
        """Caso Izquierda-Izquierda (LL):
        Inserción en orden descendente (30 -> 20 -> 10).
        Provoca desbalanceo a la izquierda en la raíz.
        Solución: Rotación simple a la derecha. La nueva raíz debe ser 20.
        """
        for k in [30, 20, 10]:
            self.arbol[k] = str(k)

        self.assertEqual(
            self.arbol.raiz.clave,
            20,
            "Rotación LL fallida: La nueva raíz debía ser 20.",
        )
        self._validar_invariantes_avl(self.arbol)

    def test_rotacion_simple_izquierda_RR(self):
        """Caso Derecha-Derecha (RR):
        Inserción en orden ascendente (10 -> 20 -> 30).
        Provoca desbalanceo a la derecha en la raíz.
        Solución: Rotación simple a la izquierda. La nueva raíz debe ser 20.
        """
        for k in [10, 20, 30]:
            self.arbol[k] = str(k)

        self.assertEqual(
            self.arbol.raiz.clave,
            20,
            "Rotación RR fallida: La nueva raíz debía ser 20.",
        )
        self._validar_invariantes_avl(self.arbol)

    def test_rotacion_doble_izquierda_derecha_LR(self):
        """Caso Izquierda-Derecha (LR):
        Inserción en forma de zig-zag (30 -> 10 -> 20).
        Provoca desbalanceo en el hijo izquierdo hacia su derecha.
        Solución: Rotación doble Izquierda-Derecha. La nueva raíz debe ser 20.
        """
        for k in [30, 10, 20]:
            self.arbol[k] = str(k)

        self.assertEqual(
            self.arbol.raiz.clave,
            20,
            "Rotación LR fallida: La nueva raíz debía ser 20.",
        )
        self._validar_invariantes_avl(self.arbol)

    def test_rotacion_doble_derecha_izquierda_RL(self):
        """Caso Derecha-Izquierda (RL):
        Inserción en forma de zag-zig (10 -> 30 -> 20).
        Provoca desbalanceo en el hijo derecho hacia su izquierda.
        Solución: Rotación doble Derecha-Izquierda. La nueva raíz debe ser 20.
        """
        for k in [10, 30, 20]:
            self.arbol[k] = str(k)

        self.assertEqual(
            self.arbol.raiz.clave,
            20,
            "Rotación RL fallida: La nueva raíz debía ser 20.",
        )
        self._validar_invariantes_avl(self.arbol)

    # -------------------------------------------------------------------------
    # 3. Operaciones de Consulta y Modificación (Diccionario)
    # -------------------------------------------------------------------------
    def test_busqueda_y_sobrescritura(self):
        """Verifica la asignación `arbol[clave] = valor` tanto para inserción

        como para la actualización de un valor existente sin alterar la estructura.
        """
        # Inserción
        self.arbol[10] = "valor_inicial"
        self.assertEqual(self.arbol[10], "valor_inicial")

        # Sobrescritura de clave existente
        self.arbol[10] = "valor_actualizado"
        self.assertEqual(self.arbol[10], "valor_actualizado")
        self.assertEqual(
            self.arbol.tamaño,
            1,
            "Sobrescribir un nodo no debe incrementar el tamaño del árbol.",
        )

    # -------------------------------------------------------------------------
    # 4. Casos Borde en Eliminaciones
    # -------------------------------------------------------------------------
    def test_eliminar_unica_raiz(self):
        """Eliminar el único nodo debe dejar al árbol completamente limpio."""
        self.arbol[10] = "raiz"
        self.arbol.eliminar(10)

        self.assertEqual(self.arbol.tamaño, 0)
        self.assertEqual(list(self.arbol.inorden()), [])

    def test_eliminar_nodo_con_dos_hijos(self):
        """Eliminar un nodo interno con dos hijos obliga a reemplazarlo por su

        predecesor o sucesor inorden, manteniendo la estructura equilibrada.
        """
        for k in [10, 5, 15]:
            self.arbol[k] = k

        self.arbol.eliminar(10)  # Eliminación de la raíz con 2 hijos
        self._validar_invariantes_avl(self.arbol)

    # -------------------------------------------------------------------------
    # 5. Prueba de Estrés, Rebalanceo en Cascada y Poda
    # -------------------------------------------------------------------------
    def test_estres_insercion_eliminacion_y_poda(self):
        """Prueba integradora masiva:
        1. Inserta 500 elementos aleatorios (rebalanceos continuos).
        2. Ejecuta un recorrido con poda dentro de un rango delimitado.
        3. Elimina 450 elementos para forzar múltiples desbalanceos en cascada hacia arriba.
        """
        N = 500
        lista = random.sample(range(0, 10000), N)

        # Fase 1: Inserción masiva
        for i, clave in enumerate(lista):
            self.arbol[clave] = i

        self._validar_invariantes_avl(self.arbol)

        # Fase 2: Recorrido acotado por rango (Poda / Range Search)
        min_rango, max_rango = 100, 500
        recorrido_poda = list(self.arbol.inorden_con_poda(min_rango, max_rango))
        for item in recorrido_poda:
            self.assertTrue(
                min_rango <= item.clave <= max_rango,
                f"El nodo {item.clave} está fuera del rango acotado [{min_rango}, {max_rango}].",
            )

        # Fase 3: Eliminación masiva (pasa de 500 a 50 nodos)
        for clave in lista[:450]:
            self.arbol.eliminar(clave)

        self._validar_invariantes_avl(self.arbol)


if __name__ == "__main__":
    unittest.main()