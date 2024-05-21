## INTRO:
# not efficient but ok

## DATASTRUCTURE:
class disjoint_set:
    def __init__(self):
        self.parent = self          # at the beginning, when u create 1 elem. disjoint set it
                                    # point to itself (it's its own representative)


def set_find(s):                # function to get the representative of a node
    while s.parent != s:
        s = s.parent
    return s

def set_union(s1, s2):          # checking the 2 repres. of 2 set are different
    s1 = set_find(s1)
    s1.parent = set_find(s2)
    

    

    