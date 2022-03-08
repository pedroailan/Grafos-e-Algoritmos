class Grafo:
    def __init__(self, ponderado = False, direcionado = False):
        self.ponderado = ponderado
        self.direcionado = direcionado
        self.grafo = {}
    
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
        

    def busca_profundidade(self, visitados = [], vertice = ""):
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
                self.busca_profundidade(visitados, x)
            else:
                self.grafo[vertice].remove(x)
        print(f"Travessia: {visitados}")        
