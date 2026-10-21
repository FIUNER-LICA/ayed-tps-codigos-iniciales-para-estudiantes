import matplotlib.pyplot as plt
import networkx as nx
from ayedfiuner.algoritmos.grafos import (
    aplicar_camino_maxima_capacidad,
    aplicar_dijkstra,
    aplicar_prim,
)
from ayedfiuner.estructuras.grafo import Grafo


def graficar_grafo(grafo, seed=42):
    # 1. Crear el grafo dirigido en NetworkX
    G = nx.DiGraph()

    # 2. Poblar NetworkX recorriendo la estructura personalizada
    for v in grafo:
        G.add_node(v.clave)
        for w in v.obtener_conexiones():
            peso = v.obtener_peso(w)
            G.add_edge(v.clave, w.clave, weight=peso)

    # 3. Definir la distribución visual de los nodos
    pos = nx.spring_layout(G, seed=42)

    # 4. Dibujar nodos, aristas y etiquetas de nodos
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=100,
        arrowsize=10,
        edge_color="gray",
        font_size=8,
    )

    # 5. Dibujar los pesos sobre cada arista
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, rotate=True, font_size=8
    )

    plt.title("Representación del Grafo Dirigido")
    plt.axis("off")
    plt.show()


def crear_grafo_no_dirigido():
    grafo = Grafo()
    grafo.agregar_arista(0, 1, 5)
    grafo.agregar_arista(1, 0, 5)

    grafo.agregar_arista(0, 2, 3)
    grafo.agregar_arista(2, 0, 3)

    grafo.agregar_arista(0, 3, 10)
    grafo.agregar_arista(3, 0, 10)

    grafo.agregar_arista(1, 2, 2)
    grafo.agregar_arista(2, 1, 2)

    grafo.agregar_arista(1, 4, 6)
    grafo.agregar_arista(4, 1, 6)

    grafo.agregar_arista(1, 5, 9)
    grafo.agregar_arista(5, 1, 9)

    grafo.agregar_arista(2, 3, 4)
    grafo.agregar_arista(3, 2, 4)

    grafo.agregar_arista(2, 4, 7)
    grafo.agregar_arista(4, 2, 7)

    grafo.agregar_arista(2, 5, 8)
    grafo.agregar_arista(5, 2, 8)

    grafo.agregar_arista(3, 5, 3)
    grafo.agregar_arista(5, 3, 3)

    grafo.agregar_arista(3, 6, 6)
    grafo.agregar_arista(6, 3, 6)

    grafo.agregar_arista(4, 5, 1)
    grafo.agregar_arista(5, 4, 1)

    grafo.agregar_arista(4, 7, 5)
    grafo.agregar_arista(7, 4, 5)

    grafo.agregar_arista(4, 8, 12)
    grafo.agregar_arista(8, 4, 12)

    grafo.agregar_arista(5, 6, 2)
    grafo.agregar_arista(6, 5, 2)

    grafo.agregar_arista(5, 7, 4)
    grafo.agregar_arista(7, 5, 4)

    grafo.agregar_arista(5, 8, 7)
    grafo.agregar_arista(8, 5, 7)

    grafo.agregar_arista(6, 7, 3)
    grafo.agregar_arista(7, 6, 3)

    grafo.agregar_arista(6, 9, 8)
    grafo.agregar_arista(9, 6, 8)

    grafo.agregar_arista(7, 8, 2)
    grafo.agregar_arista(8, 7, 2)

    grafo.agregar_arista(7, 9, 6)
    grafo.agregar_arista(9, 7, 6)

    grafo.agregar_arista(8, 9, 3)
    grafo.agregar_arista(9, 8, 3)

    grafo.agregar_arista(9, 0, 15)
    grafo.agregar_arista(0, 9, 15)
    return grafo


