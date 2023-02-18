# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if (self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

    # Delete last node by key
    def pop_last(self, key):
        if (self.head != None):
            temp = None
            previousToLast = None
            lastNode = None
            if (self.head.data == key):
                lastNode = self.head

            temp = self.head
            while (temp.next != None):
                if (temp.next.data == key):
                    previousToLast = temp
                    lastNode = temp.next
                temp = temp.next

            if (lastNode != None):
                if (lastNode == self.head):
                    self.head = self.head.next
                    lastNode = None
                else:
                    previousToLast.next = lastNode.next
                    lastNode = None

    # display the content of the list
    def PrintList(self):
        temp = self.head
        if (temp != None):
            print("The list contains:", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


# test the code
MyList = LinkedList()

# Add five elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(20)
MyList.push_back(40)
MyList.PrintList()

# Delete last occurrence of 20
MyList.pop_last(20)
MyList.PrintList()
