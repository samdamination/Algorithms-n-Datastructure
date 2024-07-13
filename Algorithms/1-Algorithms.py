import math

## BINARY SEARCH ()
def binary_search(A, key):
    l = 0
    r = len(A)
    while r > l:
        mid = math.floor(l+r) // 2
        if A[mid] == key:
            return True
        elif A[mid] < key:
            l = mid + 1
        else:
            r = mid
    return False



## BUBBLESORT - inplace
def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A



## INSERTION SORT
def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        x = A[i]
        while j > -1 and A[j] > x: # also? A[j+1] instead of x   NOPEEE j changes
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x
    return A



## SELECTION SORT - inplace
def selection_sort(A):
    for i in range(len(A) - 1): 
        min = i
        for j in range (i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    #return A



## QUICKSORT ----
def quicksort(A, begin, end):
    if begin < end:
        k = partition(A, begin, end)
        quicksort(A, begin, k - 1)
        quicksort(A, k + 1, end)


def partition(A, begin, end):
    pivot = A[end]
    j = begin                           # j indica primo elemento non sortato a sinistra (da scambiare se si trova un min del pivot)
    for i in range(begin, end+1):       # +1 pk end è len(A)-1
        if A[i] <= pivot:               # se il numero è minore di pivot lo sposto all'inizio (j)
            A[i], A[j] = A[j], A[i]
            j = j + 1
    return j - 1                        # j - 1 pk con ultimo swap j punta a uno in anvanti al pivot 



## MERGESORT ----
def mergesort(A):
    n = len(A)
    if n <= 1:
        return A
    mid = n // 2
    L = mergesort(A[0:mid])
    R = mergesort(A[mid:n])
    return merge(L, R)

def merge(A, B):
    R = []
    i = 0
    j = 0
    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or B[j] > A[i]):
            R.append(A[i])
            i = i + 1
        else:
            R.append(B[j])
            j = j + 1
    return R



## HEAPSORT ----
def buildmaxheap(A):
    i = math.floor(len(A)-1 // 2)
    while i >= 0:
        maxheapify(A, i, len(A))
        i = i - 1

def maxheapify(A, i, hs):
    l = 2 * i + 1               # right(i)   !!! inexes start 0
    r = 2 * i + 2               # left(i)
    if l < hs and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r < hs and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxheapify(A, largest, hs)      # sistemi in basso quello che hai scambiato

def heapsort(A):
    buildmaxheap(A)
    hs = len(A)
    i = hs - 1
    while hs > 1:
        A[0], A[i] = A[i], A[0]
        hs = hs - 1
        maxheapify(A, 0, hs)
        i = i - 1







### ======================== SECOND PART ======================== ###







## BFS ---
def bfs(G, s):
    n = len(G)
    D = [None]*n
    P = [None]*n

    Q = [None]*n
    Q_head = 0
    Q_tail = 0

    Q[Q_tail] = s
    Q_tail = Q_tail + 1
    D[s] = 0

    while Q_head != Q_tail:
        u = Q[Q_head]
        Q_head = Q_head + 1
        for v in G[u]:
            if D[v] == None:
                D[v] = D[u] + 1
                P[v] = u
                Q[Q_tail] = v
                Q_tail = Q_tail + 1
    return D, P



## DFS ---
def dfs(G):
    n = len(G)
    D = [None]*n
    F = [None]*n
    t = 0

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
                elif F[u] == None:
                    F[u] = t
                    t = t + 1
                    S.pop()
                else:
                    S.pop()
    return D, F



## MST ---
# Kruskal (need: disjoint sets, read undir. graph)
# input format: a b 30 (= a connects b and viceversa w. cost 30)
def kruskal(G):
    n = len(G)
    E = []
    T = [None]*n
    for u in range(n):
        for v, c in G[u]:
            if u < v:
                E.append((c, u, v))
    E.sort() 
    S = [None]*n
    for u in range(n):
        S[u] = disjoint_set()
    for u in range(n):
        T[u] = []
    for c, u, v in E:
        if find_representative(S[u]) != find_representative(S[v]):
            set_union(S[u], S[v])
            T[u].append((v, c))
            T[v].append((u, c))
    return T


# Prim (need: priorityQueue/Heap, read undir. graphs)
# --- aux
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
        if 2*i+1 < len(Q):
            if Q[m] > Q[2*i+1]:
                m = 2*i+1
            if 2*i+2 < len(Q):
                if Q[m] > Q[2*i+2]:
                    m = 2*i+2
        if m == i:
            return x
        Q[m], Q[i] = Q[i], Q[m]
        i = m
# ---

def prim(G):
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
            V[u] = True
        V[v] = True
        for v2, c2 in G[v]:
            if not V[v2]:
                enqueue(Q, (c2, v2, v))
    return T



## DIJKSTRA ---
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







### ======================== DYNAMIC PROOGRAMMING ======================== ###







# Bellman-Ford

# Longest Increasing Subsequence

# Edit distance

# ...?