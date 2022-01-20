import graph

if __name__=="__main__":
    # this solution suppose that the graph wheights are Native numbers
    # task fully connected graph case:
    g1 = graph.read_graph_from_file("test_fully_connected.txt")    
    # inorder for the solution to be correct first use dijkstra(SourceNode) and then use printSolution(TargetNode)
    g1.dijkstra('n1')
    g1.printSolution('n1')
    g1.printSolution('n2')
    g1.printSolution('n3')
    g1.printSolution('n4')
    # other cases:
    # not fully connected graph case
    g = graph.read_graph_from_file("test_graph.txt")
    g.dijkstra('n0')
    g.printSolution('n4')
    g.printSolution('n6')
    g.printSolution('n5')
    g.printSolution('n8')
    g.printSolution('n9')
    g.printSolution('n10')
    g.dijkstra('n9')
    g.printSolution('n6')
    #g.update_edge_weight('n0','n1', 1)
    g3 = graph.read_graph_from_file("test_one_node_graph.txt")
    # graph with 2 nodes and 1 edge
    g3.dijkstra('n0')
    g3.printSolution('n1') 
    # empty graph
    #g4 = graph.read_graph_from_file("test_empty_graph.txt")
    #g4.dijkstra('n0')
    #g4.printSolution('n1')
