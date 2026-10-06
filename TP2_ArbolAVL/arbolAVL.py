class NodoArbolAVL:
    def __init__(self, clave, valor):
        pass

    @property
    def clave(self):
        pass

    @property
    def valor(self):
        pass

    @property
    def padre(self):
        pass

    @property
    def hijo_izquierdo(self):
        pass

    @property
    def hijo_derecho(self):
        pass

    @property
    def altura(self):
        pass

    @clave.setter
    def clave(self, clave):
        pass

    @valor.setter
    def valor(self, valor):
        pass

    @padre.setter
    def padre(self, nodo):
        pass

    @hijo_izquierdo.setter
    def hijo_izquierdo(self, nodo):
        pass

    @hijo_derecho.setter
    def hijo_derecho(self, nodo):
        pass

    def tiene_padre(self):
        pass

    def es_raiz(self):
        pass

    def tiene_hijo_izquierdo(self):
        pass

    def tiene_hijo_derecho(self):
        pass

    def tiene_hijos(self):
        pass

    def tiene_ambos_hijos(self):
        pass

    def es_hoja(self):
        pass

    def es_hijo_izquierdo(self):
        pass

    def es_hijo_derecho(self):
        pass

    @property
    def altura_rama_izquierda(self):
        pass

    @property
    def altura_rama_derecha(self):
        pass

    def actualizar_altura(self):
        pass

    @property
    def factor_de_equilibrio(self):
        pass


class ArbolAVL:
    def __init__(self):
        pass

    @property
    def tamaño(self):
        pass

    @property
    def altura(self):
        pass

    @property
    def raiz(self):
        pass

    def esta_vacio(self):
        pass

    def agregar(self, clave, valor):
        pass

    def __agregar(self, nodo, clave, valor):
        pass

    def __rebalancear(self, nodo):
        pass

    def __rotacion_izquierda(self, nodo):
        pass

    def __rotacion_derecha(self, nodo):
        pass

    def inorden(self):
        pass

    def __inorden(self, nodo):
        pass

    def obtener(self, clave):
        pass

    def __obtener(self, nodo, clave):
        pass

    def __setitem__(self, clave, valor):
        pass

    def __getitem__(self, clave):
        pass

    def __contains__(self, clave):
        pass

    def eliminar(self, clave):
        pass

    def __eliminar(self, nodo, clave):
        pass

    def __obtener_minimo(self, nodo):
        pass

    def __delitem__(self, clave):
        pass

    def inorden_con_poda(self, clave_minima, clave_maxima):
        pass

    def __inorden_con_poda(self, nodo, clave_minima, clave_maxima):
        pass
