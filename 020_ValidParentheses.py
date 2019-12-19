# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 01:07:29 2019

@author: jrlyu
"""
    
    
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left  = ['{','[','(']
        right = ['}',']',')']
        
        stack = []
        
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if stack and left.index(stack[-1]) == right.index(c):
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        return not stack