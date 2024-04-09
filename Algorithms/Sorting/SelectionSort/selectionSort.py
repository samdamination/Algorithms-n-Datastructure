########################################
###    INSERTION SORT - Algorithm    ###
########################################

## INTRO ##
# Complexity: O(n^2)
#      worst: O(n^2)
#      best: O(n^2)
#      average: O(n^2)


def selectionSort(A):
    #
    for i in range(len(A) - 1):
        min = i
        for j in range (i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
        # print(A) # to check intermediate steps
    return A


# versione bibbia identica



### TESTS ###
A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

print(selectionSort(A))