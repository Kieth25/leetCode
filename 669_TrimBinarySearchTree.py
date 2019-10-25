# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:54:50 2019

@author: jrlyu
"""

class binaryTree():
    def __init__(self, value):
        self.right = None
        self.left  = None
        self.val   = value
    def setValue(self, x) :
        self.val = x
        
    def setLeft(self, x):
        if isinstance(x, binaryTree):
            self.left = x 
            
    def setRight(self, x):
        if isinstance(x, binaryTree):
            self.right = x 
        
        
class BinarySeachTree():
    def __init__(self):
        self.levelList = []
        
    def creatBST(self, x):
        
        root= binaryTree(x.pop(0))
        for i in x:
            self.insertValue(root, i)
        return root
    
    def insertValue(self, root, value):
        if root.val >= value:
            if root.left:
                self.insertValue(root.left, value)
            else:
                root.setLeft(binaryTree(value))
        else:
            if root.right:
                self.insertValue(root.right, value)
            else:
                root.setRight(binaryTree(value))
            
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            self.levelList = []
            self.traversalTree(root, 0)
        return self.levelList

#            
#    def traversalTree(self, root, level):
#        if len(self.levelList) <= level:
#            self.levelList.append([root.val])
#        else:
#            self.levelList[level].append(root.val)
#            
#        if root.left:
#            self.traversalTree(root.left, level+1)
#        if root.right:
#            self.traversalTree(root.right, level+1)


        
    def checkBalanced(self, root):
        if root.left:
            lTreeDepth    = self.checkTreeDepth(root.left)
            lTreeBalanced = self.checkBalanced(root.left)
        else:
            lTreeDepth    = 0
            lTreeBalanced = True
        if root.right:
            rTreeDepth    = self.checkTreeDepth(root.right)
            rTreeBalanced = self.checkBalanced(root.right)
        else:
            rTreeDepth    = 0
            rTreeBalanced = True
        
        print(lTreeDepth, rTreeDepth)
        
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
        
        
        

    def trimBST(self, root, L, R):
        pass
        
        
BST = BinarySeachTree()

node = BST.creatBST([1])

BST.checkTreeDepth(node)
#BST.levelOrder(node)

BST.checkBalanced(node)


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        if root.val < L:
            root = root.right
        if root.val > R:
            root = root.left
        
        self.trimTree(root, L, 'L')
        self.trimTree(root, R, 'R')
        
        return root
        
        
    def trimTree(self, root, th, LR):
        if root == None:
            return      
        
        if LR == "L":
            if root.val > th:
                if root.left:
                    if root.left.val >= th:
                        self.trimTree(root.left, th, LR)
                    else:
                        root.left = root.left.right
                        self.trimTree(root.left, th, LR)
            elif root.val == th:
                root.left = None
                return 
            else:
                if root.right.val < th:
                    self.right = self.trimTree(root.right, th, LR)
                else:
                    root.right = None 
        else:
            if root.val < th:
                if root.right:
                    if root.right.val <= th:
                        self.trimTree(root.right, th, LR)
                    else:
                        root.right = root.right.left
                        self.trimTree(root.right, th, LR)
            elif root.val == th:
                root.right = None
                return 
            else:
                if root.right.val > th:
                    self.trimTree(root.left, th, LR)
                else:
                    root.left = None
    