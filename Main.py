from BinaryTree import BinaryTree
from Node import Node

tree = BinaryTree()

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

print("In order:")
tree.printInOrder()

print("\nPre order:")
tree.printPreOrder()

print("\nPost order:")
tree.printPostOrder()

print("\nMin. value:")
print(tree.getMin())

print("\nMax. value:")
print(tree.getMax())

node = Node(8)
print("\nTo delete: "+str(node.nodeId))
tree.delete(node)

print("In order:")
tree.printInOrder()
