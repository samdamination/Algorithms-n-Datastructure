####### QUEUE - Datastructure #######
# --------------------------------- #

# INTRO: straightforward, see theory
#        it's infinite like a snake eating his tail (we only have to keep track of Front,Back)

# DATASTRUCTURE
Q = [None]*100 # fixed-size array to store elements in the queue

Front = 0 # points to the element that is in front of the queue

Back = 0 # point to first empty space at tail of queue

def enqueue(x):
    global Q, Front, Back
    if is_full():               # if the queue is already full - error
        print('queue full')
    else:                       # else put x in Q.tail,
        Q[Back] = x
        Back = next(Back)

def dequeue():
    global Q, Front, Back
    if is_empty():
        print('queue empty')
    else:
        x = Q[Front]
        Front = next(Front)
        return x
    

# for updatinf Front, Back after a dequeue, enqueue
def next(p):
    global Q
    p = p + 1                   # updating of 1
    if p == len(Q):             # if Back is equal to length of the queue, queue is full -> Back = 0
        p = 0
    return p

def is_empty():
    global Front, Back
    return Front == Back

def is_full():
    global Front, Back
    return next(Back) == Front



# TESTS
enqueue(21)
enqueue(12)
enqueue(9)
enqueue(6)
print(Q)
print(Front)
print(Back)
dequeue()
print(Q) # the number remains, changes only Front
print(Front)
print(Back)