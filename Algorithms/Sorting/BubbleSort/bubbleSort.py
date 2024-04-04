########################################
###    BINARY SEARCH - Algorithm     ###
########################################

## INTRO ##
# Complexity: O(n^2)

# Compara a coppie e trasporta il numero maggiore in fondo
# (se la coppia è fuori posizione li swappa). A ogni nuova iteration
# la parte finale dell'array è sempre sorted

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
