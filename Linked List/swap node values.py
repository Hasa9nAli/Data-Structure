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
        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    # swap node values
    def swapNodeValues(self, node1, node2):

        temp = self.head
        N = 0
        while temp != None:
            N += 1
            temp = temp.next

        if (node1 < 1 or node1 > N or node2 < 1 or node2 > N):
            return

        pos1 = self.head
        pos2 = self.head
        for i in range(1, node1):
            pos1 = pos1.next
        for i in range(1, node2):
            pos2 = pos2.next

        val = pos1.data
        pos1.data = pos2.data
        pos2.data = val

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

# swap values of node=1 and node=4
MyList.swapNodeValues(1, 4)

# Display the content of the list.
MyList.PrintList()
