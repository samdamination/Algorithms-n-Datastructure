####### LINKED-LIST - Datastructure #######
# --------------------------------------- #

# INTRO: 

# SINGLY-LINKED LIST (similar to a stack)
# creating object
class ListElement:
    # constructur (always take self (the object on which is called) like every member function)
    def __init__(self, v):
        # set of variable names associeted with that object (self)
        self.value = v
        self.next = None

# global variables (first punta all'ultimo oggetto inserito)
first = None

# insert v at the beginning of the list
def list_insert(v):
    global first
    new_elem = ListElement(v)           # create new element for the list
    new_elem.next = first
    first.next = new_elem

# iterate list
def list_print():
    global first
    l = first                   # otherwise list get lost after iteration because first points to none
    while l != None:
        print(l.value)
        l = l.next

# remove from list (beginning) and returns it
def list_pop():
    global first
    assert first != None, "empty list"
    result = first.value
    first = first.next
    return result



    
    

# DOUBLY-LINKED LIST
class ListElem:
    def __init__(self, v):
        self.value = v
        self.next = self        # either it's only sentinel or we'll change it in the process
        self.prev = self        # same

sentinel = ListElem(None)       # sentinel object

# insert value v after element l
def list_insert_after(v, pos):
    new_elem = ListElem(v)
    new_elem.prev = pos
    new_elem.next = pos.next
    new_elem.next.prev = new_elem
    new_elem.prev.next = new_elem
# to insert at the end pos becomes sentinel.prev (no actual need to write list_insert_before)

def list_print_forward():          
    global sentinel
    l = sentinel.next                   # //
    while l != None:
        print(l.value)
        l = l.next

def list_print_backward():          
    global sentinel
    l = sentinel.prev                   # //
    while l != None:
        print(l.value)
        l = l.prev





# TESTS