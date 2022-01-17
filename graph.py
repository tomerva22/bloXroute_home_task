from queue import PriorityQueue

class Graph:
    # A constructor to create a graph
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    
    # A function to add an edge to the graph
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    # A function to print the shortest path from last dijkstra start_vertex to dst
    def printSolution(self, dst):#, src
        self.shortest_path = ''
        self.create_path_string(dst)
        print(self.shortest_path)

    # A function to creates the shortest path string
    def create_path_string(self, j):
        # if j is last dijkstra start_vertex
        if self.routes[j] == -1 :
            self.shortest_path += str(j) 
            return
        self.create_path_string(self.routes[j])
        self.shortest_path += ' -- (' + str(self.edges[j][self.routes[j]]) + ') --> ' + str(j)

    # The classic Dijkstra algorithm
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))
        
        self.routes = [-1] * self.v

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                            self.routes[neighbor] = current_vertex
        return D

# A function to create a graph from a file
def read_graph_from_file(file_name):
    f = open(file_name, "r")
    content = f.read().split('\n')
    graph=Graph(len(content))
    for row in content:
        edge = row.split(' ')
        graph.add_edge(int(edge[0]),int(edge[1]),int(edge[2])) # 3rd param might be float.
    return graph
