# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:08:21 2019

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
        self.levelList = []
    
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            self.traversalTree(root, 0)
            
        for index, i in enumerate(self.levelList):
            if index % 2:
                self.levelList[index] = i[::-1]
            
        return self.levelList
    
    def traversalTree(self, root, level):
        if len(self.levelList) <= level:
            self.levelList.append([root.val])
        else:
            self.levelList[level].append(root.val)
        if root.left:
            self.traversalTree(root.left, level+1)
        if root.right:
            self.traversalTree(root.right, level+1)
           