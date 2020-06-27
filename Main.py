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

node = Node(8)
print("\nTo delete: "+str(node.nodeId))
tree.delete(node) #delete node with ID 8

print("In order:")
tree.printInOrder()
