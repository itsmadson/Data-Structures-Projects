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
        self.inbound_stack = [] # input list
        self.outbound_stack = [] # output list (we will reverse it)


    def enqueue(self,data):
        self.inbound_stack.append(data) # add to list form right


    def dequeue(self):
        if not self.outbound_stack: #if we dont create outbound before
            while self.inbound_stack: # all items in inbound list
                self.outbound_stack.append(self.inbound_stack.pop()) # reverse list with pop from inbound and append that in out
        return self.outbound_stack.pop() # now last item in outbound is first item in inbound list


#test it
dq = Queue()
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30)
print(dq.inbound_stack)
print('item1: ', dq.dequeue(), 'item2: ',dq.dequeue())