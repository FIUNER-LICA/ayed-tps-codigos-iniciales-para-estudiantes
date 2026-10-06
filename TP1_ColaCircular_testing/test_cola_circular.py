# -*- coding: utf-8 -*-

import unittest

from ayedfiuner.estructuras.cola_circular import ColaCircular


class TestColaCircular(unittest.TestCase):
    """Suite de pruebas unitarias exhaustiva para la estructura ColaCircular.

    Verifica la correctitud de los punteros 'frente' y 'final' ante
    operaciones intercaladas (wrapping circular), límites de capacidad,
    mantenimiento de estados (vacío/lleno) y excepciones de desbordamiento.
    """

    def setUp(self):
        """Inicializa una cola circular limpia de capacidad 3 antes de cada test."""
        self.capacidad = 3
        self.cola = ColaCircular(self.capacidad)

    # -------------------------------------------------------------------------
    # 1. Pruebas de Inicialización y Validación de Argumentos
    # -------------------------------------------------------------------------

    def test_inicializacion_argumentos_invalidos(self):
        """Verifica que el constructor rechace capacidades nulas, negativas o no numéricas."""
        capacidades_invalidas = [0, -1, -5, "tres", 3.14, None]

        for cap in capacidades_invalidas:
            with self.subTest(capacidad=cap):
                with self.assertRaises(
                    Exception,
                    msg=f"Debería lanzar excepción con capacidad inválida: {cap}",
                ):
                    ColaCircular(cap)

    def test_estado_inicial_cola_vacia(self):
        """Verifica que una cola recién creada tenga la consistencia de estado inicial."""
        self.assertTrue(self.cola.esta_vacia(), "La cola nueva debe estar vacía.")
        self.assertFalse(self.cola.esta_llena(), "La cola nueva no debe estar llena.")

    # -------------------------------------------------------------------------
    # 2. Pruebas de Funcionamiento Circular (Envolvente de Punteros)
    # -------------------------------------------------------------------------

    def test_circularidad_punteros_intercalados(self):
        """PRUEBA CLAVE DE CIRCULARIDAD:

        Forza a que el puntero 'final' envuelva al inicio del arreglo interno
        mientras el puntero 'frente' ha avanzado, manteniendo elementos activos.
        """
        # Capacidad = 3

        # Paso 1: Llenar parcialmente (2 elementos) -> arreglo: [A, B, _]
        self.cola.encolar("A")
        self.cola.encolar("B")

        # Paso 2: Desencolar 1 elemento -> arreglo: [_, B, _] ('frente' avanza al índice 1)
        self.assertEqual(self.cola.desencolar(), "A")

        # Paso 3: Encolar 2 elementos -> arreglo: [D, B, C] ('final' envuelve al índice 0)
        self.cola.encolar("C")
        self.cola.encolar("D")

        # La cola debe reportarse llena
        self.assertTrue(
            self.cola.esta_llena(),
            "La cola debería estar llena tras envolver sus punteros.",
        )

        # Paso 4: Desencolar los elementos en orden FIFO estricto (B -> C -> D)
        self.assertEqual(self.cola.desencolar(), "B")
        self.assertEqual(self.cola.desencolar(), "C")
        self.assertEqual(self.cola.desencolar(), "D")

        # La cola debe quedar vacía al finalizar
        self.assertTrue(self.cola.esta_vacia())

    def test_reutilizacion_continua_ciclos(self):
        """Somete la cola a múltiples ciclos de encolado/desencolado continuo

        corrigiendo el sombreado de variables del test original.
        """
        items = [23, 75, 100]
        for _ in range(100):  # 'ciclo' en lugar de reusar 'i'
            for item in items:
                self.cola.encolar(item)
            for item in items:
                self.assertEqual(
                    self.cola.desencolar(),
                    item,
                    msg="Inconsistencia en el orden de extracción FIFO.",
                )

        self.assertTrue(self.cola.esta_vacia())

    # -------------------------------------------------------------------------
    # 3. Control de Excepciones y Condiciones Límite (Overflow / Underflow)
    # -------------------------------------------------------------------------

    def test_error_underflow_desencolar_vacia(self):
        """Intentar desencolar en una cola vacía debe arrojar una excepción."""
        with self.assertRaises(Exception, msg="No advierte que la cola está vacía"):
            self.cola.desencolar()

    def test_error_overflow_encolar_llena(self):
        """Intentar encolar superando la capacidad máxima debe arrojar una excepción."""
        for elem in range(self.capacidad):
            self.cola.encolar(elem)

        self.assertTrue(self.cola.esta_llena())

        with self.assertRaises(Exception, msg="No advierte que la cola está llena"):
            self.cola.encolar(99)

    # -------------------------------------------------------------------------
    # 4. Verificación de Vaciado y Consistencia de Estado
    # -------------------------------------------------------------------------

    def test_metodo_vaciar_y_restablecimiento(self):
        """Verifica que 'vaciar()' restablezca integralmente el estado operativo de la cola."""
        for elem in range(self.capacidad):
            self.cola.encolar(elem)

        self.assertTrue(self.cola.esta_llena())

        # Ejecutar vaciado
        self.cola.vaciar()

        # Verificar estados
        self.assertTrue(
            self.cola.esta_vacia(),
            "Luego de vaciar(), 'esta_vacia()' debe ser True.",
        )
        self.assertFalse(
            self.cola.esta_llena(),
            "Luego de vaciar(), 'esta_llena()' debe ser False.",
        )

        # Confirmar que operativamente está vacía intentando desencolar
        with self.assertRaises(Exception):
            self.cola.desencolar()


if __name__ == "__main__":
    unittest.main()
