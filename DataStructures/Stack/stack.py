####### STACK - Datastructure #######
# --------------------------------- #

# INTRO: straightforward, see theory

# DATASTRUCTURE
# creating the stack S to store info and variable N for meta-data (size)
S = [None]*100
N = 0

# push
def push(x):
    global S, N
    if N < len(S):
        S[N] = x
        N = N + 1
    else:
        print('stack overflow')

# pop
def pop():
    global S, N
    if N > 0:
        N = N - 1
        return S[N]
    else:
        print('stack underflow')

# isEmpty
def is_empty():
    global S, N
    return N == 0




# TESTS --
push(5)
push(10)
push(-1)
print(S)
print(pop())
print(pop())