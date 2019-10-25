# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 01:07:43 2019

@author: jrlyu
"""

class Solution(object):
    def __init__(self):
        self.Parenthesis = []
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.gParenthesis(n)
                
    def gParenthesis(self, n):
        if n == 1:
            self.Parenthesis.append(['()'])
            return ['()']
        elif len(self.Parenthesis) > n:
            return self.Parenthesis[n]
        else:
            outList = list()
            for parenthesis in self.gParenthesis(n-1):
                for index in range(len(parenthesis)):
                    outList.append(parenthesis[:index] + '()' + parenthesis[index:])
        outList = list(set(outList))   
        self.Parenthesis.append(outList)              
        return outList
        
    