# -----------------------------------------
#            DYNAMIC PROGRAMMING
# -----------------------------------------
from sys import maxsize
# INTRO:
# Used for
#   - optimal substructure: (combine optimal solution of subproblems to achive final)
#   - overlapping subproblems: (like fibonacci, avoids useless computation)

# Approaches:
#   - Top-down (memoization): start with final solution and recursively break it down in smaller subproblems,
#                             store results of solved subproblems into memoization table
#   - Bottom-up (tabulation): start with smaller subproblems and graduallly build up the solution, store solved
#                             subproblems in a table

# Steps
# 1 - Identify if it is a Dynamic programming problem -> All dp have overlapping subproblems, some also opt. structure
# 2 - Decide a state expression with the Least parameters.
# 3 - (!!!) Formulate state and transition relationships.
# 4 - Do tabulation (or memorization).




# COMMON ALGORITHMS:
""" ======= Bellman-Ford ======= """
def BellmanFord(graph, V, E, src): # graph = [(u0, v0, c0), (u1, v1, c1)...] edges
    D = [float('inf')] * V         # Initialize distance of all vertices as infinite.
    D[src] = 0                # initialize distance of source as 0
 
    for i in range(V - 1):
        for j in range(E):
            if D[graph[j][0]] + graph[j][2] < D[graph[j][1]]:
                D[graph[j][1]] = D[graph[j][0]] + graph[j][2]
 
    for i in range(E):
        u = graph[i][0]
        v = graph[i][1]
        weight = graph[i][2]
        if D[u] != maxsize and D[u] + weight < D[v]:
            print("Graph contains negative weight cycle")




""" ======= Longest increasing subsequence ======= """
def incSub(A):
    table = [1]*len(A)
    i = 1
    while i < len(A):
        j = 0
        if j == i:
            j = 0
            i += 1
        else:
            while j < i:
                if A[j] < A[i]:
                    table[i] = max(table[i], table[j]+1)
                j += 1
        i += 1

    return max(table)




""" ======= Edit distance ======= """
def minEditDistance(s1, s2):
    rows = len(s1)
    cols = len(s2)

    table = []
    for i in range(rows+1):
        col = []
        for j in range(cols+1):
            if j == 0:
                col.append(i)
            elif i == 0:
                col.append(j)
            else:
                col.append(0)
        table.append(col)

    for i in range(1, rows+1):
        for j in range(1, cols+1):
            charS1 = s1[i-1]

            charS2 = s2[j-1]
            if charS1 != charS2:
                value = min(table[i-1][j], table[i-1][j-1], table[i][j-1]) + 1
            else:
                value = table[i-1][j-1]
            table[i][j] = value
    print("")
    print("strings: ", s1, s2)
    print("edits required: ", table[rows][cols])




""" ======= Weighted activity selection problem ======= """
# -
""" ======= """



# -----------------------------------------
#                   GREEDY
# -----------------------------------------

# INTRO:
# To solve problems where we make a greedy-choice and we're left with a subproblem

# COMMON ALGORITHMS:
""" Kruskal """
""" Prim """
""" Gift selection """

""" Coin change """
def minCoin(coins, amount):
    return minCoin_(coins, amount, {})

def minCoin_(coins, amount, memo):
    if amount in memo:
        return memo[amount]
    if amount <= 0:
        res = 0
    else:
        res = float("inf")
        for c in coins: # try taking each coin
            pos = 1 + minCoin_(coins, amount - c, memo) #take the coin and look for solution with that value less
            if pos < res: # if it's a better solution
                res = pos
    memo[amount] = res
    return res

def minCoinIter(coins, amount):
    memo = [float("inf")]*(amount+1)
    memo[0] = 0 # 0 coins needed to read 0
    for amt in range(1, amount+1): # for each sub-amount
        for c in coins: # for each coin c
            if c <= amt:
                takeThatCoin = memo[amt - c] + 1
                memo[amt] = min(memo[amt], takeThatCoin)

    return memo[amount-1]




""" Activity selection problem """
# -