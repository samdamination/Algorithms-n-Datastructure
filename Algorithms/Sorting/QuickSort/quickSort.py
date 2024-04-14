#############################
### QUICKSORT - Algorithm ###
#############################
import random

# INTRO:

# ALGORITHM
# pick a random pivot ( this case last element )
# partition the array in less/equal than pivot and bigger than pivot
def partition(A, begin, end):
    #print("begin", begin, "end", end)
    q = begin
    pivot = A[end]
    #print("pivot", pivot)
    for i in range(begin, end+1):
        if A[i] <= pivot:
            A[i], A[q] = A[q], A[i] # swap
            q += 1
    return q-1

def quicksort(A, begin, end):
    # Q is the position of the pivot from the partition
    # therefore its left is less/equal than pivot, its right is greater than pivot
    if begin < end:
        q = partition(A, begin, end)
        #print(A)
        quicksort(A, begin, q-1)
        quicksort(A, q+1, end)
    return A





# TESTS
A1 = [3,2,1,4,5,0,8,7]
A2 = [10,9,8,7,6,5,4,3,2,1]
A3 = [10,0,9,2,8,3,3,7,3,4,6,5]
print(quicksort(A1, 0, len(A1)-1))
print(quicksort(A2, 0, len(A2)-1))
print(quicksort(A3, 0, len(A3)-1))