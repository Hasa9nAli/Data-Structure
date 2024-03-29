# Represent a node of doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class SearchList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

        # addNode() will add a node to the list

    def addNode(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if self.head is None:
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.previous = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None

            # searchNode() will search a given node in the list

    def searchNode(self, value):
        i = 1
        flag = False
        # Node current will point to head
        current = self.head

        # Checks whether the list is empty
        if self.head is None:
            print("List is empty")
            return

        while current is not None:
            # Compare value to be searched with each node in the list
            if current.data == value:
                flag = True
                break
            current = current.next
            i = i + 1

        if flag:
            print("the index of number  is : " + str(i))
        else:
            print("the number is not found")

    def PrintList(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


dList = SearchList()
dList.addNode(1)
dList.addNode(5)
dList.addNode(4)
dList.addNode(2)
dList.addNode(3)
dList.PrintList()
dList.searchNode(4)
dList.searchNode(9)
