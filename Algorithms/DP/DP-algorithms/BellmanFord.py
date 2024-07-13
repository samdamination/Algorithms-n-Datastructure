# The main function that finds shortest distances from src to all other vertices using Bellman-Ford algorithm.
# The function also detects negative weight cycle. The row graph[i] represents i-th edge with three values u, v and w.
def BellmanFord(graph, V, E, src): # graph = [(u0, v0, c0), (u1, v1, c1)...] edges
    D = [float('inf')] * V         # Initialize distance of all vertices as infinite.
    D[src] = 0                # initialize distance of source as 0
 
    # Relax all edges |V| - 1 times. A simple shortest path from src to any other
    # vertex can have at-most |V| - 1 edges
    for i in range(V - 1):
        for j in range(E):
            if D[graph[j][0]] + graph[j][2] < D[graph[j][1]]:   # D[u] + c < D[v]
                D[graph[j][1]] = D[graph[j][0]] + graph[j][2]   # D[v] = D[u] + c
 
    # check for negative-weight cycles. The above step guarantees shortest distances if graph
    # doesn't contain negative weight cycle. If we get a shorter path, then there is a cycle.
    for i in range(E):
        u = graph[i][0]
        v = graph[i][1]
        weight = graph[i][2]
        if D[u] != float('inf') and D[u] + weight < D[v]:
            print("Graph contains negative weight cycle")
 
    print("Vertex Distance from Source")        # Optional to print out
    for i in range(V):
        print("%d\t\t%d" % (i, D[i]))