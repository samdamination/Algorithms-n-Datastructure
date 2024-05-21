## INTRO
"""Read a graph from a file object 'f' (text) containing one
    vertex and its adjacency list per line.  E.g.:

    Input:     | Graph:
    A B C      |  A --> B
    B C        |  |    /^
    C B        |  v   / |
               |  C<-/  /
               |   ^---/

    Return three containers:

    Name: (array) Vertex Id -> Vertex Name
    Adj: (array) Vertex Id -> array of Vertex Id
    Idx: (dictionary) Vertex Name -> Vertex Id
"""

## ALGORITHMS
def read_graph(f):        # f for file
    Name = []
    Adj = []
    Idx = {}              # Dictionary (curly braces): where you can index
    for l in f:           # not only by number but also strings for example. # for every line in file
        L = l.strip().split()   # crates an array with lines splitted
        if len(L) == 0:
            continue
        u_name = L[0]
        if u_name not in Idx:
            u = len(Name)
            Idx[u_name] = u
            Name.append(u_name)
            Adj.append([])          # u becomes from char to number (ex: from 'a' to 1)
        else:                       # can also put u = len(Name) at top and Idx[u_name] = u
            u = Idx[u_name]
        for i in range(1, len(L)):
            v_name = L[i]
            if v_name not in Idx:           # this if-else copied from above
                v = len(Name)          
                Idx[v_name] = v
                Name.append(v_name)
                Adj.append([])    
            else:
                v = Idx[v_name]
            Adj[u].append(v)                # Adj was all empty list at every position now we append the nodes
    return Name, Adj, Idx



## TESTS
""" Input file example:
    a b
    b c 
    c b a 
    d  
"""
print("--- tests read_graph: ---")
file = open('/Users/samdamusi/Desktop/Algorithms-n-Datastructure/Algorithms/Graph/testfiles/graph1.txt', 'r')
V, G, Idx = read_graph(file)
file.close()
print(V)
print(G)
print(Idx)










## BFS -------------------------

## INTRO
# BFS uses a Queue to keep track of next-to-be-visited vertex
# You create 2 datastructure: Distance, Predecessors

## ALGORITHM
def bfs(G, s):          # s is start (names don't exist anymore here, just concerns us the id/number node)
    n = len(G)          # G is the Adj list, s (and below u) are id/numer of the node (node 1,...)
    D = [None]*n        # Distance vector
    P = [None]*n        # Path vector (pi, stores predecessors), can add P[s] = s se si vuole s al posto di None come predecessor

    Q = [None]*n        # Queue
    Q_head = 0
    Q_tail = 0

    # enqueue s into Q
    Q[Q_tail] = s
    Q_tail = Q_tail + 1
    D[s] = 0            # initialize distance of s (from s) to 0

    while Q_head != Q_tail:
        # dequeue
        u = Q[Q_head]
        Q_head = Q_head + 1
        for v in G[u]:
            if D[v] == None:
                D[v] = D[u] + 1
                P[v] = u
                # enqueue v
                Q[Q_tail] = v
                Q_tail = Q_tail + 1
    return D, P

## TESTS:
print("--- tests BFS: ---")
D, P = bfs(G, Idx['a'])
print(D)
print(P)








## DFS -------------------------

## INTRO
# Datastructures are same, DFS uses a Stack instead of a Queue
# You create 2 datastructure: Discovery, Finish (time, intended as number of steps)
# Here called as In and Out

## ALGORITHM
def dfs(G):
    n = len(G)
    D = [None]*n        # Discovery time
    F = [None]*n        # Finish time
    t = 0               # time

    S = []              # stack

    for u in range(n):
        if D[u] == None:    # if we havent discovered the node yet
            # push u onto stack
            S.append(u)
            while len(S) > 0:       # until the stack is empty go and discover (we descover a node from the stack
                u = S[-1]           # thus the stack can have same node multiple times, if we pop the same node and see has already been discovered then loop)
                if D[u] == None:    # 1 - not yet discovered
                    D[u] = t
                    t = t + 1
                    for v in G[u]:  # for every neighbour of u
                        if D[v] == None:
                            S.append(v)
                elif F[u] == None:  # 2 - discovered, not finished
                    F[u] = t
                    t = t + 1
                    S.pop()
                else:               # 3 - discovered, finished
                    S.pop()
    return D, F

## TESTS:
print("--- tests DFS: ---")
file = open('/Users/samdamusi/Desktop/Algorithms-n-Datastructure/Algorithms/Graph/testfiles/graph2.txt', 'r')
V, G, Idx = read_graph(file)    # here nodes are 1 2 3 6 5, depends how they inseted in adj list
file.close()
D, F = dfs(G)
print(D)
print(F)



# dfs to find loops:
""" def is_cyclic(G):
    n = len(G)
    D = [None]*n        # Discovery time
    F = [None]*n        # Finish time
    t = 0               # time

    S = []              

    for u in range(n):
        if D[u] == None:    
            S.append(u)
            while len(S) > 0:      
                u = S[-1]           
                if D[u] == None:    
                    D[u] = t
                    t = t + 1
                    for v in G[u]:  
                        if D[v] == None:
                            S.append(v)
                        elif F[v] == None:           # if we encounter a discovered node but not finished
                            return True              # then loops
                elif F[u] == None:  
                    F[u] = t
                    t = t + 1
                    S.pop()
                else:               
                    S.pop()
    return False """