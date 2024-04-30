####### BST - Datastructure #######
# --------------------------------- #
import random

# INTRO: 

# DATASTRUCTURE
# defining node
class Node:
    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

# printing tree    
def bst_in_order_walk(t):   # complexity O(n) can't obv. do better 
    if t != None:           # base case: if t is non we do nothing
        bst_in_order_walk(t.left)
        print(t.key)
        bst_in_order_walk(t.right)
        # instead of the print in between put print here for post-order

def bst_min(t):
    if t == None:
        return None
    while t.left != None:   # go all the way to left bottom
        t = t.left
    return t.key

def bst_successor(t):
    if t == None:
        return None
    if t.right != None:
        return bst_min(t.right)     # se mettiamo che bst min ritorna un nodo (non key)
    p = t.parent
    while p != None and t == p.right:
        t = p
        p = p.parent
    return p

def bst_search(t, k):       
    while t != None:
        if k < t.key:
            t = t.left
        elif k > t.key:
            t = t.right
        else:
            return True
    return False
##
""" def bst_search(t, k):
    if t == None:
        return False
    if t.key == k:
        return True
    elif t.key > k:
        return bst_search(t.left)
    else:
        return bst_search(t.right) """ # ??

def bst_insert(t, k):       # per inserire una key in console si dovrà fare: t = bst_insert(t, key) pk
    if t == None:           # ritorna un tree, non lo modifica (complexity: h of tree)
        return Node(k)
    x = t                   # for not loosing t
    while True:
        if k <= x.key:      # if the key is less that this node then we look to the left
            if x.left == None:
                x.left = Node(k)
                x.left.parent = x
                return t
            x = x.left
        else:
            if x.right == None:
                x.right = Node(k)
                x.right.parent = x
                return t
            x = x.right

def random_tree(n):     # returns a tre from a sequence of n numbers
    A =[i for i in range(n)]
    random.shuffle(A)
    t = None
    for a in A:
        t = bst_insert(t, a)

def bst_height(t):
    if t == None:
        return 0
    return max(bst_height(t.left), bst_height(t.right)) + 1

def right_rotate(x):        # see image
    assert x.left != None   # returns the tree from y (so you have to do t = right_rotate(t) to rotate head)
    y = x.left
    x.left = y.right
    y.right = x
    return y

def left_rotate(x):        # simply swap left-right
    assert x.right != None
    y = x.right
    x.right = y.left
    y.left = x
    return y

def root_insert(t, k):
    if t == None:
        return Node(k)
    if k <= t.key:
        t.left = root_insert(t.left, k)
        return right_rotate(t)
    else:
        t.right = root_insert(t.right, k)
        return left_rotate(t)



# TESTS
T = None