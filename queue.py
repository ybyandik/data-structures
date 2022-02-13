# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 02:54:18 2022

@author: ybyandik
"""

class Queue:
    def __init__(self):
        # Queue should not be reached out of the class.
        # Therefore, it is defined as a private variable.
        self.__data = []
        
    def enqueue(self, item):
        self.__data.append(item)
    
    """
        In Stack, accessing the elements in the stack is based on LIFO policy.
        
        However, in Queue, accessing the elements is based on 
        first-in first-out (FIFO) policy. It means the earlier element 
        inserted to the Queue, leaves the Queue earlier.
    """
    def dequeue(self):
        # pop the first element of the Queue to ensure FIFO policy
        return self.__data.pop(0)
    
    def isEmpty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False
        
    """
        As I mentioned before, the difference between the Queue data type 
        and the Stack data type depends on which address we access 
        the data first.
        
        In Stacks, we are able to reach the last element which is generally 
        named as "Top" or "Tail". In Queues, we are able to reach only the 
        first element of the Queue, which is commonly named as "Head".
    """
    def checkHead(self):
        return self.__data[0]
    
    """
        In theory, we should not be able to access entire Queue without 
        tracing the entire Queue forward, similar to Stack. However, I am
        adding this since Python allows without much effort.
    """
    def showQueue(self):
        return self.__data
