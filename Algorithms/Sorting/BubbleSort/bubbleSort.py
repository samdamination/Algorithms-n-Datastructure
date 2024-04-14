########################################
###    BUBBLE SORT - Algorithm     ###
########################################

## INTRO ##
# Complexity: O(n^2)
#      worst: O(n^2)
#      best: flag, O(n)
#      average: O(n^2)

# Compara a coppie e trasporta i numeri minori in cima
# (se la coppia è fuori posizione li swappa). A ogni nuova iteration
# la parte finale dell'array è sempre sorted
# in questo caso si parte dal fondo
# Basically a variant of insertion sort



def bubbleSort(A):
    # n is the number of elements of A
    # for n-1 passes
    for i in range(len(A) - 1):
        # compare each pair so n-1-i (number of comparisons minus one every pass)
        for j in range(len(A) - 1 - i):
            # if left > right swap
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            #print(A) # to see intermediate results
    return A

# version that sorts from end also possible
# versione bibbia
""" def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                print(A)
    return A """



## TESTS ##
A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

print(bubbleSort(A))
