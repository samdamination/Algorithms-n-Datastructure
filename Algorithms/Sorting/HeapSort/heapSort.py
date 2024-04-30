############################
### HEAPSORT - Algorithm ###
############################
import math


# INTRO: As in the book


# ALGORITHM

def parent(i):
    return math.floor((i-1) / 2)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

# fix array when extracted max
def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] # swap
        max_heapify(A, largest, heap_size)

# The elements in the subarray A[floor(n/2) + 1 ... n] are all leaves
# Because a tree that is full has as many leaves as nodes remaining
# Therefore the leaves themselves are valid 1-element heaps (their sub-tree, which is not existing,
# it stays in the heap conditions). Therefore we need to "heapify" all nodes BOTTOM-UP from
# A[floor(n/2)] to A[0]
def build_max_heap(A):
    i = int((math.floor(len(A)-1)) / 2)
    while i >= 0:
        max_heapify(A, i, len(A))
        i -= 1

# Given an array then make it be a max-heap.
# We know that A[0] will now hold the biggest number in the heap.
# For that reason we swap A[0] with the last element in the array.
# Now the biggest number will be at the end of the array, but the max_heap is not guarantee
# to follow the conditions from position 0. For that reason we decrease the heap size of 1
# ( because we dont consider the last element anymore, it is at its final position) and heapify the
# remaining elements.
def heap_sort(A):
    build_max_heap(A)
    i = len(A)-1
    heap_size = len(A)

    while i >= 1:
        A[0], A[i] = A[i], A[0]  #swap
        heap_size -= 1
        max_heapify(A, 0, heap_size)
        i -= 1



# TESTS
A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]
B = [-1, 3, 90, 43, 2, 1, 0, -22, 0, -1, -7]
heap_sort(A)
heap_sort(B)
print(A)
print(B)