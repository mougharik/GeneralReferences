#!/usr/bin/env python3

class Stack():
    ''' Stack Class '''
    def __init__(self, data=None):
        self.stackArray = list(data)
    
    def push(self, x):
        self.stackArray.append(x) 
    
    def pop(self):
        return self.stackArray.pop()
        
    def peek(self):
        return self.stackArray[-1:]
    
    def isEmpty(self):
        return len(self.stackArray) == 0
