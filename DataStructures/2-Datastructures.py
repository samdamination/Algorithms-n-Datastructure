

import math


## STACK ---
S = [None]*100
N = 0

def push(key):
    global S,N
    if N < len(S):
        S[N] = key
        N = N + 1
    else:
        print('stack overflow')

def pop():
    global S,N
    if N > 0:
        N = N - 1
        return S[N]
    else:
        print('stack underflow')

def isempty():
    global S,N
    return N == 0



## HEAPS ---
def createmaxheap(A):
    i = math.floor(len(A)-1) // 2
    while i >= 0:
        maxheapify(A, i, len(A))
        i = i - 1

def maxheapify(A, i, hs):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < hs and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < hs and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        maxheapify(A, largest, hs)



## LINKED-LISTS ---
class ListElement:
    def __init__(self, v):
        self.value = v
        self.next = self
        self.prev = self

sentinel = ListElement(None)


def listinsertafter(key, pos):
    new_elem = ListElement(key)
    new_elem.prev = pos
    new_elem.next = pos.next
    new_elem.next.prev = new_elem
    new_elem.prev.next = new_elem

def listprint():
    el = sentinel.next
    while el != sentinel:
        print(el.value)
        el = el.next        # .prev for backward print

def listremoveafter(pos):
    to_delete = pos.next
    new_pointer = to_delete.next
    pos.next = new_pointer
    new_pointer.prev = pos



## QUEUE ---
Q = [None]*100

front = 0       # left

back = 0        # right A=[88, 76, N, N, N] back=2, front=0

def enqueue(key):
    global Q, front, back
    if isfull():
        print('queue full')
    else:
        Q[back] = key
        back = next(back)

def dequeue():
    global front, back, Q
    if isempty():
        print('empty queue')
    else:
        x = Q[front]
        front = next(front)
        return x

def isfull():
    global front, back
    return next(back) == front

def isempty():
    return front == back

def next(p):
    global Q
    p = p + 1
    if len(Q) == p:
        p = 0
    return p

## PRIORITY-QUEUE
"""..."""














### ======================== SECOND PART ======================== ###







## BINARY SEARCH TREES ---
import random

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.parent = None

def bst_in_order_walk(t):
    if t != None:
        bst_in_order_walk(t.left)
        print(t.key)
        bst_in_order_walk(t.right)

def bst_min(t):
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t.key

def bst_successor(t):
    if t == None:
        return None
    if t.right != None:
        return bst_min(t.right) # node
    p = t.parent
    while p != None and t == p.right:
        t = p
        p = p.parent
    return p

def bst_search(t, target):
    while t != None:
        if t.key < target:
            t = t.right
        elif t.key > target:
            t = t.left
        else:
            return True
    return False

def bst_insert(t, key):
    if t == None:
        return Node(key)
    x = t
    while True:
        if key <= x.key:
            if x.left == None:
                x.left = Node(key)
                x.left.parent = x
                return t
            x = x.left
        else:
            if x.right == None:
                x.right = Node(key)
                x.right.parent = x
                return t
            x = x.right

def bst_height(t):
    if t == None:
        return 0
    return max(bst_height(t.left), bst_height(t.right)) + 1

def right_rotate(x):
    assert x.left != None
    y = x.left
    x.left = y.right
    y.right = x
    return y

def left_rotate(x):
    assert x.right != None
    y = x.right
    x.right = y.left
    y.left = x
    return y

def root_insert(t, key):
    if t == None:
        return Node(key)
    if key <= t.key:
        t.left = root_insert(t.left, key)
        return right_rotate(t)
    else:
        t.right = root_insert(t.right, key)
        return left_rotate(t)

# Given a SORTED array, build a balanced BST
def array_to_bst(A, l, r):
    if l <= r:
        m = math.floor((l+r)/2)
        v = A[m]
        node = Node(v)
        node.left = array_to_bst(A, l, m-1)
        node.right = array_to_bst(A, m+1, r)
        return node
    # return None

# bst_delete ??


## RB-TREES --- (nope no-code)

## B-TREES --- (nope no-code)



## DISJOINT SETS ---
class disjoint_set:
    def __init__(self):
        self.parent = self

def set_representative(s):
    while s.parent != s:
        s = s.parent
    return s

def set_union(s1, s2):
    s1 = set_representative(s1)
    s1.parent = set_representative(s2)



## GRAPHS ---
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
def read_graph(f):
    Name = []
    Adj = []
    Idx = {}
    for l in f:
        L = l.strip().split()
        if len(L) == 0:
            continue
        u_name = L[0]
        if u_name not in Idx:
            u = len(Name)
            Idx[u_name] = u
            Name.append(u_name)
            Adj.append([])
        else:
            u = Idx[u_name]
        for i in range(1, len(L)):
            v_name = L[i]
            if v_name not in Idx:
                v = len(Name)
                Idx[v_name] = v
                Name.append(v_name)
                Adj.append([])
            else:
                v = Idx[v_name]
            Adj[u].append(v)
    return Name, Adj, Idx       # also V, G, Idx

""" --- Read Undirected Graphs --- """

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


