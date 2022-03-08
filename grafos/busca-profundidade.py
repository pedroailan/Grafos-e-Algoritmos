import os
os.system('cls' if os.name == 'nt' else 'clear')
import grafo as m


g = m.Grafo(False, False)
#l = ["A", "B", "C", "D", "E"]
l = ["1", "2", "3", "4", "5", "6", "7"]
for i in l:
    g.insere_vertice(i)

# g.insere_aresta("A", "B")
# g.insere_aresta("B", "C")
# g.insere_aresta("A", "D")
# g.insere_aresta("B", "E")

g.insere_aresta("1", "2")
g.insere_aresta("1", "3")
g.insere_aresta("2", "3")
g.insere_aresta("3", "4")
g.insere_aresta("3", "5")
g.insere_aresta("3", "6")
g.insere_aresta("3", "7")
g.insere_aresta("4", "5")


g.imprime()
g.busca_profundidade()
