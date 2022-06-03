import os 
os.system('cls' if os.name == 'nt' else 'clear')

import grafo as x

g = x.Grafo(True, False)

g.insere_vertice('A')
g.insere_vertice('B')
g.insere_vertice('C')
g.insere_vertice('D')
g.insere_vertice('E')
g.insere_vertice('F')

g.insere_aresta('A', 'B', 1)
g.insere_aresta('A', 'C', 4)
g.insere_aresta('B', 'C', 1)
g.insere_aresta('A', 'D', 5)

g.imprime()
g.dijkstra('A', 'D')

