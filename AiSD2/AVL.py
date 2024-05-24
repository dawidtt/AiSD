import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def heightBST(node):
    if node is None:
        return 0
    return max(heightBST(node.left), heightBST(node.right)) + 1

def inorderTraversal(node, result):
    if node is None:
        return
    inorderTraversal(node.left, result)
    result.append(node.key)
    inorderTraversal(node.right, result)

def buildAVL(sortedList):
    if not sortedList:
        return None
    mid = len(sortedList) // 2
    node = Node(sortedList[mid])
    node.left = buildAVL(sortedList[:mid])
    node.right = buildAVL(sortedList[mid + 1:])
    return node

def heightAVL(node):
    if node is None:
        return 0
    return max(heightAVL(node.left), heightAVL(node.right)) + 1


heightsBST = []
heightsAVL = []


measurePoints = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000, 25000, 30000, 35000, 40000, 50000]


for point in measurePoints:
    arr = [random.randint(0, point) for i in range(point)]
    rootBST = None
    for value in arr:
        rootBST = insert(rootBST, value)

    heightBSTValue = heightBST(rootBST)
    heightsBST.append(heightBSTValue)
    sortedList = []
    inorderTraversal(rootBST, sortedList)
    rootAVL = buildAVL(sortedList)
    heightAVLValue = heightAVL(rootAVL)
    heightsAVL.append(heightAVLValue)

print("Wysokości drzew BST: ", heightsBST)
print("Wysokości drzew AVL: ", heightsAVL)

