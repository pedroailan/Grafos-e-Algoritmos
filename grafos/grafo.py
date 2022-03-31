import os
class Grafo:
    def __init__(self, ponderado = False, direcionado = False):
        self.ponderado = ponderado
        self.direcionado = direcionado
        self.grafo = {}
        self.visitados = []
    
    def insere_vertice(self, vertice):
        if vertice in self.grafo:
            return
        self.grafo[vertice] = []

    def insere_aresta(self, vertice1, vertice2, peso = 0 ):
        if vertice1 not in self.grafo:
            return
        if vertice2 not in self.grafo:
            return
        else:
            if self.ponderado:
                if self.direcionado:
                    i = [vertice2, peso]
                    self.grafo[vertice1].append(i)
                else:
                    i = [vertice2, peso]
                    j = [vertice1, peso]
                    self.grafo[vertice1].append(i)
                    self.grafo[vertice2].append(j)
                    
            else:
                if self.direcionado:
                    self.grafo[vertice1].append(vertice2)
                else:
                    self.grafo[vertice1].append(vertice2)
                    self.grafo[vertice2].append(vertice1)
            
    def remove_vertice(self, vertice):
        if vertice not in self.grafo:
            return
        self.grafo.pop(vertice)
        print(f"Remove vertice: {vertice}")
        if self.ponderado:
            for i in self.grafo:
                listaDeAdjacencia = self.grafo[i]
                for n in listaDeAdjacencia:
                    if vertice == n[0]:
                        listaDeAdjacencia.remove(n)
                        break
        else:
            for i in self.grafo:
                listaDeAdjacencia = self.grafo[i]
                if vertice in listaDeAdjacencia:
                    listaDeAdjacencia.remove(vertice)

    def remove_aresta(self, vertice1, vertice2, peso = 0):
        if vertice1 not in self.grafo:
            return
        if vertice2 not in self.grafo:
            return
        else:
            print(f"Remove aresta entre {vertice1} e {vertice2}")
            if self.ponderado:
                if self.direcionado:
                    i = [vertice2, peso]
                    if i in self.grafo[vertice1]:
                        self.grafo[vertice1].remove(i)
                else:
                    i = [vertice1, peso]
                    j = [vertice2, peso]
                    if j in self.grafo[vertice1]:
                        self.grafo[vertice1].remove(j)
                        self.grafo[vertice2].remove(i)

            else:
                if self.direcionado:
                    if vertice2 in self.grafo[vertice1]:
                            self.grafo[vertice1].remove(vertice2)
                else:
                    if vertice2 in self.grafo[vertice1]:
                        self.grafo[vertice1].remove(vertice2)
                        self.grafo[vertice2].remove(vertice1)

    def qtd_vertices(self):
        return str(len(self.grafo))

    def qtd_arestas(self):
        return str(len([(vertice, adj) for vertice in self.grafo.keys() for adj in self.grafo[vertice]]))
    
    def imprime_grau(self, vertice):
        grau = str(len(self.grafo[vertice]))
        print(f"Grau de {vertice}: {grau}")
        return grau
    
    def grau(self, vertice):
        return str(len(self.grafo[vertice]))
    
    def vizinhanca(self, vertice1, vertice2):
        if vertice1 in self.grafo[vertice2]:
            return "São vizinhos: " + vertice1 + " - " + vertice2
        if vertice2 in self.grafo[vertice1]:
            return "São vizinhos: " + vertice1 + " - " + vertice2
        return "Não são vizinhos: " + vertice1 + " - " + vertice2
    
    def imprime(self):
        for i in self.grafo:
            item = self.grafo[i]
            print(str(i) + " -> " + str(item))
            
    def par_impar(self, vertice): 
        return True if float(self.grau(vertice)) % 2 == 0 else False
                     
    def hierholzer(self):
        pilha1 = [] 
        pilha2 = []
        inicial = next(iter(self.grafo))
        pilha1.append(inicial)
        i = 0
        n = list(self.grafo.keys())[i]
        while(len(pilha1) > 0):
            adj = self.grafo[n]
            if adj:
                aresta = adj[0]
                pilha1.append(aresta)
                self.grafo[n] = list(filter(lambda x: x != aresta, adj))
                for x in self.grafo.keys():
                    if x == aresta:
                        s = self.grafo[x]
                        self.grafo[x] = list(filter(lambda x: x != n, s))
                        n = x
            else:
                top = pilha1[-1]
                if len(self.grafo[top]) > 0:
                    n = top
                else:
                    pilha2.append(pilha1.pop())
            i += 1
        print(f"Tour de Euler: {pilha2}")

    def busca_profundidade_GND(self, visitados = [], vertice = ""):
        if not vertice:
            vertice = list(self.grafo.keys())[0]
            visitados.append(vertice)
        elif vertice not in visitados:
            visitados.append(vertice)

        while(len(self.grafo[vertice]) > 0):
            x = self.grafo[vertice][0]
            if x not in visitados:
                visitados.append(x)
                if vertice in self.grafo[x]:
                    self.grafo[x].remove(vertice)

                self.grafo[vertice].remove(x)
                return self.busca_profundidade_GND(visitados, x)
            else:
                self.grafo[vertice].remove(x)
        print(f"Travessia: {visitados}")
    
    def DFS(self, vertice):
        self.visitados.append(vertice)
        for i in self.grafo[vertice]:
            if i not in self.visitados:
                self.DFS(i)

    def BFS(self, vertice):
        final = False
        fila = []
        visitados = []
        fila.append(vertice)
        visitados.append(vertice)
        saida = list(self.grafo.keys())[-1]
        while(fila):
            v = fila[0]
            fila.remove(v)
            for i in self.grafo[v]:
                if i not in visitados:
                    visitados.append(i)
                    fila.append(i)
                if i == saida:
                    final= True 
                    break
            if final:
                break
        print(visitados)
        return visitados

    def listar_vertice_sem_arcos_de_entrada(self):
        i = 0
        v = []
        j = []
        for i in self.grafo.values():
            j.extend(i)
        for i in self.grafo:
            if i not in j:
                v.append(i)
        return v

    def possui_arco_de_entrada(self, vertice):
        j = []
        for i in self.grafo.values():
            j.extend(i)
        if vertice in j: return True
        else: return False

    def busca_profundidade(self, vertice, visitados):
        if vertice not in visitados:
            visitados.append(vertice)
            for i in self.grafo[vertice]:
                self.busca_profundidade(i, visitados)
        return visitados
    
    def kahn(self, vSemArco):
        L = []
        S = vSemArco
        while(S):
            v = S.pop()
            L.append(v)
            while(self.grafo[v]):
                w = self.grafo[v][0]
                self.grafo[v].remove(w)
                if not self.possui_arco_de_entrada(w):
                    S.append(w)
        if not self.grafo.values() : print("Grafo possui ciclo")
        else: return L

    def visite(self, vertice, L):
        if vertice not in L:
            for i in self.grafo[vertice]:
                self.visite(i, L)
            L.append(vertice)

    def print_matriz(self, matriz, tamanho):
        for i in range(tamanho):
            for y in range(tamanho):
                print(format(matriz[i][y], "<3"), end= " ")
            print()
    
    def ler_arquivo(self, nome):
        arquivo = open(nome, 'r')
        tamanho = 0
        matriz = [[]]
        i = 0
        j = 0
        for linha in arquivo.readlines():
            if i == 0:
                 tamanho = len(linha) - 1
                 matriz = [[0] * tamanho for i in range(tamanho)] #cria matriz mediante o tamanho linha e colunas do txt
            for item in linha:
                if item != "\n":
                    matriz[i][j] = item.replace("#", "0").replace(" ", "1") # altera os caracteres e insere na matriz
                    j += 1
            j = 0
            i += 1
        return (matriz, tamanho)

    def rotula(self, matriz, tamanho):
        count = 1
        for i in range(tamanho):
            for j in range(tamanho):
                item = matriz[i][j]
                if item == "1":
                    matriz[i][j] = count
                    count += 1

        for i in range(tamanho):
            for j in range(tamanho):
                item = str(matriz[i][j])
                if item != "0":
                    self.insere_vertice(str(item))

        vertices = self.grafo.keys()
        for i in range(tamanho - 1):
            for j in range(tamanho - 1):
                item = str(matriz[i][j])
                if item in vertices:
                    direita = str(matriz[i][j + 1])
                    if direita != "0": self.insere_aresta(item, direita)
                    abaixo = str(matriz[i + 1][j])
                    if abaixo != "0": self.insere_aresta(item, abaixo)
        return matriz
    
    def escreve_arquivo(self, nome_arquivo ,matriz, tamanho, caminho):
        if os.path.exists(nome_arquivo):
             os.remove(nome_arquivo)

        for i in range(tamanho):
            for j in range(tamanho):
                item = str(matriz[i][j])
                if item not in caminho:
                    matriz[i][j] = "#"
                else:
                    matriz[i][j] = "1"
        f = open(nome_arquivo, 'w+')
        linha = ''
        for i in range(tamanho):
            for j in range(tamanho):
                item = str(matriz[i][j])
                linha += f"{item} "
            f.writelines(linha + '\n')
            linha = ''
        f.close()
