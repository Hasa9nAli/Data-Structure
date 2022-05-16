class Stack_class:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) == self.size:
            print("The Stack is full")
        else:
            self.stack.append(item)

    def pop(self):
        if self.stack == []:
            print("The Stack is empty ")
        else:
            return self.stack.pop()

    def display(self):
        if self.stack == []:
            print("The Stack is empty ")
        else:
            print("element of stack is:")
            for item in reversed(self.stack):
                print(item)


s=Stack_class(2)
s.push(1)
s.push(2)
s.push(3)
s.display()


'''
#56*822^/+
stac1.push(5)
stac1.push(6)
arg2=stac1.pop()#6
arg1=stac1.pop()#5
stac1.push(arg1*arg2)#30


stac1.push(8)
stac1.push(2)
stac1.push(2)

arg2=stac1.pop()#2
arg1=stac1.pop()#2
stac1.push(arg1**arg2)#4
#30 8 4
arg2=stac1.pop()#4
arg1=stac1.pop()#8
stac1.push(arg1/arg2)#2
arg2=stac1.pop()#2
arg1=stac1.pop()#30
stac1.push(arg1+arg2)
'''

'''



stac1=Stack_Class(4)
#56*822^/+
stac1.push(5)
stac1.push(6)
arg2=stac1.pop()#6
arg1=stac1.pop()#5
stac1.push(arg1*arg2)#30


stac1.push(8)
stac1.push(2)
stac1.push(2)

arg2=stac1.pop()#2
arg1=stac1.pop()#2
stac1.push(arg1**arg2)#4
#30 8 4
arg2=stac1.pop()#4
arg1=stac1.pop()#8
stac1.push(arg1/arg2)#2
arg2=stac1.pop()#2
arg1=stac1.pop()#30
stac1.push(arg1+arg2)
print(stac1.stack)

'''




'''
#56*822^/+
stac1.push(5)
stac1.push(6)
arg2=stac1.pop()#6
arg1=stac1.pop()#5
stac1.push(arg1*arg2)#30


stac1.push(8)
stac1.push(2)
stac1.push(2)

arg2=stac1.pop()#2
arg1=stac1.pop()#2
stac1.push(arg1**arg2)#4
#30 8 4
arg2=stac1.pop()#4
arg1=stac1.pop()#8
stac1.push(arg1/arg2)#2
arg2=stac1.pop()#2
arg1=stac1.pop()#30
stac1.push(arg1+arg2)
'''

'''

stac1=Stack_Class(4)
#56*822^/+
stac1.push(5)
stac1.push(6)
arg2=stac1.pop()#6
arg1=stac1.pop()#5
stac1.push(arg1*arg2)#30


stac1.push(8)
stac1.push(2)
stac1.push(2)

arg2=stac1.pop()#2
arg1=stac1.pop()#2
stac1.push(arg1**arg2)#4
#30 8 4
arg2=stac1.pop()#4
arg1=stac1.pop()#8
stac1.push(arg1/arg2)#2
arg2=stac1.pop()#2
arg1=stac1.pop()#30
stac1.push(arg1+arg2)
print(stac1.stack)

'''



