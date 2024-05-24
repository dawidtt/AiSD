import time
import random

# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a node
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def deletePostOrder(root):
    def postorderTraversalAndDelete(node):
        if node is not None:
            postorderTraversalAndDelete(node.left)
            postorderTraversalAndDelete(node.right)
            deleteNode(node)
            node = None

    def deleteNode(node):
        if node.left is None and node.right is None:
            node = None
        elif node.left is None:
            node.key = node.right.key
            node.left = node.right.left
            node.right = node.right.right
        elif node.right is None:
            node.key = node.left.key
            node.left = node.left.left
            node.right = node.left.right if node.left is not None else None
        else:
            maxNode = findMax(node.left)
            node.key = maxNode.key
            node.left = deleteNode(node.left)
        return node

    def findMax(node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    postorderTraversalAndDelete(root)
    return root

measurePoints = [50, 100, 250, 500, 750, 1000, 2000, 3000, 4000, 5000, 7000, 10000, 15000, 30000, 50000]
arr = []
timeMeasurementsAdding = []
timeMeasurementsDeleting = []

for i in range(len(measurePoints)):
    for j in range(measurePoints[i]):
        arr.append(random.randint(0, measurePoints[i]))
    start = time.time()
    root = None
    for item in arr:
        root = insert(root, item)
    end = time.time()
    timeMeasurementsAdding.append(end - start)
    start = time.time()
    deletePostOrder(root)
    end = time.time()
    timeMeasurementsDeleting.append(end - start)
    arr = []

print(timeMeasurementsAdding)
print(timeMeasurementsDeleting)
