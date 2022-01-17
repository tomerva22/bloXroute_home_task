import graph

if __name__=="__main__":
    # this solution suppose that the graph wheights are Native numbers
    g = graph.read_graph_from_file("F:\\Interview Tasks\\bloXroute\\2\\test_graph.txt")
    # inorder for the solution to be correct first use dijkstra(SourceNode) and then use printSolution(TargetNode)
    g.dijkstra(0)
    g.printSolution(4)
    g.printSolution(6)
    g.printSolution(5)
