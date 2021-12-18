class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        # head=>John->None
        if self.head is None:
            self.head = newNode
        else:
            # head=>John->Ben->None || John->Mathew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            # Ben->newNode->None
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


ll = LinkedList()
firstNode = Node("Jhon")
ll.insert(firstNode)
ll.printList()
