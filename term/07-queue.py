class ListQueue:

    def __init__(self):
        self.items = []
        self.size = 0


    def enqueue(self,data):
        self.items.insert(0,data) #insert form right
        self.size += 1


    def dequeue(self):
        data = self.items.pop() #pop from left
        self.size -= 1
        return data


#Stack base queue
class Queue:

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []


    def enqueue(self,data):
        self.inbound_stack.append(data)


    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()


#test it
dq = Queue()
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30)
print(dq.inbound_stack)
print('item1: ', dq.dequeue(), 'item2: ',dq.dequeue())