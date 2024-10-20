from collections import deque

class Graph:
    def __init__(self):
        # initalizing an empty graph represnted as a dict
        self.graph = {}
    
    def add_edge(self, u, v):
    # adds an edge between nodes u and v
        if u not in self.graph:
        # create a list for u if not present in already
            self.graph[u] = []
        if v not in self.graph:
        # create a list for v if not present in already
            self.graph[v] = []
        # creating adjacency list (undirected)
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
    # started with BFS --> starting node
        visited = set() # Keeps track of visted nodes
        queue = deque([start]) # initalizes a queue with a starting node
        visited.add(start) # marking as visted

        while queue: # continue until it is empty
            node = queue.popleft() # removing and returning the first node from the queue
            print(node, end=" ")

            for neighbor in self.graph[node]: # visiting neighbor
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def bfs_with_distances(self, start):
        
        visited = set()
        queue = deque([(start, 0)])  # Start with a tuple (node, distance)
        visited.add(start)

        distances = {start: 0}

        while queue:
            node, dist = queue.popleft()
            print(f"Node: {node}, Distance: {dist}")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distances[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1))  # Enqueue as tuple

    def display_menu(self):
        print("\n----Graph Menu ----")
        print("1. Add Edge")
        print("2. BFS Traversal")
        print("3. BFS Traversal with Distances")
        print("4. Exit")

def main():
    graph = Graph()

    while True:
        add_more = input("Do you want to add a large graph (y/n)? ")
        if add_more.lower() == "y":
            edges = int(input("How many edges do you want: "))
            for i in range(edges):
                u = input("Enter the first node: ")
                v = input("Enter the second node: ")
                graph.add_edge(u, v)
                print(f"Edge added between {u} and {v}")
            break
        else:
            break

    while True:
        graph.display_menu()
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            u = input("Enter the first node: ")
            v = input("Enter the second node: ")
            graph.add_edge(u, v)
            print(f"Edge added between {u} and {v}")
        
        elif choice == 2:
            start = input("Enter the starting node for BFS: ")
            if start in graph.graph:
                print(f"BFS traversal starting from node {start}:")
                graph.bfs(start)
            else:
                print("Node not found in the graph")
        
        elif choice == 3:
            start = input("Enter the starting node for BFS with distances: ")
            if start in graph.graph:
                graph.bfs_with_distances(start)
            else:
                print("Node not found in the graph")

        elif choice == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
