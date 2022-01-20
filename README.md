# bloXroute_home_task

The goal is to find the fastest path in a graph.

You have a graph of 6 nodes. Each node is connected to the other. 
Connection from Node1 to Node2 is not the same in the cost as connection from Node2 to Node1. 
This means there are 6*5 = 30 connections.
Given the graph connection cost (you can set it as you want), you should find the fastest route between node1 and node2.

Your program should accept a file that contains the graph connections cost, and the name of source and target nodes.
The program should return the fastest route, and the cost of each leg.
For example: SourceNode -- (5) --> Node1 -- (7) -->  ... -- > NodeN -- (3) --> TargetNode

Each step is in the following format:
<node name> -- (<cost of the leg>) -->

You will be checked on:
1. correct result
2. code optimization (how much time it took to find the fastest route)
3. clear code (writing standards)
4. Object Oreiented 
