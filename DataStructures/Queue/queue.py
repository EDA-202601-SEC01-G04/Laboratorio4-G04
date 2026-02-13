def new_queue():
    queue = {"size": 0,
             "elements": []}
    return queue

def enqueue(my_queue, element):
    my_queue["size"]+=1
    my_queue["elements"].append(element)
    return my_queue