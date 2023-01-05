# m - colouring graph problem
# m = number of colours
# n = number of vertices
# graph[][] = adjacency matrix
# all adjacent vertices should have different colours
# return true if graph can be coloured with m colours else false

def isSafe(graph, colour, c, v):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colour[i] == c:
            return False
    return True

def graphColouring(graph, m, colour, v):
    if v == len(graph):
        return True
    for c in range(1, m+1):
        if isSafe(graph, colour, c, v):
            colour[v] = c
            if graphColouring(graph, m, colour, v+1):
                return True
            colour[v] = 0
    return False

graph = [[0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]]

m = 3
colour = [0] * len(graph)
print(graphColouring(graph, m, colour, 0))