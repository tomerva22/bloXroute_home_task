from queue import PriorityQueue
import os

class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def update_weight(self, new_weight):
        self.weight = new_weight

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    # used to insert an edge
    def add_neighbor(self, edge):
        self.edges[edge.dst] = edge

    
class Graph:
    # A constructor to create a graph
    def __init__(self):#, edges
        #self.num_of_nodes = len(edges)
        self.nodes = {}
        # there is no reason to hold edges list for this task, I've done it to represent as many small obj as possible
        # if we want to add it we should add it to init and add_edge
        # self.edges = []
        
    # add node to the graph
    def add_node(self, name):
        if name in self.nodes:
            print("Node already exists, no action is done.")
        else:
            new_node = Node(name)
            self.nodes[new_node.name] = new_node

    # A function to add an edge to the graph
    def add_edge(self, edge):
        if not edge.src in self.nodes:
            print(edge.src + " not in the graph.")
            return
        if not edge.dst in self.nodes:
            print(edge.dst + " not in the graph.")
            return
        self.nodes[edge.src].add_neighbor(edge)
        #self.edges.append(edge)

    # A function to print the shortest path from last dijkstra start_vertex to dst
    def printSolution(self, dst):#, src
        self.shortest_path = ''
        if (not dst in self.routes) and dst in self.nodes:
            print("No available path to node " + dst + ".")
            return
        if not dst in self.routes:
            print("Node " + dst + " not in this graph.")
            return
        self.create_path_string(dst)
        print(self.shortest_path)

    # A function to creates the shortest path string
    def create_path_string(self, j):
        # if j is last dijkstra start_vertex
        if self.routes[j] == None :
            self.shortest_path += str(j) 
            return
        self.create_path_string(self.routes[j])
        if j in self.nodes[self.routes[j]].edges.keys():
            self.shortest_path += ' -- (' + str(self.nodes[self.routes[j]].edges[j].weight) + ') --> ' + str(j)

    def update_edge_weight(self, src, dst, new_weight):
        if not src in self.nodes:
            print(src + " not in the graph.")
            return
        if not dst in self.nodes:
            print(dst + " not in the graph.")
            return
        if not dst in self.nodes[src].edges:
            print("The edge (" + src + "," + dst + ") not in the graph.")
            return
        self.nodes[src].edges[dst].update_weight(new_weight)
        #pointers test
        #for edge in self.edges:
        #    if edge.src == src and edge.dst == dst:
        #        print(self.nodes[src].edges[dst].weight == edge.weight)

    # The classic Dijkstra algorithm
    def dijkstra(self, start_vertex):
        if not start_vertex in self.nodes:
            print("Node " + start_vertex + " not in this graph.")
            self.routes = {}
            return None
        D = {node:float('inf') for node in self.nodes}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))
        
        self.routes = {start_vertex: None}#node:None for node in self.nodes
        self.visited = []

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor,edge in self.nodes[current_vertex].edges.items():
                if self.nodes[current_vertex].edges[neighbor] != None:
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + edge.weight
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                            self.routes[neighbor] = current_vertex
        return D

# A function to create a graph from a file
def read_graph_from_file(file_name):
    f = open(os.path.join(os.getcwd(), file_name), "r")
    content = f.read().split('\n')
    graph=Graph()
    for row in content:
        node_edges = row.split(' ')
        if row == '':
            break
        src = node_edges[0]
        dst = node_edges[1]
        weight = node_edges[2]
        if not src in graph.nodes:
            graph.add_node(src)
        if not dst in graph.nodes:
            graph.add_node(dst)
        edge = Edge(src, dst, int(weight))
        graph.add_edge(edge)
    return graph
