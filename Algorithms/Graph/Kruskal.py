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



## INTRO
# Reading an undirected graph with costs for edges

## ALGORITHMS
# like in read_graph
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








## INTRO:
# Takes a graph (tree) and returns another graph (tree), the minimal spanning tree

## ALGORITHM:
def kruskal(G):
    n = len(G)
    E = []
    for u in range(n):
        for v, c in G[u]:
            if u < v:
                E.append((c, u, v))
    E.sort()
    S = [None]*n
    for u in range(n):
        S[u] = disjoint_set()               # create a disjoint set for each element
    T = [None]*n
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



    

               

