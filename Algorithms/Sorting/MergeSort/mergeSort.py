############################
### MERGESORT -Algorithm ###
############################

# INTRO

# ALGORITHM
# merge
def merge(A, B):
    R = []      # result array
    i = 0       # i for A
    j = 0       # j for B
    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or B[j] > A[i]):     # se i deve finire e (j ha finito o j è piu grande di i)
            R.append(A[i])                                  # aggiungi alla soluzione i
            i = i + 1                                       # incrementa i
        else:
            R.append(B[j])
            j = j + 1
    return R

# mergesort
def mergesort(A):
    N = len(A)                    # divide O(1)
    if N <= 1:                    # divide
        return A                  # divide
    middle = N // 2               # divide
    A1 = mergesort(A[0 : middle]) # conquer
    A2 = mergesort(A[middle : N]) # conquer
    return merge(A1,A2)           # combine \Theta(n)

# TESTS

