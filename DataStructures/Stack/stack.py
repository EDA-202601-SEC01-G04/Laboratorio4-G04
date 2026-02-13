from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as st

def new_stack():
    my_stack =  st.new_list()
    return my_stack 

def push(my_stack, element):
    my_stack = st.add_first(my_stack, element)
    return my_stack 

def pop(my_stack):
    element = st.remove_first(my_stack)
    return element 

def is_empty(my_stack):
    empty = st.is_empty(my_stack)
    return empty

def top(my_stack):
    top = st.get_element(my_stack, 0)
    return top

def size(my_stack):
    size = size(my_stack)
    return size