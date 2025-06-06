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
        if self.head is None:
            self.head = node
            self.tail = self.head
        else: