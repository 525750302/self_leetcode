#
# @lc app=leetcode.cn id=140 lang=python
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.dic = {}
        self.result = []
        for i in range(len(wordDict)):
            self.dic[wordDict[i]] = 1
        self.mathWord(s,0,"")

        return self.result

    def mathWord(self,s,begin,sentence):
        if begin >= len(s):
            self.result.append(sentence)
        for i in range(begin,len(s)+1):
            if self.dic.get(s[begin:i]) ==1:
                if sentence == "":
                    new_sentence = s[begin:i]
                else:
                    new_sentence = sentence + " " + s[begin:i]
                self.mathWord(s,i,new_sentence)



# @lc code=end

