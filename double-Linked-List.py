"""this program written by Hasan Ali
to contact with me please send the message to this email --> hasanalihasan05@gmail.com
"""
from hashlib import new


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = None
            self.head.prev = None
        else:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode

    def insertAtEnd(self, data):
        rocket = self.head
        if self.head is None:
            newNode = Node(data)
            self.head = newNode

        else:
            newNode = Node(data)
            while rocket.next is not None:
                rocket = rocket.next
            rocket.next = newNode
            newNode.prev = rocket

    def deleteLinkedList(self, value):
        current = self.head
        if self.head is None:
            print("the linked list is empty")
            return
        elif current.data == value:
            self.head = self.head.next
            if self.head.next.next is not None:
                self.head = self.head.next.next
                

        else:
            while current.next is not None:
                if current.data == value:
                    current.prev.next = current.next.next
                    current.next.next.prev = current.prev

                current = current.next
            if current.data == value:
                current.prev.next = None


    def printDoubleLinkedList(self):
        current = self.head
        if self.head is None:
            print("sorry this linked list is empty")
            return
        else:
            while current is not None:
                print(current.data, end="--->")
                current = current.next


firstLinked = DoubleLinkedList()
firstLinked.insertAtBegin(20)
firstLinked.insertAtBegin(10)
firstLinked.insertAtBegin(30)
firstLinked.insertAtBegin(900)
firstLinked.insertAtEnd(100)
firstLinked.insertAtEnd(200)
firstLinked.insertAtEnd(900)
firstLinked.printDoubleLinkedList()
print("\n")
firstLinked.deleteLinkedList(100)
firstLinked.printDoubleLinkedList()
