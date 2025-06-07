from collections import deque
class Node:

    def __init__(self,data): #every node has root and right/left child (optional)
        self.data = data
        self.right_child = None
        self.left_child = None


    def inorder(self,root_node):
        current = root_node
        if current is None: #if root is None
            return
        self.inorder(current.left_child) #traverse left subtree
        print(current.data)
        self.inorder(current.right_child) #traverse right subtree


    def preorder(self,root_data):
        current = root_data
        if current is None:
            return
        print(current.data) #traverse root
        self.preorder(current.left_child) #traverse left subtree
        self.preorder(current.right_child) #then right substree


    def postorder(self,root_order):
        current = root_order
        if current is None:
            return
        self.postorder(current.left_child) #traverse left subtree
        self.postorder(current.right_child) #then right subtree
        print(current.data) #then root


    def bfs(self,root_node):
        root = root_node
        list_of_nodes = []
        traversal_queue = deque([root])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
        return list_of_nodes

#test it
n1=Node('root node')
n2=Node('left child node')
n3=Node('right child node')
n4=Node('left grandchild node')
#describe relationst
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4
#print only left childs
current = n1
while current:
    print(current.data)
    current = current.left_child
#print orders.
print('inorder: ',n1.inorder(n1))
print('postorder: ',n1.postorder(n1))
print('preorder: ',n1.preorder(n1))
#test bfs
print('bfs :',n1.bfs(n1))

