class Stack:
    def __init__(self):
        self.stack =[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if(len(self.stack)==0):
            print("Stack is Empty ")
            return 
        return self.stack.pop()
    def peek(self):
        if(len(self.stack)==0):
            print("Stack is Empty")
        else :
            print("The top element ",self.stack[-1])
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def display(self):
        for i in self.stack:
            print(i)

myStack=Stack()

myStack.push(3)
myStack.push(4)
myStack.peek()
myStack.pop()
print("The size of stack is ",myStack.size())
print("The Stack is empty :",myStack.isEmpty())
myStack.display()

