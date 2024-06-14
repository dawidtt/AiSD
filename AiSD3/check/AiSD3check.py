def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        graph = []
        for line in file:
            graph.append(list(map(int, line.split())))
    return graph

def findEulerianCycle(graph, n):
    eulerianCycle = []
    tempGraph = [row[:] for row in graph]
    stack = []
    stack.append(0)
    while stack:
        v = stack[-1]
        foundEdge = False
        for w in range(n):
            if tempGraph[v][w] == 1:
                stack.append(w)
                tempGraph[v][w] = tempGraph[w][v] = 0
                foundEdge = True
                break
        if not foundEdge:
            eulerianCycle.append(stack.pop())
    return eulerianCycle

def findHamiltonianCycle(graph, n):
    stack = []
    stack.append((0, [0], [False] * n))
    while stack:
        currentVertex, path, visited = stack.pop()
        if len(path) == n:
            if graph[currentVertex][0]:
                return path + [0]
        for neighbor in range(n):
            if graph[currentVertex][neighbor] and not visited[neighbor]:
                newPath = path + [neighbor]
                newVisited = visited.copy()
                newVisited[neighbor] = True
                stack.append((neighbor, newPath, newVisited))
    return None

def main():

    filename = 'dane.txt'
    graph = read_graph_from_file(filename)
    n = len(graph)


    eulerianCycle = findEulerianCycle(graph, n)
    print("Cykl Eulera:", ' '.join(map(lambda x: str(x + 1), eulerianCycle)))


    hamiltonianCycle = findHamiltonianCycle(graph, n)
    if hamiltonianCycle:
        print("Cykl Hamiltona:", ' '.join(map(lambda x: str(x + 1), hamiltonianCycle)))
    else:
        print("Brak cyklu Hamiltona")

if __name__ == "__main__":
    main()
