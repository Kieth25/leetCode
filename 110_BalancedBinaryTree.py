# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:06:25 2019

@author: jrlyu
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        pass
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        if not root:
            return True
        return self.checkBalanced(root)
        
        
    def checkBalanced(self, root):
        if root.left:
            lTreeBalanced = self.checkBalanced(root.left)
            if not lTreeBalanced:
                return False
            lTreeDepth    = self.checkTreeDepth(root.left)
            
        else:
            lTreeDepth    = 0
            lTreeBalanced = True
        if root.right:
            rTreeBalanced = self.checkBalanced(root.right)
            if not rTreeBalanced:
                return False
            rTreeDepth    = self.checkTreeDepth(root.right)
            
        else:
            rTreeDepth    = 0
            rTreeBalanced = True
        
        if abs(lTreeDepth - rTreeDepth) <= 1:
            return True and lTreeBalanced and rTreeBalanced
        else:
            return False
        
    
    def checkTreeDepth(self, root, depth=1):
        if not root:
            return 0
        elif not(root.right or root.left):
            return depth
        else:
            if root.left:
                leftTreeDepth = self.checkTreeDepth(root.left, depth+1)
            else:
                leftTreeDepth = depth
            if root.right:
                rightTreeDepth = self.checkTreeDepth(root.right, depth+1)
            else:
                rightTreeDepth = depth
            return max(leftTreeDepth,rightTreeDepth)
        
        