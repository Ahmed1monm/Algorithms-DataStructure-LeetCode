import queue
graph = {
    "a":["b","c"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "f":[],
    "e":[]
}

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