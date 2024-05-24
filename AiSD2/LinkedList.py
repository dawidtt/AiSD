import time
import random

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertSorted(self, item):

        newNode = Node(item)


        if self.head is None or self.head.item >= item:
            newNode.next = self.head
            self.head = newNode
        else:

            current = self.head
            while current.next is not None and current.next.item < item:
                current = current.next


            newNode.next = current.next
            current.next = newNode

    def printList(self):

        resultArray = []
        current = self.head
        while current is not None:
            resultArray.append(current.item)
            current = current.next
        return resultArray

    def deleteAll(self):

        while self.head is not None:

            self.head = self.head.next

if __name__ == '__main__':
    linkedList = LinkedList()


    measurePoints = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000, 25000, 30000, 35000, 40000, 50000]
    arr = []
    timeMeasurementsAdding = []
    timeMeasurementsSearch = []
    timeMeasurementsDeleting = []

    for i in range(len(measurePoints)):

        arr = [random.randint(0, measurePoints[i]) for i in range(measurePoints[i])]


        startTime = time.time()
        for item in arr:
            linkedList.insertSorted(item)
        endTime = time.time()
        timeMeasurementsAdding.append(endTime - startTime)


        startTime = time.time()
        searchArray = linkedList.printList()
        endTime = time.time()
        timeMeasurementsSearch.append(endTime - startTime)


        startTime = time.time()
        linkedList.deleteAll()
        endTime = time.time()
        timeMeasurementsDeleting.append(endTime - startTime)


        arr = []


    print("Pomiary czasu dodawania:", timeMeasurementsAdding)
    print("Pomiary czasu przeszukiwania:", timeMeasurementsSearch)
    print("Pomiary czasu usuwania:", timeMeasurementsDeleting)
