from progetto.GraphGenerator import AcyclicGraphGenerator
from progetto.GraphGenerator import CyclicGraphGenerator
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


@time_it
def hasCycleDFS(G):
    """
    Inizializzo tutti gli indici corrispondenti ai vertici del grafo nella lista visited con False, in quanto
    non ancora visitati. Utilizzo la funzione hasCycleDFSsubGraph per scorrere tutte le visite DFS possibili,
    utilizzando come nodo di partenza a mano a mano tutti i vertici del grafo.
    """
    visited = [False] * (G.numNodes())
    for i in range(G.numNodes()):
        if visited[i] == False:
            if G.hasCycleDFSsubGraph(i, visited, -1) == True:
                return True
    return False



if __name__ == "__main__":
    print("Acyclic")
    G = progetto.Graph_AdjacencyList.GraphAdjacencyList()
    n = 10001
    print(CyclicGraphGenerator(G, n))
    G.print()
    print("Number of edges:" + str((G.numEdges())))


    print(hasCycleDFS(G))
