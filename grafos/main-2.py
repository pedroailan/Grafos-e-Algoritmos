import os 
os.system('cls' if os.name == 'nt' else 'clear')

import grafo as x


g1 = x.Grafo(False, False)
ler = g1.ler_arquivo("grafos/L1.txt")
criarGrafo = g1.rotula(ler[0], ler[1])
print("Executando busca em largura...")
bfs = g1.BFS("1")
print("Escrevendo no arquivo...")
g1.escreve_arquivo("grafos/L1_RESULT.txt", ler[0], ler[1], bfs)

g2 = x.Grafo(False, False)
ler = g2.ler_arquivo("grafos/L2.txt")
criarGrafo = g2.rotula(ler[0], ler[1])
print("Executando busca em largura...")
bfs = g2.BFS("1")
print("Escrevendo no arquivo...")
g2.escreve_arquivo("grafos/L2_RESULT.txt", ler[0], ler[1], bfs)

g3 = x.Grafo(False, False)
ler = g3.ler_arquivo("grafos/L3.txt")
criarGrafo = g3.rotula(ler[0], ler[1])
print("Executando busca em largura...")
bfs = g3.BFS("1")
print("Escrevendo no arquivo...")
g3.escreve_arquivo("grafos/L3_RESULT.txt", ler[0], ler[1], bfs)

g4 = x.Grafo(False, False)
ler = g4.ler_arquivo("grafos/L4.txt")
criarGrafo = g4.rotula(ler[0], ler[1])
print("Executando busca em largura...")
bfs = g4.BFS("1")
print("Escrevendo no arquivo...")
g4.escreve_arquivo("grafos/L4_RESULT.txt", ler[0], ler[1], bfs)