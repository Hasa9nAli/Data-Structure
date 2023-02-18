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

    # Delete all nodes by key
    def pop_all(self, key):
        while (self.head != None and self.head.data == key):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None

        temp = self.head
        if (temp != None):
            while (temp.next != None):
                if (temp.next.data == key):
                    nodeToDelete = temp.next
                    temp.next = temp.next.next
                    nodeToDelete = None
                else:
                    temp = temp.next

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
MyList.push_back(10)
MyList.push_back(20)
MyList.PrintList()

# Delete all occurrences of 20
MyList.pop_all(20)
MyList.PrintList()
