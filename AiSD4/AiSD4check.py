import time
import random


def readDataFromFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        n = int(lines[0].strip())
        weights = list(map(int, lines[1].strip().split()))
        values = list(map(int, lines[2].strip().split()))
        b = int(lines[3].strip())

    return n, weights, values, b


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
    selectedWeights = [weights[i] for i in selectedItems]
    selectedValues = [values[i] for i in selectedItems]

    return dp[n][b], selectedItems, selectedWeights, selectedValues


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

    selectedWeights = [weights[i] for i in selectedItems]
    selectedValues = [values[i] for i in selectedItems]

    return totalValue, selectedItems, selectedWeights, selectedValues


filename = 'data.txt'
n, weights, values, b = readDataFromFile(filename)

relativeErrors = []

maxValueDynamic, selectedItemsDynamic, selectedWeightsDynamic, selectedValuesDynamic = knapsackDynamic(b, weights, values)

maxValueGreedy, selectedItemsGreedy, selectedWeightsGreedy, selectedValuesGreedy = greedyKnapsack(b, weights, values)


# Relative Error Calculation
relativeError = (maxValueDynamic - maxValueGreedy) / maxValueDynamic
relativeErrors.append(relativeError)


print("Względny błąd: ", relativeErrors)
print("Algorytm dynamiczny - Wybierane rozmiary: ", selectedWeightsDynamic)
print("Algorytm dynamiczny - Wybierane wartości: ", selectedValuesDynamic)
print("Algorytm zachłanny - Wybierane rozmiary: ", selectedWeightsGreedy)
print("Algorytm zachłanny - Wybierane wartości: ", selectedValuesGreedy)
