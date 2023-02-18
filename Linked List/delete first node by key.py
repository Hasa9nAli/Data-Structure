# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Delete first node by key
  def pop_first(self, key):     
    
    temp = self.head
    if(temp != None):      
      if(temp.data == key):
        nodeToDelete = self.head
        self.head = self.head.next
        nodeToDelete = None     
      else:
        while(temp.next != None):
          if(temp.next.data == key):
            nodeToDelete = temp.next
            temp.next = temp.next.next
            nodeToDelete = None
            break
          temp = temp.next

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                
MyList = LinkedList()

#Add five elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(10)
MyList.push_back(20)
MyList.PrintList()

#Delete first occurrence of 20
MyList.pop_first(20)
MyList.PrintList()
