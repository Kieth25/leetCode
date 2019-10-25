# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:24:31 2019

@author: jrlyu
"""


class Solution(object):
    def __init__(self):
        self.finalReult = []
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        negativeTarget = False
        answer = []
        outList = [[]]

        if target < 0:
            negativeTarget = True
            nums = [-i for i in nums]
            target = -target

        for i in sorted(nums):
            outList = [j for j in outList if sum(j) <= target and len(j) < 4]
            outList = outList + [j + [i] for j in outList]
            answer += [j for j in outList if sum(j)==target and len(j)==4]

        if negativeTarget:
            answer = [[-j for j in i] for i in answer]

        ##### Reove Same element list
        temp_set = set(tuple(x) for x in answer)
        answer = [ list(x) for x in temp_set ]      
        return answer
    
    
class myCombination(object):
    @staticmethod    
    def run(mylist, count):
        yield from myCombination.subset([], mylist, count)
    
    @staticmethod    
    def subset(prefix, mylist, count):
        if count is 0:
            yield prefix
        else :
            for i in range (len(mylist)):
                yield from myCombination.subset(prefix + [mylist[i]], mylist[i+1:], count - 1)
                
                
nums = [-500,-481,-480,-469,-437,-423,-408,-403,-397,-381,-379,-377,-353,-347,-337,-327,-313,-307,-299,-278,-265,-258,-235,-227,-225,-193,-192,-177,-176,-173,-170,-164,-162,-157,-147,-118,-115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,74,93,101,104,105,112,112,116,129,133,146,152,157,158,166,177,183,186,220,263,273,320,328,332,356,357,363,372,397,399,420,422,429,433,451,464,484,485,498,499]
target = 2139


sol = Solution()
sol.fourSum(nums,target)