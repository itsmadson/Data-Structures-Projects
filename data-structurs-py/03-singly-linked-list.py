#Node
class Node:

    def __init__ (self,data=None): #simple node with data and next
        self.data = data
        self.next = None


    def __str__ (self,data):
        return str(data)

#Craete obj of that node
n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')
#link next
n1.next = n2
n2.next = n3
#print list
current = n1
while current:
    print(current.data)
    current = current.next

#Singly Linked List
class SinglyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0 #size of list


    def append(self,data):
        node = Node(data)
        if self.tail==None: #if list is empty and its first node
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next #go to find last node to insert new node after that
            current.next = node
        self.size += 1


    def appendhead(self,data):
        node = Node(data)
        if self.head: #if we have head next node in my node and then new node is new head
            self.head.next = node
            self.head = node
        else: # we dont have any node so head and tail are the same node
            self.tail = node
            self.head = node
        self.size += 1


    def iter(self): #for better traversal using iteration
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val


    def delete (self,data):
        current = self.tail
        prev = self.tail
        del_status = False
        while current:
            if current and current.data == data:
                if current == self.tail:
                    self.tail = current.next #garbage collection will delete nodes that no one point to it
                    del_status = True
                elif current.next == None: #for delete head
                    prev.next = None
                    self.head = prev
                    del_status = True
                else: #if its in the middle
                    prev.next = current.next
                    del_status = True
                if del_status:
                    self.size -= 1

            prev = current
            current = current.next


    def search (self,data):
        for node in self.iter(): # use iter func traversal it return each node value
            if data == node:
                return True
        return False

    def clear (self): #for clear entire list we just need to unpoint tail and head, garbage collection fuck entire list
        self.tail = None
        self.head = None

# #test it
words = SinglyLinkedList() #make SLL
words.append('egg')
words.append('ham')
words.append('spam')
#print it
current = words.tail
while current:
    print(current.data)
    current= current.next
#print using iter
for word in words.iter(): print(word)