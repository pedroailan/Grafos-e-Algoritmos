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

print("----------- Grafo 1 --------------")
print("DFS")
g.dfs()
v = g.listar_vertice_sem_arcos_de_entrada()
# for i in verticesSemArcosDeEntrada:
#     travessia = g.busca_profundidade(i, [])
#     print(f"Travessia para {i}: {travessia}")

print("\nKahn")
travessia = g.kahn(v)
print(travessia)
print()

g2 = m.Grafo(False, True)

l2 = [
    "CUECAS",
    "CALCAS",
    "CINTO",
    "CAMISA",
    "GRAVATA",
    "PALETO",
    "MEIAS",
    "SAPATOS",
    "RELOGIO"
]

for i in l2:
    g2.insere_vertice(i)

g2.insere_aresta("CUECAS", "CALCAS")
g2.insere_aresta("CUECAS", "SAPATOS")
g2.insere_aresta("CALCAS", "CINTO")
g2.insere_aresta("CALCAS", "SAPATOS")
g2.insere_aresta("CINTO", "PALETO")
g2.insere_aresta("CAMISA", "CINTO")
g2.insere_aresta("CAMISA", "GRAVATA")
g2.insere_aresta("GRAVATA", "PALETO")
g2.insere_aresta("MEIAS", "SAPATOS")

print("----------- Grafo 2 --------------")
print("DFS")
g2.dfs()
v = g2.listar_vertice_sem_arcos_de_entrada()
# for i in verticesSemArcosDeEntrada:
#     travessia = g2.busca_profundidade(i, [])
#     print(f"Travessia para {i}: {travessia}")

print("\nKahn")
travessia = g2.kahn(v)
print(travessia)
