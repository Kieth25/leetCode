# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:51:07 2019

@author: jrlyu
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        
        
        
        
        
class Sudoku():
    def __init__(self, board):
        self.board = board
        self.row   = len(board)
        self.col   = len(board[0])
        self.subBoxList = None
        self.subBoxRow = 3
        self.subBoxCol = 3
        
    def createBasicSubBoxes(self):
        self.subBoxList =  [[ int(i/self.subBoxRow) + int(j/self.subBoxCol)*self.subBoxRow for i in range(self.col)] for j in range(self.row)]
#        pass.
        
    def checkSubBoxes(self):
        for index in range(self.subBoxRow*self.subBoxCol):
            for i in
            
            
        
        
    def checkRowCol(self):
        for i in range(self.row):
            rowValue = self.board[:][i] 
            if self.isDuplicate(rowValue):
                return False
            
        for j in range(self.col):
            colValue = self.board[j][:] 
            if self.isDuplicate(colValue):
                return False
        return True
        
    def isDuplicate(self, valueList):
        return not(sum([int(i) for i in valueList if i!='.' ]) == 
                   sum([int(i) for i in set(valueList) if i!='.' ])
                   )
        
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".","5",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


sd = Sudoku(board)

sd.checkRowCol()