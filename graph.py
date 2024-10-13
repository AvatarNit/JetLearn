# breadth-first search traversal
# directed, undirected graphs --> 

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def display_menu(self):
        print("\n----Graph Menu ----")
        print("1. Add Edge")
        print("2. BFS Traversal")
        print("3. Exit")

def main():
    graph = Graph()

    while (True):
        graph.display_menu()
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            u = input("Enter the first node: ")
            v = input("Enter the second node: ")
            graph.add_edge(u, v)
            print(f"Edge added between {u} and {v}")
        
        elif choice == 2:
            start = input("Enter the starting node for BFS: ")
            if start in graph.graph:
                print("BFS traversal starting from node" , start, ":")
                graph.bfs(start)
            else:
                print("Node not found in the graph")

        elif choice == 3:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option")

if __name__ == "__main__":
    main()