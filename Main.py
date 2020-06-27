from BinaryTree import BinaryTree
from Node import Node

tree = BinaryTree() #instantiation of the binary tree

#instantiation and insertion of different nodes to the tree
node = Node(6)
tree.insert(node)

node = Node(2)
tree.insert(node)

node = Node(3)
tree.insert(node)

node = Node(1)
tree.insert(node)

node = Node(8)
tree.insert(node)

node = Node(7)
tree.insert(node)

node = Node(10)
tree.insert(node)

#print methods: in-order, pre-order, post-order
print("In order:")
tree.printInOrder()

print("\nPre order:")
tree.printPreOrder()

print("\nPost order:")
tree.printPostOrder()

print("\nMin. value:")
print(tree.getMin()) #get mininum value of the tree

print("\nMax. value:")
print(tree.getMax()) #get the maximun value of the tree

node = Node(10)
print("\nDelete: "+str(node.nodeId))
tree.delete(node) #delete node with ID 10 (one child)

node = Node(9)
print("\nDelete: "+str(node.nodeId))
tree.delete(node) #delete node with ID 9 (no children)

node = Node(8)
print("\nDelete: "+str(node.nodeId))
tree.delete(node) #delete node with ID 8 (two children)

node = Node(6)
print("\nDelete: "+str(node.nodeId))
tree.delete(node) #delete node with ID 6 (root)

print("In order:")
tree.printInOrder()
