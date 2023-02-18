class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def Display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert_start(self, data):
        nowNode = Node(data)
        if self.head is None:
            self.head = nowNode
        temp = self.head
        nowNode.next = temp
        self.head = nowNode

    def insert_end(self, data):
        nowNode = Node(data)
        if self.head is None:
            self.head = nowNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = nowNode
            nowNode.prev = temp

    def inster_Between(self, data, afterdata):
        newNode = Node(data)
        temp = self.head
        if self.head is None:
            self.head = newNode
        else:
            while temp:
                if temp.data == afterdata:
                    newNode.next = temp.next
                    newNode.prev = temp
                    temp.next = newNode
                    temp.next.prev = newNode
                temp = temp.next

    def delet_first(self):
        if self.head is None:
            print('the List is Empty')
        else:
            if self.head.next is None:

                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def delet_end(self):
        if self.head is None:
            print('the List is Empty')
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None

    def delet_node(self, data):
        if self.head is None:
            print('list is empty')
        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    if temp.prev is None:
                        if self.head.next is None:
                            self.head = None
                        else:
                            self.head = self.head.next.next
                            self.head.prev = None
                    else:
                        if temp.next is None:
                            temp.prev.next = None
                        else:
                            temp.prev.next = temp.next.next
                            temp.next.prev = temp.prev.prev

                temp = temp.next


L = Doubly_Linked_List()
L.insert_end('A')
L.insert_end('B')
L.insert_end('C')
L.insert_end('D')

L.Display()
print('')


L.delet_node('A')

L.Display()
