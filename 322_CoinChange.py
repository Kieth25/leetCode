# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:10:09 2019

@author: jrlyu
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        coinCount = [-1 for i in range(amount+1)]
        coinCount[0] = 0
        
        largeNum = 9999999999999999999
        
        for index in range(1,amount+1):
            minCoinCount = largeNum
            for coin in coins:
                if index==coin:
                    coinCount[index] = 1
                    minCoinCount = largeNum
                    break
                if index > coin:
                    if coinCount[index-coin] != -1:
                        minCoinCount = min(minCoinCount,coinCount[index-coin]+1)
            if minCoinCount != largeNum:
                coinCount[index] = minCoinCount
        return coinCount[-1]



