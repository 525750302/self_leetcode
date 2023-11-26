#
# @lc app=leetcode.cn id=187 lang=python
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        DNA = s[:10]
        dic = {}
        dic[DNA] = 1
        res = []
        for i in range(10,len(s)):
            DNA = DNA[1:] + s[i]
            dic[DNA] = dic.get(DNA,0) + 1
        for key in dic.keys():
            if dic[key] > 1:
                res.append(key)
        
        return res

            
# @lc code=end

