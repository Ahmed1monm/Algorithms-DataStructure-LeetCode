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






