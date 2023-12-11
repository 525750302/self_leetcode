#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1 , -1):
            if i + 1 <= n:
                dp[i] = dp[i + 1] + dp[i]
            if i + 2 <= n:
                dp[i] = dp[i] + dp[i + 2]
        
        return dp[0]
# @lc code=end

