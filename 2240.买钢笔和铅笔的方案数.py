#
# @lc app=leetcode.cn id=2240 lang=python
#
# [2240] 买钢笔和铅笔的方案数
#

# @lc code=start
class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        higher = max(cost1, cost2)
        lower = min(cost1, cost2)
        max_st = total // higher
        ans = 0
        for i in range(max_st, -1, -1):
            ans += (total - i * higher) // lower + 1
        
        return ans



# @lc code=end

