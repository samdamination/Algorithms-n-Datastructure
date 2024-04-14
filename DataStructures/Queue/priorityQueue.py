####### PRIOTITY QUEUE - Datastructure #######
# ------------------------------------------ #

# INTRO: heap of tuples (x, p) where x is the element and p is the
#        priority which determines the structure of the heap (max-heap)

# DATASTRUCTURE:
Q = []

def insert(x, p):
    global Q
    Q.append((x, p))
    i = len(Q) - 1           # last element position
    while i > 0 and Q[parent(i)][1] < Q[i][1]             # not equal bc then it's the root. check parents means (i-1)//2. Q[..][0] is x, Q[..][1] is p
        #swap Q[parent(i)] <=> Q[i]
        Q[parent(i)], Q[i] = Q[i], Q[parent(i)]
        i = parent(i)

def parent(i):
    ...




def dequeue():
    ...

