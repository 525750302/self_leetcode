#
# @lc app=leetcode.cn id=1400 lang=python
#
# [1400] 构造 K 个回文字符串
#

# @lc code=start
class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        odd_count = 0
        max_count = 0
        for i in dic.keys():
            if dic[i] % 2 == 1:
                odd_count += 1
            max_count += dic[i]
            if odd_count > k:
                return False
        if max_count < k:
            return False
        
        return True
        

# @lc code=end

