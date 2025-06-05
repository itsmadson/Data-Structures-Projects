class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class stack:

    def __init__(self):
        self.top = None #last item
        self.size = 0


    def push(self,data):
        node = Node(data)
        if self.top: # if stack is not empty
            node.next = self.top
            self.top = node
        else: #stack is empty
            self.top = node
        self.size += 1


    def pop(self): #return top element with deleting it
        if self.top: #if stack is not empty
            data = self.top.data
            self.size -= 1
            if self.top.next: #if its more than 2 item
                self.top = self.top.next
            else: #if its just one node and its self.top
                self.top = None
            return data
        else: #if stack is empty
            return None

    def peek(self): #just return top element without deleting it
        if self.top:
            return self.top.data
        else:
            return None


#Bracket Matching (like ide or for calculators)