

# ------------- auxiliary: reading -----------------
def add_vertex(Adj, Name, Idx, u_name): 
    if u_name in Idx:
        u = Idx[u_name]
    else:
        u = len(Adj)
        Adj.append([])
        Name.append(u_name)
        Idx[u_name] = u
    return u

def read_undirected_graph(filename):
    f = open(filename)
    Name = []
    Idx = {}
    Adj = []
    for l in f:
        u_name, v_name, c = l.strip().split()         
        c = float(c)                                   
        u = add_vertex(Adj, Name, Idx, u_name)
        v = add_vertex(Adj, Name, Idx, v_name)
        Adj[u].append((v, c))
        Adj[v].append((u, c))
    f.close()
    return Adj, Name, Idx
# -------------------------------------------------



# ------------- auxiliary: Priority Queue, Heap -----------------
def enqueue(Q, x):          # simple insertion in a heap
    Q.append(x)
    i = len(Q) - 1
    while i > 0:
        p = (i - 1) // 2
        if Q[p] <= Q[i]:    # p is parent
            return
        Q[p], Q[i] = Q[i], Q[p]
        i = p

def extract_min(Q):         # basically dequeue (extract from heap)
    x = Q[0]
    Q[0] = Q[-1]            # take last element and put on start
    Q.pop()
    i = 0                   # node where we start from
    while True:
        m = i               # keeps track of currrent minimum
        if 2*i + 1 < len(Q):
            if Q[m] > Q[2*i+1]:
                m = 2*i + 1
            if 2*i + 2 < len(Q):          # if statement nested bc if 2*i+1<len(Q) false also 2*i+2<len(Q)
                if Q[m] > Q[2*i+2]:     
                    m = 2*i + 2
        if m == i:
            return x
        Q[m], Q[i] = Q[i], Q[m]
        i = m
# -------------------------------------------------



## INTRO:
# Using a Queue, where we put triples (cost used to do the sorting,
# vertex we are reaching, vertex we are coming from)

## ALGORITHM:
def prim(G):
    n = len(G)
    T = [None]*n
    for u in range(n):
        T[u] = []

    Q = []
    enqueue(Q, (0.0, 0, None))      # initially we have a cost of 0.0 to connect vertex 0 from None(predecessor)

    V = [False]*n                   # visited vertices

    while len(Q) != 0:              # main loop of the algorithm (similar to common algo structure)
        c, v, u = extract_min(Q)    # extract c, v, u (see intro description)
        if V[v]:                    # if we already visited v we go on
            continue
        if u != None:               # we need it for first case (inserting the starting vertex, if it's first edge)
            T[u].append((v, c))
            T[v].append((u, c))
            V[u] = True                #not needed
        V[v] = True
        for v2, c2 in G[v]:         # for each neighbors of the vertex v we just added, we insert them in queue with their cost
            if not V[v2]:
                enqueue(Q, (c2, v2, v))
    return T
            


## TESTS:
G, V, Idx = read_undirected_graph('/Users/samdamusi/Desktop/Algorithms-n-Datastructure/Algorithms/Graph/testfiles/graphCost1.txt')
T = prim(G)
print(T)
for u in range(len(T)):     # printing the seq of edges with cost
    for v, c in T[u]:
        if u < v:
            print(V[u], V[v], c)

        