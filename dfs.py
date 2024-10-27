from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # add edges
    def addEdge(self, u, v):
        self.graph[u].append(v)
    

    # isCyclicUtil : helps to perform depth-first search starting from a specific node
    # isCyclic : this function initializes the visited and recStack list and iterated over all the visited nodes to ensure that every node in the graph is checked

    # to check cycle
    def isCyclicUtil(self, v, visited, recStack):
        # mark current nodes as visited
        # add to recStack
        visited[v] = True
        recStack[v] = True

        # recursion for all the neighbors
        # if any neighbor is visited and in recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True
        # the node needs to be popped from the recursion stack
        # before function ends
        recStack[v] = False
        return False
    
    def isCyclic(self):
        visited = [False]*(self.V)
        recStack = [False]*(self.V)
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node,visited,recStack):
                    return True
        return False

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

if g.isCyclic():
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

g1 = Graph(4)
g1.addEdge(0,1)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(1,3)
g1.addEdge(3,0)


if g1.isCyclic():
    print("Graph has a cycle")
else:
    print("Graph has no cycle")