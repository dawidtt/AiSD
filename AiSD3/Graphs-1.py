import random
import time

def createHamiltonianCycle(n):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        graph[i][(i + 1) % n] = 1
        graph[(i + 1) % n][i] = 1
    return graph

def addEdges(graph, n, targetDensity):
    currentEdges = sum(sum(row) for row in graph) // 2
    maxEdges = n * (n - 1) // 2
    targetEdges = int(targetDensity * maxEdges)
    while currentEdges < targetEdges:
        u, v = random.sample(range(n), 2)
        if graph[u][v] == 0:
            graph[u][v] = graph[v][u] = 1
            currentEdges += 1

def generateGraph(n, targetDensity):
    graph = createHamiltonianCycle(n)
    addEdges(graph, n, targetDensity)
    for i in range(n):
        degree = sum(graph[i])
        if degree % 2 != 0:
            for j in range(n):
                if graph[i][j] == 0:
                    graph[i][j] = graph[j][i] = 1
                    break
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
    measurePoints = [300, 350, 400, 450, 500, 550, 600]
    timeMeasurementsEuler30 = []
    timeMeasurementsEuler70 = []
    timeMeasurementsHamilton30 = []
    timeMeasurementsHamilton70 = []

    density30 = 0.3
    density70 = 0.7

    for n in measurePoints:
        graph30 = generateGraph(n, density30)
        graph70 = generateGraph(n, density70)

        start = time.time()
        eulerCycle30 = findEulerianCycle(graph30, n)
        end = time.time()
        timeMeasurementsEuler30.append(end - start)

        start = time.time()
        hamiltonCycle30 = findHamiltonianCycle(graph30, n)
        end = time.time()
        timeMeasurementsHamilton30.append(end - start)

        start = time.time()
        eulerCycle70 = findEulerianCycle(graph70, n)
        end = time.time()
        timeMeasurementsEuler70.append(end - start)

        start = time.time()
        hamiltonCycle70 = findHamiltonianCycle(graph70, n)
        end = time.time()
        timeMeasurementsHamilton70.append(end - start)

    print("Czas znajdowania cyklu Eulera dla 30%", timeMeasurementsEuler30)
    print("Czas znajdowania cyklu Eulera dla 70%", timeMeasurementsEuler70)
    print("Czas znajdowania cyklu Hamiltona dla 30%", timeMeasurementsHamilton30)
    print("Czas znajdowania cyklu Hamiltona dla 70%", timeMeasurementsHamilton70)

if __name__ == "__main__":
    main()
