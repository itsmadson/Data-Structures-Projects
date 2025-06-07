class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class circularlist:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self,data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node # add it in the end of list and replace it with new self.head
        else:
            self.tail = node
            self.head = node # empty list
        self.head.next = self.tail # rule of circular list
        self.size += 1


    def iter(self): #for better traversal using iteration
        current = self.tail
        while current:
            val = current.data
            yield val
            current = current.next
            if current == self.tail:
                break


    def delete(self,data):
        current = self.tail
        prev = self.tail
        del_status = False
        while current:
            if current.data == data:
                if current == self.tail: #if its tail (first)
                    self.tail = current.next
                    self.head.next = self.tail # point to new tail
                elif current == self.head: #if its head (last)
                    prev.next = self.tail
                    self.head = prev
                else:
                    prev.next = current.next #if its in the middle
                del_status = True
            prev = current
            current = current.next
            if current == self.tail: # dont stuck in loop
                break
        if del_status:
            self.size -= 1

#test it
words = circularlist()
words.append('idk')
words.append('space')
words.append('discord')
#print it
for word in words.iter():
    print(word)