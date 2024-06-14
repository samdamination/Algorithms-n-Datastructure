# -----------------------------------------
#            DYNAMIC PROGRAMMING
# -----------------------------------------

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
""" Bellman-Ford """

""" Longest increasing subsequence """

""" Edit distance """

""" Weighted activity selection problem """

""" ... """



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

""" Activity selection problem """