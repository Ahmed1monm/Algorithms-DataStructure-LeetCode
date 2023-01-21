import queue
graph = {
    "a":["b","c"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "f":[],
    "e":[]
}


def depth_first_search(graph, source, goal):
    stack = [source]
    tree = []

    while len(stack) > 0:
        current = stack.pop()
        tree.append(current)
        if current == goal:
            return tree
        for neighbor in graph[current] :
            stack.append(neighbor)

def bridth_first_search(graph, source, goal):
    q = queue.Queue() 
    q.put(source,block=True,timeout=None)
    tree = []
    
    while not q.empty() :
        current = q.get(block= True, timeout=False)
        tree.append(current)
        if current == goal:
            return tree
        for neighbor in graph[current] :
            q.put(neighbor,block=True,timeout=None)


print( bridth_first_search(graph,"a","e") )


