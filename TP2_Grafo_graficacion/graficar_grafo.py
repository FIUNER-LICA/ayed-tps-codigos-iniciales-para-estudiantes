import matplotlib.pyplot as plt
import networkx as nx
from ayedfiuner.algoritmos.grafos import (
    aplicar_camino_maxima_capacidad,
    aplicar_dijkstra,
    aplicar_prim,
)
from ayedfiuner.estructuras.grafo_dirigido import GrafoDirigido


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
    pos = nx.spring_layout(
        G,
    )

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


if __name__ == "__main__":
    grafo = GrafoDirigido()

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

    for v in grafo:
        for w in v.obtener_conexiones():
            print(f"{v.clave} conecta con {w.clave} con peso {v.obtener_peso(w)}")

    graficar_grafo(grafo)

    # Dijkstra

    print("-" * 20)
    print("Aplicando Dijkstra...")
    aristas = aplicar_dijkstra(grafo, 0)
    print(f"Resultados: {aristas}")

    grafo_2 = GrafoDirigido()
    suma_total = 0
    for arista in aristas:
        suma_total += arista[2]
        grafo_2.agregar_arista(arista[0], arista[1], arista[2])
    print(f"Suma total de aristas: {suma_total}")

    graficar_grafo(grafo_2)

    # Prim

    print("-" * 20)
    print("Aplicando Dijkstra...")
    aristas = aplicar_prim(grafo, 0)
    print(f"Resultados: {aristas}")

    grafo_3 = GrafoDirigido()
    suma_total = 0
    for arista in aristas:
        suma_total += arista[2]
        grafo_3.agregar_arista(arista[0], arista[1], arista[2])
    print(f"Suma total de aristas: {suma_total}")
    graficar_grafo(grafo_3)

    # Cuellos de botella

    print("-" * 20)
    print("Aplicando Dijkstra...")
    aristas = aplicar_camino_maxima_capacidad(grafo, 0)
    print(f"Resultados: {aristas}")

    grafo_4 = GrafoDirigido()
    for arista in aristas:
        grafo_4.agregar_arista(arista[0], arista[1], arista[2])
    graficar_grafo(grafo_4)
