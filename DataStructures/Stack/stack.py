from DataStructures.List import array_list as sll

def new_stack(): 
    stack =sll.new_list()
    return stack

def push(my_stack, element):
    my_stack = sll.add_first(my_stack, element)
    return my_stack 

def pop(my_stack):
    element = sll.remove_first(my_stack)
    return element 

def is_empty(my_stack):
    empty = sll.is_empty(my_stack)
    return empty

def top(my_stack):
    top = sll.get_element(my_stack, 0)
    return top

def size(my_stack):
    size = sll.size(my_stack)
    return size