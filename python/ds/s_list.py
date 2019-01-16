#!/usr/bin/env python3

class Node():
    ''' Node Class '''
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.next = nextNode
    
    def setData(self, x):
        self.data = x

    def getData(self):
        return self.data

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next

class LinkedList():
    ''' Singly LinkedList Class '''
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        ''' Time Complexity: O(1)
            - inserts a new node at the head of the list
                with the given data and increments the size
        '''
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        self.size += 1

    def remove(self, data):
        ''' Time Complexity: O(n)
            - searches the list until 'data' is found to remove
                it from the list
            - if no match is found, a ValueError will be raised
        '''
        nodePtr = self.head
        lastPtr = None
        found = False
        while nodePtr is not None and found is False:
            if nodePtr.getData() == data:
                if lastPtr is None:
                    self.head = nodePtr.getNext()
                else:
                    lastPtr.setNext(nodePtr.getNext())
                found = True
                self.size -= 1
            else:
                lastPtr = nodePtr
                nodePtr = nodePtr.getNext()
        if not found:
            raise ValueError('Data is not in list.')

    def search(self, data):
        ''' Time Complexity: O(n)
            - search list for a data value, when found
                that particular node will be returned
            - if no match is found, a ValueError will be raised
        '''
        nodePtr = self.head
        while nodePtr is not None:
            if nodePtr.getData() == data:
                return nodePtr
            nodePtr = nodePtr.getNext()
        
        raise ValueError('Data is not in list.')

    def traverse(self):
        ''' Time Complexity: O(n)
            - prints the list seperated by '->'
        '''
        nodePtr = self.head
        while nodePtr is not None:
            print(nodePtr.getData(), end='')
            nodePtr = nodePtr.getNext()
            if nodePtr is not None:
                print('->', end='')
        print('')

    def getSize(self):
        ''' Time Complexity: O(1)
            - returns the size
        '''
        return self.size
    
    def isEmpty(self):
        ''' Time Complexity: O(1)
            - checks if list is empty, returns a bool
        '''
        return self.getSize() == 0
