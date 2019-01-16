#!/usr/bin/env python3

from collections import deque

class Queue():
    ''' Queue Class '''
    def __init__(self, data=None):
        self.queue = deque(data)

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        return self.queue.popleft()
    
    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0