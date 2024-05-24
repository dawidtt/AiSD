import random
import time

def createEulerianGraph(n):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        graph[i][(i + 1) % n] = 1
        graph[(i + 1) % n][i] = 1
    maxEdges = n * (n - 1) // 2
    targetEdges = int(maxEdges * 0.5)
    currentEdges = sum(sum(row) for row in graph) // 2
    while currentEdges < targetEdges:
        u, v = random.sample(range(n), 2)
        if graph[u][v] == 0:
            graph[u][v] = graph[v][u] = 1
            currentEdges += 1
    for i in range(n):
        degree = sum(graph[i])
        if degree % 2 != 0:
            for j in range(n):
                if i != j and graph[i][j] == 0:
                    graph[i][j] = graph[j][i] = 1
                    break
    return graph

def findAllHamiltonianCycles(graph, n):
    cycles = []
    visited = [False] * n

    def backtrack(vertex, path):
        if len(path) == n:
            if graph[vertex][path[0]]:
                cycle = path + [path[0]]
                normalizedCycle = normalizeCycle(cycle)
                if normalizedCycle not in cycles:
                    cycles.append(normalizedCycle)
            return
        for neighbor in range(n):
            if graph[vertex][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                backtrack(neighbor, path + [neighbor])
                visited[neighbor] = False

    visited[0] = True
    backtrack(0, [0])
    return cycles

def normalizeCycle(cycle):
    n = len(cycle) - 1
    minCycle = cycle
    for i in range(n):
        rotatedCycle = cycle[i:] + cycle[:i]
        if rotatedCycle < minCycle:
            minCycle = rotatedCycle
    return tuple(minCycle)

measurePoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
timeMeasurementsHamilton50 = []
for n in measurePoints:
    graph = createEulerianGraph(n)
    start = time.time()
    cycles = findAllHamiltonianCycles(graph, n)
    end = time.time()
    timeMeasurementsHamilton50.append(end - start)

print(timeMeasurementsHamilton50)
