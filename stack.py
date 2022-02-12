# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 02:07:25 2022

@author: ybyandik
"""

class Stack:
    def __init__(self):
        # Stack should not be reached out of the class.
        # Therefore, it is defined as a private variable.
        self.__data = []
    
    def push(self, item):
        self.__data.append(item)
    
    def pop(self):
        if not(self.empty()):
            return self.__data.pop() #pops the last element
        else:
            raise Warning("The stack is empty.")

    def isEmpty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False
    
    def checkTop(self):
        return self.__data[-1]
        
    """
        In the definition of Stack, only the last element (or top) 
        should be reachable. To access other elements, we need to remove 
        all elements from the list, starting with the last added element and 
        backwards. 
        
        This is called last-in first-out (LIFO) policy.
        
        Therefore, being able to access the entire stack at once is against 
        the definition of the stack structure. However, even though the below 
        implementation is against the definition of stack, I am adding it
        since Python allows.
    """

    def showStack(self):
        return self.__data