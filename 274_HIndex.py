# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 00:08:36 2019

@author: jrlyu
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = [0] + sorted(citations)

        for h_index in range(len(citations)):
            if not citations[-h_index] >= h_index:
                h_index = h_index-1
                break
        return h_index 
        
        
        
        
sol = Solution()

sol.hIndex([1])