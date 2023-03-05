"""this program written by Hasan Ali
to contact with me please send the message to this email --> ihasanalihasan@gmail.com
"""
class Node:
    def __init__(self,data): 
        self.data = data 
        self.next = None 
    

class SingleLinkedList:
    def __init__(self):
        self.head = None 

    """function to insert data at start linked list """

    def insertAtBegin(self,data): 
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode
            self.head.next = None 
        
        else: 
            newNode.next = self.head 
            self.head = newNode
    """end the function insert at begin"""

    """function of insert data at end linked list"""

    def insertAtEnd(self,data):
        newNode = Node(data)
        current = self.head 
        if self.head is None: 
            self.head = newNode
            self.head.next = None
            self.current = self.head
            self.current.next = None
        else: 
            while current.next is not None: 
                current = current.next
            current.next = newNode
    
    """end the function insert at end"""

    """function to insert between node """
    def insertBetween(self,data,prevNode):
        newNode = Node(data)
        current = self.head
        if prevNode.next is None:
            print("there is't element ro insert between")
            return
        else: 
            newNode.next =  prevNode.next
            prevNode.next = newNode
        
    """end the function insert between"""

    def deleteNode(self,data): 
        current = self.head 
        if self.head is None:
            print("sorry the linked list is empty you can't delete a Node")
            return 
        if current.data == data:
            self.head = self.head.next

        else : 
            while current.next is not None: 
                prev = current
                current = current.next
                if current.data == data: 
                    prev.next = current.next 
                    current.next = None
                    return
    """end the function delete"""

    """function to find the last node"""

    def findLastNode(self):
        current = self.head
        while current.next is not None: 
            current = current.next
        return current

    """end the function findLastNode"""
    """function of reverse linked list"""
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    """end the function of reverse linked list"""
    """ function to sorting linked list """

    def sortingLinkedList(self):
        current = self.head 
        index = None
        if self.head is None: 
            print("sorry the linked list is empty")
        
        else: 
            while current is not None: 
                index = current.next
                while index is not None:
                    if (index.data < current.data):
                        index.data, current.data = current.data, index.data
                    index = index.next
                current = current.next

    """end the function of sorting linked list"""    
    """function to print all the node in the linked list """

    def printLinkedList(self): 
        current = self.head 
        if self.head is None: 
            print("sorry the linked list is empty")
            return 
        else: 
            while current is not None: 
                print(current.data, end="---> ")
                current = current.next
"""end the printLinkedList """
"""link two linked list with each other """

def linkTwoLinkedList(nameOfFirstLinkedList, nameOfSecondLinkedList):
    lastNode = nameOfFirstLinkedList.findLastNode()
    lastNode.next = nameOfSecondLinkedList.head 



# firstLinked  = SingleLinkedList()
# firstLinked.insertAtBegin(10)
# firstLinked.insertAtBegin(-200)
# firstLinked.insertAtBegin(22)
# firstLinked.insertAtBegin(-100)
# firstLinked.insertAtEnd(997)
# firstLinked.insertBetween(999, firstLinked.head.next.next.next)
# firstLinked.insertAtBegin(998)
# firstLinked.printLinkedList()
# print("\nthe second linked list start\n")
# firstLinked.sortingLinkedList()
# print("linked list after sorting\n")
# firstLinked.printLinkedList()
# print("\n")
# secondLinked = SingleLinkedList()
# secondLinked.insertAtEnd(10)
# secondLinked.insertAtEnd(20)
# secondLinked.insertAtEnd(30)
# secondLinked.insertAtEnd(40)
# secondLinked.insertAtEnd(50)
# secondLinked.printLinkedList()
# print("\n")



# firstLinked.printLinkedList()
# print("\n")
# """link two linked list """
# linkTwoLinkedList(firstLinked,secondLinked)
# firstLinked.printLinkedList()
# print("\n")
# firstLinked.reverse()
# firstLinked.printLinkedList()


# ----------------------------------------------------------------
# print("\n")

l1 = SingleLinkedList()
l1 = SingleLinkedList()
l1.printLinkedList()
l1.insertAtEnd(1)
l1.insertAtEnd(3)
l1.insertAtEnd(7)
l1.insertAtEnd(10)
l1.insertAtEnd(9)
l1.insertAtEnd(2)
l1.insertAtEnd(11)
l1.insertAtEnd(4)
l1.insertAtEnd(8)
l1.insertAtEnd(13)
l2 = SingleLinkedList()

while l1.current is not None:
    if l1.current.data % 2 ==0 :  
        l2.insertAtEnd(l1.current.data)
    l1.current = l1.current.next

l1.printLinkedList()
print("\n")

l2.printLinkedList()
print("\n")
