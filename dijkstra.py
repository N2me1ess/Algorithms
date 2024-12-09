from graph import Graph
import heapq as hq

class Path:
    def __init__(self, w, s):
        self.w = w
        self.s = s

    def getW(self):
        return self.w

    def getS(self):
        return self.s

def dijkstra (G, s):
    D = {n : Path(float('inf'), f"{s}") for n in G.getNodes()}
    D[s] = Path(0, f"{s}")

    pq = []
    hq.heappush(pq, (0, s))

    while pq:
        __, u = hq.heappop(pq)

        for v in G.getNeighbors(u):
            w = G.edgeWeight(u, v)

            # Recurrence Formulation D[v] = min(D[u] + edgeweight(u, v), D[v])
            if D[u].getW() + w < D[v].getW():
                newPath = Path(D[u].getW() + w, D[u].getS() + f" --> {v}")
                D[v] = newPath

                hq.heappush(pq, (D[v].getW(), v))

    return D

def printShortestPaths(D, s):
    for n, path in D.items():
        print(f"Shortest Path from {s} to {n}: {path.getS()}. Weight: {path.getW()}")


if __name__ == "__main__":
    G = Graph()
    s = 3
    for i in range(5):
        G.addNode(i)

    G.addEdge(3, 2, 2)
    G.addEdge(3, 4, 1)
    G.addEdge(2, 0, 1)
    G.addEdge(4, 0, 3)
    G.addEdge(2, 4, 1)
    G.addEdge(4, 1, 3)

    D = dijkstra(G, s)

    printShortestPaths(D, s)