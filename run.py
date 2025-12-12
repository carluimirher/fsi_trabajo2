# Search methods

import search
import time

destinos_romania = [['A', 'B'], ['O', 'E'], ['G', 'Z'], ['N', 'D'], ['M', 'F']]

for x in range(0, 1):
    total_start_time = time.perf_counter()

    ab = search.GPSProblem(destinos_romania[x][0], destinos_romania[x][1]
                        , search.romania)

    print("-----------------------------------------------------\n")
    print(f"Id {x+1}; Origen: {destinos_romania[x][0]}; Destino: {destinos_romania[x][1]}")

    #node, n_open, n_close, cost = search.breadth_first_graph_search(ab)
    #node, n_open, n_close, cost = search.depth_first_graph_search(ab)
    node, n_open, n_close, cost = search.bab(ab)
    #node, n_open, n_close, cost = search.babh(ab)

    print(node.path())

    total_time = time.perf_counter() - total_start_time


    print(f"Nodos generados: {n_open}; Nodos visitados: {n_close}; Coste total: {cost}")
    print(f"Tiempo total tardado: {total_time*1000000:.1f}μs\n")
print("-----------------------------------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