def crear_grafo_dirigido():
    grafo = Grafo()
    grafo.agregar_arista(0, 1, 5)
    grafo.agregar_arista(0, 2, 3)
    grafo.agregar_arista(0, 3, 10)

    grafo.agregar_arista(1, 2, 2)
    grafo.agregar_arista(1, 4, 6)
    grafo.agregar_arista(1, 5, 9)

    grafo.agregar_arista(2, 3, 4)
    grafo.agregar_arista(2, 4, 7)
    grafo.agregar_arista(2, 5, 8)

    grafo.agregar_arista(3, 5, 3)
    grafo.agregar_arista(3, 6, 6)

    grafo.agregar_arista(4, 5, 1)
    grafo.agregar_arista(4, 7, 5)
    grafo.agregar_arista(4, 8, 12)

    grafo.agregar_arista(5, 6, 2)
    grafo.agregar_arista(5, 7, 4)
    grafo.agregar_arista(5, 8, 7)

    grafo.agregar_arista(6, 7, 3)
    grafo.agregar_arista(6, 9, 8)

    grafo.agregar_arista(7, 8, 2)
    grafo.agregar_arista(7, 9, 6)

    grafo.agregar_arista(8, 9, 3)
    grafo.agregar_arista(9, 0, 15)

    return grafo


def crear_grafo_guia_8_problema_9():
    grafo = Grafo()
    grafo.agregar_arista("u", "x", 1)
    grafo.agregar_arista("x", "u", 1)

    grafo.agregar_arista("u", "v", 2)
    grafo.agregar_arista("v", "u", 2)

    grafo.agregar_arista("x", "y", 1)
    grafo.agregar_arista("y", "x", 1)

    grafo.agregar_arista("x", "v", 2)
    grafo.agregar_arista("v", "x", 2)

    grafo.agregar_arista("v", "w", 3)
    grafo.agregar_arista("w", "v", 3)

    grafo.agregar_arista("u", "w", 5)
    grafo.agregar_arista("w", "u", 5)

    grafo.agregar_arista("x", "w", 3)
    grafo.agregar_arista("w", "x", 3)

    grafo.agregar_arista("y", "w", 1)
    grafo.agregar_arista("w", "y", 1)

    grafo.agregar_arista("y", "z", 1)
    grafo.agregar_arista("z", "y", 1)

    grafo.agregar_arista("w", "z", 5)
    grafo.agregar_arista("z", "w", 5)
    return grafo


def crear_grafo(opcion):
    if opcion == "no dirigido":
        return crear_grafo_no_dirigido()
    if opcion == "dirigido":
        return crear_grafo_dirigido()
    if opcion == "guia 8 problema 9":
        return crear_grafo_guia_8_problema_9()


if __name__ == "__main__":
    grafo = crear_grafo("dirigido")  # "no dirigido", "dirigido", "guia 8 problema 9"

    for v in grafo:
        for w in v.obtener_conexiones():
            print(f"{v.clave} conecta con {w.clave} con peso {v.obtener_peso(w)}")

    graficar_grafo(grafo)

    clave_inicio = 0

    # Dijkstra

    print("-" * 20)
    print("Aplicando Dijkstra...")
    aristas = aplicar_dijkstra(grafo, clave_inicio)
    print(f"Resultados: {aristas}")

    grafo_2 = Grafo()
    suma_total = 0
    for arista in aristas:
        suma_total += arista[2]
        grafo_2.agregar_arista(arista[0], arista[1], arista[2])
    print(f"Suma total de aristas: {suma_total}")

    graficar_grafo(grafo_2)

    # Prim

    print("-" * 20)
    print("Aplicando Prim...")
    aristas = aplicar_prim(grafo, clave_inicio)
    print(f"Resultados: {aristas}")

    grafo_3 = Grafo()
    suma_total = 0
    for arista in aristas:
        suma_total += arista[2]
        grafo_3.agregar_arista(arista[0], arista[1], arista[2])
    print(f"Suma total de aristas: {suma_total}")
    graficar_grafo(grafo_3)

    # Cuellos de botella

    print("-" * 20)
    print("Aplicando Camino de máxima capacidad...")
    aristas = aplicar_camino_maxima_capacidad(grafo, clave_inicio)
    print(f"Resultados: {aristas}")

    grafo_4 = Grafo()
    for arista in aristas:
        grafo_4.agregar_arista(arista[0], arista[1], arista[2])
    graficar_grafo(grafo_4)
