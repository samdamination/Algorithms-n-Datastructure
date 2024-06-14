# ----------- disjoint set  import -----------
class disjoint_set:
    def __init__(self):
        self.parent = self          # at the beginning, when u create 1 elem. disjoint set it
                                    # point to itself (it's its own representative)


def set_find(s):                # function to get the representative of a node
    while s.parent != s:
        s = s.parent
    return s

def set_union(s1, s2):          # checking the 2 repres. of 2 set are different
    s1 = set_find(s1)
    s1.parent = set_find(s2)
# ----------- ----------- ----------- -----------



# ----------- read undir. graph  import -----------
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
        u_name, v_name, c = l.strip().split()           # input format: a b 30 (= a connects b and viceversa w. cost 30)
        c = float(c)                                    # transform '30' to number
        u = add_vertex(Adj, Name, Idx, u_name)
        v = add_vertex(Adj, Name, Idx, v_name)
        Adj[u].append((v, c))
        Adj[v].append((u, c))
    f.close()
    return Adj, Name, Idx
# ----------- ----------- ----------- -----------








## INTRO:
# Takes a graph (tree) and returns another graph (tree), the minimal spanning tree

## ALGORITHM:
def kruskal(G):
    n = len(G)
    E = []
    T = [None]*n                            # solution (Adj graph spanning tree)
    for u in range(n):                      # transforming Adj graph into set of edges (cost, u, v)
        for v, c in G[u]:
            if u < v:                       # questo perchè se no ci sono 2 entry (undirected)
                E.append((c, u, v))
    E.sort()                                # sorted in base al primo elemento del triplet (in this case the cost)
    S = [None]*n
    for u in range(n):
        S[u] = disjoint_set()               # create a disjoint set for each element
    for u in range(n):
        T[u] = []
    for c, u, v in E:                             # scan the edges in sorted order
        if set_find(S[u]) != set_find(S[v]):       # check wheter u and v are in same set or not
            set_union(S[u], S[v])
            T[u].append((v, c))                    # add that edge to the tree
            T[v].append((u, c))
    return T



## TESTS:
G, V, Idx = read_undirected_graph('/Users/samdamusi/Desktop/Algorithms-n-Datastructure/Algorithms/Graph/testfiles/graphCost1.txt')
print('--- input graph G with costs ---')
print(G)
print('--- min spanning tree kruskal ---')
T = kruskal(G)
print(T)
for u in range(len(T)):
    for v, c in T[u]:
        if u < v:
            print(V[u], V[v], c)



    

               

# E set before sort
[(1.0, 0, 1),
(2.0, 0, 3), 
(1.0, 1, 2), 
(1.0, 2, 3), 
(3.0, 2, 4), 
(1.0, 3, 5), 
(3.0, 3, 6), 
(2.0, 4, 6), 
(1.0, 5, 7), 
(3.0, 5, 6), 
(1.0, 6, 8), 
(3.0, 6, 7), 
(1.0, 6, 9), 
(3.0, 6, 10), 
(2.0, 7, 8), 
(2.0, 8, 9), 
(3.0, 9, 10), 
(3.0, 9, 11), 
(1.0, 10, 11)]

# E set after sort
[(1.0, 0, 1), 
 (1.0, 1, 2), 
 (1.0, 2, 3), 
 (1.0, 3, 5), 
 (1.0, 5, 7), 
 (1.0, 6, 8), 
 (1.0, 6, 9), 
 (1.0, 10, 11), 
 (2.0, 0, 3), 
 (2.0, 4, 6), 
 (2.0, 7, 8), 
 (2.0, 8, 9), 
 (3.0, 2, 4), 
 (3.0, 3, 6), 
 (3.0, 5, 6), 
 (3.0, 6, 7), 
 (3.0, 6, 10), 
 (3.0, 9, 10), 
 (3.0, 9, 11)]

# Graph G as input
[[(1, 1.0), (3, 2.0)], 
[(0, 1.0), (2, 1.0)], 
[(1, 1.0), (3, 1.0), (4, 3.0)], 
[(0, 2.0), (2, 1.0), (5, 1.0), (6, 3.0)], 
[(2, 3.0), (6, 2.0)], 
[(3, 1.0), (7, 1.0), (6, 3.0)], 
[(3, 3.0), (5, 3.0), (4, 2.0), (8, 1.0), (7, 3.0), (9, 1.0), (10, 3.0)], 
[(5, 1.0), (6, 3.0), (8, 2.0)], 
[(6, 1.0), (9, 2.0), (7, 2.0)], 
[(8, 2.0), (6, 1.0), (10, 3.0), (11, 3.0)], 
[(6, 3.0), (9, 3.0), (11, 1.0)], 
[(9, 3.0), (10, 1.0)]]