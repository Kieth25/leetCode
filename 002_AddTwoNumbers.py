# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 01:08:36 2019

@author: jrlyu
"""

class Solution(object):
    @staticmethod    
    def ListNodeIter(listNode):
        while listNode:
            val = listNode.val
            listNode = listNode.next
            yield val
            
    @staticmethod  
    def ListNodeToNum(listNode):    
        outNum = 0
        for index, num in enumerate(Solution.ListNodeIter(listNode)):
            outNum += num * (10**index)
        return outNum  
        
    @staticmethod  
    def NumToListNode(Num):
        
        firstListNode = ListNode(Num % 10)
        currentListNode = firstListNode 
        
        while int(Num/10) > 0:
            
            Num = int(Num/10)
            
            currentListNode.next = ListNode(Num % 10)
            currentListNode = currentListNode.next
            
        return firstListNode
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1 = Solution.ListNodeToNum(l1)
        n2 = Solution.ListNodeToNum(l2)
        
        return Solution.NumToListNode(n1 + n2)
            

        
        
        