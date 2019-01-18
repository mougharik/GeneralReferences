#!/usr/bin/env python3


class Node():
    ''' Node Class '''
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.right = None
        self.left = None

    def setRight(self, rChild):
        self.right = rChild

    def setLeft(self, lChild):
        self.left = lChild

    def setParent(self, parent):
        self.parent = parent

    def setValue(self, value):
        self.value = value

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getParent(self):
        return self.parent

    def getValue(self):
        return self.value


class BST():
    ''' Binary Search Tree Class '''
    def __init__(self):
        self.root = None

    def insert(self, value=None, parent=None):
        ''' Time Complexity: O(log n)
            - allocate new node and percolate down tree to find
                an appropriate location for it
        '''
        newNode = Node(value, parent)
        if self.isEmpty():
            self.root = newNode
        else:
            nodePtr = self.root
            while nodePtr is not None:
                parentPtr = nodePtr
                if newNode.getValue() < nodePtr.getValue():
                    nodePtr = nodePtr.getLeft()
                else:
                    nodePtr = nodePtr.getRight()
            if newNode.getValue() < parentPtr.getValue():
                parentPtr.setLeft(newNode)
            else:
                parentPtr.setRight(newNode)
            newNode.setParent(parentPtr)

    def remove(self, value):
        ''' Time Complexity: O(log n)
            - removes node with 'value' from tree
        '''
        if self.isEmpty():
            return

        nodePtr = self.search(value)
        if nodePtr is not None:
            if nodePtr.getLeft() is None and nodePtr.getRight() is None:
                self.restructure(nodePtr)
                nodePtr = None
            elif nodePtr.getLeft() is not None and nodePtr.getRight() is not None:
                maxLeft = self.maxNode(nodePtr.getLeft())
                self.remove(maxLeft.getValue())
                nodePtr.setValue(maxLeft.getValue())
            else:
                if nodePtr.getLeft() is not None:
                    self.restructure(nodePtr, nodePtr.getLeft())
                elif nodePtr.getRight() is not None:
                    self.restructure(nodePtr, nodePtr.getRight())

    def search(self, value):
        ''' Time Complexity: O(log n)
            - iterative traversal of tree to search for 'value'
        '''
        nodePtr = None
        if not self.isEmpty():
            nodePtr = self.root
            while nodePtr is not None and nodePtr.getValue() is not value:
                if nodePtr.getValue() < value:
                    nodePtr = nodePtr.getRight()
                else:
                    nodePtr = nodePtr.getLeft()
        return nodePtr

    def minNode(self, node=None):
        ''' Time Complexity: O(log n)
            - iterative method that returns the left most
                node of the tree
        '''
        if not self.isEmpty():
            if node is None:
                nodePtr = self.root
            else:
                nodePtr = node
            while nodePtr.getLeft() is not None:
                nodePtr = nodePtr.getLeft()
        return nodePtr

    def maxNode(self, node=None):
        ''' Time Complexity: O(log n)
            - iterative method that returns the right most
                node of the tree
        '''
        if not self.isEmpty():
            if node is None:
                nodePtr = self.root
            else:
                nodePtr = node
            while nodePtr.getRight() is not None:
                nodePtr = nodePtr.getRight()
        return nodePtr

    def restructure(self, node, newChild=None):
        ''' Time Complexity: O(1)
            - utility function for remove method that reassigns 
                parent-child relationship to maintain tree structure
        '''
        if newChild is not None:
            newChild.setParent(node.getParent())
        if node.getParent() is not None:
            if self.isLeftChild(node):
                node.getParent().setLeft(newChild)
            elif self.isRightChild(node):
                node.getParent().setRight(newChild)

    def isRightChild(self, node):
        ''' Time Complexity: O(1)
            - returns true if node is a right child,
                false otherwise
        '''
        return node is node.getParent().getRight()

    def isLeftChild(self, node):
        ''' Time Complexity: O(1)
            - returns true if node is a left child,
                false otherwise
        '''
        return node is node.getParent().getLeft()

    def preOrder(self, node):
        ''' Time Complexity: O(n)
            - print in preorder: parent, left, right
        '''
        if node is None:
            return

        print(node.getValue(), end=' ')
        self.preOrder(node.getLeft())
        self.preOrder(node.getRight())

    def inOrder(self, node):
        ''' Time Complexity: O(n)
            - print in inorder: left, parent, right
        '''
        if node is None:
            return

        self.inOrder(node.getLeft())
        print(node.getValue(), end=' ')
        self.inOrder(node.getRight())

    def postOrder(self, node):
        ''' Time Complexity: O(n)
            - print in postorder: left, right, parent
        '''
        if node is None:
            return

        self.postOrder(node.getLeft())
        self.postOrder(node.getRight())
        print(node.getValue(), end=' ')

    def countNodes(self, node):
        ''' Time Complexity: O(n)
            - recursively counts all nodes in tree
        '''
        if node is None:
            return 0
        return self.countNodes(node.getLeft()) + self.countNodes(node.getRight()) + 1

    def countLeaves(self, node):
        ''' Time Complexity: O(n)
            - recursively counts all leaves in tree
        '''
        if node is None:
            return 0
        if node.getLeft() is None and node.getRight() is None:
            return 1

        return self.countLeaves(node.getLeft()) + self.countLeaves(node.getRight())

    def isEmpty(self):
        ''' Time Complexity: O(1)
            - returns true if tree is empty,
                false otherwise
        '''
        return self.getRoot() is None
    
    def getRoot(self):
        ''' Time Complexity: O(1)
            - returns root node
        '''
        return self.root