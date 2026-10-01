import random
from ayedfiuner.estructuras.arbolAVL import ArbolAVL
import matplotlib.pyplot as plt
import networkx as nx


def dibujar_arbol_jerarquico(arbol, nombre_archivo="arbol_jerarquico.png"):
    """Dibuja y guarda una representación visual 2D jerárquica de un árbol AVL.

    Utiliza el recorrido inorden para calcular las posiciones horizontales (X)
    y la profundidad del nodo para las posiciones verticales (Y), evitando que
    los nodos se superpongan o se desparramen horizontalmente.

    Args:
        arbol (ArbolAVL): Instancia del árbol AVL a graficar. Debe contar con el
          método esta_vacio() y el atributo raíz.
        nombre_archivo (str, optional): Nombre o ruta del archivo de imagen a
          guardar. Por defecto es "arbol_jerarquico.png".
    """
    # -------------------------------------------------------------------------
    # 1. Validación inicial
    # -------------------------------------------------------------------------
    if arbol.esta_vacio():
        print("El árbol está vacío. No hay nada que graficar.")
        return

    # -------------------------------------------------------------------------
    # 2. Estructuras de datos para el grafo
    # -------------------------------------------------------------------------
    G = nx.DiGraph()  # Grafo dirigido para representar las relaciones padre-hijo
    pos = {}  # Diccionario {clave: (coordenada_x, coordenada_y)}
    etiquetas = {}  # Diccionario {clave: "texto a mostrar en el nodo"}

    # Contador global para determinar la posición en X en base al recorrido inorden.
    # Al incrementarse secuencialmente, garantiza que los nodos más a la izquierda
    # tengan un valor X menor y no existan colisiones horizontales.
    x_counter = 0

    # -------------------------------------------------------------------------
    # 3. Función auxiliar recursiva (Recorrido Inorden)
    # -------------------------------------------------------------------------
    def calcular_coordenadas(nodo, profundidad=0):
        """Calcula de forma recursiva las coordenadas (x, y) de cada nodo.

        Args:
            nodo (NodoAVL): Nodo actual que se está procesando.
            profundidad (int): Nivel actual dentro del árbol (0 para la raíz).
        """
        nonlocal x_counter
        if nodo is None:
            return

        # Referencias a los subárboles hijo
        hijo_izq = nodo.hijo_izquierdo
        hijo_der = nodo.hijo_derecho

        # PASO A: Recorrer el subárbol izquierdo primero
        calcular_coordenadas(hijo_izq, profundidad + 1)

        # PASO B: Procesar el nodo actual (Inorden)
        # ---------------------------------------------------------------------
        # 1. Registrar el nodo en el grafo
        G.add_node(nodo.clave)

        # 2. Asignar coordenadas:
        #    X: se asigna según el orden de visita (Inorden: Izquierda -> Raíz -> Derecha)
        #    Y: se asigna como -profundidad para que la raíz quede arriba (Y=0) y
        #       los descendientes vayan hacia abajo (Y=-1, -2, etc.)
        pos[nodo.clave] = (x_counter, -profundidad)

        # 3. Construir la etiqueta descriptiva que mostrará el nodo
        etiquetas[nodo.clave] = (
            f"{nodo.clave}\nFE: {nodo.factor_de_equilibrio}\nValor: {nodo.valor}"
        )

        # 4. Incrementar la coordenada X para el próximo nodo que se procese
        x_counter += 1

        # 5. Agregar las aristas (conexiones dirijidas padre -> hijo)
        if hijo_izq:
            G.add_edge(nodo.clave, hijo_izq.clave)
        if hijo_der:
            G.add_edge(nodo.clave, hijo_der.clave)

        # PASO C: Recorrer el subárbol derecho al final
        calcular_coordenadas(hijo_der, profundidad + 1)

    # -------------------------------------------------------------------------
    # 4. Cálculo de coordenadas a partir de la raíz
    # -------------------------------------------------------------------------
    calcular_coordenadas(arbol.raiz)

    # -------------------------------------------------------------------------
    # 5. Renderizado del gráfico con Matplotlib
    # -------------------------------------------------------------------------
    plt.figure(figsize=(12, 7))

    # Dibujar los nodos en el plano con sus coordenadas calculadas
    nx.draw_networkx_nodes(
        G, pos, node_size=2000, node_color="skyblue", edgecolors="black"
    )

    # Dibujar las aristas con flechas indicando la dirección
    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True,
        arrowsize=15,
        edge_color="gray",
        node_size=2000,  # Evita que las flechas se solapen dentro del círculo del nodo
    )

    # Dibujar los textos centrados en cada nodo
    nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=8, font_weight="bold")

    # Ajustes finales de presentación
    plt.title("Estructura del Árbol AVL", fontsize=14, fontweight="bold")
    plt.axis("off")  # Ocultar los ejes cartesianos
    plt.tight_layout()

    # Guardar en disco y mostrar por pantalla
    plt.savefig(nombre_archivo, dpi=300)
    plt.show()


# =============================================================================
# Bloque de ejecución principal
# =============================================================================
if __name__ == "__main__":
    # Opcional: fija una semilla para obtener el mismo árbol en cada ejecución
    # random.seed(42)

    arbolAVL = ArbolAVL()

    # Generar y agregar 10 elementos aleatorios al árbol
    N = 10
    lista = random.sample(range(0, 100), N)
    for i, clave in enumerate(lista):
        arbolAVL[clave] = i

    # Generar el gráfico
    dibujar_arbol_jerarquico(arbolAVL)