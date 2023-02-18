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

    # delete odd nodes of the list
    def deleteOddNodes(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            if (self.head != None):
                evenNode = self.head
                oddNode = self.head.next
                while (evenNode != None and oddNode != None):
                    evenNode.next = oddNode.next
                    oddNode = None
                    evenNode = evenNode.next
                    if (evenNode != None):
                        oddNode = evenNode.next

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

# Add five elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.push_back(50)

# Display the content of the list.
MyList.PrintList()

# delete odd nodes of the list
MyList.deleteOddNodes()

print("After deleting odd nodes.")
# Display the content of the list.
MyList.PrintList()
