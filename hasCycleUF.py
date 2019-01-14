import random
import quickFind
import progetto.Graph_AdjacencyList
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str(end-start) + " seconds")
        return result
    return wrapper

def AcyclicGraphGenerator(G, n):
    edges = 0
    nodes = []
    for i in range(n):
        nodes.append(G.addNode(i))
    connessi = [nodes[0]]
    for k in nodes[1:]:
        j = random.choice(connessi)
        G.insertEdge(k.id, j.id)
        edges += 1
        connessi.append(k)
    return edges


def CyclicGraphGenerator(G, n):
    edges = 3
    nodes = []
    for i in range(n):
        nodes.append(G.addNode(i))
    connessi = [nodes[0], nodes[1], nodes[2]]
    G.insertEdge(connessi[0].id, connessi[1].id)
    G.insertEdge(connessi[1].id, connessi[2].id)
    G.insertEdge(connessi[2].id, connessi[0].id)

    for k in nodes[3:]:
        j = random.choice(connessi)
        G.insertEdge(k.id, j.id)
        edges += 1
        connessi.append(k)
    return edges

class EdgeIterator:
    def __init__(self, G):
        self.curr = -1
        self.edges = G.getEdges()

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr < len(self.edges):
            self.curr += 1
            edges = self.edges[self.curr]

            break

        else:
            raise StopIteration

        return edges


@time_it
def hasCycleUF(G):

    uf = quickFind.QuickFindBalanced()
    for node in G.getNodes():
        uf.makeSet(node.id)
    iterator = EdgeIterator(G)
    while next(iterator):
        for edge in G.getEdges():
          hr = uf.findRoot(uf.nodes[edge.head])
          tr = uf.findRoot(uf.nodes[edge.tail])
          if hr == tr:
              return True
          else:
              uf.union(hr, tr)
        return False





if __name__ == "__main__":
    print("Acyclic")
    G = progetto.Graph_AdjacencyList.GraphAdjacencyList()
    n = 10001
    print(AcyclicGraphGenerator(G, n))
    G.print()
    print("Number of edges:" + str((G.numEdges())))


    print(hasCycleUF(G))