

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
def enqueue(Q, x):          
    Q.append(x)
    i = len(Q) - 1
    while i > 0:
        p = (i - 1) // 2
        if Q[p] <= Q[i]:    
            return
        Q[p], Q[i] = Q[i], Q[p]
        i = p

def extract_min(Q):         
    x = Q[0]
    Q[0] = Q[-1]            
    Q.pop()
    i = 0                   
    while True:
        m = i               
        if 2*i + 1 < len(Q):
            if Q[m] > Q[2*i+1]:
                m = 2*i + 1
            if 2*i + 2 < len(Q):          
                if Q[m] > Q[2*i+2]:     
                    m = 2*i + 2
        if m == i:
            return x
        Q[m], Q[i] = Q[i], Q[m]
        i = m
# -------------------------------------------------



## INTRO:
# Copy from Prim and change one line

## ALGORITHM:
def dijkstra(G):
    n = len(G)
    T = [None]*n
    for u in range(n):
        T[u] = []

    Q = []
    enqueue(Q, (0.0, 0, None))      

    V = [False]*n                   

    while len(Q) != 0:              
        c, v, u = extract_min(Q)    
        if V[v]:                    
            continue
        if u != None:               
            T[u].append((v, c))
            T[v].append((u, c))
        V[v] = True
        for v2, c2 in G[v]:        
            if not V[v2]:
                enqueue(Q, (c + c2, v2, v)) # only difference c + c2
    return T
            


## TESTS:
"""Input file format:
a e 1
e i 1
a f 2
f i 1
i j 3
f b 1
f g 3
b c 1
b g 3
j g 2
d g 1
c g 3
d h 2
g h 1
g k 3
h k 3
h m 3
k m 1
c d 2
"""
G, V, Idx = read_undirected_graph('/Users/samdamusi/Desktop/Algorithms-n-Datastructure/Algorithms/Graph/testfiles/graphCost1.txt')
print(Idx)
T = dijkstra(G)
print(T)
for u in range(len(T)):     # printing the seq of edges with cost
    for v, c in T[u]:
        if u < v:
            print(V[u], V[v], c)

        