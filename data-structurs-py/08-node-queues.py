class Node(object):

    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,data):
        node = Node(data,None,None)
        if self.head is None: #if list is empty
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.size += 1


    def dequeue(self):
        current = self.tail
        if self.size == 1: # if we just have one node
            self.size -=1
            self.head = None
            self.tail = None
        elif self.size > 1: #if its more than one node
             self.tail = self.tail.next
             self.tail.prev = None
             self.size -= 1
