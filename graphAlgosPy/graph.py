# Graph Class

from collections import defaultdict


class Graph:
    def __init__(self):
        # Represent our edges in a nxn matrix
        self.edges = defaultdict(dict)
        self.nNodes = 0

    def getNodes(self):
        return self.edges.keys()

    def addNode(self, node):
        if node not in self.getNodes():
            self.edges[node] = {}
            self.nNodes += 1
        else:
            print(f"Node: {node} already added")

    def checkValidNode(self, n):
        return n in self.edges

    def edgeWeight(self, n1, n2):
        return self.edges[n1].get(n2, -1)

    def getNeighbors(self, n):
        if self.checkValidNode(n):
            return self.edges[n].keys()
        return {}

    def addEdge(self, n1, n2, weight=1):
        if self.checkValidNode(n1) and self.checkValidNode(n2):
            self.edges[n1][n2] = weight

            # print(f"successfully added edge {n1}, {n2}, Weight: {weight}")
        else:
            pass
            # print(f"unsuccessfully added edge {n1}, {n2}, Weight: {weight}")

    def removeEdge(self, n1, n2):
        if self.checkValidNode(n1) and self.checkValidNode(n2):
            del self.edges[n1][n2]

            print(f"successfully removed edge {n1}= {n2}")
        else:
            print(f"unsuccessfully removed edge {n1}, {n2}")

    def printEdges(self):
        for node, neighbors in self.edges.items():
            print(f"Node {node}: {neighbors}")


if __name__ == "__main__":
    graph1 = Graph()
    graph1.addNode("dorm")
    graph1.addNode("tressider")
    graph1.addNode("huang")
    graph1.addNode("farillaga")
    graph1.addEdge("dorm", "tressider", 5)
    graph1.addEdge("huang", "farillaga", 10)
    graph1.addEdge("dorm", "huang", 5)

    graph1.printEdges()
