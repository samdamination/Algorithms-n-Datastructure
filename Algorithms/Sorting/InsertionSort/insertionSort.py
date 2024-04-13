########################################
###    INSERTION SORT - Algorithm    ###
########################################

## INTRO ##
# Complexity: O(n^2)
#      worst: reverse order, O(n^2)
#      best: already sorted, linear O(n)
#      average: O(n^2)


# NOT IN PLACE !!!
def insertionSort(A):
    # per tutta la parte di array non sortato (il primo elem. lo e)
    for i in range(1, len(A)):
        # j tiene traccia dell'ultimo elemento dell'array sortato (all'inizio è i-1)
        j = i - 1
        # salviamo come temp il primo elem. dell'array non sortato, che sarà da inserire
        x = A[i]
        # quando l'elem. dell'array sortato (j) è maggiore di x crea spazio e diminuisci j
        # j deve essere > -1 se indice array complessivo parte da 0 ot. out of bound
        while j > -1 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        # fuori dal while = j indica elem. minore di x
        # copia x in j + 1
        A[j + 1] = x
    return A



# versione bibbia
""" def insertionSort(A):
	i = 1
	while i < len(A):
		k = i
		while k > 0 and A[k] < A[k - 1]:
			A[k], A[k - 1] = A[k - 1], A[k] # swap
			print(A)
			k -= 1
		i += 1
	return A """



### TESTS ###
A = [5, 6, 12, 8, 4, 10, 3, 12, 11, 1]

print(insertionSort(A))
    
