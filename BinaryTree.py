from Node import Node
class BinaryTree:
    """Binary tree class"""
    root = None
    nodeCounter = 0
    
    def isEmpty(self):
        """Tells wether the tree is empty or not"""
        if self.nodeCounter == 0:
            return True
        else:
            return False

    def insert(self, newNode):
        """Insertion method
"""
        return self.insertAux(newNode, self.root)
        
    def insertAux(self, newNode, currentNode):
        """Recursive insertion method
"""
        if self.isEmpty():
            self.root = newNode
            self.nodeCounter+=1
        
        elif newNode.nodeId<currentNode.nodeId:
            if currentNode.left == None:
                currentNode.left = newNode
                return
            else:
                return self.insertAux(newNode, currentNode.left)
        elif newNode.nodeId>currentNode.nodeId:
            if currentNode.right == None:
                currentNode.right = newNode
            else:
                return self.insertAux(newNode, currentNode.right)
            
    def delete(self, node):
        """Deletion method
"""
        self.getNodeToDel(self.root, self.root, node)
    

    def getNodeToDel(self, currentNode, fatherNode, node):
        """Finds the node that's going to be deleted
"""
        if (currentNode == None):
            return None
        elif (currentNode.nodeId == node.nodeId):
            self.deleteAux(currentNode, fatherNode) #deletion method call
            return 
        self.getNodeToDel(currentNode.left, currentNode, node)
        self.getNodeToDel (currentNode.right, currentNode, node)
        
    def deleteAux(self, node, father):
        """ Recursive method that deletes the indicated node
"""
        if (node.left == None and node.right == None): #no children
            if (father.left == node):
                father.left = None
            else:
                father.right = None
            
        elif (node.left == None or node.right == None):#one child
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if (father.left == node):
                father.left = child
            else:
                father.right = child

        elif (node.left != None and node.right != None): #two children
            replacement = self.getMaxLeft(node.left)
            newId = replacement.getId()
            self.delete(replacement)
            node.setId(newId)
            

    def getMaxLeft(self, node):
        """Returns the maximun node to the left of the node that's going to be deleted
"""
        if node.right == None:
            return node
        else:
            return self.getMaxLeft(node.right)

    def getMin(self):
        """Returns the minimun node of the binary tree"""
        return self.getMinAux(self.root)

    def getMinAux(self, node):
        """Get minimun node recursive method """
        if (node.left == None):
            return node
        else:
            return self.getMinAux(node.left)

    def getMax(self):
        """Returns the maximun node of the binary tree"""
        return self.getMaxAux(self.root)

    def getMaxAux(self, node):
        """Get maximun node recursive method """
        if (node.right == None):
            return node
        else:
            return self.getMaxAux(node.right)


    def printInOrder(self):
        self.printInOrderAux(self.root)

    def printInOrderAux(self,node):
        if (node == None):
            return None
        self.printInOrderAux(node.left)
        print(node.nodeId)
        self.printInOrderAux(node.right)

    def printPreOrder(self):
        self.printPreOrderAux(self.root)

    def printPreOrderAux(self,node):
        if (node == None):
            return None
        print(node.nodeId)
        self.printPreOrderAux(node.left)
        self.printPreOrderAux(node.right)

    def printPostOrder(self):
        self.printPostOrderAux(self.root)

    def printPostOrderAux(self, node):
        if (node == None):
            return None
        self.printPostOrderAux(node.left)
        self.printPostOrderAux(node.right)
        print(node.nodeId)



        
    
