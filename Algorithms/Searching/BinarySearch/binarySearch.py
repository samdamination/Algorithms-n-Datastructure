########################################
###    BINARY SEARCH - Algorithm     ###
########################################

## INTRO ##
# Complexity: T(n) = T(n/3) + O(1)
#              T(n) = O(log(n))


# in-class vesion
def binarySearch(A, x):
    # assert A is sorted in non-decreasing order
    l = 0
    r = len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] == x:
            return True
        elif A[m] < x:
            l = m + 1
        else:           # A[m] > x
            r = m
    return False


## TESTS ##
A = [1, 3, 4, 5, 6, 8, 10, 11, 12, 12]

print(binarySearch(A, 88))
print(binarySearch(A, 8))







# pseudocode version (one more elif ???)
def binarySearch(A, key):
    # assert A is sorted in non-decreasing order
    first = 1
    last = len(A)
    while first <= last:
        middle = (first + last) // 2
        if A[middle] == key:
            return True
        elif first == last:
            return False
        elif A[middle] > key:
            last = middle - 1
        else:
            first = middle + 1
    return False



# bible version (RECURSIVE)
def binarySearch(A, x):
    # Assume A is sorted
    if len(A) == 0:
        return False
    m = len(A) // 2
    if x > A[m]:
        return binarySearch(A[m+1:len(A)], x)
    elif x < A[m]:
        return binarySearch(A[0:m], x)
    else:
        return True
    