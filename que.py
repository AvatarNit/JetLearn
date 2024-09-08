class Queue:
    # Constructer
    def __init__(self,size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size
    
    # adding to queue
    def enqueue(self, item):
        if self.available == 0:
            print("Queue Overflow!")
            return
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -= 1
    
    # remove from queue
    def dequeue(self):
        if self.available == self.size:
            print("Queue underflow!")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1
    
    def getRear(self):
        print(f"Rear Item: {self.queue[self.rear-1]}")
    
    def getFront(self):
        print(f"Front Item: {self.queue[self.front]}")

    def print_queue(self):
        print("Current queue: " , self.queue)


queue1 = Queue(4)

queue1.dequeue()

queue1.enqueue(10)
queue1.enqueue(12)
queue1.enqueue(9)
queue1.enqueue(4)
queue1.enqueue(7)

queue1.getFront()
queue1.getRear()

queue1.dequeue()
queue1.getFront()

queue1.print_queue()