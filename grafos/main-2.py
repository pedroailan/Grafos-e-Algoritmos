import os 
os.system('cls' if os.name == 'nt' else 'clear')

import grafo as x


g2 = x.Grafo(False, False)
directory = os.getcwd()

print(directory)
g2.ler_arquivo("grafos/L1.txt")
g2.busca_profundidade_GND([], "1")