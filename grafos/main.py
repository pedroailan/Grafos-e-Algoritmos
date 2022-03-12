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


print("----------- Grafo 1 --------------")
g.imprime()
print("DFS")
g.dfs()
v = g.listar_vertice_sem_arcos_de_entrada()

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
g2.imprime()
print("DFS")
g2.dfs()
v = g2.listar_vertice_sem_arcos_de_entrada()

print("\nKahn")
travessia = g2.kahn(v)
print(travessia)
print()


g3 = m.Grafo(False, True)

l2 = [
    "1",
    "1",
    "3",
    "4",
    "5",
]

for i in l2:
    g3.insere_vertice(i)

g3.insere_aresta("1", "2")
g3.insere_aresta("1", "4")
g3.insere_aresta("2", "2")
g3.insere_aresta("1", "5")
g3.insere_aresta("5", "3")

print("----------- Grafo 3 --------------")
g3.imprime()
print("DFS")
g3.dfs()
v = g3.listar_vertice_sem_arcos_de_entrada()

print("\nKahn")
travessia = g3.kahn(v)
print(travessia)