import random
import progetto.Graph_AdjacencyList

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

if __name__ == "__main__":
    print("Acyclic")
    G = progetto.Graph_AdjacencyList.GraphAdjacencyList()
    print("Number of edges:", AcyclicGraphGenerator(G, 10))
    G.print()
