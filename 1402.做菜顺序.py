#
# @lc app=leetcode.cn id=1402 lang=python
#
# [1402] 做菜顺序
#

# @lc code=start
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        max_val = 0
        s = 0
        count = 0
        for i in range(len(satisfaction)):
            count += satisfaction[i]
            s += count
            if max_val < s:
                max_val = s
        
        return max_val
# @lc code=end

