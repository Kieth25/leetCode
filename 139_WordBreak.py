# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:19:47 2019

@author: jrlyu
"""
class Solution(object):
    def __init__(self):
        self.wordBreakFlag = False
        self.funCallNun = 0
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict         = set(wordDict)
        condenseWordDict = set(wordDict)

        for word in wordDict:
            if self.isCombineBy(word, condenseWordDict - {word}):
                self.wordBreakFlag = False
                condenseWordDict -= {word}
        print(condenseWordDict)
        self.wordBreakFlag = False
        return self.isCombineBy(s, condenseWordDict)
        
        
    def isCombineBy(self, s, wordDict, lastWord=""):
#        print(s,self.wordBreakFlag)
        self.funCallNun += 1
        if self.wordBreakFlag:
            return True
        if s == "":
            self.wordBreakFlag = True
            return True

        #### Remove unnecessary word
        wordDict = {word for word in wordDict if word in s} 
        
        #### Check start with World List
        startWithWordList = [word for word in wordDict if s.startswith(word)] 
        #### Extend Word Dict 
#        extendWordDict = [ lastWord + word for word in startWithWordList]
#        wordDict  = wordDict | set(extendWordDict)
        
        return any([False] + [self.isCombineBy(s[len(word):], wordDict, word) for word in startWithWordList])
                
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#s        ="cars"
#wordDict = ["car","ca","rs"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]

sol = Solution()
sol.wordBreak(s,wordDict)


