import os
os.system('cls' if os.name == 'nt' else 'clear')
import grafo as m


g = m.Grafo(False, True)
#l = ["A", "B", "C", "D", "E"]
l = ["5", "7", "3", "11", "8", "2", "9", "10"]
for i in l:
    g.insere_vertice(i)

# g.insere_aresta("A", "B")
# g.insere_aresta("B", "C")
# g.insere_aresta("A", "D")
# g.insere_aresta("B", "E")

g.insere_aresta("5", "11")
g.insere_aresta("7", "11")
g.insere_aresta("7", "8")
g.insere_aresta("3", "8")
g.insere_aresta("3", "10")
g.insere_aresta("11", "2")
g.insere_aresta("11", "9")
g.insere_aresta("11", "10")
g.insere_aresta("8", "9")


g.imprime()
#g.busca_profundidade()
verticesSemArcosDeEntrada = g.arcos_de_entrada()
for i in verticesSemArcosDeEntrada:
    travessia = g.busca_profundidade(i, [])
    print(travessia)
print("\nKahn")
travessia = g.kahn(verticesSemArcosDeEntrada)
print(travessia)

