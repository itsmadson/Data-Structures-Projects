class Node:

    def __init__(self,data): #every node has root and right/left child (optional)
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:

    def __init__(self):
        self.root_node = None


    def find_min(self):
        current = self.root_node
        while current.left_child: #find leftmost leaf
            current = current.left_child
        return current


    def find_max(self):
        current = self.root_node
        while current.right_child: #find rightmost leaf
            current = current.right_child
        return current


    def insert(self,data):
        node = Node(data)
        if self.root_node is None: # if tree is empty
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True: #loop of compare
                parent = current
                if node.data < parent.data: #if node is smaller than parent go left
                    current = current.left_child
                    if current is None: #where we dont have left child we put node
                        parent.left_child = node
                        return
                    else: # if node is greater than parent go right
                        current = current.right_child
                        if current is None: #where we dont have right child
                            parent.right_child = node
                            return


    def get_node_with_parent(self,data): # helper node to return node with its parent
        parent = None
        current = self.root_node
        if current is None: # tree is empty
            return (parent, None)
        while True:
            if current.data == data: #root is data
                return (parent,current)
            elif current.data > data: #go left if its smaller
                parent = current
                current = current.left_child
            else: # go right if its greater
                parent = current
                current = current.right_child
        return (parent,current)


    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        if node is None:
            return False

        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif node.left_child or node.right_child:
            children_count = 1
        else:
            children_count = 0

        # Case 1: Node has no children (leaf)
        if children_count == 0:
            if parent:
                if parent.left_child == node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None

        # Case 2: Node has one child
        elif children_count == 1:
            next_node = node.left_child if node.left_child else node.right_child
            if parent:
                if parent.left_child == node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        # Case 3: Node has two children
        else:
            # Find leftmost child in right subtree
            parent_of_leftmost = node
            leftmost = node.right_child
            while leftmost.left_child:
                parent_of_leftmost = leftmost
                leftmost = leftmost.left_child

            # Replace node data with leftmost's data
            node.data = leftmost.data

            # Delete the leftmost node
            if parent_of_leftmost.left_child == leftmost:
                parent_of_leftmost.left_child = leftmost.right_child
            else:
                parent_of_leftmost.right_child = leftmost.right_child


    def search (self,data):
        current = self.root_node
        while True:
            if current is None: #empty tree
                return current
            elif current.data == data: #data is root
                return data
            elif current.data > data: #data is smaller that root go left
                current = current.left_child
            else: #data is greater than root go right
                current = current.right_child