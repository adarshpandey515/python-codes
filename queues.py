class Queue:
    def __init__(self) -> None:
        self.queue=[]
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        if(len(self.queue)==0):
            print("Queue is Empty")
            return 
        return self.queue.pop(0)
    def getFront(self):
        return self.queue[0]
    def getRear(self):
        return self.queue[-1]
    def display(self):
        for i in self.queue:
            print(i)
    
myQueue=Queue()
myQueue.enqueue("hello")
myQueue.enqueue("me")
myQueue.enqueue("you")
myQueue.display()
myQueue.dequeue()
myQueue.display()
print(myQueue.getFront())
print(myQueue.getRear())
