#
# @lc app=leetcode.cn id=260 lang=python
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        res = []
        for i in dic.keys():
            if dic[i] == 1:
                res.append(i)
        return res 
# @lc code=end

