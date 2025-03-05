# Definição de um nó (vertice) no grafo
class Node(object):
    def __init__(self, name):
        """Assume que name é uma string"""
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

# Definição de uma aresta (conexão entre dois nós) no grafo
class Edge(object):
    def __init__(self, src, dest):
        """Assume que src e dest são nós"""
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

# Definição de um grafo direcionado (Digraph)
class Digraph(object):
    """edges é um dicionário que mapeia cada nó para uma lista de seus filhos (destinos)"""
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Nó duplicado')
        else:
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Nó não está no grafo')
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]  # Remove a última quebra de linha

# Definição de um grafo não-direcionado (Graph)
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())  # Adiciona a aresta reversa
        Digraph.addEdge(self, rev)

# Função para construir um grafo de cidades
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

# Função para imprimir um caminho formatado
def printPath(path):
    """Assume que path é uma lista de nós"""
    return '->'.join(str(node) for node in path)

# Algoritmo de busca em profundidade (DFS) para encontrar o caminho mais curto
def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Caminho atual (DFS):', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # Evita ciclos
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath is not None:
                    shortest = newPath
        elif toPrint:
            print('Já visitado', node)
    return shortest

# Função que inicia a busca do caminho mais curto com DFS
def shortestPath(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)

# Teste da busca pelo caminho mais curto usando DFS
def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    if sp is not None:
        print('Menor caminho de', source, 'para', destination, 'é', printPath(sp))
    else:
        print('Não há caminho de', source, 'para', destination)

testSP('Chicago', 'Boston')
print()

# Algoritmo de busca em largura (BFS) para encontrar o caminho mais curto
def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    while pathQueue:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Caminho atual (BFS):', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

# Redefinição da função de caminho mais curto para usar BFS
def shortestPath(graph, start, end, toPrint=False):
    return BFS(graph, start, end, toPrint)

# Teste opcional para BFS (comentar para evitar impressão extensa)
# testSP('Boston', 'Phoenix')
