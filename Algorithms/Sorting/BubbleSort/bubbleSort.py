########################################
###    BINARY SEARCH - Algorithm     ###
########################################

## INTRO ##
# Complexity: O(n^2)

# Compara a coppie e trasporta il numero maggiore in fondo
# (se la coppia è fuori posizione li swappa). A ogni nuova iteration
# la parte finale dell'array è sempre sorted
# in questo caso si parte dal fondo



def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
            #print(A) # to see intermediate results
    return A



## TESTS ##
A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

bubbleSort(A)
