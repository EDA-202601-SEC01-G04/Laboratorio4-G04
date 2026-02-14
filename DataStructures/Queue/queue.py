def new_queue():
    queue = {"first":None, "last":None, "size":0}
    return queue

def enqueue(my_queue, element):
    this_node = {"info": element, "next":None}
    
    if my_queue["size"] == 0:
        my_queue["first"] = this_node
        my_queue["last"] = this_node
    else:
        my_queue["last"]["next"] = this_node
        my_queue["last"] = this_node
        
    my_queue["size"]+=1
    return my_queue

def dequeue(my_queue):
    if my_queue["size"] == 0:
        raise IndexError("dequeue from empty queue")
    else:
        removed_element = my_queue["first"]["info"]
        my_queue["first"] = my_queue["first"]["next"]
        my_queue["size"] -= 1
        if my_queue["size"] == 0:
            my_queue["last"]=None
            
    return removed_element

def peek(my_queue):
    if my_queue["size"] == 0:
        raise IndexError("dequeue from empty queue")
    else:
        resp = my_queue["first"]["info"]
        return resp

def is_empty(my_queue):
    resp = my_queue["size"] == 0
    return resp

def size(my_queue):
    resp = my_queue["size"]
    return resp