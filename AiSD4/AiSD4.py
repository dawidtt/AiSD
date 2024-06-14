import time
import random


def knapsackDynamic(b, weights, values):
    n = len(weights)
    dp = [[0] * (b + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(b + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = b
    selectedItems = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selectedItems.append(i - 1)
            w -= weights[i - 1]

    selectedItems.reverse()
    return dp[n][b], selectedItems


def greedyKnapsack(b, weights, values):
    n = len(weights)
    ratio = [(values[i] / weights[i], weights[i], values[i], i) for i in range(n)]
    ratio.sort(reverse=True, key=lambda x: x[0])

    totalValue = 0
    totalWeight = 0
    selectedItems = []

    for r in ratio:
        if totalWeight + r[1] <= b:
            totalWeight += r[1]
            totalValue += r[2]
            selectedItems.append(r[3])

    return totalValue, selectedItems


# Test data
timeMeasurementsDynamic = []
timeMeasurementsGreedy = []
relativeErrors = []
measurePoints = [25, 50, 100, 250, 500, 750, 1000, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 15000]
b = 500
weights = []
values = []
for i in range(len(measurePoints)):
    for j in range(measurePoints[i]):
        weights.append(random.randint(1, 200))
        values.append(random.randint(1, 250))

    # Dynamic Programming
    startTime = time.time()
    maxValueDynamic, selectedItemsDynamic = knapsackDynamic(b, weights, values)
    endTime = time.time()
    timeDynamic = endTime - startTime
    timeMeasurementsDynamic.append(timeDynamic)

    # Greedy Algorithm
    startTime = time.time()
    maxValueGreedy, selectedItemsGreedy = greedyKnapsack(b, weights, values)
    endTime = time.time()
    timeGreedy = endTime - startTime
    timeMeasurementsGreedy.append(timeGreedy)

    # Relative Error Calculation
    relativeError = (maxValueDynamic - maxValueGreedy) / maxValueDynamic
    relativeErrors.append(relativeError)

print("Czas dla dynamicznego: ", timeMeasurementsDynamic)
print("Czas dla zachłannego: ", timeMeasurementsGreedy)
print("Względny błąd: ", relativeErrors)
