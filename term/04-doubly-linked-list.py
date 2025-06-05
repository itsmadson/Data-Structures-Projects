class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = None
        self.prev = None #prev for Doubly

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0


    def append(self,data):
        node = Node(data)
        if self.tail is None: #if its first element
            self.tail = node
            self.head = self.tail
        else:
            self.head.next = node #its append in the end
            node.prev = self.head
            self.head = node
        self.size += 1


    def iter(self): #for better traversal using iteration
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val


    def delete(self,data):
        current = self.tail
        del_status =False
        if current and current.data == data : #if its first item
            self.tail = self.tail.next
            self.tail.prev = None
            del_status = True
        elif self.head.data == data : #if its last item
            self.head.prev.next = None
            self.head = self.head.prev
            del_status = True
        else: #if its in the middle
            while current:
                if current.data == data :
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    del_status = True
                current = current.next
        if del_status: #if node deleted
            self.size -= 1


