# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:15:30 2019

@author: jrlyu
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.checkTreeMinDepth(root)
    
    
    def checkTreeMinDepth(self, root, depth=1):
        if not root:
            return 0
        elif not(root.right or root.left):
            return depth
        else:
            if root.left:
                leftTreeDepth = self.checkTreeMinDepth(root.left, depth+1)
            else:
                leftTreeDepth = float('inf')
            if root.right:
                rightTreeDepth = self.checkTreeMinDepth(root.right, depth+1)
            else:
                rightTreeDepth = float('inf')
            return min(leftTreeDepth,rightTreeDepth)
        