class Node:
    """Class whose objects will be used as nodes of the binary tree
"""
    nodeId = 0
    left = None
    right = None
    def __init__(self, nodeId):
        """ Constructor method"""
        self.nodeId = nodeId
        
    def __str__(self):
        """Representative string of the Node"""
        return "Node ID: %s"%(str(self.nodeId))

    def setId(self,newId):
        self.nodeId = newId

    def getId(self):
        return self.nodeId
